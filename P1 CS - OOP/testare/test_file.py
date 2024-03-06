import unittest

from business.service_materii import ServiceMaterii
from business.service_note import ServiceNote
from business.service_studenti import ServiceStudenti
from erori.Repository_Error import RepoError
from erori.Validation_Error import ValidError
from infrastructura.file_repo_materii import FileRepoMaterii
from infrastructura.file_repo_note import FileRepoNote
from infrastructura.file_repo_studenti import FileRepoStudenti
from infrastructura.repo_materii import RepoMaterii
from infrastructura.repo_note import RepoNote
from infrastructura.repo_studenti import RepoStudenti
from validare.validator_materie import ValidatorMaterie
from validare.validator_note import ValidatorNote
from validare.validator_student import ValidatorStudent


class TestNoteService(unittest.TestCase):

    def setUp(self):
        #   code executed before every testMethod
        reMat = RepoMaterii()
        reStd = RepoStudenti()
        reNot = RepoNote()
        cale_Mat = r"C:\Users\Sebi\PycharmProjects\P1 CS - OOP\testare\test_materii.txt"
        freMat = FileRepoMaterii(cale_Mat)
        cale_Std = r"C:\Users\Sebi\PycharmProjects\P1 CS - OOP\testare\test_studenti.txt"
        freStd = FileRepoStudenti(cale_Std)
        cale_Not = r"C:\Users\Sebi\PycharmProjects\P1 CS - OOP\testare\test_note.txt"
        freNot = FileRepoNote(cale_Not)

        notaVal = ValidatorNote()
        studVal = ValidatorStudent()
        matVal = ValidatorMaterie()

        self.svNote = ServiceNote(notaVal, reNot, reStd, reMat, freStd, freMat, freNot)
        self.svStud = ServiceStudenti(studVal, reStd, freStd)
        self.svMat = ServiceMaterii(matVal, reMat, freMat)

        self.svStud.adauga_student_file(1, "Ion")
        self.svMat.adauga_materie_file(1, "ASC", "Vancea")
        self.svNote.asignare_nota_file(1, 1, 1, 7.77)

    def tearDown(self):
        cale_Mat = r"C:\Users\Sebi\PycharmProjects\P1 CS - OOP\testare\test_materii.txt"
        with open(cale_Mat, "w") as f:
            pass
        cale_Std = r"C:\Users\Sebi\PycharmProjects\P1 CS - OOP\testare\test_studenti.txt"
        with open(cale_Std, "w") as f:
            pass
        cale_Not = r"C:\Users\Sebi\PycharmProjects\P1 CS - OOP\testare\test_note.txt"
        with open(cale_Not, "w") as f:
            pass

    def test_asignare(self):
        self.assertTrue(len(self.svNote.get_all_note_file()) == 1)
        # test for an invalid student
        self.assertRaises(RepoError, self.svNote.asignare_nota_file, 2, 2, 1, 3.44)
        # test for duplicated id
        self.assertRaises(RepoError, self.svNote.asignare_nota_file, 1, 1, 1, 5.66)
        # test for invalid id
        self.assertRaises(ValidError, self.svNote.asignare_nota_file, -1, 1, 1, 8.66)

    def test_sterge_student_si_note(self):
        self.svNote.sterge_student_si_notele_lui_file(1)
        self.assertTrue(len(self.svNote.get_all_note_file()) == 0)
        self.assertTrue(len(self.svStud.get_all_studenti_file()) == 0)
        self.assertTrue(len(self.svMat.get_all_materii_file()) == 1)

    def test_sterge_materie_si_note(self):
        self.svNote.sterge_materie_si_notele_ei_file(1)
        self.assertTrue(len(self.svNote.get_all_note_file()) == 0)
        self.assertTrue(len(self.svStud.get_all_studenti_file()) == 1)
        self.assertTrue(len(self.svMat.get_all_materii_file()) == 0)

    def test_modifica_student_si_note(self):
        self.svStud.modifica_student_file(1, "Vasile")
        self.svNote.modifica_student_si_notele_lui_file(1)
        note = self.svNote.get_all_note_file()
        self.assertTrue(len(note) == 1)
        self.assertTrue(note[0].get_student().get_nume() == "Vasile")

    def test_modifica_materie_si_note(self):
        self.svMat.modifica_materie_file(1, "FP", "Istvan")
        self.svNote.modifica_materie_si_notele_ei_file(1)
        note = self.svNote.get_all_note_file()
        self.assertTrue(len(note) == 1)
        self.assertTrue(note[0].get_materie().get_nume_materie() == "FP")
        self.assertTrue(note[0].get_materie().get_profesor_materie() == "Istvan")

    def test_sefi_promotie(self):
        self.assertEqual(self.svNote.get_sefi_promotie_file()[0].get_nume(), "Ion")
        self.assertEqual(self.svNote.get_sefi_promotie_file()[0].get_medie(), 7.77)


if __name__ == '__main__':
    unittest.main()
