const dialog = document.getElementById('dialog_register');
const closeDialogButton = document.getElementById('close');
const dialog_cad = document.getElementById('jaCadastrado')
const closeJaCadastrado = document.getElementById('close_cad')
const openDialogButton = document.getElementById('openDialog');

const openText = document.getElementById('desga');

if (passNot === true) {
  dialog.showModal();
  // console.log('senha filha da puta')
}
if (jaCad === true) {
  dialog_cad.showModal();
}



closeDialogButton.onclick = () => {
  dialog.close();
}
closeJaCadastrado.onclick = () => {
  dialog_cad.close();
}
