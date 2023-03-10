from abc import ABC, abstractmethod

# Interface
<<<<<<< HEAD
class Burger(ABC):
    # Crea la implementaciòn por defecto
    @abstractmethod
    def burger_factory(self):
        pass

    # Logìca del negocio
    def information(self) -> str:
        burger = self.burger_factory()
        print(f"Price of the burger: {burger.add_price()}")


# Creador concreto para la hamburgesa
class BurgerCreator(Burger):
    def burger_factory(self) -> Burger:
        return CheeseCreator()

    def burger_factory(self) -> Burger:
        return VeggieCreator()


# Creador concreto 
=======
>>>>>>> 8687547 (Concrete example done)
class CheeseBurger(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Creador del producto contreto
class CheeseCreator(CheeseBurger):
    def information(self) -> str:
        return f"Operation: {self.operation()}"

    def operation(self) -> str:
        return 'Cheese burger created, and the price of the burger is: $25'

# Producto 2

class VeggieBurger(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class VeggieCreator(VeggieBurger):
    def information(self) -> str:
        return f"Operation: {self.operation()}"

    def operation(self) -> str:
        return 'Veggie burger created, and the price of the burger is: $15'


<<<<<<< HEAD
=======
# Creator
class Burger(ABC):
    # Crea la implementaciòn por defecto
    @abstractmethod
    def burger_factory(self):
        pass

    # Logìca del negocio
    def information(self) -> str:
        burger = self.burger_factory()
        print(f"Price of the burger: {burger.add_price()}")


# Creador concreto para la hamburgesa
class BurgerCreator(Burger):
    def burger_factory(self) -> Burger:
        return CheeseCreator()

    def burger_factory(self) -> Burger:
        return VeggieCreator()


>>>>>>> 8687547 (Concrete example done)
# Codigo del cliente que mostrara los productos concretos
def client_code(creator: Burger) -> None:
    print("Client: I'm aware of the creator's class, but it still works")
    info = creator.information()
    print(f"{info}", end="")


if __name__ == "__main__":
    print("App: Launched with the concrete product 1")
    client_code(CheeseCreator())
    print("\n")
    print("App: Launched with the concrete product 2")
    client_code(VeggieCreator())
