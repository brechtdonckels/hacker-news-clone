from django.test import TestCase
from django.urls import reverse


class HomepageViewTest(TestCase):

    def test_homepage_view_status_code(self):
        """
        Ensure the homepage view returns a 200 status code (OK).
        """
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_view_template(self):
        """
        Ensure the homepage view uses the correct template.
        """
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "core/homepage.html")
