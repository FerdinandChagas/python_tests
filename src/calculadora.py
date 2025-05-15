import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='example.log', encoding='utf-8', level=logging.DEBUG)

def soma(a,b):
    try:
        return a+b
    except TypeError:
        logging.error("Os valores devem ser numéricos.")
        return 0

def sub(a,b):
    try:
        if a < b:
            raise ValueError
        return a-b
    except ValueError:
        logging.warning("O primeiro valor deve ser maior que o segundo.")
        return 0

def mult(a,b):
    aux = 0
    for _ in range(b):
        aux = soma(aux,a)
    return aux

def div(a,b):
    try:
        if b == 0:
            raise RuntimeError
        return a/b  ## BLOCO A
    except ZeroDivisionError:
        logging.warning("Não pode dividir por 0.")
        aux = div(a,1)                              ## BLOCO B
        logging.debug(f'{a} dividido por {b+1} = {aux}')
    except Exception:
        logging.error("Tente novamente mais tarde.")
