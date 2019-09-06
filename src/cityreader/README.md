#  Sprint Challenge: Intro to Python (cityreader)

## Minimum Viable Product
To meet MVP in the city reader portion you will need to create a class to hold a city location. Call the class `City`. It should have fields for `name`, `lat` and `lon` (representing latitude and longitude).
_We have a collection of US cities with population over 750,000 stored in the file "cities.csv". (CSV stands for "comma-separated values".)_
In the body of the `cityreader` function, use Python's built-in "csv" module to read this file so that each record is imported into a City instance. Then return the list with all the City instances from the function. 
_Google "python 3 csv" for references and use your Google-fu for other examples._

`Note that the first line of the CSV is header that describes the fields, this should not be loaded into a City object.`