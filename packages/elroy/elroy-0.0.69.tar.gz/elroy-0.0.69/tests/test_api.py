from elroy.api import Elroy
from elroy.config.ctx import ElroyContext


def test_api(ctx: ElroyContext):
    assistant = Elroy(token="testuser", database_url=ctx.db.url)

    response = assistant.message("This is a test: repeat the following words: Hello World")
    assert "hello world" in response.lower()
