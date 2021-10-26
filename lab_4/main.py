# Zadanie 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks > 50:
            return True
        else:
            return False


s1 = Student(name='Paweł Zalewski', marks=55)
s2 = Student(name='Julia Przybylska', marks=38)
print('Zadanie 1:')
print(s1.is_passed())
print(s2.is_passed())


# Zadanie 2
class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka znajduje się w mieście {self.city} przy ulicy {self.street}, kod pocztowy to {self.zip_code}, jest otwarta w godzinach {self.open_hours}, można również dzwonić pod numer{self.phone}.'


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Student/Studentka {self.student} zamówił książkę "{self.books}" w dniu {self.order_date} u pracownika {self.employee}.'


class Employee:
    def __init__(self, first_name, last_name, hire_date, city, street, zip_code, phone):
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
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages,title):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        self.title=title

    def __str__(self):
        return f'Książka "{self.title}" znajduje się w {self.library}, została wydana {self.publication_date}, jej autorem jest {self.author_name} {self.author_surname}, posiada {self.number_of_pages} stron.'


l1 = Library(city="Katowice", street="Paderewskiego", zip_code="40-281", open_hours="8.00-16.00", phone="783548649")
l2 = Library(city="Ruda Śląśka", street="Kubiny", zip_code="41-710", open_hours="8.00-16.00", phone="956384267")

e1 = Employee(first_name="Paulina", last_name="Góral", hire_date="10,10,2018", city="Katowice", street="Witosa", zip_code="40-284", phone="659324865")
e2 = Employee(first_name="Maciej", last_name="Kawecki", hire_date="14.07.2018", city="Ruda Śląska", street="Podgórska", zip_code="41-709", phone="168954326")

b1 = Book(library=l1, publication_date="10.05.2005", author_name="Dominik", author_surname="Dudek", number_of_pages=356,title="Ania z Zielonego Wzgórza")
b2 = Book(library=l2, publication_date="18.06.1999", author_name="Sylwia", author_surname="Peterson", number_of_pages=986,title="Harry Potter")

o1 = Order(employee=e1.last_name+' ' +e1.first_name, student=s1.name, books=b1.title, order_date='12.05.2021')
o2 = Order(employee=e2.last_name+' ' +e2.first_name, student=s2.name, books=b2.title, order_date='28.09.2021')


print('\nZadanie 2:')
print(o1)
print(o2)

# Zadanie 3
class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f'Nieruchomość o metrażu {self.area} m2, ilości pokoi {self.rooms}, cenie w wysokośći {self.price} PLN, w mieście {self.address} posiada płot długości {self.plot} m.'



class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f'Nieruchomość o metrażu {self.area} m2, ilości pokoi {self.rooms}, cenie w wysokośći {self.price} PLN, w mieście {self.address} znajduje się na piętrze {self.floor}.'


h1 = House(area=150, rooms=7, price=800000, address="Ruda Śląska", plot=100)
f1 = Flat(area=60, rooms=4, price=250000, address="Katowice", floor=6)

print('\nZadanie 3:')
print(h1)
print(f1)
