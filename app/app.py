import streamlit as st
import requests
from bs4 import BeautifulSoup


def get_word_of_the_day():
    url = 'https://www.berndeutsch.ch/random'
    res = requests.get(url)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')
    soup = soup.find('div', {'id': 'content'})
    soup = soup.find('div', {'class': 'container'})
    soup = soup.find('div', {'class': 'col-xs-12'})

    word = soup.h1.text
    meaning = soup.p.text.replace('Bedeutung: ', '')

    return word, meaning


st.markdown('### Word of the Day')

a = 0
if st.button('Next'):
    word, meaning = get_word_of_the_day()
    st.markdown(f'## {word}')
    st.markdown(f'{meaning}')

