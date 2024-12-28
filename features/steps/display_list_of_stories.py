from behave import given, when, then

from django.urls import reverse
from django.test import Client

from stories.models import Story


@given("the following stories exist")
def step_given_stories_exist(context):
    """
    Create the stories defined in the feature file.
    """
    for row in context.table:
        Story.objects.create(
            title=row["title"], url=row["url"], upvotes=int(row["upvotes"])
        )


@given("no stories exist")
def step_given_no_stories_exist(context):
    """
    Ensure there are no stories in the database.
    """
    Story.objects.all().delete()


@when("I visit the homepage")
def step_when_visit_homepage(context):
    """
    Simulate visiting the homepage using Django's test client.
    """
    client = Client()
    context.response = client.get(reverse("homepage"))


@then("I should see a list of all stories")
def step_then_see_list_of_stories(context):
    """
    Assert that the number of stories displayed matches the number of stories in the database.
    """
    # Get response content
    response_content = context.response.content.decode()

    # Determine the number of stories in the database
    stories_count = Story.objects.count()

    # Determine the number of stories found in the page
    displayed_stories_count = response_content.count('<div class="story-item">')

    # Check that the number of stories found in the page is the same as the number of stories in the database
    assert (
        displayed_stories_count == stories_count
    ), f"Expected {stories_count} stories to be displayed, but found {displayed_stories_count}."


@then("each story should display its title and URL")
def step_then_see_title_and_url(context):
    """
    Verify that each story's title and URL are displayed on the page.
    """
    # Get response content
    response_content = context.response.content.decode()

    # Get all stories from the database
    stories = Story.objects.all()

    # Check if title and url are shown on the page for each story
    for story in stories:
        assert (
            story.title in response_content
        ), f"Expected title '{story.title}' to be in the response"
        assert (
            story.url in response_content
        ), f"Expected URL '{story.url}' to be in the response"


@then("the stories should be sorted by upvotes in descending order")
def step_impl_sort_stories_by_upvotes(context):
    """
    Verify that the stories are sorted by upvotes in descending order on the homepage.
    """
    # Get the response content
    response_content = context.response.content.decode()

    # Get all the stories from the database, but orderd by upvotes
    stories = Story.objects.all().order_by("-upvotes")

    # Check that stories are displayed in the same order as in the database
    for i in range(1, len(stories)):
        previous_title = stories[i - 1].title
        current_title = stories[i].title

        previous_position = response_content.find(previous_title)
        current_position = response_content.find(current_title)

        assert (
            previous_position < current_position
        ), f"Expected '{previous_title}' to appear before '{current_title}' in the response."


@then('I should see a message saying "No stories have been submitted yet."')
def step_then_see_no_stories_message(context):
    """
    Assert that the "no stories" message is displayed when there are no stories.
    """
    response_content = context.response.content.decode()
    assert (
        "No stories have been submitted yet." in response_content
    ), 'Expected "No stories have been submitted yet." to be in the response'
