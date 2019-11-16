import requests
import pandas as pd

from bs4 import BeautifulSoup


def fetch_books_categorywise(book_type):
    pass


def fetch_books_avelene_choice():
    url = 'https://www.goodreads.com/list/show/10198.Books_With_a_Goodreads_Average_Rating_of_4_5_or_higher_and_With_At_Least_1000_Ratings'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_names = [a.text for a in soup.select('a.bookTitle span')]
    book_authors = [a.text for a in soup.select('a.authorName span')]
    score = [b.text.split(': ')[-1] for b in soup.find_all('a', href="#") if 'score' in b.text]
    people_voted = [b.text.split(' people voted')[0] for b in soup.find_all('a', href="#") if 'people voted' in b.text]
    book_names, book_authors, score, people_voted = book_names[:5], book_authors[:5], score[:5], people_voted[:5]
    list_of_list = [book_names, book_authors, score, people_voted]
    column_names = ['book_names', 'book_authors', 'score', 'people_voted']
    df = convert_list_dataframe(column_names, list_of_list)
    return df


def convert_list_dataframe(column_name_list, list_of_data_list):
    df = pd.DataFrame(columns=column_name_list, index=range(1, len(list_of_data_list[0])+1))
    for i in range(len(list_of_data_list)):
        df.iloc[:, i] = list_of_data_list[i]
    return df
