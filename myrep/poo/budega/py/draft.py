class client:
    def __init__(self, nome: str) -> None:
        self.__nome: str = nome

    def getNome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return self.__nome
    

class market:
    def __init__(self, num_count: int) -> None:
        self.__counters: list[client | None] = []
        self.__waiting: list[client] = []
        self.__numCount: int = num_count

        for _ in range(num_count):
            self.__counters.append(None)

    def arrive(self, c: client) -> None:
        self.__waiting.append(c)

    def __str__(self) -> str:
        return f"Caixas: {[x.getNome() if x is not None else "-----" for x in self.__counters]} \n Espera: {[x.getNome() for x in self.__waiting]}"

def main() -> None:
    m = market(1)

    while True:
        line: str = input()
        args: list[str] = line.split(" ")

        match args[0]:
            case "end":
                break
            case "init":
                m = market(int(args[1]))
            


main()