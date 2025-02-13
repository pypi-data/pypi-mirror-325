import flet as ft
from .styles import Colors, FontSize
from datetime import date as dateT

today = dateT.today().strftime("%d-%m-%Y")


class Date(ft.Container):
    """
    Un componente personalizado para mostrar una fecha.

    El componente `Date` combina un texto de plantilla ("Fecha:") con una fecha especificada por el usuario.
    Es ideal para aplicaciones que necesiten mostrar fechas con un formato específico de manera consistente.

    Este componente se construye sobre el control `Container` de Flet y utiliza una fila (`Row`) para alinear el texto de la plantilla y la fecha.

    Ejemplo:

    ```
    import flet as ft

    def main(page: ft.Page):
        date_display = Date(date="25 - 01 - 2025", template="Fecha:")
        page.add(date_display)

    ft.app(target=main)
    ```
    -----

    Observación: Puedes modificar directamente  el control del template o del date haciendo referencia a los Atributos ``text_template`` y ``text_date`` respectivamente.

    -----

    Online docs: (Enlace a documentación personalizada si aplica)
    """

    def __init__(self, date: str = today, template: str = None):

        super().__init__()
        self.__date = date
        self.__template = template

        self.text_template = ft.Text(
            value=self.__template,
            size=FontSize.normal_font_size,
            weight=ft.FontWeight.W_600,
        )
        self.text_date = ft.Text(
            value=self.__date,
            size=FontSize.normal_font_size,
            weight=ft.FontWeight.W_600,
        )
        self.content = ft.Row(controls=[self.text_template, self.text_date])

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if isinstance(date, dateT):
            date = date.strftime("%d-%m-%Y")
        self.__date = date
        self.text_date.value = self.__date

    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, template):
        self.__template = template
        self.text_template.value = self.__template
