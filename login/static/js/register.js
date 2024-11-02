const dialog = document.getElementById('dialog_register');
const closeDialogButton = document.getElementById('close');
const openDialogButton = document.getElementById('openDialog');

if (passNot === true) {
  dialog.showModal();
}

closeDialogButton.onclick = () => {
  dialog.close();
}

openDialogButton.onclick = () => {
  alert('open')
}