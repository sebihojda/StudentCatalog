from infrastructura.file_repo_materii import FileRepoMaterii
from infrastructura.file_repo_note import FileRepoNote
from infrastructura.file_repo_studenti import FileRepoStudenti
from validare.validator_student import ValidatorStudent
from validare.validator_materie import ValidatorMaterie
from validare.validator_note import ValidatorNote
from infrastructura.repo_note import RepoNote
from infrastructura.repo_materii import RepoMaterii
from infrastructura.repo_studenti import RepoStudenti
from business.service_note import ServiceNote
from business.service_materii import ServiceMaterii
from business.service_studenti import ServiceStudenti
from prezentare.consola import UI
from testare.teste import *

if __name__ == '__main__':
    validator_student = ValidatorStudent()
    validator_materie = ValidatorMaterie()
    validator_note = ValidatorNote()
    repo_studenti = RepoStudenti()
    repo_materii = RepoMaterii()
    repo_note = RepoNote()
    cale_studenti = "studenti.txt"
    file_repo_studenti = FileRepoStudenti(cale_studenti)
    cale_materii = "materii.txt"
    file_repo_materii = FileRepoMaterii(cale_materii)
    cale_note = "note.txt"
    file_repo_note = FileRepoNote(cale_note)
    service_studenti = ServiceStudenti(validator_student, repo_studenti, file_repo_studenti)
    service_materii = ServiceMaterii(validator_materie, repo_materii, file_repo_materii)
    service_note = ServiceNote(validator_note, repo_note, repo_studenti, repo_materii, file_repo_studenti, file_repo_materii, file_repo_note)
    consola = UI(service_studenti, service_materii, service_note)
    teste = Teste()
    teste.ruleaza_toate_testele()
    consola.run()
