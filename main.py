class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

        def afficherInformations(self):
            print(f"Employé : {self.numeroPermis}")
            print(f"Nom : {self.nom}")
            print(f"Prénom : {self.prenom}")
            if self.voitureService != None:
                print("Possede une Voiture de service :")
                self.voitureService.afficherInformations()
            else:
                print("Aucune voiture de service ")