// script.js
const registerButton = document.getElementById("register");
// Seleciona o diálogo e o botão de fechar
const dialog = document.getElementById("userDialog");
const closeDialogButton = document.getElementById("close");


// Verifica se `userNot` é verdadeiro e exibe o diálogo
if (userNot === true) {
    dialog.showModal();
}

// Fecha o diálogo quando o botão de fechar é clicado
closeDialogButton.addEventListener("click", () => {
    dialog.close();
})

// Redireciona para a página de registro ao clicar no botão
registerButton.addEventListener("click", function () {
    window.location.href = registerUrl; // Redireciona para a página de registro
});
