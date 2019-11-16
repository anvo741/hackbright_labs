from random import randint

"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """A melon order."""
        
        self.species = species
        self.qty = qty

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        species = self.species
        base_price = randint(5, 9)
        if species == 'Christmas':
            base_price = base_price * 1.5
        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        order_type = self.order_type
        base_price = self.get_base_price()
        fee = 0
        if order_type == 'international' and qty < 10:
            fee = 3
        total = (1 + self.tax) * self.qty * base_price
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    shipped = False
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    shipped = False
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_codea


class GovernmentMelonOrder(AbstractMelonOrder):
    '''A US government melon order.'''

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact than an order has been inspected."""
        self.passed_inspection = passed
