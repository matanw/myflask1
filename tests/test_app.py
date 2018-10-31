def test1():
    pass

def test2(list):
    assert list[0]==11


def test3(app):
    pass


def test4(client):
    rv=client.get("/add_commit/a4")
    assert 200 == rv.status_code
    rv=client.get("/list")
    assert 200 == rv.status_code
    print(rv)

def test5(client):
    rv=client.get("/add_commit/a5")
    assert 200 == rv.status_code
    rv=client.get("/list")
    assert 200 == rv.status_code
    print(rv)

def test6(client):
    rv=client.get("/add_commit/a6")
    assert 200 == rv.status_code
    rv=client.get("/list")
    assert 200 == rv.status_code
    print(rv)
