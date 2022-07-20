class User:
    def __init__(self, _name, _password,_logged_in, id = None ):
        self.name = _name
        self.logged_in = _logged_in
        self.password = _password
        self.id = id
