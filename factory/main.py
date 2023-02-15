from abc import ABC


class Foo(ABC):
    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def __get_iterator__(self):
        return iter(self)
