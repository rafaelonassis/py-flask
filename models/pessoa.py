class Pessoa():
    def __init__(individuo, altura ,peso):
        individuo.altura = altura
        individuo.peso = peso
        individuo.imc = 0
        individuo.description = ''

    def from_dict(dictionary):
        altura = dictionary['altura']
        peso = dictionary['peso']

        pessoa = Pessoa(altura, peso)
        return pessoa
    
    def to_dict(individuo):
        retorno = dict()
        retorno['altura'] = individuo.altura
        retorno['peso'] = individuo.peso
        retorno['imc'] = individuo.imc
        retorno['description'] = individuo.description

        return retorno