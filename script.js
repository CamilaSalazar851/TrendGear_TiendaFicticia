const firebaseURL = "https://trendgear-65491-default-rtdb.firebaseio.com/clientes.json";

const hamburger = document.getElementById("hamburger");
const nav = document.getElementById("nav");

hamburger.addEventListener("click", () => {
  nav.classList.toggle("active");
});

async function cargarClientes() {
  const response = await fetch(firebaseURL);
  const data = await response.json();

  if (!data) {
    console.log("No hay datos en Firebase todavía");
    return;
  }

  renderizarClientes(data);
  calcularKPIs(data);
}

function renderizarClientes(data) {
  const container = document.getElementById("clientesContainer");
  container.innerHTML = "";

  Object.values(data)
    .filter(cliente => cliente)
    .forEach(cliente => {
      const montoFormateado = cliente.amountSpent.toLocaleString("en-US", {
        style: "currency",
        currency: "USD"
      });

      const card = `
        <div class="cliente-card">
          <div class="cliente-nombre">${cliente.name}</div>
          <div class="cliente-email">${cliente.email}</div>
          <div class="cliente-info"><span>Producto</span><span>${cliente.productPurchased}</span></div>
          <div class="cliente-info"><span>Monto</span><span>${montoFormateado}</span></div>
          <div class="cliente-info"><span>Edad</span><span>${cliente.age}</span></div>
          <div class="cliente-info"><span>Ciudad</span><span>${cliente.city}</span></div>
          <div class="cliente-info"><span>Pago</span><span>${cliente.paymentMethod}</span></div>
          <span class="badge">${cliente.membershipStatus}</span>
        </div>
      `;

      container.innerHTML += card;
    });
}

function calcularKPIs(data) {
  const clientes = Object.values(data).filter(cliente => cliente);
  const totalClientes = clientes.length;
  const ingresoTotal = clientes.reduce((suma, c) => suma + c.amountSpent, 0);
  const edadPromedio = clientes.reduce((suma, c) => suma + c.age, 0) / totalClientes;

  document.getElementById("totalClientes").textContent = totalClientes;
  document.getElementById("ingresoTotal").textContent = ingresoTotal.toLocaleString("en-US", {
    style: "currency",
    currency: "USD"
  });
  document.getElementById("edadPromedio").textContent = edadPromedio.toFixed(1);
}

cargarClientes();
