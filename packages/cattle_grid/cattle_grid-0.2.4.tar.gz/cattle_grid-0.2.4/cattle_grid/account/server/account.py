import logging
import aio_pika

from uuid import uuid4

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from bovine.types import ServerSentEvent

from cattle_grid.dependencies.fastapi import Broker, MethodInformation
from cattle_grid.activity_pub.actor import (
    create_actor,
    actor_to_object,
)
from cattle_grid.model.account import InformationResponse, EventType

from cattle_grid.account.models import ActorForAccount
from cattle_grid.account.router.info import create_information_response

from .requests import CreateActorRequest
from .dependencies import CurrentAccount

logger = logging.getLogger(__name__)

account_router = APIRouter(prefix="/account", tags=["account"])


async def queue_for_connection(connection, username: str, event_type: EventType):
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    exchange = await channel.declare_exchange(
        "amq.topic", aio_pika.ExchangeType.TOPIC, durable=True
    )

    queue = await channel.declare_queue(
        f"queue-{username}-{uuid4()}",
        durable=False,
    )
    await queue.bind(exchange, routing_key=f"receive.{username}.{event_type.value}")

    return queue


def get_message_streamer(broker: Broker):
    connection = broker._connection

    async def stream_messages(username: str, event_type: EventType):
        try:
            async with connection:
                queue = await queue_for_connection(connection, username)

                async with queue.iterator() as iterator:
                    try:
                        async for message in iterator:
                            async with message.process():
                                message_body = message.body.decode()
                                yield message_body
                    except Exception as e:
                        logger.exception(e)
        except Exception as e:
            logger.exception(e)

    return stream_messages


@account_router.get(
    "/stream/{event_type}",
    response_description="EventSource",
    operation_id="stream",
)
async def stream(
    event_type: EventType,
    account: CurrentAccount,
    stream_messages=Depends(get_message_streamer),
):
    """EventSource corresponding to all messages received
    by the account.

    This method returns an
    [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)
    providing server sent events."""
    username = account.name

    async def event_stream():
        try:
            async for message in stream_messages(username, event_type):
                data = ServerSentEvent(data=message).encode()

                yield data
        except Exception as e:
            logger.exception(e)

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@account_router.post("/create", status_code=201, operation_id="create_actor")
async def create_actor_method(body: CreateActorRequest, account: CurrentAccount):
    """Allows one to create a new actor. The allowed values for base_url
    can be retrieved using the info endpoint."""
    actor = await create_actor(body.base_url, preferred_username=body.handle)
    await actor.fetch_related("identifiers")
    await ActorForAccount.create(account=account, actor=actor.actor_id)

    return actor_to_object(actor)


@account_router.get("/info", operation_id="account_info")
async def return_settings(
    account: CurrentAccount, method_information: MethodInformation
) -> InformationResponse:
    """Returns information about the server and the account."""
    return await create_information_response(account, method_information)
