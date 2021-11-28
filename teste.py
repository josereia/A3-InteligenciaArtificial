class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age


lst_pessoas = [
    Pessoa("Guilherme",19),
    Pessoa("Lucas",13)
]

def get_key_nome(c):
      return c.age

lst_pessoas.sort(key=get_key_nome)
print(lst_pessoas[0].name)