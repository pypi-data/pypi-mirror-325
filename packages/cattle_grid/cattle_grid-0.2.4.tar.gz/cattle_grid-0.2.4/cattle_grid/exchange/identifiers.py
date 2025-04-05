from urllib.parse import urlparse

from cattle_grid.activity_pub.models import (
    PublicIdentifierStatus,
)
from cattle_grid.config.account import get_base_urls


def is_identifier_part_of_base_urls(identifier: str, base_urls: list[str]) -> bool:
    if not identifier.startswith("acct:"):
        return False

    identifier_domain = identifier.split("@")[1]

    return any(identifier_domain == urlparse(base_url).netloc for base_url in base_urls)


async def determine_identifier_status(identifier):
    base_urls = get_base_urls()

    if is_identifier_part_of_base_urls(identifier, base_urls):
        return PublicIdentifierStatus.verified

    return PublicIdentifierStatus.unverified
