Feature: Viewing the detailed page of a story
  As a user
  I want to view the detailed page of a story
  So that I can see its details

  Scenario: User views the detailed page of a story
    Given the following story exists:
      | title        | url                   | upvotes |
      | Learn Python | https://python.org    | 10      |
    When I visit the detailed page of the story "Learn Python"
    Then I should see the title "Learn Python"
    And I should see the URL "https://python.org"
    And I should see the upvotes count "10"
