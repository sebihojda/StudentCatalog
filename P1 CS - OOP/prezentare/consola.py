import random
import string

from erori.Repository_Error import RepoError
from erori.Validation_Error import ValidError


class UI:

    def __init__(self, service_studenti, service_materii, service_note):
        self.__service_studenti = service_studenti
        self.__service_materii = service_materii
        self.__service_note = service_note
        self.__comenzi = {
            "primii_20_la_suta_file": self.__ui_primii_20_la_suta_file,
            "sefi_promotie_file": self.__ui_sefi_promotie_file,
            "asignare_nota_file": self.__ui_asignare_nota_file,
            "sortare_dupa_valoare_file": self.__ui_sortare_note_dupa_valoare_file,
            "sortare_dupa_nume_file": self.__ui_sortare_note_dupa_nume_file,
            "print_note_file": self.__ui_print_note_file,
            "adauga_materie_file": self.__ui_adauga_materie_file,
            "cauta_materie_file": self.__ui_cauta_materie_file,
            "modifica_materie_file": self.__ui_modifica_materie_si_note_file,
            "sterge_materie_file": self.__ui_sterge_materie_si_note_file,
            "print_materii_file": self.__ui_print_materii_file,
            "adauga_student_file": self.__adauga_student_file,
            "cauta_student_file": self.__cauta_student_file,
            "modifica_student_file": self.__ui_modifica_student_si_note_file,
            "sterge_student_file": self.__ui_sterge_student_si_note_file,
            "print_studenti_file": self.__print_studenti_file,
            "help": self.__help,
            "adauga_student": self.__ui_adauga_student,
            "adauga_student_random": self.__ui_adauga_student_random,
            "adauga_materie": self.__ui_adauga_materie,
            "adauga_materie_random": self.__ui_adauga_materie_random,
            "cauta_student": self.__ui_cauta_student,
            "cauta_materie": self.__ui_cauta_materie,
            "modifica_student": self.__ui_modifica_student_si_note,
            "modifica_materie": self.__ui_modifica_materie_si_note,
            "print_studenti": self.__ui_print_studenti,
            "print_materii": self.__ui_print_materii,
            "sterge_student": self.__ui_sterge_student_si_note,
            "sterge_materie": self.__ui_sterge_materie_si_note,
            "asignare_nota": self.__ui_asignare_nota,
            "asignare_nota_random": self.__ui_asignare_nota_random,
            "print_note": self.__ui_print_note,
            "sortare_dupa_valoare": self.__ui_sortare_note_dupa_valoare,
            "sortare_dupa_nume": self.__ui_sortare_note_dupa_nume,
            "sefi_promotie": self.__ui_sefi_promotie,
            "primii_20_la_suta": self.__ui_primii_20_la_suta
        }

    def __ui_primii_20_la_suta_file(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        sefi_promotie = self.__service_note.get_primii_20_la_suta_file()
        if len(sefi_promotie) == 0:
            print("Nu exista note alocate studentilor!")
        else:
            if int(len(sefi_promotie) / 4) > 0:
                for index in range(int(len(sefi_promotie) / 4)):
                    print(sefi_promotie[index])
            else:
                print(sefi_promotie[0])

    def __ui_sefi_promotie_file(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        sefi_promotie = self.__service_note.get_sefi_promotie_file()
        for sef_promotie in sefi_promotie:
            print(sef_promotie)

    def __ui_sortare_note_dupa_nume_file(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        note_sortate = self.__service_note.sortare_note_dupa_nume_file(id_materie)
        for nota in note_sortate:
            print(nota)

    def __ui_sortare_note_dupa_valoare_file(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        note_sortate = self.__service_note.sortare_note_dupa_valoare_file(id_materie)
        for nota in note_sortate:
            print(nota)

    def __ui_asignare_nota_file(self):
        if len(self.__params) != 4:
            print("numar parametrii invalid!")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        id_materie = int(self.__params[2])
        valoare = float(self.__params[3])
        self.__service_note.asignare_nota_file(id_nota, id_student, id_materie, valoare)
        print("nota asignata cu succes")

    def __ui_print_note_file(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        note = self.__service_note.get_all_note_file()
        if len(note) == 0:
            print("nu exista note in aplicatie!")
            return
        for nota in note:
            print(nota)

    def __ui_sterge_materie_si_note_file(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        self.__service_note.sterge_materie_si_notele_ei_file(id_materie)
        print(f"materia cu id: {id_materie} si notele ei sterse cu succes!")

    def __ui_modifica_materie_si_note_file(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        nume = self.__params[1]
        profesor = self.__params[2]
        self.__service_materii.modifica_materie_file(id_materie, nume, profesor)
        self.__service_note.modifica_materie_si_notele_ei_file(id_materie)
        print("materie modificata cu succes")

    def __ui_cauta_materie_file(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        materie = self.__service_materii.cauta_materie_file(id_materie)
        print(materie)

    def __ui_adauga_materie_file(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        nume = self.__params[1]
        profesor = self.__params[2]
        self.__service_materii.adauga_materie_file(id_materie, nume, profesor)
        print("materie adaugata cu succes")

    def __ui_print_materii_file(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        materii = self.__service_materii.get_all_materii_file()
        if len(materii) == 0:
            print("nu exista materii in aplicatie!")
            return
        for materie in materii:
            print(materie)

    def __ui_sterge_student_si_note_file(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        self.__service_note.sterge_student_si_notele_lui_file(id_student)
        print(f"studentul cu id: {id_student} si notele lui sterse cu succes!")

    def __ui_modifica_student_si_note_file(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        self.__service_studenti.modifica_student_file(id_student, nume)
        self.__service_note.modifica_student_si_notele_lui_file(id_student)
        print("student modificat cu succes")

    def __cauta_student_file(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        student = self.__service_studenti.cauta_student_file(id_student)
        print(student)

    def __adauga_student_file(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        self.__service_studenti.adauga_student_file(id_student, nume)
        print("student adaugat cu succes")

    def __print_studenti_file(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        studenti = self.__service_studenti.get_all_studenti_file()
        if len(studenti) == 0:
            print("nu exista studenti in aplicatie!")
            return
        for student in studenti:
            print(student)

    def __help(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        for cheie in self.__comenzi.keys():
            print(f"{cheie}")

    def __ui_sefi_promotie(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        sefi_promotie = self.__service_note.get_sefi_promotie()
        for sef_promotie in sefi_promotie:
            print(sef_promotie)

    def __ui_primii_20_la_suta(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        sefi_promotie = self.__service_note.get_primii_20_la_suta()
        if len(sefi_promotie) == 0:
            print("Nu exista note alocate studentilor!")
        else:
            if int(len(sefi_promotie)/4) > 0:
                for index in range(int(len(sefi_promotie)/4)):
                    print(sefi_promotie[index])
            else:
                print(sefi_promotie[0])

    def __ui_print_studenti(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        studenti = self.__service_studenti.get_all_studenti()
        if len(studenti) == 0:
            print("nu exista studenti in aplicatie!")
            return
        for student in studenti:
            print(student)

    def __ui_print_materii(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        materii = self.__service_materii.get_all_materii()
        if len(materii) == 0:
            print("nu exista materii in aplicatie!")
            return
        for materie in materii:
            print(materie)

    def __ui_sterge_student_si_note(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        self.__service_note.sterge_student_si_notele_lui(id_student)
        print(f"studentul cu id: {id_student} si notele lui sterse cu succes!")

    def __ui_adauga_student(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        self.__service_studenti.adauga_student(id_student, nume)
        print("student adaugat cu succes")

    def __ui_cauta_student(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        student = self.__service_studenti.cauta_student(id_student)
        print(student)

    def __ui_modifica_student_si_note(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        self.__service_studenti.modifica_student(id_student, nume)
        self.__service_note.modifica_student_si_notele_lui(id_student)
        print("student modificat cu succes")

    def __ui_adauga_materie(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        nume = self.__params[1]
        profesor = self.__params[2]
        self.__service_materii.adauga_materie(id_materie, nume, profesor)
        print("materie adaugata cu succes")

    def __ui_cauta_materie(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        materie = self.__service_materii.cauta_materie(id_materie)
        print(materie)

    def __ui_sterge_materie_si_note(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        self.__service_note.sterge_materie_si_notele_ei(id_materie)
        print(f"materia cu id: {id_materie} si notele ei sterse cu succes!")

    def __ui_modifica_materie_si_note(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        nume = self.__params[1]
        profesor = self.__params[2]
        self.__service_materii.modifica_materie(id_materie, nume, profesor)
        self.__service_note.modifica_materie_si_notele_ei(id_materie)
        print("materie modificata cu succes")

    def __ui_asignare_nota(self):
        if len(self.__params) != 4:
            print("numar parametrii invalid!")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        id_materie = int(self.__params[2])
        valoare = float(self.__params[3])
        self.__service_note.asignare_nota(id_nota, id_student, id_materie, valoare)
        print("nota asignata cu succes")

    def __ui_asignare_nota_random(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        id_materie = int(self.__params[2])
        valoare = int(random.randint(1, 10))
        self.__service_note.asignare_nota(id_nota, id_student, id_materie, valoare)
        print("nota asignata cu succes")

    def __ui_adauga_student_random(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        length_random = int(self.__params[1])
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length_random))
        nume = str(result_str)
        self.__service_studenti.adauga_student(id_student, nume)
        print("student adaugat cu succes")

    def __ui_adauga_materie_random(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        length_random = int(self.__params[1])
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length_random))
        nume = str(result_str)
        length_random = int(self.__params[2])
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length_random))
        profesor = str(result_str)
        self.__service_materii.adauga_materie(id_materie, nume, profesor)
        print("materie adaugata cu succes")

    def __ui_print_note(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        note = self.__service_note.get_all_note()
        if len(note) == 0:
            print("nu exista note in aplicatie!")
            return
        for nota in note:
            print(nota)

    def __ui_sortare_note_dupa_valoare(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        note_sortate = self.__service_note.sortare_note_dupa_valoare(id_materie)
        for nota in note_sortate:
            print(nota)

    def __ui_sortare_note_dupa_nume(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_materie = int(self.__params[0])
        note_sortate = self.__service_note.sortare_note_dupa_nume(id_materie)
        for nota in note_sortate:
            print(nota)

    def run(self):
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid!")
                except ValidError as ve:
                    print(f"Valid Error:{ve}")
                except RepoError as re:
                    print(f"RepoError:{re}")
            else:
                print("Comanda invalida!")
