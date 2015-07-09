class Melons(object):

    def get_base_price(self):
        BASE_MELON_PRICE = 5
        return BASE_MELON_PRICE


# WatermelonOrder = Melons()
# WatermelonOrder.BASE_MELON_PRICE = 




"""This file should have our melon-type classes in it."""


class WatermelonOrder(Melons):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        BASE_MELON_PRICE = self.get_base_price()
        total = BASE_MELON_PRICE  * qty   # TODO, calculate the real amount!

        if qty >= 3:
            total = total*0.75


        return total


class CantaloupeOrder(Melons):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        BASE_MELON_PRICE = self.get_base_price()
        total = BASE_MELON_PRICE  * qty   # TODO, calculate the real amount!

        if qty >= 5:
            total = total*0.5
    

        return total





class CasabaOrder(Melons):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        
        BASE_MELON_PRICE = self.get_base_price()

        total = (BASE_MELON_PRICE+1)*qty*1.5  # TODO, calculate the real amount!

        return total


class SharlynOrder(Melons):
    species = "Sharlyn"
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""


        BASE_MELON_PRICE = self.get_base_price()

        total = (BASE_MELON_PRICE *qty)*1.5   # TODO, calculate the real amount!

        return total

class SantaClausOrder(Melons):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        BASE_MELON_PRICE = self.get_base_price()

        total = (BASE_MELON_PRICE *qty)*1.5   # TODO, calculate the real amount!

        return total

       


class ChristmasOrder(Melons):
    species = "Christmas"
    color = 'green'
    imported = False
    shape = "natural"
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        BASE_MELON_PRICE = self.get_base_price()

        total = BASE_MELON_PRICE  *  qty   # TODO, calculate the real amount!

        return total


class HornedMelonOrder(Melons):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        BASE_MELON_PRICE = self.get_base_price()

        total = (BASE_MELON_PRICE  *qty)*1.5   # TODO, calculate the real amount!

        return total

class XiguaOrder(Melons):
    species = "Xigua"
    color = 'black'
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        BASE_MELON_PRICE = self.get_base_price()

        total = (BASE_MELON_PRICE *qty*2*1.5)   # TODO, calculate the real amount!

        return total

class OgenOrder(Melons):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    season = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        BASE_MELON_PRICE = self.get_base_price()
        
        total = (BASE_MELON_PRICE+1)*qty   # TODO, calculate the real amount!

        return total

















