from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://coreyms.com").text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('webscrapper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Description', 'Youtube Link'])

for article in soup.find_all('article'):

    title = article.header.h2.a.text
    print(title)

    description = article.find('div', class_ = 'entry-content').p.text
    print(description)

    try:

        video_src = article.find('iframe', class_ = 'youtube-player')['src']
        vid_id_list = video_src.split('/')
        vid_id = vid_id_list[4].split('?')[0]
        youtube_link = f'https://www.youtube.com/watch?v={vid_id}'
        print(youtube_link)
        print()

    except:

        youtube_link = None
    
    csv_writer.writerow([title,description,youtube_link])
    

csv_file.close()