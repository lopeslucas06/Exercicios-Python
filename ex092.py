from datetime import datetime
data = datetime.today().year
carteira = {}
carteira['nome'] = str(input('Nome: '))
carteira['idade'] = data - int(input('Ano de nascimento: '))
carteira['CTPS'] = int(input('Carteira de trabalho: '))
if carteira['CTPS'] > 0:
    carteira['acontratacao'] = int(input('Ano de contratação: '))
    carteira['salario'] = float(input('Salário: '))
    carteira['aposentadoria'] = (35 - (data - carteira['acontratacao'])) + carteira['idade']
print(f'{carteira["nome"]}, você tem {carteira["idade"]} anos e irá se aposentar com {carteira["aposentadoria"]} anos!')