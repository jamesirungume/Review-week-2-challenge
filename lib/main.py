from review import Review
from customer import Customer
from restaurant import Restaurant


# Create instances of Customer and Restaurant
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Fancy Eats")

# Customers leave reviews for restaurants
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant2, 5)

# Print restaurant names
print("Restaurant Names:", restaurant1.restaurant_name(), restaurant2.restaurant_name())

# Print reviews and customers
for restaurant in [restaurant1, restaurant2]:
    print("Reviews for", restaurant.restaurant_name())
    for review in restaurant.reviews:  
        print("Customer:", review.customer.full_name(), "Rating:", review.rating)
    
    print("Customers who reviewed", restaurant.restaurant_name())
    for customer in restaurant.customers():
        print("Customer:", customer.full_name())

