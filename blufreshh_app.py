
import streamlit as st

st.set_page_config(
    page_title="BluFresh | Refresca tu verano",
    page_icon="🌊",
    layout="wide"
)

# ESTILOS
st.markdown("""
<style>
.stApp {
    background-color: #F7FCFC;
}
h1, h2, h3 {
    color: #087E8B;
}
.slogan {
    color: #F28C45;
    font-size: 22px;
    text-align: center;
}
.producto {
    background-color: #E4F7F7;
    padding: 18px;
    border-radius: 15px;
    text-align: center;
}
.stButton button {
    background-color: #087E8B;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ENCABEZADO
st.title("🌊 BluFresh")
st.markdown(
    '<p class="slogan">Refresca tu verano ☀️</p>',
    unsafe_allow_html=True
)

st.image(
    "https://images.unsplash.com/photo-1536935338788846bb9981813",
    caption="Sabores refrescantes inspirados en el mar",
    use_container_width=True
)

st.write(
    "¡Bienvenido a BluFresh! Descubre bebidas frías, "
    "sabores tropicales y colores inspirados en el océano, "
    "la arena y los atardeceres."
)

st.divider()

# MENÚ
st.header("🍹 Nuestra carta")

bebidas = {
    "Blue Ocean 🌊": {
        "precio": 12,
        "descripcion": "Bebida azul inspirada en el océano."
    },
    "Sunset Glow 🌅": {
        "precio": 13,
        "descripcion": "Bebida tropical con tonos de atardecer."
    },
    "Pink Paradise 🍓": {
        "precio": 10,
        "descripcion": "Refrescante bebida con sabor a fresa."
    },
    "Limonada Tropical 🍋": {
        "precio": 8,
        "descripcion": "Limonada fresca con un toque frutal."
    },
    "Coco Beach 🥥": {
        "precio": 12,
        "descripcion": "Bebida cremosa inspirada en la playa."
    },
    "Frappé de Mango 🥭": {
        "precio": 11,
        "descripcion": "Mango frío y textura cremosa."
    }
}

if "carrito" not in st.session_state:
    st.session_state.carrito = {}

categoria = st.selectbox(
    "Selecciona una categoría",
    ["Todas", "Tropicales", "Limonadas", "Frappés"]
)

categorias = {
    "Blue Ocean 🌊": "Tropicales",
    "Sunset Glow 🌅": "Tropicales",
    "Pink Paradise 🍓": "Tropicales",
    "Limonada Tropical 🍋": "Limonadas",
    "Coco Beach 🥥": "Tropicales",
    "Frappé de Mango 🥭": "Frappés"
}

productos = [
    nombre for nombre in bebidas
    if categoria == "Todas" or categorias[nombre] == categoria
]

columnas = st.columns(3)

for i, nombre in enumerate(productos):
    bebida = bebidas[nombre]

    with columnas[i % 3]:
        st.markdown(
            f"""
            <div class="producto">
                <h3>{nombre}</h3>
                <p>{bebida['descripcion']}</p>
                <h3>S/ {bebida['precio']:.2f}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        cantidad = st.number_input(
            f"Cantidad: {nombre}",
            min_value=1,
            max_value=10,
            value=1,
            key=f"cantidad_{nombre}"
        )

        if st.button("Agregar al carrito", key=f"agregar_{nombre}"):
            st.session_state.carrito[nombre] = (
                st.session_state.carrito.get(nombre, 0) + cantidad
            )
            st.success(f"¡{nombre} agregado al carrito!")

st.divider()

# CARRITO DE COMPRAS
st.header("🛒 Tu carrito")

if st.session_state.carrito:
    total = 0

    for nombre, cantidad in list(st.session_state.carrito.items()):
        precio = bebidas[nombre]["precio"]
        subtotal = precio * cantidad
        total += subtotal

        col1, col2, col3 = st.columns([3, 1, 1])
        col1.write(f"**{nombre}**")
        col2.write(f"{cantidad} unidad(es)")
        col3.write(f"S/ {subtotal:.2f}")

        if st.button("Eliminar", key=f"eliminar_{nombre}"):
            del st.session_state.carrito[nombre]
            st.rerun()

    st.subheader(f"Total: S/ {total:.2f}")

    st.info(
        "El pedido es una demostración. "
        "Confirma la disponibilidad con el local."
    )

    if st.button("Vaciar carrito"):
        st.session_state.carrito = {}
        st.rerun()

else:
    st.write("Tu carrito está vacío. ¡Elige tu bebida favorita!")

st.divider()

# SOBRE NOSOTROS
st.header("🏖️ Sobre BluFresh")

st.write(
    "BluFresh nace para convertir cada día de verano en una "
    "experiencia refrescante. Nos inspiramos en el azul del mar, "
    "la calidez de la arena y los colores mágicos del atardecer "
    "para ofrecer bebidas frías, creativas y llenas de sabor."
)

# CONTACTO
st.header("📍 Visítanos")

st.write("Disfruta el verano con BluFresh, frente al mar.")
st.write("📱 WhatsApp: agrega aquí el número de tu negocio.")
st.write("📸 Instagram: agrega aquí tu cuenta.")

st.caption("© 2026 BluFresh | Refresca tu verano 🌊")
