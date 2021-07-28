import jwt

# dados utilizados
payload = {"language": "Python"}
secret_word = 'acelera'
error = {"error": 2}


def create_token(payload, secret_word):
    # Gerando o jwt
    encoded = jwt.encode(payload, secret_word, algorithm='HS256')
    return encoded


def verify_signature(token):
    # Verificando o jwt
    try:
        decoded = jwt.decode(token, secret_word, algorithm='HS256')
        return decoded
    except jwt.exceptions.InvalidSignatureError:
        # Erro caso tenha algum problema de assinatura
        return error
    except:
        # Erro caso ocorra algum problema desconhecido
        print('Erro desconhecido foi encontrado!')
