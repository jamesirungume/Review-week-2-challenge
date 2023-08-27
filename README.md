Restaurant Review System

Welcome to the Restaurant Review System! This project allows customers to leave reviews for restaurants and provides insights into the dining experiences.
Table of Contents

    Classes
        Customer
        Review
        Restaurant
    Usage
    Example
    Notes

Classes
Customer

The Customer class represents a customer who can leave reviews for restaurants. It features attributes and methods such as:

    name: The given name of the customer.
    family_name: The family name of the customer.
    reviews: A list of reviews left by the customer.
    add_review(restaurant, rating): Adds a review for a restaurant with a specified rating.
    num_reviews(): Returns the total number of reviews left by the customer.
    find_by_name(name): Class method to find a customer by their full name.
    find_all_by_given_name(name): Class method to find all customers with a given given name.

Review

The Review class represents a review left by a customer for a restaurant. It includes attributes and methods like:

    customer: The customer who left the review.
    rating: The rating given in the review.
    restaurant: The restaurant that was reviewed.
    __str__(): Returns a string representation of the review.

Restaurant

The Restaurant class represents a restaurant that can receive reviews. It provides functionality for:

    name: The name of the restaurant.
    reviews: A list of reviews left for the restaurant.
    restaurant_name(): Returns the name of the restaurant.
    customers(): Returns a list of customers who reviewed the restaurant.
    average_star_rating(): Calculates and returns the average star rating of the restaurant based on reviews.

Usage

    Instantiate Customer and Restaurant objects.
    Allow customers to leave reviews for restaurants using the add_review method.
    Access restaurant information and reviews using the provided methods.
    Retrieve customer information and reviews using the provided methods.
    Calculate the average star rating of a restaurant.

Example

python

from customer import Customer
from restaurant import Restaurant

# Create customers and restaurants
john = Customer("John", "Doe")
jane = Customer("Jane", "Smith")

tasty_bites = Restaurant("Tasty Bites")
fancy_eats = Restaurant("Fancy Eats")

# Customers leave reviews for restaurants
john.add_review(tasty_bites, 4)
jane.add_review(fancy_eats, 5)

# Print restaurant names
print("Restaurant Names:", tasty_bites.restaurant_name(), fancy_eats.restaurant_name())

# Print customer reviews and reviewed restaurants
for restaurant in [tasty_bites, fancy_eats]:
    print(f"Reviews for {restaurant.restaurant_name()}:")
    for review in restaurant.reviews():
        print(f"Customer: {review.customer_review().full_name()}, Rating: {review.ratings()}")
    print(f"Customers who reviewed {restaurant.restaurant_name()}:")
    for customer in restaurant.customers():
        print("Customer:", customer.full_name())


