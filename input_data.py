import pandas as pd, os, re
from database import SessionLocal
from models import  Dataset

db = SessionLocal()

base_dir = './csvs/'
path = os.listdir('./csvs')

for csv in os.listdir('./csvs'):
    first_spot = csv.find('_')
    last_spot = csv.find('.csv')
    artist = csv[first_spot+1:last_spot]

    filepath = base_dir + csv
    df = pd.read_csv(filepath)
    singer = list(df['title'])
    image = list(df['src'])
    url = list(df['href'])
    
    for i in range(0, len(url)):
        url_first_spot = url[i].find('=')
        url[i] = "https://www.youtube.com/embed/" + url[i][url_first_spot+1:]
    
    for i in range(len(singer)):
        singer[i] = re.sub(r"[^a-zA-Z ]", "", singer[i])

    for i in range(len(singer)):
        if not 'seventeen' in singer[i].lower():
            db.add(Dataset(singer=singer[i], src=image[i], youtube_url=url[i]))
        else:
            continue

db.commit()