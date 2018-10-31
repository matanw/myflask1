
import  pytest

from app import create_app
#from entities import db
import os
import tempfile
@pytest.fixture
def list():
    return [11]




TESTDB = 'test_project.db'
TESTDB_PATH = "/Users/matanwiesner/Work/temp/test1.msa"
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH


@pytest.fixture#(scope='session')
def app():
    db_fd, db_path = tempfile.mkstemp()
    """Session-wide test `Flask` application."""

    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///' +db_path,
    }
    #app = create_app(__name__, settings_override)
    app = create_app(settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()
    #db.drop_all()
    os.unlink(db_path)
    print("down")

@pytest.fixture(scope='session')
def db1(app, request):
    """Session-wide test database."""
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        db.drop_all()
        os.unlink(TESTDB_PATH)
    #db.app = app
    db.create_all(app=app)

    request.addfinalizer(teardown)
    return db()
@pytest.fixture(scope='session')
def client(app, request):
    """Session-wide test database."""
    return app.test_client()

@pytest.fixture(scope='function')
def session(db11, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session