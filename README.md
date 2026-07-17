Diseñar y desarrollar una aplicación web interactiva (Dashboard) para la marca de tecnología TrendGear. El sistema debe consumir datos de clientes y compras almacenados en una base de datos en tiempo real de Firebase y mostrar métricas clave junto con una interfaz dinámica y responsiva para visualizar la información de los usuarios.

Base de Datos (Firebase Realtime Database)Configurar una base de datos no relacional en Firebase que contenga un nodo llamado clientes.  Cada registro de cliente debe contar con la siguiente estructura de datos exacta en formato JSON:  customerId (ID único)  name (Nombre completo)  email (Correo electrónico)  productPurchased (Producto comprado)  purchaseDate (Fecha de compra)  amountSpent (Monto gastado en formato numérico)  age (Edad del cliente)  city (Ciudad)  paymentMethod (Método de pago)  membershipStatus (Tipo de membresía: Bronze, Silver o Gold)  2. Frontend (HTML5 & CSS3)Estructura (index.html):Un encabezado (header) que incluya el logotipo de TrendGear y un menú de navegación responsivo. 

Una sección superior con tarjetas de para visualizar de forma rápida:Total de Clientes Registrados.  Total de Ingresos Generados (Suma de montos gastados).  Edad Promedio de los clientes.  Una sección principal (#clientesContainer) destinada a renderizar dinámicamente las tarjetas de cada cliente.  

Estilos (styles.css):Aplicar un diseño moderno con paleta de colores en modo oscuro (fondos oscuros #1E1E1E o similares).  Diseñar las tarjetas de clientes de manera que muestren de forma organizada sus datos principales. 

Implementar diseño responsivo (Media Queries) para asegurar que el dashboard sea cómodo de leer tanto en computadoras de escritorio como en dispositivos móviles (menú de hamburguesa para el header).

Realizar una petición asíncrona mediante fetch() a la URL de Firebase Realtime Database para obtener los datos de los clientes en formato JSON.  calcular el total de registros, acumular los ingresos y promediar las edades, actualizando estos valores dinámicamente en el DOM.

Renderizado de Tarjetas: Crear elementos HTML de forma dinámica para cada cliente, insertando su información básica (Nombre, Producto, Edad, Ciudad, Correo, etc.) dentro del contenedor de clientes.  Manejar posibles errores en la petición con bloques try...catch para evitar fallos en la aplicación.

Crear un script en Python que utilice librerías como pandas y random para simular un set de datos de hasta 200 clientes ficticios con compras lógicas de tecnología en ciudades colombianas. Exportar los datos generados a formato CSV para su posterior carga en Firebase.
