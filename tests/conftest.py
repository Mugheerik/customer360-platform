import pytest

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.database.dependencies import get_db
from app.database.database import engine


@pytest.fixture
def db_session():
    connection = engine.connect()

    transaction = connection.begin()

    session = Session(bind=connection)

    session.begin_nested()

    @pytest.fixture
    def restart_savepoint():
        pass

    try:
        yield session

    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()