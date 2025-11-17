const loginCard = document.getElementById("card-login");
const registerCard = document.getElementById("card-register");

// alternar para o card de registro
document.getElementById("swap-to-register").onclick = () => {
    loginCard.classList.remove("active");
    registerCard.classList.add("active");
};

// alternar para o card de login
document.getElementById("swap-to-login").onclick = () => {
    registerCard.classList.remove("active");
    loginCard.classList.add("active");
};

// ---- ALERTA DE ERRO ----
window.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);

    if (params.get("error") === "1") {
        alert("Usuário ou senha incorretos!");
    }
});
