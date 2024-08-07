
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='example.log', encoding='utf-8', level=logging.INFO)

login_bd = "usuario01"
senha_bd = "senha123"
count = 0

def cadastrar(login, senha):
    global login_bd, senha_bd
    try:
        if login == login_bd:
            raise ValueError()
        elif senha != "":
            login_bd = login
            senha_bd = senha
            logging.info(f'Cadastro do usuário {login} realizado com SUCESSO!')
            return True
        else:
            raise AssertionError()
    except TypeError:
        logging.error("Erro na entrada de dados.")
        return False
    except AssertionError:
        logging.warning("Senha vazia.")
        return False
    except ValueError:
        logging.warning("Nome de usuário em uso.")
        return False

def autenticar(login, senha):
    global count, login_bd, senha_bd
    try:
        if count <= 3 and login == login_bd and senha == senha_bd:
            logging.info("Autenticação realializada com SUCESSO!")
            count = 0
            return True
        elif count > 3:
            raise AttributeError()
        else:
            count += 1
            raise ValueError()
    except ValueError:
        logging.error("login/senha inválidos!")
        return False
    except AttributeError:
        logging.error("Conta suspensa.")
        return False