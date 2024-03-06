from erori.Repository_Error import RepoError


class RepoStudenti:

    def __init__(self):
        self._studenti = {}

    def adauga_student(self, student):
        if student.get_id_student() in self._studenti:
            raise RepoError("student existent!")
        self._studenti[student.get_id_student()] = student

    def sterge_student_dupa_id(self, id_student):
        if id_student not in self._studenti:
            raise RepoError("student inexistent!")
        del self._studenti[id_student]
        # self.__studenti[id_student].sterge()

    def cauta_student_dupa_id(self, id_student):
        if id_student not in self._studenti:
            raise RepoError("student inexistent!")
        return self._studenti[id_student]

    def modifica_student(self, student):
        if student.get_id_student() not in self._studenti:
            raise RepoError("student inexistent!")
        self._studenti[student.get_id_student()] = student

    def get_all(self):
        studenti = []
        for studenti_id in self._studenti:
            studenti.append(self._studenti[studenti_id])
        return studenti

    def length(self, studenti):
        if studenti == []:
            return 0
        return 1 + self.length(studenti[1:])

    def __len__(self):
        return len(self._studenti)

def test_length():
    repo = RepoStudenti()
    #studenti = repo.get_all()
    studenti = list({"1": "Ion", "2": "Vasile"})
    assert repo.length(studenti) == 2

test_length()