class Materie:

    def __init__(self, id_materie, nume, profesor):
        self.__id_materie = id_materie
        self.__nume = nume
        self.__profesor = profesor

    def get_profesor_materie(self):
        return self.__profesor

    def get_nume_materie(self):
        return self.__nume

    def get_id_materie(self):
        return self.__id_materie

    def set_profesor(self, profesor):
        self.__profesor = profesor

    def set_nume(self, nume):
        self.__nume = nume

    def __eq__(self, other):
        return self.__id_materie == other.__id_materie

    def __str__(self):
        return f"{self.__id_materie},{self.__nume},{self.__profesor}"
