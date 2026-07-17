import random
import csv
from datetime import date, timedelta

random.seed(42)

nombres = ["Laura Gómez","Carlos Ruiz","Ana Torres","Diego Pérez","Sofía Ramírez","Andrés Castro","Valentina Morales","Juan Rodríguez","Camila Salazar","Mateo Herrera","Isabella Vargas","Santiago Ortiz","Daniela Rojas","Sebastián Jiménez","Mariana Suárez","Nicolás Mendoza","Gabriela Cortés","Alejandro Reyes","Paula Restrepo","Felipe Álvarez","Natalia Guzmán","Tomás Cárdenas","María Fernanda León","David Contreras","Camilo Vega"]

productos = ["Auriculares Bluetooth","Laptop Gamer","Mouse Inalámbrico","Monitor 27\"","Teclado Mecánico","Smartwatch","Tablet 10 pulgadas","Cámara Web HD","Disco SSD 1TB","Parlante Portátil","Cargador Inalámbrico","Silla Gamer","Impresora Multifuncional","Router WiFi 6","Micrófono USB"]

ciudades = ["Bogotá","Medellín","Cali","Bucaramanga","Cúcuta","Barranquilla","Pereira","Manizales","Cartagena","Santa Marta"]

metodos_pago = ["Credit Card","Debit Card","PayPal"]

membresias = ["Bronze","Silver","Gold"]

def fecha_aleatoria(inicio, fin):
    delta = (fin - inicio).days
    return inicio + timedelta(days=random.randint(0, delta))

hoy = date(2024, 11, 15)
inicio_rango = date(2024, 1, 1)

filas = []
usados_ids = set()

for i in range(1, 201):
    customer_id = i
    nombre = random.choice(nombres)
    email = nombre.lower().replace(" ", ".").replace("é","e").replace("á","a").replace("í","i").replace("ó","o").replace("ú","u") + f"{customer_id}@mailinator.com"
    producto = random.choice(productos)
    fecha_compra = fecha_aleatoria(inicio_rango, hoy - timedelta(days=1))
    monto = round(random.uniform(15, 1800), 2)
    edad = random.randint(18, 65)
    ciudad = random.choice(ciudades)
    metodo = random.choice(metodos_pago)
    fecha_login = fecha_aleatoria(fecha_compra, hoy)
    membresia = random.choices(membresias, weights=[0.4, 0.4, 0.2])[0]

    filas.append([
        customer_id,
        nombre,
        email,
        producto,
        fecha_compra.isoformat(),
        f"{monto:.2f}",
        edad,
        ciudad,
        metodo,
        fecha_login.isoformat(),
        membresia
    ])

encabezado = ["Customer ID","Name","Email","Product Purchased","Purchase Date","Amount Spent ($)","Age","City","Payment Method","Last Login Date","Membership Status"]

with open("/home/claude/trendgear_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(encabezado)
    writer.writerows(filas)

print("Listo:", len(filas), "registros generados")
