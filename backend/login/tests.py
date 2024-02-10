from django.test import TestCase
from django.contrib.auth.models import User

class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin',
            password='admin123',
        )

    def test_login(self):
        assert self.client.login(username='admin', password='admin123')
