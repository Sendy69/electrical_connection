# Création de la classe infrastructure
class Infra:
    #Création des attributs d'instances
    def __init__(self, infra_id, length,infra_type, nb_houses ) -> None:
        self.infra_id = infra_id
        self.length = length
        self.infra_type = infra_type
        self.nb_houses = nb_houses

    # La Méthode repair_infra() permet de faire passer une infra de l'état "a_remplacer" à "infra_intacte" 
    def repair_infra(self):
        if self.infra_type == "a_remplacer":
            self.infra_type = "infra_intacte"
    
    # La Méthode get_infra_difficulty() permet de calculer la difficulté de reparation d'une infra 
    def get_infra_difficulty(self) -> float:
        infra_diff = self.length/self.nb_houses
        return infra_diff
    
    # La Méthode __radd__() permet de sommer la difficulté de reparation de 02 infras
    def __radd__(self, other_infra) -> float:
        if type(other_infra)!= Infra:
            raise Exception("L'autre objet doit être une infrastructure")
        else:
            return self.get_infra_difficulty() + other_infra
        
        