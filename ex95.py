jogadores = []
jogador = {}
gols = []
somagols = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas você jogou? '))
    jogador['partidas'] = partidas
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantidade de gols na {c}ª partida: ')))
        somagols += gols[c -1]
    jogador['gols'] = gols.copy()
    jogador['total'] = somagols
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    somagols = 0
    r = str(input('Deseja continuar? [S/N]'))[0].upper().strip()
    if r in 'N':
        break
print(f'{"Cód":<5}{"Nome":<15}{"Gols":<15}{"Total":<15}')
for pos,j in enumerate(jogadores):
    print(f'{pos:<5}{j["nome"]:<15}{j["gols"]}{j["total"]:>10}')
while True:
    r = int(input('Mostrar dados de qual jogador? 999 para sair'))
    if r == 999:
        break
    print(f'O jogador {jogadores[r]["nome"]}')   
    for c in range(1, jogadores[r]['partidas'] + 1):
        print(f'Na partida {c} fez {jogadores[r]["gols"][c - 1]} gols')