# Import required libraries
import requests
from bs4 import BeautifulSoup

# Base URL of the website
url = "https://books.toscrape.com/"

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers on the page
    books = soup.find_all("article", class_="product_pod")

    # Loop through each book and extract the desired information
    for book in books:
        # Extract the title from the <a> tag inside <h3>
        title = book.h3.a["title"]

        # Extract the price (text inside <p> tag with class 'price_color')
        price = book.find("p", class_="price_color").text

        # Extract the rating — it's inside a <p> tag with class like 'star-rating Three'
        rating_class = book.find("p", class_="star-rating")["class"]
        # The second class name (e.g., 'Three') represents the rating in words
        rating = rating_class[1]

        # Print the extracted information
        print(f"Title: {title}")
        print(f"Rating: {rating}")
        print(f"Price: {price}")
        print("-" * 50)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
