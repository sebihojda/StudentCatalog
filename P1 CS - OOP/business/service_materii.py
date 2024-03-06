from domeniu.materie import Materie


class ServiceMaterii:

    def __init__(self, validator_materie, repo_materii, file_repo_materii):
        self.__validator_materie = validator_materie
        self.__repo_materii = repo_materii
        self.__file_repo_materii = file_repo_materii

    def adauga_materie(self, id_materie, nume, profesor):
        materie = Materie(id_materie, nume, profesor)
        self.__validator_materie.valideaza(materie)
        self.__repo_materii.adauga_materie(materie)

    def adauga_materie_file(self, id_materie, nume, profesor):
        materie = Materie(id_materie, nume, profesor)
        self.__validator_materie.valideaza(materie)
        self.__file_repo_materii.adauga_materie(materie)

    def sterge_materie(self, id_materie):
        self.__repo_materii.sterge_materie_dupa_id(id_materie)

    def sterge_materie_file(self, id_materie):
        self.__file_repo_materii.sterge_materie_dupa_id(id_materie)

    def cauta_materie(self, id_materie):
        return self.__repo_materii.cauta_materie_dupa_id(id_materie)

    def cauta_materie_file(self, id_materie):
        return self.__file_repo_materii.cauta_materie_dupa_id(id_materie)

    def modifica_materie(self, id_materie, nume, profesor):
        materie = Materie(id_materie, nume, profesor)
        self.__validator_materie.valideaza(materie)
        self.__repo_materii.modifica_materie(materie)

    def modifica_materie_file(self, id_materie, nume, profesor):
        materie = Materie(id_materie, nume, profesor)
        self.__validator_materie.valideaza(materie)
        self.__file_repo_materii.modifica_materie(materie)

    def get_all_materii(self):
        return self.__repo_materii.get_all()

    def get_all_materii_file(self):
        return self.__file_repo_materii.get_all()
