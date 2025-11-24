const form = document.getElementById("loginForm");
const message = document.getElementById("message");

form.addEventListener("submit", async (e) => {
  e.preventDefault(); // evita el recargo de la página

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: `email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`
    });

    if (response.ok) {
      // ✅ Redirige a /home si el login es correcto
      window.location.href = "/home";
    } else if (response.status === 401) {
      message.textContent = "Correo o contraseña incorrectos";
      message.style.color = "red";
    } else {
      message.textContent = "Error inesperado. Intenta más tarde.";
      message.style.color = "red";
    }
  } catch (err) {
    message.textContent = "Error de conexión al servidor";
    message.style.color = "red";
  }
});
