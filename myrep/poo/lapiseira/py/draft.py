class Grafite:
    def __init__ (self, calibre:float, hardness:str, size:int ):
        self.__calibre = calibre
        self.__hardness = hardness
        self.__size = size

    def getcalibre(self):
        return self.__calibre
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size:int):
        self.__size = size
    
    def usagepersheet(self) -> int:
        if self.__hardness == 'HB':
            return 1
        elif self.__hardness == '2B':
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        return 0
    
    def __str__(self):
        return f"{self.__calibre}:{self.__hardness}:{self.__size}"
    
class Pencil:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__ponta: Grafite | None = None
        self.__tambor: list[Grafite] = [ ]

    def HasGrafite(self) -> bool:
        if self.__ponta != None:
            return True
        else:
            return False

    def insert(self, grafite: Grafite) -> bool:
        if grafite.getcalibre() != self.__calibre:
            print("fail: calibre incompativel")
            return False
        self.__tambor.append(grafite)
        return True
   
    def remove(self) -> Grafite | None:
        if self.HasGrafite():
           g = self.__ponta
           self.__ponta = None
           return g
        else:
            print("fail: nao existe grafite no bico")
            return None

    def pull(self) -> bool:
        if self.__ponta != None:
            print("fail: ja existe grafite no bico")
            return False

        if self.__tambor != []:
            self.__ponta = self.__tambor[0]
            self.__tambor.remove(self.__ponta)
            return True
        else:
            return False

    def writePage(self) -> None:
        if self.HasGrafite() == False:
            print("fail: nao existe grafite no bico")
            return
        
        assert self.__ponta is not None
        gasto = self.__ponta.usagepersheet()
        tam_A = self.__ponta.getSize()
        if self.__ponta.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return

        if tam_A - gasto < 10:
            self.__ponta.setSize(10)
            print("fail: folha incompleta")
            return
        
        self.__ponta.setSize(tam_A - gasto)

    def __str__(self) -> str:
        aux = ""
        if self.__ponta != None:
            aux = f"[{self.__ponta}]" #to chamando
        else:
            aux = "[]"
        aux2 = ""
        for x in self.__tambor:
            aux2 += f"[{x}]"

        return f"calibre: {self.__calibre}, bico: {aux}, tambor: <{aux2}>" 
      
def main():
    pencil: Pencil | None = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "init":
            calibre = float(args[1])
            pencil = Pencil(calibre)
        elif args[0] == "remove":
            if pencil:
                pencil.remove()
            else:
                print("fail: remover")
        elif args[0] == "insert":
            if not pencil:
               print("fail")
               continue
            teste = Grafite(float(args[1]),(args[2]), int (args[3]))
            pencil.insert(teste)
        elif args[0] == "write":
            assert pencil is not None
            pencil.writePage()
        elif args[0] == "pull":
            assert pencil is not None
            pencil.pull()

main()