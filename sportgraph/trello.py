import json
import os
from trello import TrelloClient
from typing import List, Tuple
from datetime import date


def to_int(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        return 0


def extract_dates(dates: List[str]) -> List[date]:
    result = []
    for d in dates:
        year = to_int(d[0:4])
        month = to_int(d[5:7])
        day = to_int(d[8:10])
        result.append(date(year, month, day))
    return sorted(result)


def get_comment_text(comment):
    return comment['data']['text']


def get_date_string(comment):
    return comment['date']


def get_api_keys():
    with open(os.path.join(os.path.dirname(__file__), 'trello_api.json')) as f:
        j = json.load(f)
        return (j['key'], j['secret'], j['token'])


def request_all_comments() ->Tuple[List[str], List[str]]:
    key, secret, token = get_api_keys()
    client = TrelloClient(api_key=key, api_secret=secret, token=token)
    dates = []
    comments = []
    for board in client.list_boards():
        if board.name == 'Notizen':
            lists = board.get_lists('all')
            for l in lists:
                if l.name == 'Sport':
                    cards = l.list_cards()
                    for card in cards:
                        if card.name == 'Laufen':
                            for comment in card.get_comments():
                                dates.append(get_date_string(comment))
                                comments.append(get_comment_text(comment))
    return (dates, comments)
