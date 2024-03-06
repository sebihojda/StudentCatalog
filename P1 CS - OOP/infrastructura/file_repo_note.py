from domeniu.materie import Materie
from domeniu.nota import Nota
from domeniu.student import Student
from infrastructura.repo_note import RepoNote


class FileRepoNote(RepoNote):

    def __init__(self, calea_catre_fisier):
        RepoNote.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_nota = int(parts[0])
                    id_student = int(parts[1])
                    nume_student = parts[2]
                    student = Student(id_student, nume_student)
                    id_materie = int(parts[3])
                    nume_materie = parts[4]
                    profesor = parts[5]
                    materie = Materie(id_materie, nume_materie, profesor)
                    valoare_nota = parts[6]
                    nota = Nota(id_nota, student, materie, valoare_nota)
                    self._note[id_nota] = nota

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for nota in self._note.values():
                f.write(Nota.print(nota)+"\n")

    def adauga_nota(self, nota):
        self.__read_all_from_file()
        RepoNote.adauga_nota(self, nota)
        self.__write_all_to_file()

    def sterge_nota_dupa_id(self, id_nota):
        self.__read_all_from_file()
        RepoNote.sterge_nota_dupa_id(self, id_nota)
        self.__write_all_to_file()

    def modifica_nota(self, nota):
        self.__read_all_from_file()
        RepoNote.modifica_nota(self, nota)
        self.__write_all_to_file()

    def cauta_nota_dupa_id(self, id_nota):
        self.__read_all_from_file()
        return RepoNote.cauta_nota_dupa_id(self, id_nota)

    def get_all(self):
        self.__read_all_from_file()
        return RepoNote.get_all(self)

    def size(self):
        self.__read_all_from_file()
        return len(self._note)
