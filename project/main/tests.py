from django.test import TestCase, Client
from .models import Dishes, Categories
from django.contrib.auth.models import User


class TestAuthentification(TestCase):

    def test_registration(self):
        form_data = {'username': "Nina", 'password1': "qwer05350113", 'password2': "qwer05350113"}
        response = self.client.post("/Register", data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        form_data = {'username': "Ngd", 'password': "qwer"}
        response = self.client.post("/login", data=form_data)
        self.assertEqual(response.status_code, 200)


class DishesCreateTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='Nina')
        user.set_password('qwer05350113')
        user.save()
        self.client.login(username="Nina", password="qwer05350113")

    def test_dishes_post_valid_form(self):
        form_data = {'nameofdishes': "fish", "description": "fish from russia",
                     'howTOcook': "i don't know"}
        response = self.client.post("/Add_a_dish", data=form_data)
        self.assertEqual(response.status_code, 200)


    def test_dishes_post_invalid_form(self):
        form_data = {'nameofdishes': "fish"}
        self.client.post("/Add_a_dish", data=form_data)
        self.assertFalse(Dishes.objects.filter(nameofdishes='fish').exists())




