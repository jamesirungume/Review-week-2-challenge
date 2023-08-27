class Restaurant:
    all_restaurants =[]

    def __init__(self,name):
        self.name=name
        self.reviews=[]
        Restaurant.all_restaurants.append(self)

    def restaurant_name(self):
        return self.name 
    
    def reviews(self):
        return self.reviews
    
    def customers(self):
       return [review.customer for review in self.reviews]
    
    def average_satr_rating(self):
        total_sum_rating = sum(review.rating() for review in self.reviews)
        return total_sum_rating/len(self.reviews)
