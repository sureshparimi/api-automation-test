Feature: GET close approach data for asteroids and NEOs
@smoketest
Scenario Outline: GET close approach data
    Given I send the parameters "<date_min>","<date_max>","<dist_min>","<dist_max>" and "<fullname>" and "<sort>" to retrive the close approach data
    Then I verify the response for Signature and count and fields and data
    And I verify the data contains "<dist_min>","<dist_max>" and "<fullname>"
    Examples:
         |   date_min     |   date_max    |   dist_min    |   dist_max   | fullname         | sort |
         |    2021-01-01  |   2023-01-01  |     0         |   0.2        | (2021 AS1)       | date | 
         |    2021-01-01  |   2023-01-01  |      0         |   10LD      | (1995 CR)        | -date|     

 
