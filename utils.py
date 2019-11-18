import requests
import pandas as pd

from bs4 import BeautifulSoup


def fetch_books_avelene_choice():
    rating = []
    url = 'https://www.goodreads.com/list/show/10198.Books_With_a_Goodreads_Average_Rating_of_4_5_or_higher_and_With_At_Least_1000_Ratings'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_names = [book_title.text for book_title in soup.select('a.bookTitle span')]
    book_authors = [author.text for author in soup.select('a.authorName span')]
    rating_all = [avg_rating.text.replace('\n', '') for avg_rating in soup.select('div span') if 'avg rating' in avg_rating.text]
    for avg_rating in rating_all:
        if avg_rating not in rating:
            rating.append(avg_rating)
    rating = [avg_rating.split(' avg rating')[0] for avg_rating in rating]
    book_names, book_authors, rating = book_names[:5], book_authors[:5], rating[:5]
    list_of_book_information = [book_names, book_authors, rating]
    column_names = ['Book Title', 'Authors', 'Avg Rating']
    df = convert_list_dataframe(column_names, list_of_book_information)
    return df


def fetch_books_categorywise(book_genre_type):
    url = 'https://www.goodreads.com/genres/{}'.format(book_genre_type.lower())
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_names = [book_title['alt'] for book_title in soup.find_all('img', {"class": "bookImage"})]
    book_names = book_names[:5]
    list_of_book_information = [book_names]
    column_names = ['Book Title']
    df = convert_list_dataframe(column_names, list_of_book_information)
    return df


def fetch_books_user_search(book_name):
    book_name = book_name.replace(' ', '+')
    url = 'https://www.goodreads.com/search?q={}&qid='.format(book_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_names = [book_title.text for book_title in soup.select('a.bookTitle span')]
    book_authors = [book_author.text for book_author in soup.select('a.authorName span')]
    book_authors = book_authors[:len(book_names)]
    book_ratings = [rating.text.split(' avg rating')[0].replace(' ', '') for rating in
                    soup.select('div span span', {'class': 'stars staticStars notranslate'}) if 'avg rating' in rating.text]
    list_of_book_information = [book_names, book_authors, book_ratings]
    column_names = ['Book Title', 'Book Author', 'Avg Rating']
    df = convert_list_dataframe(column_names, list_of_book_information)
    return df


def convert_list_dataframe(column_name_list, list_of_data_list):
    df = pd.DataFrame(columns=column_name_list, index=range(1, len(list_of_data_list[0])+1))
    for i in range(len(list_of_data_list)):
        df.iloc[:, i] = list_of_data_list[i]
    return df
