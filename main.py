#basic impl (move to node)
import wikipedia as wiki
from bs4 import BeautifulSoup as bs

'''
Note:   Whenever you ask a user to input something, errors are possible.
        Avoid errors by wrapping with try catch or error handling statements.
'''

def main():
    query = input('Tell us your search query: ')
    N = input('How many related articles do you want to read? ')

    # find wikipedia root for the query
    search = wiki.search(query, 5)
    print(search)
    print('We found the following pages related to your query: ')
    for i in range(len(search)):
        print(str(i+1) + '. ' + search[i])

    inp2 = 'Which page are you looking to explore (from {} to {}): \nIf the article you were looking for was not found, enter 0'.format(1, len(search))
    i = input(inp2)

    if i == 0:
        print('We found the following related queries: ')
        search = wiki.search(query, 20)

    # find the page details
    search_item = search[int(i)-1]
    page_obj = wiki.WikipediaPage(search_item)
    page_obj_html = page_obj.html()
    print(page_obj_html)


    # phtml = wiki.WikipediaPage(search_item)
    # print(pobj)
    # print(phtml.html())

    # s = wikipedia.suggest(query)
    # m = wikipedia.summary(query)
    # and then find top N similar articles
    return query#, N

main()
