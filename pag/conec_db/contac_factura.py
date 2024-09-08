import sqlite3

class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

class Contact_Inventario(Singleton):
    def __init__(self):
        super().__init__()
        self.connection = None
        self._open_connection()

    def _open_connection(self):
        self.connection = sqlite3.connect("./db/data.db", check_same_thread=False)

    def _ensure_connection(self):
        if self.connection is None:
            self._open_connection()

    def get_contact_by_name(self, nombre):
        self._ensure_connection()
        cursor = self.connection.cursor()
        query = "SELECT * FROM Datos_Inventario WHERE NOMBRE = ?"
        cursor.execute(query, (nombre,))
        contact = cursor.fetchone()
        return contact

class Factura(Singleton):
    def __init__(self):
        super().__init__()
        self.inventario_db = Contact_Inventario()  # Añadido para acceder a inventario

    def _open_connection(self):
        self.connection = sqlite3.connect("./db/data.db", check_same_thread=False)

    def _ensure_connection(self):
        if self.connection is None:
            self._open_connection()

    def add_factura(self, factura_numero, nombre_articulo, valor_articulo, cantidad, subtotal, descripcion):
        self._ensure_connection()
        query = '''INSERT INTO FACTURA (FACTURA, NOMBRE_ARTICULO, VALOR_ARTICULO, CANTIDAD, SUBTOTAL, DESCRIPCION) 
                      VALUES (?, ?, ?, ?, ?, ?)'''
        self.connection.execute(query, (factura_numero, nombre_articulo, valor_articulo, cantidad, subtotal, descripcion))
        self.connection.commit()

    def get_factura(self):
        self._ensure_connection()
        cursor = self.connection.cursor()
        query = "SELECT * FROM FACTURA"
        cursor.execute(query)
        facturas = cursor.fetchall()
        return facturas

    def delete_factura(self, factura_id):
        self._ensure_connection()
        query = "DELETE FROM FACTURA WHERE ID = ?"
        self.connection.execute(query, (factura_id,))
        self.connection.commit()

    def update_factura(self, factura_id, factura_numero, nombre_articulo, valor_articulo, cantidad, subtotal, descripcion):
        self._ensure_connection()
        query = '''UPDATE FACTURA SET FACTURA = ?, NOMBRE_ARTICULO = ?, VALOR_ARTICULO = ?, CANTIDAD = ?, SUBTOTAL = ?, DESCRIPCION = ?
                      WHERE ID = ?'''
        self.connection.execute(query, (factura_numero, nombre_articulo, valor_articulo, cantidad, subtotal, descripcion, factura_id))
        self.connection.commit()
        return self.connection.total_changes

    def get_product_price(self, nombre_articulo):
        contact = self.inventario_db.get_contact_by_name(nombre_articulo)
        if contact:
            return contact[2]  # Suponiendo que el precio está en la tercera posición
        return None
