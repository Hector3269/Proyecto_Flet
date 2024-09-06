import flet as ft
from conec_db.contact_inventario import Contact_Inventario
from fpdf import FPDF
import pandas as pd
import datetime


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Tabla de Datos', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')


class Pag_Inventario(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page
        self.data = Contact_Inventario()
        self.selected_row = None

        self.nombre = ft.TextField(
            width=280,
            height=40,
            label="Nombre",
            border_color=ft.colors.LIGHT_GREEN_ACCENT_400,
            label_style=ft.TextStyle(color=ft.colors.CYAN_ACCENT_200),
            prefix_icon=ft.icons.QUEUE,
            border='underline'
        )
        self.precio = ft.TextField(
            width=280,
            height=40,
            label="Precio",
            border_color=ft.colors.LIGHT_GREEN_ACCENT_400,
            label_style=ft.TextStyle(color=ft.colors.CYAN_ACCENT_200),
            prefix_icon=ft.icons.MONEY,
            border='underline',
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        self.costo = ft.TextField(
            width=280,
            height=40,
            label="Costo",
            border_color=ft.colors.LIGHT_GREEN_ACCENT_400,
            label_style=ft.TextStyle(color=ft.colors.CYAN_ACCENT_200),
            prefix_icon=ft.icons.MONEY,
            border='underline',
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        self.existencias = ft.TextField(
            width=280,
            height=40,
            label="Existencias",
            border_color=ft.colors.LIGHT_GREEN_ACCENT_400,
            label_style=ft.TextStyle(color=ft.colors.CYAN_ACCENT_200),
            prefix_icon=ft.icons.PRODUCTION_QUANTITY_LIMITS,
            border='underline',
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        self.descripcion = ft.TextField(
            width=280,
            height=40,
            label="Descripcion",
            border_color=ft.colors.LIGHT_GREEN_ACCENT_400,
            label_style=ft.TextStyle(color=ft.colors.CYAN_ACCENT_200),
            prefix_icon=ft.icons.DESCRIPTION,
            border='underline'
        )
        self.imagen = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.IMAGE, color='white'),
                ft.Text(
                    "Seleccionar imagen",
                    weight='w500',  # Peso del texto
                    color='white',

                )
            ],
                alignment='center'
            ),
            bgcolor='transparent'
        )


        self.searh_field = ft.TextField(
            suffix_icon=ft.icons.SEARCH,
            label="Buscar por el nombre",
            border=ft.InputBorder.UNDERLINE,
            border_color=ft.colors.LIGHT_GREEN_ACCENT_400,
            label_style=ft.TextStyle(color=ft.colors.CYAN_ACCENT_200),
            on_change=self.searh_data,
        )
        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2, "purple"),
            data_row_color={ft.ControlState.SELECTED: ft.colors.BLUE_600, ft.ControlState.PRESSED: "black"},
            border_radius=10,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text("Nombre", color=ft.colors.LIGHT_GREEN_ACCENT_400, weight="bold")),
                ft.DataColumn(ft.Text("Precio", color=ft.colors.CYAN_ACCENT_200, weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Costo", color=ft.colors.CYAN_ACCENT_200, weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Existencia", color=ft.colors.CYAN_ACCENT_200, weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Descripcion", color=ft.colors.LIGHT_GREEN_ACCENT_400, weight="bold")),
            ],
        )

        self.show_data()

        self.form = ft.Container(
            gradient=ft.LinearGradient(
                [ft.colors.RED, ft.colors.BLUE_ACCENT_400, ft.colors.CYAN_ACCENT_200]),
            border_radius=10,
            col=4,
            padding=10,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Ingrese sus datos",
                            size=40,
                            text_align="center",
                            font_family="vivaldi", ),
                    self.nombre,
                    self.precio,
                    self.costo,
                    self.existencias,
                    self.descripcion,
                    self.imagen,
                    ft.Container(
                        content=ft.Row(
                            spacing=5,
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[

                                ft.ElevatedButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SAVE, color='white'),  # Icono de guardar
                                            ft.Text(
                                                'Guardar',
                                                weight='w500',  # Peso del texto
                                                color='white',  # Color del texto
                                            ),
                                        ],
                                        alignment='center',
                                    ),
                                    bgcolor='transparent',  # Fondo transparente para el botón
                                    on_click=self.add_data,
                                ),
                                ft.ElevatedButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.EDIT, color='white'),  # Icono de editar
                                            ft.Text(
                                                'Actualizar',
                                                weight='w500',  # Peso del texto
                                                color='white',  # Color del texto
                                            ),
                                        ],
                                        alignment='center',
                                    ),
                                    bgcolor='transparent',  # Fondo transparente para el botón
                                    on_click=self.update_data,
                                ),
                                ft.ElevatedButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.DELETE, color='white'),  # Icono de borrar
                                            ft.Text(
                                                'Borrar',
                                                weight='w500',  # Peso del texto
                                                color='white',  # Color del texto
                                            ),
                                        ],
                                        alignment='center',
                                    ),
                                    bgcolor='transparent',  # Fondo transparente para el botón
                                    on_click=self.delete_data,
                                ),
                            ]
                        )
                    )
                ]
            )
        )

        self.table = ft.Container(
            gradient=ft.LinearGradient(
                [ft.colors.RED_ACCENT_200, ft.colors.BLUE_ACCENT_400, ft.colors.CYAN_ACCENT_200]),
            border_radius=10,
            padding=10,
            col=8,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        padding=10,
                        content=ft.Row(
                            controls=[
                                self.searh_field,
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    on_click=self.edit_flied_text,
                                    icon_color="white",
                                ),
                                ft.IconButton(tooltip="Descargar en PDF",
                                              icon=ft.icons.PICTURE_AS_PDF,
                                              icon_color="white",
                                              on_click=self.save_pdf,
                                              ),
                                ft.IconButton(tooltip="Descargar en EXCEL",
                                              icon=ft.icons.SAVE_ALT,
                                              icon_color="white",
                                              on_click=self.save_excel,
                                              ),
                            ]
                        ),
                    ),

                    ft.Column(
                        expand=True,
                        scroll="auto",
                        controls=[
                            ft.ResponsiveRow([
                                self.data_table
                            ]),
                        ]
                    )
                ]
            )
        )
        self.conent = ft.ResponsiveRow(
            controls=[
                self.form,
                self.table
            ]
        )

    def show_data(self):
        self.data_table.rows = []
        for x in self.data.get_contact():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed=self.get_index,
                    cells=[
                        ft.DataCell(ft.Text(x[1])),
                        ft.DataCell(ft.Text(str(x[2]))),
                        ft.DataCell(ft.Text(str(x[3]))),
                        ft.DataCell(ft.Text(str(x[4]))),
                        ft.DataCell(ft.Text(x[5])),
                    ]
                )
            )
        self.update()

    def add_data(self, e):
        nombre = self.nombre.value
        precio = str(self.precio.value)
        costo = str(self.costo.value)
        existencias = str(self.existencias.value)
        descripcion = self.descripcion.value

        if len(nombre) and len(precio) and len(costo) and len(existencias) and len(descripcion) > 0:
            contact_exists = False
            for row in self.data.get_contact():
                if row[1] == nombre:
                    contact_exists = True
                    break

            if not contact_exists:
                self.clean_fields()
                self.data.add_contact(nombre, precio, costo, existencias, descripcion)
                self.show_data()
            else:
                print("El contacto ya existe en la base de datos.")
        print("Escriba sus datos")

    def get_index(self, e):
        if e.control.selected:
            e.control.selected = False
        else:
            e.control.selected = True
        nombre = e.control.cells[0].content.value
        for row in self.data.get_contact():
            if row[1] == nombre:
                self.selected_row = row
                break
        self.update()

    def edit_flied_text(self, e):
        try:
            self.nombre.value = self.selected_row[1]
            self.precio.value = self.selected_row[2]
            self.costo.value = self.selected_row[3]
            self.existencias.value = self.selected_row[4]
            self.descripcion.value = self.selected_row[5]
            self.update()
        except TypeError:
            print("Error")

    def update_data(self, e):
        nombre = self.nombre.value
        precio = str(self.precio.value)
        costo = str(self.costo.value)
        existencias = str(self.existencias.value)
        descripcion = self.descripcion.value

        if len(nombre) and len(precio) and len(costo) and len(existencias) and len(descripcion) > 0:
            self.clean_fields()
            self.data.update_contact(self.selected_row[0], nombre, precio, costo, existencias, descripcion)
            self.show_data()

    def delete_data(self, e):
        self.data.delete_contact(self.selected_row[1])
        self.show_data()

    def searh_data(self, e):
        search = self.searh_field.value.lower()
        nombre = list(filter(lambda x: search in x[1].lower(), self.data.get_contact()))
        self.data_table.rows = []
        if not self.searh_field.value == "":
            if len(nombre) > 0:
                for x in nombre:
                    self.data_table.rows.append(
                        ft.DataRow(
                            on_select_changed=self.get_index,
                            cells=[
                                ft.DataCell(ft.Text(x[1])),
                                ft.DataCell(ft.Text(str(x[2]))),
                                ft.DataCell(ft.Text(str(x[3]))),
                                ft.DataCell(ft.Text(str(x[4]))),
                                ft.DataCell(ft.Text(x[5])),
                            ]
                        )
                    )
                    self.update()
        else:
            self.show_data()

    def clean_fields(self):
        self.nombre.value = ""
        self.precio.value = ""
        self.costo.value = ""
        self.existencias.value = ""
        self.descripcion.value = ""
        self.update()

    def save_pdf(self, e):
        pdf = PDF()
        pdf.add_page()
        column_widths = [10, 40, 20, 80, 40]
        # Agregar filas a la tabla
        data = self.data.get_contact()
        header = ("ID", "NOMBRE", "PRECIO", "COSTO", "EXISTENCIA", "DESCRIPCION")
        data.insert(0, header)
        for row in data:
            for item, width in zip(row, column_widths):
                pdf.cell(width, 10, str(item), border=1)
            pdf.ln()
        file_name = datetime.datetime.now()
        file_name = file_name.strftime("DATA %Y-%m-%d_%H-%M-%S") + ".pdf"
        pdf.output(file_name)

    def save_excel(self, e):
        file_name = datetime.datetime.now()
        file_name = file_name.strftime("DATA %Y-%m-%d_%H-%M-%S") + ".xlsx"
        contacts = self.data.get_contact()
        df = pd.DataFrame(contacts, columns=["ID", "NOMBRE", "PRECIO", "COSTO", "EXISTENCIA", "DESCRIPCION"])
        df.to_excel(file_name, index=False)

    def build(self):
        return self.conent


def main_inventario(page: ft.Page):
    page.bgcolor = "black"
    page.title = "Empleados"
    page.window.min_width = 1100
    page.window.min_height = 500
    form_ui = Pag_Inventario(page)
    form_ui.data.close_connection()
    page.add(Pag_Inventario(page))


ft.app(main_inventario)