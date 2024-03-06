from domeniu.nota import Nota
from domeniu.sef_promotie_DTO import SefPromotieDTO


class ServiceNote:
    def __init__(self, validator_note, repo_note, repo_studenti, repo_materii, file_repo_studenti, file_repo_materii,
                 file_repo_note):
        self.__validator_nota = validator_note
        self.__repo_note = repo_note
        self.__repo_studenti = repo_studenti
        self.__repo_materii = repo_materii
        self.__file_repo_note = file_repo_note
        self.__file_repo_studenti = file_repo_studenti
        self.__file_repo_materii = file_repo_materii

    def asignare_nota(self, id_nota, id_student, id_materie, valoare_nota):
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        materie = self.__repo_materii.cauta_materie_dupa_id(id_materie)
        nota = Nota(id_nota, student, materie, valoare_nota)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.adauga_nota(nota)

    def asignare_nota_file(self, id_nota, id_student, id_materie, valoare_nota):
        student = self.__file_repo_studenti.cauta_student_dupa_id(id_student)
        materie = self.__file_repo_materii.cauta_materie_dupa_id(id_materie)
        nota = Nota(id_nota, student, materie, valoare_nota)
        self.__validator_nota.valideaza(nota)
        self.__file_repo_note.adauga_nota(nota)

    def get_all_note(self):
        return self.__repo_note.get_all()

    def get_all_note_file(self):
        return self.__file_repo_note.get_all()

    def sterge_student_si_notele_lui(self, id_student):
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_student() == student]
        for nota_student in note_student:
            self.__repo_note.sterge_nota_dupa_id(nota_student.get_id_nota())
        self.__repo_studenti.sterge_student_dupa_id(id_student)

    def sterge_student_si_notele_lui_file(self, id_student):
        student = self.__file_repo_studenti.cauta_student_dupa_id(id_student)
        note = self.__file_repo_note.get_all()
        note_student = [x for x in note if x.get_student() == student]
        for nota_student in note_student:
            self.__file_repo_note.sterge_nota_dupa_id(nota_student.get_id_nota())
        self.__file_repo_studenti.sterge_student_dupa_id(id_student)

    def sterge_materie_si_notele_ei(self, id_materie):
        materie = self.__repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        for nota_student in note_student:
            self.__repo_note.sterge_nota_dupa_id(nota_student.get_id_nota())
        self.__repo_materii.sterge_materie_dupa_id(id_materie)

    def sterge_materie_si_notele_ei_file(self, id_materie):
        materie = self.__file_repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__file_repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        for nota_student in note_student:
            self.__file_repo_note.sterge_nota_dupa_id(nota_student.get_id_nota())
        self.__file_repo_materii.sterge_materie_dupa_id(id_materie)

    def modifica_student_si_notele_lui(self, id_student):
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_student() == student]
        for nota_student in note_student:
            nota_student.set_student(student)

    def modifica_student_si_notele_lui_file(self, id_student):
        student = self.__file_repo_studenti.cauta_student_dupa_id(id_student)
        note = self.__file_repo_note.get_all()
        note_student = [x for x in note if x.get_student().get_id_student() == id_student]
        for nota_student in note_student:
            nota_student.set_student(student)
            self.__file_repo_note.modifica_nota(nota_student)

    def modifica_materie_si_notele_ei(self, id_materie):
        materie = self.__repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        for nota_student in note_student:
            nota_student.set_materie(materie)

    def modifica_materie_si_notele_ei_file(self, id_materie):
        materie = self.__file_repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__file_repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        for nota_student in note_student:
            nota_student.set_materie(materie)
            self.__file_repo_note.modifica_nota(nota_student)

    def sortare_note_dupa_valoare(self, id_materie):
        materie = self.__repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        note_student.sort(reverse=True)
        return note_student

    def sortare_note_dupa_valoare_file(self, id_materie):
        materie = self.__file_repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__file_repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        # note_student.sort(key=lambda x: x.get_nota(), reverse=True)
        lista = self.selection_sort(note_student, key=lambda x: x.get_nota(), reverse=True)
        #lista = self.shake_sort(note_student, key=lambda x: x.get_nota(), reverse=True)
        return lista

    def sortare_note_dupa_nume(self, id_materie):
        materie = self.__repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        note_student.sort(key=lambda x: x.get_student().get_nume().casefold())
        return note_student

    def sortare_note_dupa_nume_file(self, id_materie):
        materie = self.__file_repo_materii.cauta_materie_dupa_id(id_materie)
        note = self.__file_repo_note.get_all()
        note_student = [x for x in note if x.get_materie() == materie]
        # note_student.sort(key=lambda x: x.get_student().get_nume().casefold())
        lista = self.selection_sort(note_student, key=lambda x: x.get_student().get_nume().casefold())
        #lista = self.shake_sort(note_student, key=lambda x: x.get_student().get_nume().casefold())
        return lista

    def get_sefi_promotie(self):
        info_studenti = {}
        note = self.__repo_note.get_all()
        for nota in note:
            id_student_nota = nota.get_student().get_id_student()
            valoare_nota = nota.get_nota()
            if id_student_nota not in info_studenti:
                info_studenti[id_student_nota] = []
            info_studenti[id_student_nota].append(valoare_nota)
        sefi_promotie = []
        for id_student in info_studenti:
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            nume_student = student.get_nume()
            medie_student = self.suma(info_studenti[id_student]) / len(info_studenti[id_student])
            sef_promotie_dto = SefPromotieDTO(nume_student, medie_student)
            sefi_promotie.append(sef_promotie_dto)
        sefi_promotie.sort(reverse=True)
        return sefi_promotie[:1]

    def suma(self, lista):
        if lista == []:
            return 0
        return lista[0] + self.suma(lista[1:])

    def get_sefi_promotie_file(self):
        info_studenti = {}
        note = self.__file_repo_note.get_all()
        for nota in note:
            id_student_nota = nota.get_student().get_id_student()
            valoare_nota = float(nota.get_nota())
            if id_student_nota not in info_studenti:
                info_studenti[id_student_nota] = []
            info_studenti[id_student_nota].append(valoare_nota)
        sefi_promotie = []
        for id_student in info_studenti:
            student = self.__file_repo_studenti.cauta_student_dupa_id(id_student)
            nume_student = student.get_nume()
            medie_student = self.suma(info_studenti[id_student]) / len(info_studenti[id_student])
            sef_promotie_dto = SefPromotieDTO(nume_student, medie_student)
            sefi_promotie.append(sef_promotie_dto)
        sefi_promotie.sort(reverse=True)
        return sefi_promotie[:1]

    def get_primii_20_la_suta(self):
        info_studenti = {}
        note = self.__repo_note.get_all()
        for nota in note:
            id_student_nota = nota.get_student().get_id_student()
            valoare_nota = nota.get_nota()
            if id_student_nota not in info_studenti:
                info_studenti[id_student_nota] = []
            info_studenti[id_student_nota].append(valoare_nota)
        sefi_promotie = []
        for id_student in info_studenti:
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            nume_student = student.get_nume()
            medie_student = sum(info_studenti[id_student]) / len(info_studenti[id_student])
            sef_promotie_dto = SefPromotieDTO(nume_student, medie_student)
            sefi_promotie.append(sef_promotie_dto)
        sefi_promotie.sort(reverse=True)
        return sefi_promotie[:]

    def get_primii_20_la_suta_file(self):
        info_studenti = {}
        note = self.__file_repo_note.get_all()
        for nota in note:
            id_student_nota = nota.get_student().get_id_student()
            valoare_nota = float(nota.get_nota())
            if id_student_nota not in info_studenti:
                info_studenti[id_student_nota] = []
            info_studenti[id_student_nota].append(valoare_nota)
        sefi_promotie = []
        for id_student in info_studenti:
            student = self.__file_repo_studenti.cauta_student_dupa_id(id_student)
            nume_student = student.get_nume()
            medie_student = sum(info_studenti[id_student]) / len(info_studenti[id_student])
            sef_promotie_dto = SefPromotieDTO(nume_student, medie_student)
            sefi_promotie.append(sef_promotie_dto)
        sefi_promotie.sort(reverse=True)
        return sefi_promotie[:]

    def selection_sort(self, lista, key=lambda x: x, reverse=False):
        size = len(lista)
        copie_lista = lista
        lista = list(map(key, lista))

        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                # select the minimum element in every iteration
                if lista[j] < lista[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (lista[ind], lista[min_index]) = (lista[min_index], lista[ind])
            copie_lista[ind], copie_lista[min_index] = copie_lista[min_index], copie_lista[ind]

        if reverse == True:
            return reversed(copie_lista)
        else:
            return copie_lista

    def shake_sort(self, a, key=lambda x: x, reverse=False):
        n = len(a)
        copie_lista = a
        a = list(map(key, a))
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True):

            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # loop from left to right same as the bubble
            # sort
            for i in range(start, end):
                if (a[i] > a[i + 1]):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    copie_lista[i], copie_lista[i + 1] = copie_lista[i + 1], copie_lista[i]
                    swapped = True

            # if nothing moved, then array is sorted.
            if (swapped == False):
                break

            # otherwise, reset the swapped flag so that it
            # can be used in the next stage
            swapped = False

            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end - 1

            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end - 1, start - 1, -1):
                if (a[i] > a[i + 1]):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    copie_lista[i], copie_lista[i + 1] = copie_lista[i + 1], copie_lista[i]
                    swapped = True

            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1

        if reverse == True:
            return reversed(copie_lista)
        else:
            return copie_lista
