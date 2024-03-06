from business.service_materii import ServiceMaterii
from business.service_note import ServiceNote
from business.service_studenti import ServiceStudenti
from erori.Repository_Error import RepoError
from infrastructura.file_repo_materii import FileRepoMaterii
from infrastructura.file_repo_note import FileRepoNote
from infrastructura.file_repo_studenti import FileRepoStudenti
from infrastructura.repo_materii import RepoMaterii
from infrastructura.repo_note import RepoNote
from infrastructura.repo_studenti import RepoStudenti
from validare.validator_materie import ValidatorMaterie
from validare.validator_note import ValidatorNote
from validare.validator_student import ValidatorStudent


class Teste:
    def __init__(self):
        pass

    def test_asign_nota(self):
        reMat = RepoMaterii()
        reStd = RepoStudenti()
        reNot = RepoNote()
        cale_Mat = "testare/test_materii.txt"
        freMat = FileRepoMaterii(cale_Mat)
        cale_Std = "testare/test_studenti.txt"
        freStd = FileRepoStudenti(cale_Std)
        cale_Not = "testare/test_note.txt"
        freNot = FileRepoNote(cale_Not)

        notaVal = ValidatorNote()
        studVal = ValidatorStudent()
        matVal = ValidatorMaterie()

        svNote = ServiceNote(notaVal, reNot, reStd, reMat, freStd, freMat, freNot)
        svStud = ServiceStudenti(studVal, reStd, freStd)
        svMat = ServiceMaterii(matVal, reMat, freMat)

        svStud.adauga_student(1, 'ion')
        assert int(reStd.cauta_student_dupa_id(1).get_id_student()) == 1
        assert reStd.cauta_student_dupa_id(1).get_nume() == 'ion'
        svMat.adauga_materie(1, 'asc', 'vancea')
        assert reMat.cauta_materie_dupa_id(1).get_id_materie() == 1
        assert reMat.cauta_materie_dupa_id(1).get_nume_materie() == 'asc'
        assert reMat.cauta_materie_dupa_id(1).get_profesor_materie() == 'vancea'
        # print(reStd.cauta_student_dupa_id(1))
        # print(reMat.cauta_materie_dupa_id(1))
        svNote.asignare_nota(1, 1, 1, 10)
        # print(reNot.cauta_nota_dupa_id(1))
        assert float(reNot.cauta_nota_dupa_id(1).get_nota()) == 10
        assert int((reNot.cauta_nota_dupa_id(1).get_id_nota())) == 1
        assert int(len(reNot.get_all())) == 1
        svStud.adauga_student(2, 'vasile')
        svMat.adauga_materie(2, 'fp', 'istvan')
        svNote.asignare_nota(2, 2, 2, 8.35)
        assert int(len(reNot.get_all())) == 2
        # print(reNot.cauta_nota_dupa_id(2))
        try:
            svStud.adauga_student(2, 'marian')
            assert False
        except RepoError:
            pass
        try:
            svMat.adauga_materie(2, 'lc', 'diana pop')
            assert False
        except RepoError:
            pass
        svStud.adauga_student(3, 'marian')
        svMat.adauga_materie(3, 'lc', 'diana pop')
        try:
            svNote.asignare_nota(2, 3, 3, 7.35)
            assert False
        except RepoError:
            pass
        assert int(len(reNot.get_all())) == 2

    def test_sterge_student_si_notele_lui(self):
        reMat = RepoMaterii()
        reStd = RepoStudenti()
        reNot = RepoNote()
        cale_Mat = "testare/test_materii.txt"
        freMat = FileRepoMaterii(cale_Mat)
        cale_Std = "testare/test_studenti.txt"
        freStd = FileRepoStudenti(cale_Std)
        cale_Not = "testare/test_note.txt"
        freNot = FileRepoNote(cale_Not)

        notaVal = ValidatorNote()
        studVal = ValidatorStudent()
        matVal = ValidatorMaterie()

        svNote = ServiceNote(notaVal, reNot, reStd, reMat, freStd, freMat, freNot)
        svStud = ServiceStudenti(studVal, reStd, freStd)
        svMat = ServiceMaterii(matVal, reMat, freMat)

        svStud.adauga_student(1, 'ion')
        svMat.adauga_materie(1, 'asc', 'vancea')
        svNote.asignare_nota(1, 1, 1, 10)

        assert int(len(reNot.get_all())) == 1
        svNote.sterge_student_si_notele_lui(reStd.cauta_student_dupa_id(1).get_id_student())
        assert int(len(reNot.get_all())) == 0
        assert int(len(reStd.get_all())) == 0

        try:
            svNote.sterge_student_si_notele_lui(reStd.cauta_student_dupa_id(1).get_id_student())
            assert False
        except RepoError:
            pass

    def test_modifica_student_si_notele_lui(self):
        reMat = RepoMaterii()
        reStd = RepoStudenti()
        reNot = RepoNote()
        cale_Mat = "testare/test_materii.txt"
        freMat = FileRepoMaterii(cale_Mat)
        cale_Std = "testare/test_studenti.txt"
        freStd = FileRepoStudenti(cale_Std)
        cale_Not = "testare/test_note.txt"
        freNot = FileRepoNote(cale_Not)

        notaVal = ValidatorNote()
        studVal = ValidatorStudent()
        matVal = ValidatorMaterie()

        svNote = ServiceNote(notaVal, reNot, reStd, reMat, freStd, freMat, freNot)
        svStud = ServiceStudenti(studVal, reStd, freStd)
        svMat = ServiceMaterii(matVal, reMat, freMat)

        svStud.adauga_student(1, 'ion')
        svMat.adauga_materie(1, 'asc', 'vancea')
        svNote.asignare_nota(1, 1, 1, 10)
        assert int(len(reNot.get_all())) == 1

        svStud.modifica_student(1, 'alin')
        # print(reStd.cauta_student_dupa_id(1))
        assert int(len(reStd.get_all())) == 1

        svNote.modifica_student_si_notele_lui(reStd.cauta_student_dupa_id(1).get_id_student())
        # print(reNot.cauta_nota_dupa_id(1))
        assert int(len(reNot.get_all())) == 1
        assert int(len(reStd.get_all())) == 1

        try:
            svNote.modifica_student_si_notele_lui(reStd.cauta_student_dupa_id(2).get_id_student())
            assert False
        except RepoError:
            pass

    def test_sortare_dupa_valoare(self):
        reMat = RepoMaterii()
        reStd = RepoStudenti()
        reNot = RepoNote()
        cale_Mat = "testare/test_materii.txt"
        freMat = FileRepoMaterii(cale_Mat)
        cale_Std = "testare/test_studenti.txt"
        freStd = FileRepoStudenti(cale_Std)
        cale_Not = "testare/test_note.txt"
        freNot = FileRepoNote(cale_Not)

        notaVal = ValidatorNote()
        studVal = ValidatorStudent()
        matVal = ValidatorMaterie()

        svNote = ServiceNote(notaVal, reNot, reStd, reMat, freStd, freMat, freNot)
        svStud = ServiceStudenti(studVal, reStd, freStd)
        svMat = ServiceMaterii(matVal, reMat, freMat)

        svStud.adauga_student(1, 'ion')
        svMat.adauga_materie(1, 'asc', 'vancea')
        svNote.asignare_nota(1, 1, 1, 10)
        svNote.asignare_nota(4, 1, 1, 2.55)
        svNote.asignare_nota(5, 1, 1, 6.55)

        svStud.adauga_student(2, 'vlad')
        svNote.asignare_nota(2, 2, 1, 8.33)
        svNote.asignare_nota(7, 2, 1, 3.55)

        svStud.adauga_student(3, 'marian')
        svMat.adauga_materie(2, 'fp', 'vancea')
        svNote.asignare_nota(3, 3, 2, 6.55)
        svNote.asignare_nota(8, 3, 1, 6.55)

        svStud.adauga_student(4, 'catalin')
        svMat.adauga_materie(3, 'lc', 'pop diana')
        svNote.asignare_nota(6, 3, 3, 6.88)

        # print(reStd.get_all())
        # print(reNot.get_all())

        assert int(len(reStd.get_all())) == 4
        assert int(len(reNot.get_all())) == 8

        note = svNote.sortare_note_dupa_valoare(reMat.cauta_materie_dupa_id(1).get_id_materie())
        # for nota in note:
        #   print(nota)

    def test_sefi_promotie(self):
        reMat = RepoMaterii()
        reStd = RepoStudenti()
        reNot = RepoNote()
        cale_Mat = "testare/test_materii.txt"
        freMat = FileRepoMaterii(cale_Mat)
        cale_Std = "testare/test_studenti.txt"
        freStd = FileRepoStudenti(cale_Std)
        cale_Not = "testare/test_note.txt"
        freNot = FileRepoNote(cale_Not)

        notaVal = ValidatorNote()
        studVal = ValidatorStudent()
        matVal = ValidatorMaterie()

        svNote = ServiceNote(notaVal, reNot, reStd, reMat, freStd, freMat, freNot)
        svStud = ServiceStudenti(studVal, reStd, freStd)
        svMat = ServiceMaterii(matVal, reMat, freMat)

        svStud.adauga_student(1, 'ion')
        svMat.adauga_materie(1, 'asc', 'vancea')
        svNote.asignare_nota(1, 1, 1, 10)
        svNote.asignare_nota(4, 1, 1, 2.55)
        svNote.asignare_nota(5, 1, 1, 6.55)

        svStud.adauga_student(2, 'vlad')
        svNote.asignare_nota(2, 2, 1, 8.33)
        svNote.asignare_nota(7, 2, 1, 3.55)

        svStud.adauga_student(3, 'marian')
        svMat.adauga_materie(2, 'fp', 'vancea')
        svNote.asignare_nota(3, 3, 2, 6.55)
        svNote.asignare_nota(8, 3, 1, 6.55)

        svStud.adauga_student(4, 'catalin')
        svMat.adauga_materie(3, 'lc', 'pop diana')
        svNote.asignare_nota(6, 3, 3, 6.88)

        sefi_promotie = svNote.get_sefi_promotie()
        assert len(sefi_promotie) == 1
        # for sef_promotie in sefi_promotie:
        #   print(sef_promotie)

    def test_primii_20_la_suta(self):
        reMat = RepoMaterii()
        reStd = RepoStudenti()
        reNot = RepoNote()
        cale_Mat = "testare/test_materii.txt"
        freMat = FileRepoMaterii(cale_Mat)
        cale_Std = "testare/test_studenti.txt"
        freStd = FileRepoStudenti(cale_Std)
        cale_Not = "testare/test_note.txt"
        freNot = FileRepoNote(cale_Not)

        notaVal = ValidatorNote()
        studVal = ValidatorStudent()
        matVal = ValidatorMaterie()

        svNote = ServiceNote(notaVal, reNot, reStd, reMat, freStd, freMat, freNot)
        svStud = ServiceStudenti(studVal, reStd, freStd)
        svMat = ServiceMaterii(matVal, reMat, freMat)

        svStud.adauga_student(1, 'ion')
        svMat.adauga_materie(1, 'asc', 'vancea')
        svNote.asignare_nota(1, 1, 1, 10)
        svNote.asignare_nota(4, 1, 1, 2.55)
        svNote.asignare_nota(5, 1, 1, 6.55)

        svStud.adauga_student(2, 'vlad')
        svNote.asignare_nota(2, 2, 1, 8.33)
        svNote.asignare_nota(7, 2, 1, 3.55)

        svStud.adauga_student(3, 'marian')
        svMat.adauga_materie(2, 'fp', 'vancea')
        svNote.asignare_nota(3, 3, 2, 6.55)
        svNote.asignare_nota(8, 3, 1, 6.55)

        svStud.adauga_student(4, 'catalin')
        svMat.adauga_materie(3, 'lc', 'pop diana')
        svNote.asignare_nota(6, 3, 3, 6.88)
        svNote.asignare_nota(17, 4, 3, 6.98)

        svStud.adauga_student(5, 'adelin')
        svNote.asignare_nota(9, 5, 1, 7.65)
        svNote.asignare_nota(10, 5, 1, 5.55)
        svNote.asignare_nota(11, 5, 1, 7.55)

        svStud.adauga_student(6, 'rares')
        svNote.asignare_nota(12, 6, 1, 8.33)
        svNote.asignare_nota(13, 6, 1, 5.55)

        svStud.adauga_student(7, 'robert')
        svNote.asignare_nota(14, 7, 2, 7.55)
        svNote.asignare_nota(15, 7, 1, 4.55)

        svStud.adauga_student(8, 'marcu')
        svNote.asignare_nota(16, 8, 3, 7.88)

        #medii = svNote.get_primii_20_la_suta()
        #for elev in medii:
         #   print(elev)

        sefi_promotie = svNote.get_sefi_promotie()
        assert len(sefi_promotie) == 1
        #for sef_promotie in sefi_promotie:
        #   print(sef_promotie)

        sefi_promotie = svNote.get_primii_20_la_suta()
        assert int(len(sefi_promotie)/4) == 2
        #for index in range(int(len(sefi_promotie)/4)):
         #  print(sefi_promotie[index])

    def ruleaza_toate_testele(self):
        self.test_asign_nota()
        self.test_sterge_student_si_notele_lui()
        self.test_modifica_student_si_notele_lui()
        self.test_sortare_dupa_valoare()
        self.test_sefi_promotie()
        self.test_primii_20_la_suta()
