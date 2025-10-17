#aula sobre Programação Orientada a Objetos (POO) aplicada a uma fazenda.
#Criação de classes para representar diferentes tipos de animais na fazenda,


class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def emitir_som(self) -> str:
        return "O animal emite um som."

    def apresentar(self) -> str:
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."


class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self) -> str:
        return "Au! Au!"


class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor_pelo: str):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self) -> str:
        return "Miau!"


class Vaca(Animal):
    def __init__(self, nome: str, idade: int, producao_leite_litros: float):
        super().__init__(nome, idade)
        self.__producao_leite_litros = float(producao_leite_litros)  # encapsulado

    def emitir_som(self) -> str:
        return "Muuu!"

    def obter_producao_leite(self) -> float:
        return self.__producao_leite_litros

    def registrar_ordenha(self, litros: float) -> None:
        self.__producao_leite_litros = float(litros)


if __name__ == "__main__":
    # Instâncias conforme enunciado
    rex = Cachorro("Rex", 3, "Labrador")
    mimi = Gato("Mimi", 5, "Branco")
    mimosa = Vaca("Mimosa", 7, 25.5)

    # Apresentações
    print(rex.apresentar())
    print(mimi.apresentar())
    print(mimosa.apresentar())

    # Emissão de sons (polimorfismo)
    print(rex.emitir_som())
    print(mimi.emitir_som())
    print(mimosa.emitir_som())

    # Encapsulamento: produção de leite
    print(f"Produção atual de leite (Mimosa): {mimosa.obter_producao_leite()} litros")
    mimosa.registrar_ordenha(28.0)
    print(f"Produção após ordenha (Mimosa): {mimosa.obter_producao_leite()} litros")