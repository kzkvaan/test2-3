class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def name(self) -> str:
        return self._name


    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def pages(self) -> int:
        return self._pages


    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook:

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration


    def duration(self) -> float:
        return self._duration

    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError
            raise ValueError
        self._duration = float(value)


book = PaperBook("Ребекка", "Дафна Дюморье", 1)
print(book)
book.pages = 479
print(book.pages)