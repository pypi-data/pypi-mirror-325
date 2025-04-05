from cattle_grid.model.account import NameAndVersion, InformationResponse
from cattle_grid.model.extension import MethodInformationModel
from cattle_grid.version import __version__


from cattle_grid.account.models import Account
from cattle_grid.account.permissions import allowed_base_urls


def protocol_and_backend():
    protocol = NameAndVersion(name="CattleDrive", version="0.1.0")
    backend = NameAndVersion(name="cattle_grid", version=__version__)

    return dict(protocol=protocol, backend=backend)


async def create_information_response(
    account: Account, method_information: list[MethodInformationModel]
) -> InformationResponse:
    await account.fetch_related("actors")

    actor_ids = [x.actor for x in account.actors]
    base_urls = await allowed_base_urls(account)

    return InformationResponse(
        base_urls=base_urls,
        actors=actor_ids,
        **protocol_and_backend(),
        method_information=method_information,
    )
