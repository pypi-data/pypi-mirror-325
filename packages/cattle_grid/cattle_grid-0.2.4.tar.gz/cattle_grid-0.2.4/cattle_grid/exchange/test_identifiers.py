import pytest

from .identifiers import is_identifier_part_of_base_urls


@pytest.mark.parametrize(
    "identifier, base_urls, expected",
    [
        ("acct:test@one.test", ["http://one.test"], True),
        ("acct:test@two.test", ["http://one.test"], False),
    ],
)
def test_is_identifier_part_of_base_urls(identifier, base_urls, expected):
    assert is_identifier_part_of_base_urls(identifier, base_urls) == expected
