from random import randint
from time import sleep
dados = {'jogador1': randint(1,6 ), 'jogador2': randint(1,6 ), 'jogador3': randint(1,6 ), 'jogador4': randint(1,6 ), }
for i in dados.items():
   print(f'O {i[0]} tirou {i[1]}')
   sleep(1)
print('Ranking de jogadores')
c = 1
for item in sorted(dados, key = dados.get, reverse=True):
    print (f'{c}° Lugar: {item} com {dados[item]}')
    c+= 1
    sleep(1)
