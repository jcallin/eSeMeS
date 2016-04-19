### eSeMeS
##Bronco Hack 2016 project which implements web search through text message


This project is built to be hosted on Heroku and is available (when I have the server up) at https://git.heroku.com/stormy-temple-83951.git

#Try it out:
Currently, we implement 4 query types: directions, wikipedia, yelp, and services (for stuff like hospitals, lawyers, etc)
Just text a query to your twilio number after booting up your server running the application and forwarding HTTP POSTs from your twilio number to the server

Directions: '[Mode] from [location] to [destination]'
--Example "Driving from san jose to santa barbara"

Yelp: 'Yelp [service] in [location]'
--Example "Yelp sushi in San Jose"

Services: 'Find [service] near [zip code]'
--Example "Find hospital near 95050"

