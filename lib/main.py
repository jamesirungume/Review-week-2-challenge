from review import Review
from customer import Customer
from restaurant import Restaurant

# Create instances of Customer and Restaurant
customer1 = Customer("James", "Murigu")
customer2 = Customer("Jane", "Smith")

restaurantA = Restaurant("Cook Room")
restaurantB = Restaurant("Healthy Dish")

# Customers leave reviews for restaurants
customer1.add_review(restaurantA, 2)
customer2.add_review(restaurantB, 1)

# Print restaurant names
print("Restaurant Names:", restaurantA.restaurant_name(), restaurantB.restaurant_name())

# Print reviews and customers for each restaurant
for restaurant in [restaurantA, restaurantB]:
    print("Reviews for", restaurant.restaurant_name())
    for review in restaurant.reviews:
        print("Customer:", review.customer_review().full_name(), "Rating:", review.rating)

    print("Customers who reviewed", restaurant.restaurant_name())
    for customer in restaurant.customers():
        print("Customer:", customer.full_name())

# Test the reviewed_restaurants() method for Customer
print(customer1.full_name(), "reviewed restaurants:", customer1.reviewed_restaurants())
print(customer2.full_name(), "reviewed restaurants:", customer2.reviewed_restaurants())

# Test the num_reviews() method for Customer
print(customer1.full_name(), "number of reviews:", customer1.num_reviews())
print(customer2.full_name(), "number of reviews:", customer2.num_reviews())

# Test the find_by_name() method for Customer
print("Finding customer by name:", Customer.find_by_name("James Murigu"))
# Test the find_all_by_given_name() method for Customer
print("Finding customers by given name:", Customer.find_all_by_given_name("Jane"))

# Test the average_star_rating() method for Restaurant
print("Average Star Rating for", restaurantA.restaurant_name(), ":", restaurantA.average_star_rating())
print("Average Star Rating for", restaurantB.restaurant_name(), ":", restaurantB.average_star_rating())
