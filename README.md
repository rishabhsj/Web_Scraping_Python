# Airbnb Web Scraping
Code to scrape Airbnb links to fetch property details using python and json. <br>

### Problem Statement
Please write some code that scrapes property name, property type (e.g Apartment), number of bedrooms, bathrooms and list of the amenities for the following 3 properties:

- URLs:<br>
-- `https://www.airbnb.co.uk/rooms/33571268` <br>
-- `https://www.airbnb.co.uk/rooms/33090114` <br>
-- `https://www.airbnb.co.uk/rooms/50633275` <br>
  
### Approach solving the problem:
- Research and learn about web scraping <br>
- Fetch all the data/contents from each link using html response and requests <br>
- Finding the site contents and <div> tags in the scarped data <br>
- Splitting data in lines <br>
- From the scraped data, its seen that the first index of data is always the property name and thus storing the name of the property in variable. <br>
- Then enumerating the specific strings in the site data to find the matching requirements such as number of bedrooms, bathrooms and list of amenities <br>
- Saving all the required data in a dictionary <br>
- Output data is displayed as console output and also saved as json file with the file name as name of the property <br>
- Showing error message for unsuccessful scraping of url or specific data <br>
- Making methods static and using try-exception block for better handling of exceptions <br>

### How to Run:

`Create virtual environment` <br>

Requirements:
`pip install -r requirements.txt`

Run main.py 

Outputs in the Result folder and on console.

References<br><br>
https://requests.readthedocs.io/projects/requests-html/en/latest/ <br>
https://www.w3schools.com/python/default.asp <br>
https://www.codecademy.com/courses/learn-web-scraping
