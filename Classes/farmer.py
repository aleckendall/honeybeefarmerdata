class Farmer:

    def __init__(self, country_, telephone_, apiaries_=[]):
        self.country = country_
        self.telephone = telephone_
        self.apiaries = apiaries_

    def set_country(self, country_):
        self.country = country_
        return

    def get_country(self):
        return self.country

    def set_telephone(self, telephone_):
        self.telephone = telephone_
        return

    def get_telephone(self):
        return self.telephone

    def set_apiaries(self, apiaries_):
        self.apiaries = apiaries_
        return

    def get_apiaries(self):
        return self.apiaries