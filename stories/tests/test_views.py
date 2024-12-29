from django.test import TestCase
from django.urls import reverse

from stories.models import Story


class StoriesListViewTest(TestCase):

    def test_list_of_stories_view_status_code(self):
        """
        Ensure the list of stories view returns a 200 status code (OK).
        """
        response = self.client.get(reverse("stories:list"))
        self.assertEqual(response.status_code, 200)

    def test_list_of_stories_view_template(self):
        """
        Ensure the list of stories view uses the correct template.
        """
        response = self.client.get(reverse("stories:list"))
        self.assertTemplateUsed(response, "stories/story_list.html")


class StoryDetailViewTest(TestCase):

    def setUp(self):
        self.story = Story.objects.create(
            title="Learn Python", url="https://learnpython.com", upvotes=10
        )

    def test_detailed_page_of_story_view_status_code(self):
        """
        Ensure the detailed page of a story view returns a 200 status code (OK).
        """
        response = self.client.get(reverse("stories:detail", args=[self.story.pk]))
        self.assertEqual(response.status_code, 200)

    def test_detailed_page_of_story_view_template(self):
        """
        Ensure the detailed page of a story view uses the correct template.
        """
        response = self.client.get(reverse("stories:detail", args=[self.story.pk]))
        self.assertTemplateUsed(response, "stories/story_detail.html")
