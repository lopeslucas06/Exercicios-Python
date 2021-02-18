pessoa = {}
pessoas = []
soma = cont = 0
mulher = []
maior = []
while True:
    pessoa['nome'] = str(input('Nome: '))    
    pessoa['sexo'] = str(input('Sexo: [M/F] '))[0].upper().strip()
    if pessoa['sexo'] in 'F':
        mulher.append(pessoa['nome'])  
    pessoa['idade'] = int(input('Idade: '))  
    soma += pessoa['idade']  
    cont += 1
    pessoas.append(pessoa.copy())        
    r = str(input('Deseja continuar? [S/N] '))[0].upper().strip()
    if r == 'N':
        break
media = soma / cont
print(f'O número de pessoas cadastradas foram {len(pessoas)}')
print(f'A média das idades é de {media:.2f} anos!')
print(f'As mulheres são {mulher}')
for p in pessoas:
    if p['idade'] > media:
        maior.append(p['nome'])
print(f'As pessoas acima da média de idade são {maior}')
        

    
    

