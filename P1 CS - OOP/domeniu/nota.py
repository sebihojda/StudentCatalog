class Nota:
    def __init__(self, id_nota, student, materie, nota):
        self.__id_nota = id_nota
        self.__student = student
        self.__materie = materie
        self.__nota = nota
        # self.__sters = False

    '''
    @property
    def materie(self):
        return self.__materie
    @materie.setter
    def materie(self, materieNoua):
        self.__materie = materieNoua
    '''

    def get_student(self):
        return self.__student

    def get_materie(self):
        return self.__materie

    def set_student(self, student):
        self.__student = student

    def set_materie(self, materie):
        self.__materie = materie

    # def get_sters(self):
    #   return self.__sters

    def get_nota(self):
        return float(self.__nota)

    def get_id_nota(self):
        return self.__id_nota

    # def sterge(self):
    #   self.__sters = True

    def print(self):
        return f"{self.__id_nota},{self.__student},{self.__materie},{self.__nota}"

    def __str__(self):
        return f"ID:{self.__id_nota}|Student:{self.__student}|Materie:{self.__materie}|Nota:{self.__nota}"

    def __lt__(self, other):
        return self.__nota < other.__nota
