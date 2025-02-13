import flet as ft
from .styles import Colors, FontSize


class TextArea(ft.Row):
    """
    Un componente personalizado que permite al usuario escribir y visualizar texto en formato Markdown.

    `TextArea` combina un área de texto editable con la capacidad de mostrar su contenido
    como Markdown renderizado. Es ideal para tomar notas, redactar documentos breves y ver
    contenido estilizado. El diseño incluye soporte para hover y un marcador de posición.

    Atributos:
        text (str): Texto inicial del área (opcional).
        placeHolder (str): Texto mostrado cuando el área está vacía (opcional).
        height (int): Altura del contenedor principal en píxeles (opcional, por defecto 400).
        width (int): Anchura del contenedor principal en píxeles (opcional, por defecto 400).
        expand (bool): Si el área debe expandirse para ocupar todo el espacio disponible
                       (opcional, por defecto `False`).

    Ejemplo:
        ```python
        import flet as ft
        from mymodule import TextArea

        def main(page: ft.Page):
            textarea = TextArea(
                text="Texto inicial",
                placeHolder="Escribe aquí...",
                height=300,
                width=500
            )
            texto = textarea.get_text() #Obtiene el texto del control
            page.add(textarea)
            print(texto)#Salida: Texto Inicial

        ft.app(target=main)
        ```
    ----
    Observacion. Puedes usar width = None para que el expand = True funcione sin complicaciones. Asi el control se expandera el 100% del ancho del contenedor padre.
    """

    def __init__(
        self,
        text: str = "",
        placeHolder="Escribe una nota...",
        height: int = 400,
        widht: int = 400,
        expand=False,
    ):

        super().__init__()
        """
        Inicializa un componente `TextArea`.

        Args:
            text (str, opcional): Texto inicial del área. Por defecto, vacío.
            placeHolder (str, opcional): Texto mostrado cuando el área está vacía.
                                         Por defecto, "Escribe una nota...".
            height (int, opcional): Altura del componente en píxeles. Por defecto, 400.
            widht (int, opcional): Anchura del componente en píxeles. Por defecto, 400.
            expand (bool, opcional): Indica si el componente debe expandirse para llenar el espacio disponible. Por defecto, `False`.
        """
        self.__text: str = text
        self.__height = height
        self.__width = widht
        self.__expand = expand
        self.__placeHolder = placeHolder

        # Contenido inicial
        self.content = ft.Column(
            controls=[
                ft.Text(
                    value=self.__placeHolder,
                    size=FontSize.normal_font_size,
                    color=ft.Colors.with_opacity(0.6, ft.Colors.WHITE),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
        )

        # Contenedor principal
        self.container = ft.Container(
            bgcolor=Colors.color_C,
            expand=self.__expand,
            content=self.content,
            width=self.__width,
            height=self.__height,
            on_hover=self.on_hover,
            border_radius=5,
            border=ft.border.all(1, ft.Colors.with_opacity(0.6, ft.Colors.WHITE)),
            on_click=self.on_click,
            padding=10,
        )

        # Campo de texto para edición
        self.container_input = ft.TextField(
            multiline=True,
            text_size=FontSize.normal_font_size,
            border="none",
            expand=True,
            on_blur=self.view_markdown,
        )

        self.controls = [self.container]

    def view_markdown(self, e, text=None):
        """
        Cambia el contenido del componente al modo de visualización Markdown.

        Args:
            e: Evento que activa este método (puede ser `None`).
            text (str, opcional): Texto a renderizar en formato Markdown. Si no se proporciona,
                                  se usará el valor actual del área de texto.
        """
        if not text:
            text = self.container_input.value

        container_markdown = ft.Markdown(
            value=text,
            extension_set="gitHubWeb",
            code_theme="atom-one-dark",
            code_style_sheet=ft.TextStyle(font_family="Roboto Mono"),
            expand=1,
        )

        scrollable_content = ft.Column(
            controls=[container_markdown],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        self.container.content = scrollable_content
        self.container.update()

    def on_click(self, e):
        """
        Cambia el componente al modo de edición.

        Al hacer clic, se muestra el campo de texto editable, permitiendo modificar el contenido.
        """
        self.container.content = self.container_input
        self.container.update()
        self.container_input.focus()

    def on_hover(self, e):
        """
        Ajusta el estilo del componente cuando el cursor pasa por encima (hover).

        Si no hay texto, se muestra un borde destacado y el marcador de posición. Cuando el hover
        termina, se restauran los estilos originales.
        """
        if (
            e.data == "true"  # Hover activo
            and not self.container_input.value  # Sin texto en el input
            and not self.__text  # Sin texto por defecto
        ):
            self.container.border = ft.border.all(1, ft.Colors.WHITE)
            self.container.content = self.content
            self.content.controls[0].color = ft.Colors.WHITE
            # self.content.update() #TODO: CORREGIR BUG
        else:  # Hover desactivado
            self.container.border = ft.border.all(
                1, ft.Colors.with_opacity(0.6, ft.Colors.WHITE)
            )
            if not self.container_input.value:
                self.container.content = self.content
                self.content.controls[0].color = ft.Colors.with_opacity(
                    0.6, ft.Colors.WHITE
                )
                self.load_text()

        self.container.update()

    @property
    def text(self):
        self.__text = self.container_input.value
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text
        self.container_input.value = self.__text

    def load_text(self):
        """
        Carga el texto inicial en el componente, si está definido.

        Esto se usa principalmente después de que el componente se monta.
        """
        if self.__text:
            self.__text = self.container_input.value
            # Dado que el input y el texto de entrada del contenedor asi como el markdown comporten contexto (el texto) es necesario indicarle que si el input se ve modificado (especificamente cuando esta vacio) el self.__text sea conciente de que tambien tenga el mismo valor.
            # De esta forma evito un bug en el cual el view_markdown carga con texto que el input ya no contiene.
            self.view_markdown(None, self.__text)

    def did_mount(self):
        """
        Método especial de Flet que se ejecuta después de que el componente se renderiza.

        Carga el texto inicial si está definido.
        """
        self.load_text()
