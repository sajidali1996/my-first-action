from main import greet

def test_dummy():
    assert True

def test_greet_prints(capsys):
    greet()
    captured = capsys.readouterr()
    assert "Hello from Python inside GitHub Actions" in captured.out
