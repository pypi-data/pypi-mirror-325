import re

import pytest

from elroy.cli.chat import process_and_deliver_msg
from elroy.config.constants import USER
from elroy.repository.goals.queries import get_active_goal_names


@pytest.mark.asyncio
async def test_create_and_mark_goal_complete(ctx):
    ctx.io.add_user_responses("Test Goal", "", "", "", "", "")

    await process_and_deliver_msg(USER, ctx, "/create_goal Test Goal")

    assert "Test Goal" in get_active_goal_names(ctx)

    assert "Test Goal" in ctx.io.get_sys_messages()

    ctx.io.add_user_responses("Test Goal", "The test was completed!")

    await process_and_deliver_msg(USER, ctx, "/mark_goal_completed Test Goal")

    assert "Test Goal" not in get_active_goal_names(ctx)

    assert re.search(r"Test Goal.*completed", ctx.io.get_sys_messages()) is not None


@pytest.mark.asyncio
async def test_invalid_update(ctx):
    ctx.io.add_user_responses("Nonexistent goal", "Foo")
    await process_and_deliver_msg(USER, ctx, "/mark_goal_completed")

    response = ctx.io.get_sys_messages()
    assert re.search(r"Error.*.*not exist", response) is not None


@pytest.mark.asyncio
async def test_invalid_cmd(ctx):
    await process_and_deliver_msg(USER, ctx, "/foo")
    response = ctx.io.get_sys_messages()
    assert re.search(r"Invalid.*foo.*help", response) is not None
