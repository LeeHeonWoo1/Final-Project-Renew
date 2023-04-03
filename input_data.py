import pandas as pd, os, re
from database import SessionLocal
from models import TestDataset

db = SessionLocal()

base_dir = './csvs/'
path = os.listdir('./csvs')

for csv in os.listdir('./csvs'):
    filepath = base_dir + csv
    df = pd.read_csv(filepath)
    singer = list(df['title'])
    image = list(df['src'])
    url = list(df['href'])

    for i in range(len(singer)):
        singer[i] = re.sub(r"[^a-zA-Z ]", "", singer[i])

    for i in range(len(singer)):
        db.add(TestDataset(singer=singer[i], src=image[i], youtube_url=url[i]))

db.commit()