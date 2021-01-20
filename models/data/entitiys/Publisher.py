
class Publisher:

    def __init__(self, publisher, publisher_date):
        self.publisher = publisher
        self.publisher_date = publisher_date
    
    def dic(self):
        pub = {
            "publisher": self.publisher,
            "publisher_date": self.publisher_date
        }
        return pub
