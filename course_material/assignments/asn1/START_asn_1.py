from PIL import Image
import requests
import pandas as pd

# Logging Setup
# We can use the logging module to log information about our code.
# This will do the same thing for us as print statements or using the debugger, again in a different way. 
# Logging can be made more elaborate, but we can start with just the basics - basically a print statement for logs only. 
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='testing.log', encoding='utf-8', level=logging.DEBUG)
#logging.debug('This will get logged')

# Note: the arrow and variable type thing at the end of function definitions is a type hint.
# It's not required, and it won't be enforced when code runs, it is basically a more formalized comment. 

def sampleTestFunction() -> int:
    return 7
class myProduct():

    def __init__(self, name, category, subcat, imageURL, prodURL, rating, numRate, discPrice, price) -> None:
        """
        Initialize a product object. Each product has a name, category, subcategory, image URL, product URL, rating, number of ratings, discount price, and price.

        Note that the price and ratings should be converted to floats and integers respectively. Error handling is good here. 

        Args:
            name (str): The name of the product.
            category (str): The category of the product.
            subcat (str): The subcategory of the product.
            imageURL (str): The URL of the product image.
            prodURL (str): The URL of the product.
            rating (float): The rating of the product.
            numRate (int): The number of ratings.
            discPrice (str): The discount price of the product.
            price (str): The base price of the product.
        """
        pass

    def __str__(self) -> str:
        """
        Returns:
            str: A string representation of the product.
        """
        pass

    def get_rating(self) -> float:
        """
        Get the rating of the product.

        Returns:
            float: The rating of the product.
        """
        pass
    def add_rating(self, rating, numberRate=1) -> float:
        """
        Add more ratings to the product. Update the rating based on the new rating and the number of ratings added.
        Note that you'll need to recalculate the weighted average of the ratings, based on the original number of ratings and their mean, and the new rating and the number of new ratings with their mean,
        Also update the number of ratings.

        Args:
            rating (float): The mean of the new ratings to add.
            numberRate (int, optional): The number of ratings the above value is based on. Defaults to 1.

        Returns:
            float: The new rating.
        """
        pass
    
    def get_purchase_price(self) -> float:
        """
        Get the purchase price - if there is a discount price set, return that, otherwise return the base price.

        Returns:
            float: The purchase price of the product.
        """
        pass

    def get_base_price(self) -> float:
        pass

    def set_discount_percent(self, discount) -> float:
        """
        Update the discount price based on a percentage discount. Calculate this discount based on the percentage of the base price.
        Truncate (i.e. do not round) the price to two decimal places - the cent value. 

        Args:
            discount (float): The percentage discount to apply.

        Returns:
            float: The new discount price.
        """
        pass

    def set_disc_price(self, newPrice) -> float:
        
        """
        Set the discount price to a specific value.

        Args:
            newPrice (float): The new discount price.

        Returns:
            float: The new discount price.
        """
        pass

    def displayIMG(self):
        pass
    # Override the operaters that you need for the functionality here. 

    def __lt__(self, other) -> bool:
        """
        Compare two products based on their price.
        """
        pass
    def __eq__(self, other) -> bool:
        """
        Check if two products are equal. Equal products have the same name.
        """
        pass
    
    # If you need any other helper methods, add them here.
    # Remember, the tests will only call the methods that are specified, so you're free
    # to add any other methods you want to organize your code, but they'll need to be called by
    # the other methods to be included in the tests.

class myInventory():

    def __init__(self, inv_name="My Inventory", file_path=None) -> None:
        # Think about the best data structure to use to store the product objects. 
        # Consider how it will typically be accessed and what operations will be performed on it.
        # As long as you meet what the the other methods expect, you can use any data structure, but some may be easier or quicker. 
        pass

    def read_file(self, path) -> int:
        """
        Read in a CSV file and populate the inventory with the products in the file. Each product should have a stock of 10, unless otherwise specified.
        Note that the CSV file will have the following columns: name, main_category, sub_category, image, link, ratings, no_of_ratings, discount_price, actual_price.
        Duplicate names should not be allowed in the inventory, if a duplicate attempts to be added, the function should ignore it.
        Also, the ratings and no_of_ratings should be converted to floats and integers respectively.
        Additionally, the discount_price and actual_price should be converted to floats, and any non-numeric characters should be removed.
        
        Args:
            path (str): The path to the CSV file.
        
        Returns:
            int: The number of products in the inventory.
        """
        pass
    
    def __len__(self) -> int:
        pass

    def getProduct(self, product_name) -> myProduct:
        """
        Get a product from the inventory.

        Args:
            product (str): The name of the product.

        Returns:
            myProduct: The product object.
        """
        pass

    def adjust_stock(self, product, stock) -> None:
        """
        Adjusts the stock of a product to a new value.

        Args:
            product (str): The name of the product.
            stock (int): The new stock value.
        """
        pass
    def getCategory(self, category=None) -> list:
        """
        Get a subset of the inventory based on a category.

        Args:
            category (str, optional): The category to filter by. Defaults to None.

        Returns:
            list: A list of myProduct objects.
        """
        pass

    def getPrices(self, min_price, max_price) -> list:
        """
        Get a subset of the inventory based on a price range.

        Args:
            max_price (float): The maximum price.
            min_price (float): The minimum price.

        Returns:
            list: A list of myProduct objects.
        """
        pass

    def itemRating(self, product_name) -> float:
        """
        Get the rating of a product.

        Args:
            product_name (str): The name of the product.

        Returns:
            float: The rating of the product.
        """
        pass
    
    def do_purchase(self, product_quantity_tuple_list) -> float:
        """
        Perform a purchase of multiple products.

        If the quantity of a product is not available, the purchase should get as many as possible, and the total price should be calculated based on the available quantity.

        Args:
            product_quantity_tuple_list (list): A list of tuples, where each tuple contains a myProduct item name and an integer representing the quantity purchased.

        Returns:
            float: The total price of all the purchased products, calculated using the get_purchase_price function.
            items_purchased (list): A list of tuples, where each tuple contains the name of the product, the quantity purchased, and the total price for that product.
        """
        pass
    
    def addReviews(self, product_name, rating, numberRate=1) -> float:
        """
        Add a review to a product.

        Args:
            product_name (str): The name of the product.
            rating (float): The rating to add.
            numberRate (int, optional): The number of ratings the rating is based on. Defaults to 1.

        Returns:
            float: The new rating of the product.
        """
        pass
    def __eq__(self, other) -> bool:
        """
        Check if two inventories are equal. Equal inventories have the same products.

        Args:
            other (myInventory): The other inventory to compare to.
        """
        pass
    def __str__(self) -> str:
        pass
    def __len__(self) -> int:
        """
        Get the number of products in the inventory.

        Returns:
            int: The number of products in the inventory.
        """
        pass
    def __add__(self, other) -> myInventory:
        """
        Combine two inventories into one.

        Args:
            other (myInventory): The other inventory to combine with.

        Returns:
            myInventory: The combined inventory.
        """
        pass
    
    def __radd__(self, other) -> myInventory:
        pass
    
    # If you need any other helper methods, add them here.

    