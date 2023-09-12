"""
url 데이터를 db에 커밋하는 파일입니다.
"""

import os
import re
from datetime import datetime
import pandas as pd
from database import SessionLocal
from models import Dataset, Board


def make_dance_dataset():
    """
    춤 youtube url을 db에 커밋하는 함수입니다.
    """
    database = SessionLocal()
    base_dir = "./csvs/"
    path = os.listdir("./csvs")

    for csv in path:
        filepath = base_dir + csv
        dataframe = pd.read_csv(filepath)
        singer = list(dataframe["title"])
        image = list(dataframe["src"])
        url = list(dataframe["href"])

        for i, _ in enumerate(url):
            url_first_spot = url[i].find("=")
            url[i] = "https://www.youtube.com/embed/" + url[i][url_first_spot + 1 :]

        for i, _ in enumerate(singer):
            singer[i] = re.sub(r"[^a-zA-Z ]", "", singer[i])

        for i, _ in enumerate(singer):
            if not "seventeen" in singer[i].lower():
                database.add(
                    Dataset(singer=singer[i], src=image[i], youtube_url=url[i])
                )
            else:
                continue

    database.commit()


def make_test_articles():
    """
    테스트 게시글을 DB에 커밋합니다.
    """
    database = SessionLocal()
    for i in range(0, 100):
        test_article = Board(
            title=f"{i}번째 테스트 게시글입니다.",
            section="홍보 게시판",
            content=f"{i}번째 테스트 게시글의 본문입니다.",
            writer=f"{i}raswe",
            write_date=datetime.now(),
        )
        database.add(test_article)

    database.commit()


make_dance_dataset()
make_test_articles()
