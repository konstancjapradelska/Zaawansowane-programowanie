from Property import Property


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Nieruchomość o metrażu {self.area} m2, ilości pokoi {self.rooms}, ' \
               f'cenie w wysokośći {self.price} PLN, w mieście {self.address} ' \
               f'posiada płot długości {self.plot} m.'

