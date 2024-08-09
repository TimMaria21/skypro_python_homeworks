class User:

    def __init__(self, first_name, last_name):
        self.userF = first_name
        self.userL = last_name

    def prFirst_name(self):
        print(self.userF)

    def prLast_name(self):
        print(self.userL)

    def prAll_name(self):
        print(self.userF, self.userL)