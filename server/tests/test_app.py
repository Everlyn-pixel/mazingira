def test_app(client):
    """Test that the app is running."""
    res = client.get('/')
    assert res.status_code == 200
