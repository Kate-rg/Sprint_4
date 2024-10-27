from main import BooksCollector
import pytest

class TestBooksCollector:


    def test_add_new_book_add_book(self):
        books_collector = BooksCollector()

        book_name = "To Kill a Mockingbird"

        assert book_name not in books_collector.books_genre

        books_collector.add_new_book(book_name)

        assert book_name in books_collector.books_genre



    def test_add_new_book_add_repeat_book(self):
        books_collector = BooksCollector()

        book_name = "To Kill a Mockingbird"

        books_collector.add_new_book(book_name)

        books_collector.add_new_book(book_name)

        assert len(books_collector.books_genre) == 1



    @pytest.mark.parametrize("book_name", ["", "A" * 41])
    def test_negative_add_new_book_add_long_name_book(self, book_name):
        books_collector = BooksCollector()

        books_collector.add_new_book(book_name)

        assert book_name not in books_collector.books_genre



    @pytest.mark.parametrize("book_name", ["A", "A" * 39, "A" * 40])
    def test_add_new_book_add_permissible_name_book(self, book_name):
        books_collector = BooksCollector()

        books_collector.add_new_book(book_name)

        assert book_name in books_collector.books_genre



    @pytest.mark.parametrize("book_name, genre", [
        ("Книга 1", "Фантастика"),
        ("Книга 2", "Ужасы"),
        ("Книга 3", "Детективы"),
        ("Книга 4", "Мультфильмы"),
        ("Книга 5", "Комедии")
    ])
    def test_set_book_genre_set_book_available_genre(self, book_name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)

        assert books_collector.books_genre[book_name] == genre



    def test_set_book_genre_when_genre_not_available(self):
       books_collector = BooksCollector()
       books_collector.add_new_book("Книга 1")
       books_collector.set_book_genre("Книга 1", "Неизвестный жанр")

       assert books_collector.books_genre["Книга 1"] == ''



    @pytest.mark.parametrize("book_name, genre", [
    ("Дюна", "Фантастика"),
    ("Шрек", "Мультфильмы"),
    ("Трое в лодке, не считая собаки", "Комедии")
])
    def test_get_books_for_children_get_books_for_children_rith(self, book_name, genre):
        books_collector = BooksCollector()

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)

        actual_books = books_collector.get_books_for_children()

        assert book_name in actual_books



    @pytest.mark.parametrize("book_name, genre", [
    ("Оно", "Ужасы"),
    ("Шерлок Холмс", "Детективы")
])
    def test_negative_get_books_for_children(self, book_name, genre):
        books_collector = BooksCollector()

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)

        actual_books = books_collector.get_books_for_children()

        assert book_name not in actual_books



    @pytest.mark.parametrize("book_name, genre", [
        ("Дюна", "Фантастика"),
        ("Оно", "Ужасы"),
        ("Убийство в Восточном экспрессе", "Детективы"),
        ("Шрек", "Мультфильмы"),
        ("Трое в лодке, не считая собаки", "Комедии")
    ])
    def test_get_books_with_specific_genre_get_books_with_specific_available_genre(self, book_name, genre):
        books_collector = BooksCollector()

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)

        actual_books = books_collector.get_books_with_specific_genre(genre)
        assert actual_books[0] == book_name



    def test_add_book_in_favorites_added(self):
        books_collector = BooksCollector()

        book_name = "1984"
        books_collector.add_new_book(book_name)

        books_collector.add_book_in_favorites(book_name)

        assert book_name in books_collector.favorites



    def test_delete_book_from_favorites(self):
        books_collector = BooksCollector()

        book_name = "1984"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)

        books_collector.delete_book_from_favorites(book_name)

        assert book_name not in books_collector.favorites





