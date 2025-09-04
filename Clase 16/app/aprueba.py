import mysql.connector
from mysql.connector import Error

def test_connection():
    try:
        # 🔹 Cambiá estos valores por los de tu servidor
        connection = mysql.connector.connect(
            host="127.0.0.1",      # o la IP/hostname del servidor
            user="root",
            password="12345678",
            database="pruebas"  # opcional si querés probar solo la conexión
        )

        if connection.is_connected():
            print("✅ Conexión exitosa a MySQL")
            print("Servidor:", connection.get_server_info())

            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Base de datos actual:", record[0])

    except Error as e:
        print("❌ Error al conectar a MySQL:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Conexión cerrada")

if __name__ == "__main__":
    test_connection()
