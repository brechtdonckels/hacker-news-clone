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


@when("I visit the list of stories page")
def step_when_visit_list_of_stories_page(context):
    """
    Simulate visiting the list of stories page using Django's test client.
    """
    list_of_stories_link_url = context.test.live_server_url + reverse("stories:list")
    context.page.goto(list_of_stories_link_url)


@then("I should see a list of all stories")
def step_then_see_list_of_stories(context):
    """
    Assert that the number of stories displayed matches the number of stories in the database.
    """
    # Get page content
    page_content = context.page.content()

    # Determine the number of stories in the database
    stories_count = Story.objects.count()

    # Determine the number of stories found in the page
    stories_on_page_count = page_content.count('<div class="story-item">')

    # Check that the number of stories found in the page is the same as the number of stories in the database
    assert (
        stories_on_page_count == stories_count
    ), f"Expected {stories_count} stories to be displayed, but found {stories_on_page_count}."


@then("each story should display its title, URL and number of upvotes")
def step_then_see_title_and_url(context):
    """
    Verify that each story's title and URL are displayed on the page, as well as the number of upvotes.
    """
    # Get page content
    page_content = context.page.content()

    # Get all stories from the database
    stories = Story.objects.all()

    # Check if title and url are shown on the page for each story
    for story in stories:
        assert (
            story.title in page_content
        ), f"Expected title '{story.title}' to be in the response"
        assert (
            story.url in page_content
        ), f"Expected URL '{story.url}' to be in the response"
        assert (
            str(story.upvotes) in page_content
        ), f"Expected number of upvotes '{str(story.upvotes)}' to be in the response"


@then("the stories should be sorted by upvotes in descending order")
def step_impl_sort_stories_by_upvotes(context):
    """
    Verify that the stories displayed on the page match the database order by upvotes.
    """
    # Get all story items from the page
    story_items = context.page.locator(".story-item").all()

    # Extract titles and upvotes from the page
    stories_on_page = [
        {
            "title": item.locator(".story-title").inner_text(),
            "url": item.locator(".story-url").inner_text(),
            "upvotes": int(item.locator(".story-upvotes").inner_text()),
        }
        for item in story_items
    ]

    # Get stories from the database ordered by upvotes
    stories_on_database = list(
        Story.objects.all().order_by("-upvotes").values("title", "url", "upvotes")
    )

    # Compare the displayed stories with the database stories
    assert stories_on_page == stories_on_database, (
        f"Expected stories on the page to match the database order. "
        f"Displayed: {stories_on_page}, Database: {stories_on_database}"
    )


@then("I should see a message saying '{no_stories}'")
def step_then_see_no_stories_message(context, no_stories):
    """
    Assert that the "no stories" message is displayed when there are no stories.
    """
    page_content = context.page.content()
    assert no_stories in page_content, f'Expected "{no_stories}" to be in the response'
