from domeniu.materie import Materie
from infrastructura.repo_materii import RepoMaterii


class FileRepoMaterii(RepoMaterii):

    def __init__(self, calea_catre_fisier):
        RepoMaterii.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_to_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._materii.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_materie = int(parts[0])
                    nume = parts[1]
                    profesor = parts[2]
                    materie = Materie(id_materie, nume, profesor)
                    self._materii[id_materie] = materie

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for materie in self._materii.values():
                f.write(str(materie)+"\n")

    def adauga_materie(self, materie):
        self.__read_all_to_file()
        RepoMaterii.adauga_materie(self, materie)
        self.__write_all_to_file()

    def modifica_materie(self, materie):
        self.__read_all_to_file()
        RepoMaterii.modifica_materie(self, materie)
        self.__write_all_to_file()

    def sterge_materie_dupa_id(self, id_materie):
        self.__read_all_to_file()
        RepoMaterii.sterge_materie_dupa_id(self, id_materie)
        self.__write_all_to_file()

    def cauta_materie_dupa_id(self, id_materie):
        self.__read_all_to_file()
        return RepoMaterii.cauta_materie_dupa_id(self, id_materie)

    def get_all(self):
        self.__read_all_to_file()
        return RepoMaterii.get_all(self)

    def size(self):
        self.__read_all_to_file()
        return len(self._materii)
