from behave import given, when, then

from django.urls import reverse

from accounts.models import User
from stories.models import Comment, Story


@given("the following story exists")
def step_given_story_exists(context):
    """
    Create the story defined in the feature file.
    """
    for row in context.table:
        Story.objects.create(
            title=row["title"], url=row["url"], upvotes=int(row["upvotes"])
        )


@given("the following comments exist for the story")
def step_given_comments_exist(context):
    """
    Create comments for the given story.
    """
    story = Story.objects.all().first()

    for row in context.table:
        username = row["username"]

        user, created = User.objects.get_or_create(
            username=username, email=f"{username}@example.com"
        )

        Comment.objects.create(
            story=story,
            author=user,
            text=row["text"],
        )


@given("no comments exist for the story")
def step_no_comments_exist(context):
    """
    Delete any comments associated with the story in the database.
    """
    story = Story.objects.all().first()
    story.comments.all().delete()


@when('I visit the detailed page of the story "{story_title}"')
def step_when_visit_detailed_page(context, story_title):
    """
    Visit the detailed page of a specific story.
    """
    story = Story.objects.get(title=story_title)
    detailed_url = reverse("stories:detail", args=[story.id])
    context.page.goto(context.base_url + detailed_url)


@then('I should see the title "{expected_title}"')
def step_then_see_title(context, expected_title):
    """
    Verify the title is displayed on the detailed story page.
    """
    page_content = context.page.content()

    assert (
        expected_title in page_content
    ), f"Expected to see the title '{expected_title}', but it was not found."


@then('I should see the URL "{expected_url}"')
def step_then_see_url(context, expected_url):
    """
    Verify the URL is displayed on the detailed story page.
    """
    page_content = context.page.content()

    assert (
        expected_url in page_content
    ), f"Expected to see the URL '{expected_url}', but it was not found."


@then('I should see the upvotes count "{expected_upvotes}"')
def step_then_see_upvotes(context, expected_upvotes):
    """
    Verify the upvotes count is displayed on the detailed story page.
    """
    page_content = context.page.content()

    assert (
        expected_upvotes in page_content
    ), f"Expected to see the upvotes count '{expected_upvotes}', but it was not found."


@then("I should see the following comments")
def step_then_see_comments(context):
    """
    Verify that the comments defined in the feature file are displayed on the detailed story page.
    """
    page_content = context.page.content()

    for row in context.table:
        username = row["username"]
        text = row["text"]

        assert (
            username in page_content
        ), f"Expected username '{username}' to be in the response"
        assert (
            text in page_content
        ), f"Expected comment text '{text}' to be in the response"


@then('I should see a message saying "{no_comments}"')
def step_then_see_no_comments_message(context, no_comments):
    """
    Assert that the "no comments" message is displayed when there are no comments.
    """
    page_content = context.page.content()
    assert (
        no_comments in page_content
    ), f"Expected '{no_comments}' to be in the response"
