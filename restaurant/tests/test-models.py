# tests/test-models.py
from django.test import TestCase
from restaurant.models import Menu  # Replace 'yourapp' with your actual app name

class MenuTest(TestCase):
    
    def test_menu_string_representation(self):
        # Create a new instance of the Menu model
        menu = Menu.objects.create(title="Pasta", price=12.5, inventory=10)  
        
        # Check if the string representation matches the expected value
        self.assertEqual(str(menu), "Pasta")  # Assuming __str__() returns the title
