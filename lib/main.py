from review import Review
from customer import Customer
from restaurant import Restaurant



customer1 = Customer("James", "Murigu")
customer2 = Customer("Jane", "Smith")

restaurantA = Restaurant("Cook Room")
restaurantB = Restaurant("Healthy Dish")


customer1.add_review(restaurantA, 2)
customer2.add_review(restaurantB, 1)


print("Restaurant Names:", restaurantA.restaurant_name(), restaurantB.restaurant_name())


for restaurant in [restaurantA, restaurantB]:
    print("Reviews for", restaurant.restaurant_name())
    for review in restaurant.reviews:  
        print("Customer:", review.customer.full_name(), "Rating:", review.rating)
    
    print("Customers who reviewed", restaurant.restaurant_name())
    for customer in restaurant.customers():
        print("Customer:", customer.full_name())

