class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages,title):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        self.title=title

    def __str__(self):
        return f'Książka "{self.title}" znajduje się w {self.library}, została wydana {self.publication_date}, jej autorem jest {self.author_name} {self.author_surname}, posiada {self.number_of_pages} stron.'

