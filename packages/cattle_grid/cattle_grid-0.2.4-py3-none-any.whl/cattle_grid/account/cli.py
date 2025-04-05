import click
import asyncio
import logging


from cattle_grid.database import database
from .models import Account
from .account import create_account, add_permission, list_permissions, remove_permission

logger = logging.getLogger(__name__)


async def run_with_database(config, coro):
    try:
        async with database(db_uri=config.db_uri):
            await coro
    except Exception as e:
        logger.exception(e)


async def new_account(name: str, password: str, permission: list[str]):
    account = await create_account(name, password)
    for p in permission:
        await add_permission(account, p)


async def list_accounts():

    accounts = await Account.all().prefetch_related("permissions")
    for account in accounts:
        print(f"{account.name}: ", ", ".join(list_permissions(account)))


async def modify_permissions(
    name: str, add_permissions: list[str], remove_permissions: list[str]
):
    account = await Account.get_or_none(name=name)
    if account is None:
        print(f"Account {name} does not exist")
        exit(1)
    for p in add_permissions:
        await add_permission(account, p)
    for p in remove_permissions:
        await remove_permission(account, p)


def add_account_commands(main):
    @main.group()
    def account():
        """Used to manage accounts associated with cattle_grid"""

    @account.command()
    @click.argument("name")
    @click.argument("password")
    @click.option(
        "--admin", is_flag=True, default=False, help="Set the admin permission"
    )
    @click.option(
        "--permission",
        help="Adds the permission to the account",
        multiple=True,
        default=[],
    )
    @click.pass_context
    def new(ctx, name, password, admin, permission):
        """Creates a new account"""

        if admin:
            permission = list(permission) + ["admin"]

        asyncio.run(
            run_with_database(
                ctx.obj["config"], new_account(name, password, permission)
            )
        )

    @account.command()
    @click.argument("name")
    @click.option(
        "--add_permission",
        help="Adds the permission to the account",
        multiple=True,
        default=[],
    )
    @click.option(
        "--remove_permission",
        help="Adds the permission to the account",
        multiple=True,
        default=[],
    )
    @click.pass_context
    def modify(ctx, name, add_permission, remove_permission):
        """Modifies an account"""

        asyncio.run(
            run_with_database(
                ctx.obj["config"],
                modify_permissions(
                    name,
                    add_permissions=add_permission,
                    remove_permissions=remove_permission,
                ),
            )
        )

    @account.command("list")
    @click.pass_context
    def list_account(ctx):
        """Lists existing accounts"""
        asyncio.run(run_with_database(ctx.obj["config"], list_accounts()))
