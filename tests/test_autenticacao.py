from src.autenticacao import cadastrar,autenticar



def test_cadastrar():
    assert cadastrar("usuario02","senha123") == True
    assert cadastrar("", "") == False


def test_autenticar():
    assert autenticar("","") == False
    assert autenticar("usuario01", "senha123") == True
    assert autenticar("usuario01", "senha_nova") == False

    