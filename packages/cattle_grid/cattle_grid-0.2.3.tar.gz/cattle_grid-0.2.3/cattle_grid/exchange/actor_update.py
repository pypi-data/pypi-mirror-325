import logging

from cattle_grid.activity_pub.models import (
    Actor,
    PublicIdentifier,
)
from cattle_grid.model.exchange import (
    UpdateAction,
    UpdateActionType,
    UpdateIdentifierAction,
)

from .identifiers import determine_identifier_status

logger = logging.getLogger(__name__)


def find_identifier(actor: Actor, to_find: str) -> PublicIdentifier | None:
    for identifier in actor.identifiers:
        if identifier.identifier == to_find:
            return identifier
    return None


def new_primary_preference(actor):
    return max(identifier.preference for identifier in actor.identifiers) + 1


async def handle_actor_action(actor: Actor, action: UpdateAction) -> None:
    match action.action:
        case UpdateActionType.add_identifier:
            # FIXME: Need way to validate identifiers

            logger.info(action)

            # check if identifier already exists ...

            await actor.fetch_related("identifiers")

            action = UpdateIdentifierAction.model_validate(action.model_dump())
            preference = 0

            if action.primary:
                preference = new_primary_preference(actor)

            status = await determine_identifier_status(action.identifier)

            logger.info(
                "adding identifier %s with status %s for %s",
                action.identifier,
                status,
                actor.actor_id,
            )

            await PublicIdentifier.create(
                actor=actor,
                identifier=action.identifier,
                name="through_exchange",
                preference=preference,
                status=status,
            )

            return True
        case UpdateActionType.update_identifier:
            await actor.fetch_related("identifiers")
            public_identifier = find_identifier(actor, action.identifier)
            if public_identifier is None:
                raise ValueError("Identifier not found")

            if action.primary:
                public_identifier.preference = new_primary_preference(actor)
            await public_identifier.save()

            return True

    return False
