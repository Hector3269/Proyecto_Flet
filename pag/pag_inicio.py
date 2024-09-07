import flet as ft


class Pag_Inicio:
    def __init__(self, page: ft.Page):
        self.page = page

        # Variable para controlar si el menú está desplegado o no
        self.menu_visible = False

        # Barra superior
        self.barra = ft.Container(
            content=ft.Row([
                ft.IconButton(
                    width=70,
                    height=50,
                    icon=ft.icons.MENU,
                    icon_size=30,
                    on_click=self.toggle_menu  # Llamada a la función para abrir/cerrar el menú
                ),
                ft.Text("Arrax", size=24, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.IconButton(icon=ft.icons.ACCOUNT_TREE, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.ACCOUNT_CIRCLE, icon_color=ft.colors.WHITE),
                ],
                    alignment=ft.MainAxisAlignment.END)
            ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            border_radius=10,
            padding=20,
            gradient=ft.LinearGradient(
                [ft.colors.RED, ft.colors.BLUE_ACCENT_400, ft.colors.CYAN_ACCENT_200]),
            height=80,
        )

        # Contenedor para el menú lateral
        self.menu = ft.Container(
            content=self.create_menu(),
            gradient=ft.LinearGradient(
                [ft.colors.RED, ft.colors.BLUE_ACCENT_400, ft.colors.CYAN_ACCENT_200]),
            border_radius=10,
            width=200,
            height=self.page.height,  # Ajusta el tamaño del menú a la altura de la página
            padding=20,
            visible=False  # El menú estará oculto al inicio
        )

        # Añadir elementos a la página
        self.page.add(self.barra, self.menu)

    def create_menu(self):
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.icons.HOME, size=30, color=ft.colors.WHITE),
                        ft.Text("Arrax", size=24, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(color=ft.colors.WHITE54),
                self.create_menu_item(ft.icons.DASHBOARD, "Panel de Control"),
                self.create_menu_item(ft.icons.SHOPPING_CART, "Sistema de Ventas", [
                    {"icon": ft.icons.SELL, "text": "Ventas"},
                    {"icon": ft.icons.INVENTORY, "text": "Inventario"},
                ]),
                self.create_menu_item(ft.icons.PEOPLE, "Personal", [
                    {"icon": ft.icons.PERSON, "text": "Empleados"}
                ]),
                self.create_menu_item(ft.icons.QR_CODE, "QR", [
                    {"icon": ft.icons.CREATE, "text": "Crear QR"}
                ]),
                self.create_menu_item(ft.icons.LOGIN, "Inicio Sesión", [
                    {"icon": ft.icons.HOW_TO_REG, "text": "Registro"}
                ]),
                self.create_menu_item(ft.icons.SETTINGS, "Configuración"),
                ft.Divider(color=ft.colors.WHITE54),
                ft.ListTile(
                    leading=ft.CircleAvatar(
                        content=ft.Image(src="./img/images.jpeg", fit=ft.ImageFit.COVER),
                        radius=20,
                    ),
                    title=ft.Text("Mary Karen", color=ft.colors.WHITE),
                    subtitle=ft.Text("Desarrolladora Web", color=ft.colors.WHITE54),
                ),
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        )

    def create_menu_item(self, icon, text, subitems=None):
        # Contenido del botón de menú
        button_content = [
            ft.Row(
                [
                    ft.Icon(icon, size=30, color=ft.colors.WHITE),
                    ft.Text(text, size=18, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.START,
            )
        ]
        # Agrega los subitems si existen
        if subitems:
            subitems_column = ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(subitem["icon"], size=24, color=ft.colors.WHITE),
                            ft.Text(subitem["text"], size=16, color=ft.colors.WHITE54),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ) for subitem in subitems
                ],
                spacing=10,
                visible=False,  # Inicialmente oculto
            )
            button_content.append(subitems_column)
            setattr(self, f"{text}_subitems", subitems_column)  # Guarda la referencia a los subitems

        return ft.TextButton(
            content=ft.Column(button_content),
            on_click=lambda e: self.toggle_subitems(text),  # Llama a la función para mostrar/ocultar subitems
        )

    def toggle_menu(self, e):
        # Cambiar la visibilidad del menú
        self.menu_visible = not self.menu_visible
        self.menu.visible = self.menu_visible
        self.page.update()

    def toggle_subitems(self, text):
        # Alternar visibilidad de subitems
        subitems_column = getattr(self, f"{text}_subitems", None)
        if subitems_column:
            subitems_column.visible = not subitems_column.visible
            self.page.update()


def main(page: ft.Page):
    page.title = "Barra Lateral Desplegable - Arrax"
    page.bgcolor = ft.colors.WHITE
    page.update()
    Pag_Inicio(page)


ft.app(target=main)
