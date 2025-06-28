def identificar_bandeira(numero_cartao):
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')):
        return "MasterCard"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    elif numero_cartao.startswith('6011') or numero_cartao.startswith('65') or numero_cartao.startswith(('644', '645', '646', '647', '648', '649')):
        return "Discover"
    elif numero_cartao.startswith('35'):
        return "JCB"
    elif numero_cartao.startswith(('36', '38', '39')):
        return "Diners Club"
    else:
        return "Bandeira desconhecida"

def validar_luhn(numero_cartao):
    soma = 0
    inverter = numero_cartao[::-1]

    for i, digito in enumerate(inverter):
        n = int(digito)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        soma += n

    return soma % 10 == 0

def limpar_numero(numero):
    return numero.replace(" ", "").replace("-", "")

# --------- Programa principal ---------
numero = input("Digite o número do cartão de crédito: ")
numero_limpo = limpar_numero(numero)

if not numero_limpo.isdigit():
    print("Número inválido: contém caracteres não numéricos.")
else:
    if validar_luhn(numero_limpo):
        bandeira = identificar_bandeira(numero_limpo)
        print(f"Bandeira identificada: {bandeira}")
        print("O número do cartão é válido.")
    else:
        print("Número inválido: não é um número de cartão de crédito válido.")
    