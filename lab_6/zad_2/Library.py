class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka znajduje się w mieście {self.city} przy ulicy {self.street}, kod pocztowy to {self.zip_code}, jest otwarta w godzinach {self.open_hours}, można również dzwonić pod numer{self.phone}.'
