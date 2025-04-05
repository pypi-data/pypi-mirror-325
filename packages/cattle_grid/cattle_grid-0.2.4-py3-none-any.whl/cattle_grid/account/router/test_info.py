import pytest

from cattle_grid.testing.fixtures import database  # noqa

from cattle_grid.account.account import create_account, add_permission
from cattle_grid.model.account import InformationResponse

from .info import create_information_response


@pytest.fixture
async def test_admin_account():
    account = await create_account("test_account", "test_password")
    await add_permission(account, "admin")

    return account


async def test_create_information_response(test_admin_account):
    response = await create_information_response(test_admin_account, [])

    assert isinstance(response, InformationResponse)
