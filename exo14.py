class Rectangle:
    def init(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def air_rectangle(self):
        return self.longueur * self.largeur

    def get_largeur(self):
        return self.largeur

    def get_longueur(self):
        return self.longueur
        

rectangle = Rectangle(5,4)
print(rectangle.get_largeur())
print(rectangle.get_longueur())
print(rectangle.air_rectangle())