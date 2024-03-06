from erori.Repository_Error import RepoError


class RepoMaterii:

    def __init__(self):
        self._materii = {}

    def adauga_materie(self, materie):
        if materie.get_id_materie() in self._materii:
            raise RepoError("materie existenta!")
        self._materii[materie.get_id_materie()] = materie

    def sterge_materie_dupa_id(self, id_materie):
        if id_materie not in self._materii:
            raise RepoError("materie inexistenta!")
        del self._materii[id_materie]
        # self.__studenti[id_student].sterge()

    def cauta_materie_dupa_id(self, id_materie):
        if id_materie not in self._materii:
            raise RepoError("materie inexistenta!")
        return self._materii[id_materie]

    def modifica_materie(self, materie):
        if materie.get_id_materie() not in self._materii:
            raise RepoError("materie inexistenta!")
        self._materii[materie.get_id_materie()] = materie

    def get_all(self):
        materii = []
        for materie_id in self._materii:
            materii.append(self._materii[materie_id])
        return materii

    def __len__(self):
        return len(self._materii)
