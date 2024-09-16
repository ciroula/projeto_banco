import pytest

from banco.models.conta import Conta

#jeito antigo
#@pytest.fixture
#def conta_valida():
#    conta = Conta(222, 444)
#    return conta

#jeito novo
@pytest.fixture
def conta_valida():
    return Conta(222, 444)

def test_validando_atributo_numero_conta(conta_valida):
    assert conta_valida.numero_conta == 222
    
def test_validando_atributo_agencia(conta_valida):
    assert conta_valida.agencia == 444
    
def test_validando_atributo_saldo(conta_valida):
    assert conta_valida._saldo == 0
    
def test_depositar_valor_positivo(conta_valida):
    conta_valida.depositar(100)
    assert conta_valida._saldo == 100
    
def test_sacar_valor_positivo_com_saldo_insuficiente(conta_valida):
    conta_valida.depositar(100)
    conta_valida.sacar(100)
    assert conta_valida._saldo ==0
    