Feature: Viewing the detailed page of a story
  As a user
  I want to view the detailed page of a story
  So that I can see its details and read comments

  Scenario: User views the detailed page of a story with comments
    Given the following story exists:
      | title        | url                   | upvotes |
      | Learn Python | https://python.org    | 10      |
    And the following comments exist for the story:
      | username | text                      |
      | alice    | This is a great resource! |
      | bob      | Very helpful, thanks!     |
    When I visit the detailed page of the story "Learn Python"
    Then I should see the title "Learn Python"
    And I should see the URL "https://python.org"
    And I should see the upvotes count "10"
    And I should see the following comments:
      | username | text                      |
      | alice    | This is a great resource! |
      | bob      | Very helpful, thanks!     |

  Scenario: User views the detailed page of a story without comments
    Given the following story exists:
      | title        | url                       | upvotes |
      | Django Tips  | https://djangoproject.com | 5       |
    And no comments exist for the story
    When I visit the detailed page of the story "Django Tips"
    Then I should see the title "Django Tips"
    And I should see the URL "https://djangoproject.com"
    And I should see the upvotes count "5"
    And I should see a message saying "No comments yet. Be the first to comment!"
