import pytest

def login(usuari, contrasenya):
    if usuari == "admin" and contrasenya == "1234":
        return "Acces concedit"
    return "Acces denegat"

def test_login():
    assert login('admin', '1234') == "Acces concedit"
    assert login('caca', '24') == "Acces denegat"