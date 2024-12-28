from django.core.exceptions import ValidationError
from django.test import TestCase

from stories.models import Story


class StoryModelTest(TestCase):
    def test_can_create_story_with_valid_data(self):
        """
        Ensure we can create a Story instance with valid data.
        """
        story = Story.objects.create(
            title="Example Title",
            url="https://example.com",
            upvotes=5,
        )
        self.assertEqual(story.title, "Example Title")
        self.assertEqual(story.url, "https://example.com")
        self.assertEqual(story.upvotes, 5)

    def test_title_is_required(self):
        """
        Ensure the title field is required.
        """
        story = Story(url="https://example.com")
        with self.assertRaises(ValidationError):
            story.full_clean()

    def test_url_is_required(self):
        """
        Ensure the URL field is required.
        """
        story = Story(title="Example Title")
        with self.assertRaises(ValidationError):
            story.full_clean()

    def test_url_must_be_valid(self):
        """
        Ensure the URL field contains a valid URL.
        """
        story = Story(title="Example Title", url="invalid-url")
        with self.assertRaises(ValidationError):
            story.full_clean()

    def test_upvotes_field_defaults_to_zero(self):
        """
        Test that the upvotes field defaults to 0 when a new Story is created.
        """
        story = Story.objects.create(title="Example Title", url="https://example.com")
        self.assertEqual(story.upvotes, 0)

    def test_string_representation(self):
        """
        Ensure the string representation of the Story is its title.
        """
        story = Story.objects.create(
            title="Example Title",
            url="https://example.com",
        )
        self.assertEqual(str(story), "Example Title")
