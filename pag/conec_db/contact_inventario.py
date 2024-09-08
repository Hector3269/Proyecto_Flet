import sqlite3

class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

class Contact_Inventario(Singleton):
    def __init__(self):
        if not hasattr(self, 'connection'):
            self._open_connection()

    def _open_connection(self):
        try:
            self.connection = sqlite3.connect("./db/data.db", check_same_thread=False)
        except sqlite3.Error as e:
            print(f"Error opening connection: {e}")

    def _ensure_connection(self):
        try:
            if self.connection is None:
                self._open_connection()
        except sqlite3.Error as e:
            print(f"Error ensuring connection: {e}")

    def add_contact(self, nombre, precio, costo, existencias, descripcion):
        try:
            self._ensure_connection()
            query = '''INSERT INTO Datos_Inventario (NOMBRE, PRECIO, COSTO, EXISTENCIA, DESCRIPCION) 
                       VALUES (?, ?, ?, ?, ?)'''
            self.connection.execute(query, (nombre, precio, costo, existencias, descripcion))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding contact: {e}")

    def get_contact(self):
        try:
            self._ensure_connection()
            cursor = self.connection.cursor()
            query = "SELECT * FROM Datos_Inventario"
            cursor.execute(query)
            contacts = cursor.fetchall()
            return contacts
        except sqlite3.Error as e:
            print(f"Error retrieving contacts: {e}")
            return []

    def delete_contact(self, nombre):
        try:
            self._ensure_connection()
            query = "DELETE FROM Datos_Inventario WHERE NOMBRE = ?"
            self.connection.execute(query, (nombre,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting contact: {e}")

    def update_contact(self, contact_id, nombre, precio, costo, existencias, descripcion):
        try:
            self._ensure_connection()
            query = '''UPDATE Datos_Inventario SET NOMBRE = ?, PRECIO = ?, COSTO = ?, EXISTENCIA = ?, DESCRIPCION = ?
                       WHERE ID = ?'''
            self.connection.execute(query, (nombre, precio, costo, existencias, descripcion, contact_id))
            self.connection.commit()
            return self.connection.total_changes
        except sqlite3.Error as e:
            print(f"Error updating contact: {e}")
            return 0

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connection closed")
