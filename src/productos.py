from typing import List, Dict, Union
from . import db

Producto = Dict[str, Union[str, float]] #"Producto => cada producto individual"

productos: List[Producto] = [ #"productos es la lista/array"
    # Buzos
    {
        "nombre": "Buzo valorant negro",
        "imagen": "buzo-valorant-negro.jpg",
        "categoria": "Buzos",
        "precio": 35.00
    },
    {
        "nombre": "Buzo valorant blanco",
        "imagen": "Buzo-valorant-blanco.jpg",
        "categoria": "Buzos",
        "precio": 35.00
    },
    {
        "nombre": "Buzo yoru negro",
        "imagen": "Buzo-yoru.jpg",
        "categoria": "Buzos",
        "precio": 40.00
    },
    {
        "nombre": "Buzo crema logo",
        "imagen": "Buzo beige liso.jpg",
        "categoria": "Buzos",
        "precio": 30.00
    },
    {
        "nombre": "Buzo valorant sage",
        "imagen": "Buzo sage.jpg",
        "categoria": "Buzos",
        "precio": 37.00
    },
    {
        "nombre": "Buzo valorant master",
        "imagen": "Buzo-valorant-master.jpg",
        "categoria": "Buzos",
        "precio": 42.00
    },
    {
        "nombre": "Buzo valorant logo negro",
        "imagen": "buzo-logo-negro.jpg",
        "categoria": "Buzos",
        "precio": 35.00
    },
    {
        "nombre": "Buzo valorant rojo",
        "imagen": "Buzo rojo liso.jpg",
        "categoria": "Buzos",
        "precio": 33.00
    },
    # Remeras
    {
        "nombre": "Remera blanca lisa",
        "imagen": "remera-blanca-lisa.jpg",
        "categoria": "Remeras",
        "precio": 20.00
    },
    {
        "nombre": "Remera fade",
        "imagen": "remera-fade.png",
        "categoria": "Remeras",
        "precio": 25.00
    },
    {
        "nombre": "Remera jett",
        "imagen": "remera-jett.jpg",
        "categoria": "Remeras",
        "precio": 27.00
    },
    {
        "nombre": "Remera logo valorant",
        "imagen": "remera-logo-valorant.jpg",
        "categoria": "Remeras",
        "precio": 30.00
    },
    {
        "nombre": "Remera negra lisa",
        "imagen": "remera-negra-lisa.jpg",
        "categoria": "Remeras",
        "precio": 20.00
    },
    {
        "nombre": "Remera omen",
        "imagen": "remera-omen.jpg",
        "categoria": "Remeras",
        "precio": 28.00
    },
    {
        "nombre": "Remera valo",
        "imagen": "remera-phoenix.jpg",
        "categoria": "Remeras",
        "precio": 22.00
    },
    {
        "nombre": "Remera valo blanca",
        "imagen": "remera-reyna-blanca.jpg",
        "categoria": "Remeras",
        "precio": 22.00
    },
    # Pantalones
    {
        "nombre": "Deportivo negro liso",
        "imagen": "deportivo-negro-liso.jpg",
        "categoria": "Pantalones",
        "precio": 30.00
    },
    {
        "nombre": "Jogger negro liso",
        "imagen": "jogger-negro-liso.jpg",
        "categoria": "Pantalones",
        "precio": 35.00
    },
    {
        "nombre": "Pantalon jett y phoenix",
        "imagen": "pantalon-jett&phoenix.jpg",
        "categoria": "Pantalones",
        "precio": 40.00
    },
    {
        "nombre": "Pantalon Jett rojo",
        "imagen": "pantalon-jett-rojo.jpg",
        "categoria": "Pantalones",
        "precio": 38.00
    },
    {
        "nombre": "Pantalon Killjoy",
        "imagen": "pantalon-killjoy.jpg",
        "categoria": "Pantalones",
        "precio": 42.00
    },
    {
        "nombre": "Pantalon all Characters",
        "imagen": "pantalon-re-loco.jpg",
        "categoria": "Pantalones",
        "precio": 45.00
    },
    {
        "nombre": "Pantalon Sage",
        "imagen": "pantalon-sage.jpg",
        "categoria": "Pantalones",
        "precio": 37.00
    },
    {
        "nombre": "Pantalon Sova",
        "imagen": "pantalon-sova.jpg",
        "categoria": "Pantalones",
        "precio": 38.00
    },
    # Accesorios
    {
        "nombre": "Collar Valorant",
        "imagen": "collar-valorant.png",
        "categoria": "Accesorios",
        "precio": 15.00
    },
    {
        "nombre": "LLavero Rango 'oro'",
        "imagen": "llavero-oro.png",
        "categoria": "Accesorios",
        "precio": 10.00
    },
    {
        "nombre": "LLavero Phantom",
        "imagen": "llavero-phantom.png",
        "categoria": "Accesorios",
        "precio": 12.00
    },
    {
        "nombre": "LLavero Platino",
        "imagen": "llavero-platino.png",
        "categoria": "Accesorios",
        "precio": 11.00
    },
    {
        "nombre": "LLavero Rango Violeta",
        "imagen": "llavero-rango-violeta.png",
        "categoria": "Accesorios",
        "precio": 13.00
    },
    {
        "nombre": "Collar Jett",
        "imagen": "collar-jett.png",
        "categoria": "Accesorios",
        "precio": 14.00
    },
    {
        "nombre": "LLavero Vandal",
        "imagen": "llavero-vandal.png",
        "categoria": "Accesorios",
        "precio": 12.00
    }
]

# def insertar_productos():
#     for producto in productos:
#         nuevo_producto = Producto(
#             nombre=producto['nombre'],
#             imagen=producto['imagen'],
#             categoria=producto['categoria'],
#             precio=producto['precio']
#         )
#         db.session.add(nuevo_producto)

#     db.session.commit()

