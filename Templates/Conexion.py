import pyodbc

# Conexión a SQL Server usando autenticación de Windows
try:
    conn = pyodbc.connect(
        "DRIVER={SQL Server};SERVER=JAIME007\\SQLEXPRESS;DATABASE=UROMED;Trusted_Connection=yes;"
    )
    print("✅ Conexión exitosa a SQL Server.")

    cursor = conn.cursor()

    # Consulta de prueba: mostrar los primeros 5 expedientes
    cursor.execute("SELECT TOP 5 * FROM expedientes")
    filas = cursor.fetchall()

    if filas:
        print("📋 Expedientes encontrados:")
        for fila in filas:
            print(fila)
    else:
        print("⚠️ La tabla 'expedientes' está vacía.")

    conn.close()
    print("🔒 Conexión cerrada correctamente.")

except pyodbc.Error as e:
    print("❌ Error al conectar con SQL Server:")
    print(e)