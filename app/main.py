from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects = []

    for customer in customers:
        customer_objects.append(Customer(customer["name"], customer["food"]))

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner_obj)
