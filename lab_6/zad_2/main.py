from Student import Student
from Library import Library
from Book import Book
from Employee import Employee
from Order import Order
from House import House
from Flat import Flat

s1 = Student(name='Paweł Zalewski', marks=55)
s2 = Student(name='Julia Przybylska', marks=38)

print('Zadanie 1:')

print(s1.is_passed())
print(s2.is_passed())

l1 = Library(city="Katowice", street="Paderewskiego",
             zip_code="40-281", open_hours="8.00-16.00", phone="783548649")
l2 = Library(city="Ruda Śląśka", street="Kubiny",
             zip_code="41-710", open_hours="8.00-16.00", phone="956384267")

e1 = Employee(first_name="Paulina", last_name="Góral", hire_date="10,10,2018",
              city="Katowice", street="Witosa",
              zip_code="40-284", phone="659324865")
e2 = Employee(first_name="Maciej", last_name="Kawecki", hire_date="14.07.2018",
              city="Ruda Śląska", street="Podgórska",
              zip_code="41-709", phone="168954326")

b1 = Book(library=l1, publication_date="10.05.2005", author_name="Dominik",
          author_surname="Dudek", number_of_pages=356,
          title="Ania z Zielonego Wzgórza")
b2 = Book(library=l2, publication_date="18.06.1999", author_name="Sylwia",
          author_surname="Peterson", number_of_pages=986,
          title="Harry Potter")

o1 = Order(employee=e1.last_name+' ' + e1.first_name, student=s1.name,
           books=b1.title, order_date='12.05.2021')
o2 = Order(employee=e2.last_name+' ' + e2.first_name, student=s2.name,
           books=b2.title, order_date='28.09.2021')

print('\nZadanie 2:')
print(o1)
print(o2)

h1 = House(area=150, rooms=7, price=800000, address="Ruda Śląska", plot=100)
f1 = Flat(area=60, rooms=4, price=250000, address="Katowice", floor=6)

print('\nZadanie 3:')

print(h1)
print(f1)
