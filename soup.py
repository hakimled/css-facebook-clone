import requests
from bs4 import BeautifulSoup
import lxml
import csv


page = requests.get('https://rahalet.com/')

def main():
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup)
main()    