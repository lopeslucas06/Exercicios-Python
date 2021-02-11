jogador = {}
gols = []
somagols = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas você jogou? '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantidade de gols na {c}ª partida: ')))
    somagols += gols[c -1]
jogador['gols'] = gols
jogador['total'] = somagols
print(jogador) 
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas!')
for c in range(1, partidas + 1):
    print(f'Na partida {c}, fez {jogador["gols"][c - 1]} gols.')