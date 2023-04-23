import requests
import re
from bs4 import BeautifulSoup
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import pprint
pp = pprint.PrettyPrinter(indent=2)


# Sitemap.xml
sitemap_url = "https://www.yourwebsite.com/sitemap.xml"

sitemap_response = requests.get(sitemap_url)
sitemap_content = sitemap_response.content

sitemap_soup = BeautifulSoup(sitemap_content, 'xml')


url_tags = sitemap_soup.find_all('url')


blog_urls = []

for url in sitemap_soup.find_all('url'):
    loc_tag = url.find('loc')
    # if your blogs urls  like blog/article-one, blog/article-two , articlePagePath is blog
    if loc_tag and 'articlePagePath' in loc_tag.text:
        blog_urls.append(loc_tag.text)

all_blog_pages_words_frequency = []

for blog_url in blog_urls:

    page_response = requests.get(blog_url)
    pp.pprint(page_response)

    page_content = page_response.content

    # parse html
    page_soup = BeautifulSoup(page_content, 'html.parser')

    # Page Title
    page_title = page_soup.title.text if page_soup.title else ''

    # Page Content
    page_text = page_soup.get_text()
    page_text = re.sub(r'\n+', ' ', page_text)
    page_text = re.sub(r'\[[^]]*\]', '', page_text)
    page_text = re.sub(r'\s+', ' ', page_text)
    page_text = re.sub(r'[^\w\s]', '', page_text)

    page_text = page_text.lower()

    words = word_tokenize(page_text)

    words = [word for word in words if word not in stopwords.words('english')]

    # optional
    # stemmer = PorterStemmer()
    # stemmed_words = [stemmer.stem(word) for word in words]
    # page_text = ' '.join(stemmed_words)

    all_blog_pages_words_frequency.extend(words)

pp.pprint(blog_urls)
frequency_distribution = FreqDist(all_blog_pages_words_frequency)
frequency_distribution.plot(40, cumulative=True)
