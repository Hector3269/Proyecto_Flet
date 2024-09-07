import flet as ft

from

fecha_facturacion = ft.TextField(label='Fecha Facturación',
                                 hint_text="Fecha Facturación",
                                 width=300)

numero_factura = ft.TextField(label='Número Factura',
                              hint_text='Número Factura',
                              width=300)

nombre_cliente = ft.TextField(label='Nombre Cliente',
                              hint_text='Nombre Cliente',
                              width=300)

direccion_cliente = ft.TextField(label='Dirección Cliente',
                                 hint_text='Dirección Cliente',
                                 width=300)

item_name_1 = ft.TextField(label='Item 1',
                           hint_text='Item 1',
                           width=300)

item_name_2 = ft.TextField(label='Item 2',
                           hint_text='Item 2',
                           width=300)

quantity_item_1 = ft.TextField(label='Cantidad Item 1',
                               value='0',
                               text_align='center',
                               width=150)

quantity_item_2 = ft.TextField(label='Cantidad Item 2',
                               value='0',
                               text_align='center',
                               width=150)

price_item_1 = ft.TextField(label='Precio Item 1',
                            value='0',
                            text_align='center',
                            width=150)

price_item_2 = ft.TextField(label='Precio Item 2',
                            value='0',
                            text_align='center',
                            width=150)

dialogo = ft.AlertDialog(title=ft.Text("Factura Generada"),
                         on_dismiss=lambda e: print("Cerrado"))
