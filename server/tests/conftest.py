@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test module."""
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    """A test client for the app."""
    return app.test_client()