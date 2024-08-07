import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='example.log', encoding='utf-8', level=logging.DEBUG)

def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    aux = 0
    for _ in range(b):
        aux = soma(aux,a)
    return aux

def div(a,b):
    try:
        return a/b  ## BLOCO A
    except ZeroDivisionError:
        logging.warning("Não pode dividir por 0.")
        aux = div(a,1)                              ## BLOCO B
        logging.debug(f'{a} dividido por {b+1} = {aux}')
    except Exception:
        logging.error("Tente novamente mais tarde.")
