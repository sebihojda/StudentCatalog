from erori.Validation_Error import ValidError


class ValidatorStudent:
    def __init__(self):
        pass

    def valideaza(self, student):
        erori = ""
        if student.get_id_student() < 0:
            erori += "id invalid!"
        if student.get_nume() == "":
            erori += "nume invalid!"
        if len(erori) > 0:
            raise ValidError(erori)
