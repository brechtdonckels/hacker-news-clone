from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import User
from stories.models import Comment, Story


class StoryModelTest(TestCase):
    def test_can_create_story(self):
        """
        Ensure we can create a Story instance.
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


class CommentModelTest(TestCase):
    def setUp(self):
        """
        Setup any initial data for the tests.
        Create a story that comments will be attached to.
        """
        self.story = Story.objects.create(
            title="Learn Python",
            url="https://python.org",
            upvotes=10,
        )
        self.user = User.objects.create_user(
            username="alice", email="alice@example.com", password="password123"
        )

    def test_can_create_comment(self):
        comment = Comment.objects.create(
            author=self.user, text="This is a great resource!", story=self.story
        )
        self.assertEqual(comment.author.username, "alice")
        self.assertEqual(comment.text, "This is a great resource!")
        self.assertEqual(comment.story, self.story)
