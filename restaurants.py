# Defining a class named Customer
class Customer:
    # A class-level variable to store all customer objects
    all_customers = []

    # Constructor to initialize customer data
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.customer_reviews = []  # List to store customer reviews
        Customer.all_customers.append(self)  # Add the customer to the list of all customers

    # Method to change the given name of a customer
    def change_given_name(self, new_given_name):
        self.given_name = new_given_name

    # Method to change the family name of a customer
    def change_family_name(self, new_family_name):
        self.family_name = new_family_name

    # Method to get the full name of a customer
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Class method to get a list of all customers
    @classmethod
    def all(cls):
        return cls.all_customers

    # Method to add a review for a restaurant
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.customer_reviews.append(review)


# Defining  a class named Restaurant
class Restaurant:
    # A class-level variable to store all restaurant objects
    all_restaurants = []

    # Constructor to initialize restaurant data
    def __init__(self, name):
        self.name = name
        self.restaurant_reviews = []  # List to store restaurant reviews
        Restaurant.all_restaurants.append(self)  # Add the restaurant to the list of all restaurants

    # Method to get the name of a restaurant
    def restaurant_name(self):
        return self.name

    # Class method to get a list of all restaurants
    @classmethod
    def all(cls):
        return cls.all_restaurants

    # Method to add a review from a customer for the restaurant
    def add_review(self, customer, rating):
        review = Review(customer, self, rating)
        self.restaurant_reviews.append(review)

    # Method to get the reviews for the restaurant
    def reviews(self):
        return self.restaurant_reviews

    # Method to get the list of customers who reviewed the restaurant
    def customers(self):
        return list(set([review.customer for review in self.restaurant_reviews]))


# Defining a class named Review
class Review:
    # A class-level variable to store all review objects
    all_reviews = []

    # Constructor to initialize review data
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)  # Add the review to the list of all reviews

    # Method to get the rating of a review
    def rating(self):
        return self.rating_value

    # Class method to get a list of all reviews
    @classmethod
    def all(cls):
        return cls.all_reviews

    # Method to get the customer who made the review
    def customer(self):
        return self.customer

    # Method to get the restaurant that was reviewed
    def restaurant(self):
        return self.restaurant

    # Class method to calculate the average star rating for a restaurant
    @classmethod
    def average_star_rating(cls, restaurant):
        restaurant_reviews = [review.rating_value for review in cls.all_reviews if review.restaurant == restaurant]
        if not restaurant_reviews:
            return 0
        return sum(restaurant_reviews) / len(restaurant_reviews)

    # Class method to get all reviews made by a specific customer
    @classmethod
    def customer_reviews(cls, customer):
        return [review for review in cls.all_reviews if review.customer == customer]

    # Class method to get the number of reviews made by a specific customer
    @classmethod
    def customer_num_reviews(cls, customer):
        return len(cls.customer_reviews(customer))

    # Class method to find a customer by their full name
    @classmethod
    def find_by_name(cls, full_name):
        return [customer for customer in cls.all_customers if customer.full_name() == full_name][0]

    # Class method to find all customers with a given first name
    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]


# customer1 = Customer("John", "Doe")
# customer2 = Customer("Jane", "Smith")
# restaurant1 = Restaurant("Delicious Delights")
# restaurant2 = Restaurant("Tasty Treats")

# customer1.add_review(restaurant1, 5)
# customer2.add_review(restaurant1, 4)
# customer1.add_review(restaurant2, 3)

# print(Customer.all())  # [customer1, customer2]
# print(Restaurant.all())  # [restaurant1, restaurant2]
# print(Review.all())  # [review1, review2, review3]
# print(restaurant1.reviews())  # [review1, review2]
# print(restaurant1.customers())  # [customer1, customer2]
# print(Review.average_star_rating(restaurant1))  # 4.5
# print(Review.customer_num_reviews(customer1))  # 2
# print(Review.find_by_name("John Doe"))  # customer1
# print(Review.find_all_by_given_name("Jane"))  # [customer2]
