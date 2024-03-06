from domeniu.student import Student


class ServiceStudenti:
    def __init__(self, validator_student, repo_studenti, file_repo_studenti):
        self.__validator_student = validator_student
        self.__repo_studenti = repo_studenti
        self.__file_repo_studenti = file_repo_studenti

    def adauga_student(self, id_student, nume):
        student = Student(id_student, nume)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.adauga_student(student)

    def adauga_student_file(self, id_student, nume):
        student = Student(id_student, nume)
        self.__validator_student.valideaza(student)
        self.__file_repo_studenti.adauga_student(student)

    def sterge_student(self, id_student):
        self.__repo_studenti.sterge_student_dupa_id(id_student)

    def sterge_student_file(self, id_student):
        self.__file_repo_studenti.sterge_student_dupa_id(id_student)

    def cauta_student(self, id_student):
        return self.__repo_studenti.cauta_student_dupa_id(id_student)

    def cauta_student_file(self, id_student):
        return self.__file_repo_studenti.cauta_student_dupa_id(id_student)

    def modifica_student(self, id_student, nume):
        student = Student(id_student, nume)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.modifica_student(student)

    def modifica_student_file(self, id_student, nume):
        student = Student(id_student, nume)
        self.__validator_student.valideaza(student)
        self.__file_repo_studenti.modifica_student(student)

    def get_all_studenti(self):
        return self.__repo_studenti.get_all()

    def get_all_studenti_file(self):
        return self.__file_repo_studenti.get_all()
