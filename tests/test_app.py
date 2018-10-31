


def test4(app):
    client=app.test_client()
    rv=client.get("/add_commit/a4")
    assert 200 == rv.status_code
    rv=client.get("/list")
    assert 200 == rv.status_code
    print(rv)

def test5(app):
    client=app.test_client()
    rv=client.get("/add_commit/a5")
    assert 200 == rv.status_code
    rv=client.get("/list")
    assert 200 == rv.status_code
    print(rv)

def test6(app):
    client=app.test_client()
    rv=client.get("/add_commit/a6")
    assert 200 == rv.status_code
    rv=client.get("/list")
    assert 200 == rv.status_code
    print(rv)
