import flet as ft
from datetime import datetime


class PagInventario(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

        fecha_actual = datetime.now().strftime('%Y-%m-%d')

        self.titulo = ft.Text(

        )
        self.fecha_facturacion = ft.TextField(
            label='Fecha Facturación',
            hint_text="Fecha Facturación",
            width=300,
            value=fecha_actual,
            read_only=True,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        self.numero_factura = ft.TextField(
            label='Número Factura',
            hint_text='Número Factura',
            width=300,
            value='001',
            read_only=True,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        self.precio = ft.TextField(
            label='Precio',
            hint_text='Precio',
            width=300,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        self.cantidad = ft.TextField(
            label='Cantidad',
            hint_text='Cantidad',
            width=300,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        self.descripcion = ft.TextField(
            label='Descripción',
            hint_text='Descripción',
            width=300,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        self.pago = ft.TextField(
            label='Pago',
            hint_text='Pago',
            width=300,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        self.cambio = ft.TextField(
            label='Cambio',
            hint_text='Cambio',
            width=300,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        self.total = ft.TextField(
            label='Total',
            hint_text='Total',
            width=300,
            text_style=ft.TextStyle(color="white"),
            border_color="white"
        )

        # Crear un contenedor que agrupe los campos de texto
        self.factura = ft.Container(
            content=ft.Column(
                controls=[
                    self.titulo,
                    self.fecha_facturacion,
                    self.numero_factura,
                    self.precio,
                    self.cantidad,
                    self.descripcion,
                    self.pago,
                    self.cambio,
                    self.total
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            padding=20,
            margin=20,
            border_radius=10,
            bgcolor="#2a2a2a"
        )

        # Agregar el contenedor a los controles de la interfaz
        self.controls.append(self.factura)


def main_factura(page: ft.Page):
    page.bgcolor = "#1f1f1f"  # Cambiar el fondo de la página
    page.title = "Factura"
    page.window.min_width = 1100
    page.window.min_height = 600  # Ajustar la altura mínima

    # Instanciar y agregar el control a la página
    pag_inventario = PagInventario(page)
    page.add(pag_inventario)


# Corrección del nombre de la función en ft.app
ft.app(target=main_factura)
