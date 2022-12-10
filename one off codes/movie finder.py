import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_movies_page():
    """
    Function to download a web page using `requests` and check the status code to validate
    if the call was successful. 
    """
    movies_url = 'https://www.themoviedb.org/movie'
    # Access the webpage using `requests`
    response = requests.get(movies_url)
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(movies_url))
    # Parse the `response' text using BeautifulSoup
    movies_doc = BeautifulSoup(response.text, 'html.parser')
    return movies_doc

def get_movies_names(doc):
    """
    Function to extract the movie names from HTML source code using BeautifulSoup.
    """
    movies_names_tags = doc.find_all('h2')[4:]  #Exclude the first 4 lines
    movies_names = []
    # Loop through the page get all the movie names from the page
    for h2 in movies_names_tags:
        movies_names.append(h2.a.text.strip())
    return movies_names

def get_movies_rating(doc):
    """
    Function to extract the movie user rating from HTML source code using the BeautifulSoup. 
    """
    desc_selector = 'user_score_chart'
    movies_rating_tags = doc.find_all('div', {'class': desc_selector})
    movies_rating = []
    # Loop through the webpage to get the ratings of all the movies in the page
    for tag in movies_rating_tags:
        movies_rating.append(tag.attrs['data-percent'])
    return movies_rating

def get_movies_urls(doc):
    """
    Function to extract the movie links from HTML source code using BeautifulSoup. 
    """
    movies_urls = []
    base_url = 'https://www.themoviedb.org'
    movies_names_tags = doc.find_all('h2')[4:]  #Exclude the first 4 lines
    # Loop through the webpage to get the URL of each movie
    for tag in movies_names_tags:
        movies_urls.append(base_url + tag.a['href'])
    return movies_urls

def scrape_movies():
    """
    Function to download web page using `requests` and
    to extract the HTML source code using BeautifulSoup.
    """
    # Let's get the popular movies listing from the TMdb website
    page_count = 1 # Initializing the movie page count to 1
    # Define lists for all the movie attributes
    all_names = []
    all_ratings = []
    all_urls = []
    
    while page_count < 15: # Looping for 15 pages of the TMdb web page
        movies_url = "https://www.themoviedb.org/movie?page=%d" %(page_count)
        # Access the webpage using `requests`
        response = requests.get(movies_url)
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception('Failed to load page {}'.format(movies_url))
        # Parse the `response' text using BeautifulSoup
        doc = BeautifulSoup(response.text, 'html.parser')
        
        urls = get_movies_urls(doc)
        
        # Append each movie attribute to respective lists
        all_names += get_movies_names(doc)
        all_ratings += get_movies_rating(doc)
        all_urls += urls 
        page_count += 1

        # Defining a dictionary to store the movie informations
    movies_dict = {
        'name': all_names,
        'rating': all_ratings,
        'url': all_urls
    }
    return pd.DataFrame(movies_dict)
print (pd.DataFrame(movies_dict))