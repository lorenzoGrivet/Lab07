import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):

        mese=self._view.dd_mese.value

        mese=int(mese)

        if mese<1 or mese > 12:
            self._view.create_alert("Mese non valido")

        risultato=self._model.calcola_um_media(mese)


        self._view.lst_result.clean()

        for a in risultato.keys():
            self._view.lst_result.controls.append(ft.Text(f"{a}: {risultato[a][0]/risultato[a][1]}"))


        self._view.update_page()



    def handle_sequenza(self, e):
        mese = self._view.dd_mese.value

        mese = int(mese)

        if mese < 1 or mese > 12:
            self._view.create_alert("Mese non valido")

        b=self._model.calcola_percorso(mese)
        pass

    def read_mese(self, e):
        self._mese = int(e.control.value)

