from infra import Infra

#Création de la classe Batiment
class Batiment:
    def __init__(self, id_building, list_infras) -> None:
        self.id_building = id_building
        if type(list_infras) == Infra: 
            self.list_infras = list_infras

    def get_building_difficulty(self) -> float:
        building_diff = 0
        for infra in self.list_infras:
            building_diff += infra.get_infra_difficulty()