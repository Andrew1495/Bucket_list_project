from itsdangerous import want_bytes


class Country:
    def __init__(self, _name, _continent, id = None):
        self.name = _name
        self.continent = _continent
        self.id = id