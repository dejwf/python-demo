Feature: showing off behave

  Scenario: run a simple test
     Given open browser
      When navigate to google
      Then search vlkancice
      Then vlkancice are in the search result page (SERP)