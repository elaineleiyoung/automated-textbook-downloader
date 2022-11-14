import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from termcolor import colored

book_dict = dict()
divider = '-'
base_path = os.path.dirname(os.path.abspath(__file__))


def generate_search_url(search_term):
    sequence = '+'
    if len(search_term.split()) <= 1:
        return f'https://libgen.is/search.php?&res=100&req={search_term}&phrase=1&view=simple&column=def&sort=year&sortmode=DESC'
    else:
        search_term = search_term.split()
        search_term = sequence.join(search_term)
        return f'https://libgen.is/search.php?&res=100&req={search_term}&phrase=1&view=simple&column=def&sort=year&sortmode=DESC'


def soupify(content):
    return BeautifulSoup(content, 'html.parser')


def get_results():
    keyword = input(r"Enter you search keyword e.g 'python django': ")
    # keyword = "Cracking the Coding Interview"
    response = requests.get(generate_search_url(keyword), verify=False)
    html_soup = soupify(response.content)
    try:
        results = html_soup.find("table", {"class": "c"}).find_all("tr")[1:]
        return results
    except:
        print(html_soup.text)


def book_downloader():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    accept_charset = 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
    accept_lang = 'en-US,en;q=0.9'
    connection = 'keep-alive'

    headers = {
        'User-Agent': user_agent,
        'Accept': accept,
        'Accept-Charset': accept_charset,
        'Accept-Language': accept_lang,
        'Connection': connection,
    }
    done = False
    while not done:
        try:
            # answer = int(input(
            #     r"Enter number of the book you'd like to download. Choose from 1-100. OR type '0' or a letter to exit the script: "))
            answer = 1
            if answer == 0:
                print('Goodbye...')
                break
            elif answer <= 100:
                download_base_url = 'http://library.lol'
                print('Downloading book....')
                download_url = download_base_url + '/main/' + book_dict[answer]['book_page'].split("md5=")[1]
                print(download_url)
                
                response = requests.get(download_url, headers=headers)
                html_soup = soupify(response.text)
                print(html_soup)
                file_url = html_soup.find(id='info').find('a').get('href')
                file_name = html_soup.select('tr h1')[0].text
                file = requests.get(file_url, stream=True)
                total_size = int(file.headers.get('content-length', 0))
                block_size = 1024
                t = tqdm(total=total_size, unit='iB', unit_scale=True)
                file_name = os.path.join(base_path, f'{file_name}.{book_dict[answer]["file_type"]}')
                with open(file_name, 'wb') as f:
                    for data in file.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                    # f.write(file.content)
                t.close()
                print(f'Downloaded book: {file_name}')
            else:
                print(int(input(
                    r"You've Entered an invalid option. Please try entering a number from 1-100 OR type '0' or a letter to exit the script: ")))
        except ValueError as e:
            print('Exception: {}'.format(e))
            break
        break


def book_info_getter():
    books = get_results()
    for num, book in enumerate(books, start=1):
        tds = book.find_all("td")
        book_id = tds[0].text
        author = tds[1].text
        title = book.find(id=book_id)
        book_page = f'https://libgen.is/{(title.get("href"))}'
        published_date = tds[4].text
        number_of_pages = tds[5].text
        language = tds[6].text
        file_size = tds[7].text
        file_type = tds[8].text
        book_dict.update({
            num: {
                'title': title.text,
                'author': author,
                'book_page': book_page,
                'published_date': published_date,
                'number_of_pages': number_of_pages,
                'language': language,
                'file_size': file_size,
                'file_type': file_type
            }
        })
    for index, book in book_dict.items():
        print(
            colored(index, 'cyan'),
            'title: ', colored(book['title'], 'yellow'), '\n',
            '\tPublished date:\t', colored(book['published_date'], 'cyan'), '\n',
            '\tNumber of pages:', colored(book['number_of_pages'], 'cyan'), '\n',
            '\tLanguage:\t\t', colored((book['language']), 'cyan'), '\n',
            '\tFile size: \t\t', colored(book['file_size'], 'cyan'), '\n',
            '\tFile type: \t\t', colored(book['file_type'], 'cyan')
        )
    print(f'{divider * 120}')
    book_downloader()


book_info_getter()