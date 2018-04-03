
Feature: Star Wars Api

  Scenario Outline: User wants to get movie data
    Given a Star Wars Api
    When user searchs for film number <film_number>
    Then <year> year release is given
    And "<movie_title>" title is given
    And <episode_number>th episode is given

    Examples: Episodes I to VII
      | film_number |  episode_number | movie_title          | year  |
      | 1           |  4              | A New Hope           | 1977  |
      | 4           |  1              | The Phantom Menace   | 1999  |
      | 7           |  7              | The Force Awakens    | 2015  |
