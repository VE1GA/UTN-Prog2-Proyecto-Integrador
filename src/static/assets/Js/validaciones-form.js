const inputNombreForm = document.getElementById('nombre');
const inputApellidoForm = document.getElementById('apellido');
const inputEmailForm = document.getElementById('email');
const inputTelefonoForm = document.getElementById('telefono');
const inputNacForm = document.getElementById('nacimiento');
const inputTextareaForm = document.getElementById('textarea');
const form = document.getElementById('form');

console.log(inputTelefonoForm);
console.log(inputNombreForm);
console.log(inputApellidoForm);
console.log(inputEmailForm);
console.log(inputNacForm);
console.log(inputTextareaForm);

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const regexNombre = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;
    const telefonoRegex = /^\d{9,11}$/;
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$/;

    const today = new Date();
    const minDate = new Date(today.getFullYear() - 13, today.getMonth(), today.getDate());


    if (regexNombre.test(inputNombreForm.value)) {
        console.log("Nombre");

        if (regexNombre.test(inputApellidoForm.value)) {
            console.log("Apellido");

            if (emailRegex.test(inputEmailForm.value)) {
                console.log("Email");

                if (telefonoRegex.test(inputTelefonoForm.value)) {
                    console.log("Telefono");
                    console.log(inputNacForm.value);
                    console.log(minDate);
                    
                    const inputDate = new Date(inputNacForm.value);
                    if (inputDate <= minDate) {
                        window.alert("Formulario cargado correctamente");
                        form.reset();

                    } else {
                        window.alert("Tienes que ser mayor a 13 años");
                    }
                } else {
                    window.alert("Error en los datos del formulario");
                    
                }
            } else {
                window.alert("Error en los datos del formulario");
            }
            } else {
                window.alert("Error en los datos del formulario");
            }
    } else {
        window.alert("Error en los datos del formulario");

    }
})