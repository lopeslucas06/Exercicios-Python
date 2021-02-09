boletim = {}
boletim['aluno'] = str(input('Nome do aluno: '))
boletim['media'] = float(input('Média do aluno: '))
print(f'Nome é igual a {boletim["aluno"]}')
print(f'Média é igual a {boletim["media"]}')
if boletim['media'] >= 7:
    print('APROVADO')
else:
    print('REPROVADO')
