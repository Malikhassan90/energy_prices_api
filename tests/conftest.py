import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def _db(app):
    db.create_all()
    yield db
    db.drop_all()
