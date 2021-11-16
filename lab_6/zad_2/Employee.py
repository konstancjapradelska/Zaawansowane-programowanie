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

