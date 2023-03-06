from wallet import wallet, InsuficienteSaldo
import pytest

def test_cantidad_inicial():
    mi_wall = wallet()
    assert mi_wall.saldo == 0


def test_cantidad_inicial_fail():
    mi_wall = wallet()
    assert mi_wall.saldo == 10

def test_gastar():
    mi_wall = wallet(100)
    mi_wall.gastar_dinero(50)
    assert mi_wall.saldo == 50

def test_anadir():
    mi_wall = wallet(100)
    mi_wall.anadir_saldo(50)
    assert mi_wall.saldo == 150
    
def test_excepcion():
    mi_wall = wallet(100)
    with pytest.raises(InsuficienteSaldo):
        mi_wall.gastar_dinero(150)