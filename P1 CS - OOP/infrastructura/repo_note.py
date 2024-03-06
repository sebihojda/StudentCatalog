from erori.Repository_Error import RepoError


class RepoNote:

    def __init__(self):
        self._note = {}

    def adauga_nota(self, nota):
        if nota.get_id_nota() in self._note:
            raise RepoError("nota existenta!")
        self._note[nota.get_id_nota()] = nota

    def sterge_nota_dupa_id(self, id_nota):
        if id_nota not in self._note:
            raise RepoError("nota inexistenta!")
        del self._note[id_nota]

    def cauta_nota_dupa_id(self, id_nota):
        if id_nota not in self._note:
            raise RepoError("nota inexistenta!")
        return self._note[id_nota]

    def modifica_nota(self, nota):
        if nota.get_id_nota() not in self._note:
            raise RepoError("nota inexistenta!")
        self._note[nota.get_id_nota()] = nota

    def get_all(self):
        note = []
        for nota_id in self._note:
            note.append(self._note[nota_id])
        return note

    def __len__(self):
        return len(self._note)
