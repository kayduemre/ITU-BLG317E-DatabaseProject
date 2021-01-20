
class FeedBack:

    def __init__(self, user_id,protect,reliability, delivery ):
        self.user_id = user_id
        self.protect = protect
        self.reliability = reliability
        self.delivery = delivery

    def dic(self):
        feedback = {
            "user_id": self.user_id,
            "protect" : self.protect,
            "reliability": self.reliability,
            "delivery": self.delivery
        }
        return feedback