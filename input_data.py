import pandas as pd, os, re
from database import SessionLocal
from models import Dataset, Board
from datetime import datetime

def make_dance_dataset():
    db = SessionLocal()
    base_dir = './csvs/'
    path = os.listdir('./csvs')
    
    for csv in path:
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
    
def make_test_articles():
    db = SessionLocal()
    for i in range(0, 100):
        test_article = Board(title=f"{i}번째 테스트 게시글입니다.", 
                             section="홍보 게시판",
                             content=f"{i}번째 테스트 게시글의 본문입니다.",
                             writer=f'{i}raswe',
                             write_date=datetime.now())
        db.add(test_article)
        
    db.commit()
    
make_dance_dataset()
make_test_articles()