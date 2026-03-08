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

    def affecterVoiture(self, voiture):
        if self.voitureService == None:
            if voiture.chauffeur == None:
                self.voitureService = voiture
                voiture.chauffeur = self
                print(f"La voiture {voiture.matricule} est bien ajoutée")
            else:
                print(f"La voiture {voiture.matricule} est deja avec un employé")
        else:
            print(f"L'employé {self.nom} {self.prenom} possède déjà une voiture")

            def retirerVoiture(self):
                if self.voitureService != None:
                    self.voitureService.chauffeur = None
                    self.voitureService = None
class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None