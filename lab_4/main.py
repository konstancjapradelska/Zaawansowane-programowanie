# Zadanie 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks>50: return True
        else: return False

s1 = Student(name = 'Paweł',marks = 55)
s2 = Student(name = 'Julia',marks = 38)
print('Zadanie 1:')
print(s1.is_passed())
print(s2.is_passed())

# Zadanie 2
class Library:
    def __init__(self, city, street,zip_code,open_hours,phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka znajduje się w mieście {self.city} przy ulicy {self.street}, kod pocztowy to {self.zip_code}, jest otwarta w godzinach {self.open_hours}, można również dzwonić pod numer{self.phone}.'

class Order:
    def __init__(self, employee, student,books,order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return f'Student {self.student} zamówił książkę "{self.books}" w dniu {self.order_date} u pracownika {self.employee}.'


class Employee:
    def __init__(self, first_name, last_name, hire_date, city, street,zip_code,phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name} zamieszkały mieście {self.city} przy ulicy {self.street}, kod pocztowy to {self.zip_code}, numer kontaktowy {self.phone}.'

class Book:
    def __init__(self, library, publication_date,author_name,author_surname,number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f'Książka znajduje się w {self.library}, została wydana {self.publication_date}, jej autorem jest {self.author_name} {self.author_surname}, posiada {self.number_of_pages} stron.'


o1=Order(employee='Jan Kowalski',student='Julia Nowak',books='Ania z Zielonego Wzgórza',order_date='12.05.2021')
o2=Order(employee='Martyna Pradelska',student='Karol Kowalczyk',books='Harry Potter',order_date='28.09.2021')


print('\nZadanie 2:')
print(o1)
print(o2)