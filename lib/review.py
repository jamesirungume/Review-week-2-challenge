class Review:
    all_reviews = []
    def __init__(self,customer,restaurant,rating):
        self.customer = customer
        self.rating =rating
        self.restaurant =restaurant
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating

    def customer_review(self):
        return self.customer

    def restaurant_review(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews


