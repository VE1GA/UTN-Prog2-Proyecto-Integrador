var datosCarrito = [];

function agregar_al_carrito(productoid, nombre, imagen, precio) {
    const producto = {
        id: productoid,
        nombre: nombre,
        imagen: imagen,
        precio: precio
    };
    datosCarrito.push(producto);
    console.log(datosCarrito);

    fetch('/agregar_carrito', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datosCarrito),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
