
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def get_nome(self):
        #Chamando get sem utilizar os ().
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        #Usando setter sem precisar chamar ().
        self.__nome = nome

