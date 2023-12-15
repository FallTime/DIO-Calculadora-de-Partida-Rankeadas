def mensagem(saldo, rank):
    print("O Herói tem o saldo de", saldo, "está no nível", rank)


def calculadora(num_vitoria, num_derrota):
    return num_vitoria - num_derrota


vitorias = 100
derrotas = 9

if vitorias > 100:
    mensagem(calculadora(vitorias, derrotas), "Imortal")
elif vitorias > 90:
    mensagem(calculadora(vitorias, derrotas), "Lendário")
elif vitorias > 80:
    mensagem(calculadora(vitorias, derrotas), "Diamante")
elif vitorias > 50:
    mensagem(calculadora(vitorias, derrotas), "Ouro")
elif vitorias > 20:
    mensagem(calculadora(vitorias, derrotas), "Prata")
elif vitorias > 10:
    mensagem(calculadora(vitorias, derrotas), "Bronze")
else:
    mensagem(calculadora(vitorias, derrotas), "Ferro")
