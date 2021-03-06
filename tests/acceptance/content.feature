Feature: Test that pages have correct content

  @dockertest
    Scenario: Google search
    Given I am on google page
    Then Title is shown on the page
    Then I quit the driver


  @BlogPageTitle
  Scenario: Blog page has a correct title
    Given I am on the blogpage
    Then There is a title shown on the page
    And The title tag has content "This is the blog page"
    Then I quit the driver

  @HomePageTitle
  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "This is the homepage"
    Then I quit the driver

   Scenario: Blog page loads the posts
    Given I am on the blogpage
     And I wait for the posts to load
    Then I can see there is a posts section on the page

  Scenario: user can create new posts
    Given I am on the new post page
    When I enter "Test Post" in the "title" field
    And I enter "Test Content" in the "content" field
    And I press the submit button
    Then I am on the blogpage
    Given I wait for the posts to load
    Then I can see there is a post with title "Test Post" in the posts section
