const loginCard = document.getElementById("card-login");
const registerCard = document.getElementById("card-register");

document.getElementById("swap-to-register").onclick = () => {
    loginCard.classList.remove("active");
    registerCard.classList.add("active");
};

document.getElementById("swap-to-login").onclick = () => {
    registerCard.classList.remove("active");
    loginCard.classList.add("active");
};
