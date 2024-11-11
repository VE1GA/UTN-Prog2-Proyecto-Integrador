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

function eliminar_del_carrito(productoid) {
    fetch('/eliminar_carrito', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: productoid }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Eliminar visualmente la tarjeta del producto del carrito
            const productoCard = document.getElementById(`producto-${productoid}`);
            if (productoCard) {
                productoCard.remove();
                window.alert('se borro el producto del carrito')
                location.reload();
            }
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}