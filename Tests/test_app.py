from src.app import home, index

def test_flask_app():
    assert home()=="Hello, world!"

def test_flask_new_app():
    assert index()=="<h1>good Afternoon</h1>"
