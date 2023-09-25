class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def change_given_name(self, new_given_name):
        self.given_name = new_given_name

    def change_family_name(self, new_family_name):
        self.family_name = new_family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def restaurant_name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def add_review(self, customer, rating):
        review = Review(customer, self, rating)
        self.reviews.append(review)

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer for review in self.reviews]))


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    @classmethod
    def average_star_rating(cls, restaurant):
        restaurant_reviews = [review.rating for review in cls.all_reviews if review.restaurant == restaurant]
        if not restaurant_reviews:
            return 0
        return sum(restaurant_reviews) / len(restaurant_reviews)

    @classmethod
    def customer_reviews(cls, customer):
        return [review for review in cls.all_reviews if review.customer == customer]

    @classmethod
    def customer_num_reviews(cls, customer):
        return len(cls.customer_reviews(customer))

    @classmethod
    def find_by_name(cls, full_name):
        return [customer for customer in cls.all_customers if customer.full_name() == full_name][0]

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
