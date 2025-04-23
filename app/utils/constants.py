from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    NGO = "ngo"
    USER = "user"

class FoodStatus(str, Enum):
    AVAILABLE = "available"
    IN_TRANSIT = "in-transit"
    DELIVERED = "delivered"

DEFAULT_PAGE_SIZE = 10
MAX_FOOD_QUANTITY = 1000  # in kg