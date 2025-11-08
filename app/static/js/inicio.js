const botaoElemento = document.getElementById('botao');

if (botaoElemento) {
    // Adiciona uma função que será executada ao clicar no botão
    botaoElemento.addEventListener('click', function() {
        alert('Você clicou no botão!');
    });
}