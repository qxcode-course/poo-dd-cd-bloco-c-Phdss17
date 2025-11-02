class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'

lista_vazia: list[int] = []
lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_preenchida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

lista_vazia.append(1)
lista_preenchida_objetos.append(Foo(6))