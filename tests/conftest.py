import pytest
from app.servercore import ServerCore

@pytest.fixture(scope='module')
def test_client():
    server = ServerCore()
    app = server.getApp()
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()