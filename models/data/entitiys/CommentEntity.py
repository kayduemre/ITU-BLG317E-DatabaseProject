
class CommentEntity:
    def __init__(self, comment, vote, like, dislike, name, date, book_id):
        self.comment = comment
        self.vote = vote
        self.like = like
        self.dislike = dislike
        self.name = name
        self.date = date
        self.book_id = book_id
    
    def dic(self):
        dic = {
           "name": self.name,
           "comment_date": self.date,
           "descriptions": self.comment,
           "like": self.like,
           "dislike": self.dislike,
           "vote": self.vote,
           "book_id": self.book_id
        }
        return dic