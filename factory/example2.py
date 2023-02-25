from abc import ABC, abstractmethod

# Creators


class Burger(ABC):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @abstractmethod
    def burger_factory(self, ingredients):
        pass

    def display(self) -> str:
        burger = self.burger_factory(self.ingredients)
        result = f"Same creator's code works with {burger.display()}"
        return result


# Concrete prodcut creator
class BurgerCreator(Burger):
    def burger_factory(self) -> Burger:
        return BurgerCreator()


# Product
class CheeseBurger(ABC):
    @abstractmethod
    def display(self) -> str:
        pass


class ProductCheeseBurger(Burger):
    def display(self) -> str:
        return "Result of cheese burger"


def client_code(creator: Burger) -> None:
    print("Client: I'm aware of the creator's class, but it still works")
    print(f"{creator.display()}", end="")


if __name__ == "__main__":
    print("App: Launched with the concrete product 1")
    client_code(ProductCheeseBurger())
