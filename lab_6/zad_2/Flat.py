from Property import Property


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Nieruchomość o metrażu {self.area} m2, ilości pokoi {self.rooms}, cenie w wysokośći {self.price} PLN, w mieście {self.address} znajduje się na piętrze {self.floor}.'

