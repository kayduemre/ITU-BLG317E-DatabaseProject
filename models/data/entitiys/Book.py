
class Book:
    def __init__(self,title,author,summary,publisher, language,page_number, price, created_date,account_id, category_id):
        self.title = title
        self.summary = summary
        self.author = author
        self.publisher = publisher
        self.language = language
        self.page_number = page_number
        self.price = price
        self.created_date =created_date
        self.account_id = account_id
        self.category_id = category_id
    
    def dic(self):
        dic = {
            "title": self.title,
            "author": self.author,
            "summary": self.summary,
            "publisher": self.publisher,
            "page_number": self.page_number,
            "language": self.language,
            "price": self.price,
            "created_date": self.created_date,
            "account_id": self.account_id,
            "category_id": self.category_id
        }
        return dic