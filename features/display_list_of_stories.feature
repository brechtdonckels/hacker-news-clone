Feature: Displaying a list of stories
  As a user
  I want to view a list of stories
  So that I can explore the content shared by others

  Scenario: User views a list of stories
    Given the following stories exist:
      | title                   | url                       | upvotes |
      | Learn Python            | https://python.org        | 5       |
      | Django Tips             | https://djangoproject.com | 10      |
    When I visit the homepage
    Then I should see a list of all stories
    And each story should display its title, URL and number of upvotes
    And the stories should be sorted by upvotes in descending order

  Scenario: User sees a message when no stories exist
    Given no stories exist
    When I visit the homepage
    Then I should see a message saying "No stories have been submitted yet."