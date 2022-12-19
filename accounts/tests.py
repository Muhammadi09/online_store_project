from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_custom_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'mislam',
            email = 'mislam@email.com',
            password = 'testpass'
        )
        self.assertEqual(user.username, 'mislam')

