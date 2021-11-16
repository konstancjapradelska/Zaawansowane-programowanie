class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Student/Studentka {self.student} zamówił książkę "{self.books}" w dniu {self.order_date} u pracownika {self.employee}.'

