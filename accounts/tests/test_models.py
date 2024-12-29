from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import User


class UserModelConfigTests(TestCase):
    """
    Test case to ensure that the project is correctly configured to use the custom user model.
    """

    def test_auth_user_model_setting(self):
        """
        Test that the AUTH_USER_MODEL setting points to the correct custom user model.
        """
        self.assertEqual(
            settings.AUTH_USER_MODEL,
            "accounts.User",
            "AUTH_USER_MODEL setting is incorrect. Expected 'accounts.User', but got '{}'".format(
                settings.AUTH_USER_MODEL
            ),
        )

    def test_get_user_model(self):
        """
        Test that get_user_model() returns the correct custom user model class.
        """
        self.assertEqual(
            get_user_model(),
            User,
            "get_user_model() returned the wrong model. Expected 'User', but got '{}'".format(
                get_user_model()
            ),
        )
