from django.test import TestCase
from django.contrib.admin.sites import site

from ..models import User


class UserModelAdminRegistrationTests(TestCase):
    """
    Test case to ensure that the custom user model is registered in the admin interface.
    """

    def test_custom_user_model_is_registered_in_admin(self):
        """
        Test that the custom user model is registered in the Django admin
        """

        # Get the registered model from the admin site
        model_registered = site.is_registered(User)

        # Assert that the User model is registered
        self.assertTrue(model_registered, "User is not registered in the admin")
