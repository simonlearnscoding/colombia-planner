class Destination:
    def __init__(self, title, estimated_time, description, preference_points, connections):
        self.title = title
        self.description = description
        self.estimated_time = estimated_time
        self.preference_points = preference_points
        self.connections = connections  # List of tuples: (Destination, Price)


# Define destinations
bogota = Destination(
    "Bogotá",
    1,
    "The vibrant capital of Colombia, known for its history, art, and gastronomy.",
    4,
    []
)
medellin = Destination(
    "Medellín",
    2,
    "The City of Eternal Spring, famous for its innovation and vibrant culture.",
    8,
    []
)
cartagena = Destination(
    "Cartagena",
    1,
    "A historic port city with colonial charm and Caribbean beaches.",
    6,
    []
)
tayrona = Destination(
    "Tayrona",
    3,
    "A national park offering breathtaking beaches and lush jungle.",
    7,
    []
)
coffee_region = Destination(
    "Coffee Region",
    2,
    "The heart of Colombian coffee production, surrounded by lush mountains.",
    9,
    []
)
san_andres = Destination(
    "San Andrés",
    3,
    "A Caribbean paradise with crystal-clear waters and coral reefs.",
    9,
    []
)
leticia = Destination(
    "Leticia",
    4,
    "Gateway to the Amazon rainforest and a hub for jungle treks.",
    8,
    []
)
guatape = Destination(
    "Guatapé",
    1,
    "A colorful town known for the iconic El Peñol Rock and stunning lakes.",
    7,
    []
)
salento = Destination(
    "Salento",
    2,
    "A charming town in the Coffee Region, close to the Cocora Valley.",
    8,
    []
)
minca = Destination(
    "Minca",
    2,
    "A tranquil town in the Sierra Nevada, perfect for nature and coffee lovers.",
    7,
    []
)
santa_marta = Destination(
    "Santa Marta",
    1,
    "A coastal city near Tayrona, offering history and beach relaxation.",
    6,
    []
)
villa_de_leyva = Destination(
    "Villa de Leyva",
    2,
    "A colonial town with cobblestone streets and preserved architecture.",
    7,
    []
)
popayan = Destination(
    "Popayán",
    2,
    "The White City, known for its colonial charm and rich history.",
    6,
    []
)
cali = Destination(
    "Cali",
    2,
    "The Salsa Capital of the World, offering vibrant nightlife and culture.",
    6,
    []
)
barichara = Destination(
    "Barichara",
    2,
    "A picturesque colonial town, known as the most beautiful in Colombia.",
    8,
    []
)
isla_de_rosario = Destination(
    "Islas del Rosario",
    1,
    "A stunning archipelago near Cartagena, famous for crystal-clear waters.",
    9,
    []
)
raquira = Destination(
    "Ráquira",
    1,
    "A small town famous for its pottery and artisan crafts.",
    6,
    []
)

# Define connections
bogota.connections = [
    (medellin, 50), (cartagena, 90), (coffee_region, 70),
    (san_andres, 140), (leticia, 160), (salento, 80),
    (santa_marta, 100), (villa_de_leyva, 50), (popayan, 120),
    (cali, 100), (barichara, 60), (raquira, 40)
]
medellin.connections = [
    (bogota, 50), (cartagena, 80), (coffee_region, 40),
    (san_andres, 130), (leticia, 150), (guatape, 30), (salento, 60),
    (santa_marta, 120), (popayan, 90), (cali, 70)
]
cartagena.connections = [
    (bogota, 90), (medellin, 80), (san_andres, 100),
    (santa_marta, 40), (isla_de_rosario, 30)
]
tayrona.connections = [
    (santa_marta, 20)  # Only accessible from Santa Marta
]
coffee_region.connections = [
    (bogota, 70), (medellin, 40), (salento, 20), (popayan, 50)
]
san_andres.connections = [
    (bogota, 140), (cartagena, 100)
]
leticia.connections = [
    (bogota, 160), (medellin, 150)
]
guatape.connections = [
    (medellin, 30), (bogota, 60)
]
salento.connections = [
    (bogota, 80), (medellin, 60), (coffee_region, 20)
]
minca.connections = [
    (santa_marta, 30)  # Only accessible from Santa Marta
]
santa_marta.connections = [
    (bogota, 100), (medellin, 120), (cartagena, 40),
    (tayrona, 20), (minca, 30)
]
villa_de_leyva.connections = [
    (bogota, 50), (barichara, 70), (raquira, 20)
]
popayan.connections = [
    (bogota, 120), (medellin, 90), (cali, 40), (coffee_region, 50)
]
cali.connections = [
    (bogota, 100), (medellin, 70), (popayan, 40)
]
barichara.connections = [
    (bogota, 60), (villa_de_leyva, 70)
]
isla_de_rosario.connections = [
    (cartagena, 30)
]
raquira.connections = [
    (villa_de_leyva, 20), (bogota, 40)
]

# List of all destinations
destinations = [
    bogota, medellin, cartagena, tayrona, coffee_region, san_andres, leticia,
    guatape, salento, minca, santa_marta, villa_de_leyva, popayan, cali,
    barichara, isla_de_rosario, raquira
]
