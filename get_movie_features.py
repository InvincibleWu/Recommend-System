from bs4 import BeautifulSoup
from urllib.request import urlopen
import pickle
def get_dws(u):
#     url = urlopen(u)
#     soup = BeautifulSoup(url)
#     letters = soup.find_all("div", class_= "credit_summary_item")
    # print(letters)
    ## if url lead to seach page, choose the first one in the search result
    directors_list = []
    writers_list = []
    stars_list = []
    try:
        url = urlopen(u)
    except Exception:
        print('404')
        return directors_list, writers_list, stars_list
    soup = BeautifulSoup(url)
    letters = soup.find_all("div", class_= "credit_summary_item")
    
    if letters == []:
        ## change to new url
        table = soup.find("table", class_="findList")
        if table is None:
            return [], [], []
        url = table.find("a").get('href')
        url = 'http://www.imdb.com' + url
        newr = urlopen(url)
        newsoup = BeautifulSoup(newr)
        letters = newsoup.find_all("div", class_= "credit_summary_item")
        
    ## get information from the direct page
    
    
    for div in letters:
    # temp = div.get_text()
        title = div.find('h4').get_text()
        # print(title)
        name_list = []
        temp = div.find_all(class_="itemprop")
        for t in temp:
            k = t.get_text()
            name_list.append(k)
        if title == 'Director:' or title == 'Directors:':
            directors_list = name_list
        if title == 'Writer:' or title == 'Writers:':
            writers_list = name_list
        if title == 'Stars:' or title == 'Stars:':
            stars_list = name_list
        
        # text.append(name_list)
    
    return directors_list, writers_list, stars_list
def read_data_from_item_file(file_path, output_file_path): 
    item_data= []
    with open(file_path, encoding = 'latin-1') as f:
        for line in f:
            l = line.split('|')
            # print(l)
            l[-1] = l[-1][0]
            # print('movieID', 'year', 'url', 'genre')
            if l[1] == 'unknown' or l[4] == None:
                item_data.append([l[0], '|', 'unknown', '|', [], '|', [], '|', [], '|', [0]])
                # print(item_data)
                # break
            else:

                a, b, c = get_dws(l[4])
                genre_list = []
                for i in range(19):
                    if l[5:][i] == '1':
                        genre_list.append(i)
                # print(l[0], '|', l[1][-5:-1], '|', a, '|', b, '|', c, '|', genre_list)
                year = l[1][-5:-1][2] + '0'
                print(l[0])
                item_data.append([l[0], '|', year, '|', a, '|', b, '|', c, '|', genre_list])

    # print(item_data)               
    file = open(output_file_path, 'wb')
    pickle.dump(item_data, file)
    file.close()

              