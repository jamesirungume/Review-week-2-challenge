from review import Review
from restaurant import Restaurant

class Customer:
    all_customers = []

    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
    
    @property
    def given_name(self):
        return self.name
    
    @given_name.setter
    def given_name(self, new_name):
        self.name = new_name
    
    @property
    def last_name(self):
        return self.family_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        self.family_name = new_last_name
        
    def full_name(self):
        return f"{self.name} {self.family_name}"
    
    def __str__(self):
        return f"{self.full_name()}"

    @classmethod
    def all(cls):
        return cls.all_customers
    
    def reviewed_restaurants(self):
        return [review.restaurant_review().restaurant_name() for review in self.reviews]
    
    def add_review(self, restaurant, rating):
        added_review = Review(self, restaurant, rating)
        self.reviews.append(added_review)
        restaurant.reviews.append(added_review)
    
    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
            
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = [customer.name for customer in cls.all_customers if customer.given_name.lower() == name.lower()]
        return matching_customers

    



