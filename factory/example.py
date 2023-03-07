# Code taken from NeetCode
# Creamos la clase hamburgesa

class Burger:
    def __init__(self, ingredients, name):
        self.ingredients = ingredients
        self.name = name

    def display(self):
        print(f"The Hamburger {self.name} was created with this ingredients: {self.ingredients}")

# Instaciamos la clase factory para que nos ayude
# a ordenar la hamburgesa que queremos


class FactoryBurger:
    def cheese_burger(self):
        ingredients = ["beef", "cheese", "beef-patty"]
        name = "CheeseBurger"
        return Burger(ingredients, name)

    def veggie_burger(self):
        ingredients = ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
        name = "VeggieBurger"
        return Burger(ingredients, name)

    def vegan_burger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        name = "VeganBurger"
        return Burger(ingredients, name)


# Ahora solo le decimos que hamburguesa queremos

# Instanciamos la clase factory
burger_factory = FactoryBurger()


# Creamos el tipo de hamburgesa que queremos
veggie = burger_factory.veggie_burger().display()
cheese = burger_factory.cheese_burger().display()
cheese = burger_factory.vegan_burger().display()
