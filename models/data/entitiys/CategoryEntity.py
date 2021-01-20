class CategoryEntity:
    def __init__(self, title, accountId, datetime):
        self.book_id = 0
        self.account_id = accountId
        self.created_date = datetime
        self.title = title
    
    def convertDictionary(self):
        dic = {
            "created_date" : self.created_date,
            "title" : self.title,
            "account_id" : self.account_id
        }
        return dic
        
    def setDatetime(self, date):
        self.created_date = date


