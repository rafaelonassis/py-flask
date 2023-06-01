def calculate(pessoa):
    calculate_imc(pessoa)
    describe_imc(pessoa)

def calculate_imc(pessoa):
    pessoa.imc = pessoa.peso / pessoa.altura ** 2

def describe_imc(pessoa):
    pessoa.description = 'Obesidade'

    if pessoa.imc < 18.5: pessoa.description = 'Magreza'
    elif pessoa.imc < 24.9: pessoa.description = 'Normal'
    elif pessoa.imc < 30: pessoa.description = 'Sobrepeso'