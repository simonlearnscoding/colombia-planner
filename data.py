class Destination:
    def __init__(self, title, estimated_time, description, preference_points, connections):
        self.title = title
        self.description = description
        self.estimated_time = estimated_time
        self.preference_points = preference_points
        self.connections = connections  # List of tuples: (Destination, Price, TravelTime)


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
    1,
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
    1,
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
    3,
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

# Define connections (Destination, Price, TravelTime in days)
bogota.connections = [
    (medellin, 50, 1), (cartagena, 90, 1), (coffee_region, 70, 1),
    (san_andres, 140, 2), (leticia, 160, 2), (salento, 80, 1),
    (santa_marta, 100, 1), (villa_de_leyva, 50, 0.5), (popayan, 120, 1.5),
    (cali, 100, 1), (barichara, 60, 1), (raquira, 40, 0.5)
]
medellin.connections = [
    (bogota, 50, 1), (cartagena, 80, 1.5), (coffee_region, 40, 0.5),
    (san_andres, 130, 2), (leticia, 150, 2), (guatape, 30, 0.5), (salento, 60, 1),
    (santa_marta, 120, 2), (popayan, 90, 1.5), (cali, 70, 1)
]
cartagena.connections = [
    (bogota, 90, 1), (medellin, 80, 1.5), (san_andres, 100, 2),
    (santa_marta, 40, 0.5), (isla_de_rosario, 30, 0.5)
]
tayrona.connections = [
    (santa_marta, 20, 0.25)  # Only accessible from Santa Marta
]
coffee_region.connections = [
    (bogota, 70, 1), (medellin, 40, 0.5), (salento, 20, 0.5), (popayan, 50, 1)
]
san_andres.connections = [
    (bogota, 140, 2), (cartagena, 100, 2)
]
leticia.connections = [
    (bogota, 160, 2), (medellin, 150, 2)
]
guatape.connections = [
    (medellin, 30, 0.5), (bogota, 60, 1)
]
salento.connections = [
    (bogota, 80, 1), (medellin, 60, 1), (coffee_region, 20, 0.5)
]
minca.connections = [
    (santa_marta, 30, 0.5)  # Only accessible from Santa Marta
]
santa_marta.connections = [
    (bogota, 100, 1), (medellin, 120, 2), (cartagena, 40, 0.5),
    (tayrona, 20, 0.25), (minca, 30, 0.5)
]
villa_de_leyva.connections = [
    (bogota, 50, 0.5), (barichara, 70, 1), (raquira, 20, 0.25)
]
popayan.connections = [
    (bogota, 120, 1.5), (medellin, 90, 1.5), (cali, 40, 0.5), (coffee_region, 50, 1)
]
cali.connections = [
    (bogota, 100, 1), (medellin, 70, 1), (popayan, 40, 0.5)
]
barichara.connections = [
    (bogota, 60, 1), (villa_de_leyva, 70, 1)
]
isla_de_rosario.connections = [
    (cartagena, 30, 0.5)
]
raquira.connections = [
    (villa_de_leyva, 20, 0.25), (bogota, 40, 0.5)
]

# List of all destinations
destinations = [
    bogota, medellin, cartagena, tayrona, coffee_region, san_andres, leticia,
    guatape, salento, minca, santa_marta, villa_de_leyva, popayan, cali,
    barichara, isla_de_rosario, raquira
]
