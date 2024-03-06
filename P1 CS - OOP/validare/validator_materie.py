from erori.Validation_Error import ValidError


class ValidatorMaterie:
    def __init__(self):
        pass

    def valideaza(self, materie):
        erori = ""
        if materie.get_id_materie() < 0:
            erori += "id invalid!"
        if materie.get_nume_materie() == "":
            erori += "nume invalid!"
        if materie.get_profesor_materie() == "":
            erori += "profesor invalid!"
        if len(erori) > 0:
            raise ValidError(erori)
