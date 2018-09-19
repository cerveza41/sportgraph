import json
import os
from trello import TrelloClient
from typing import List, Tuple
from datetime import date
import re


def extract_dates(dates: List[str]) -> List[date]:
    result = []
    for d in dates:
        year = __to_int(d[0:4])
        month = __to_int(d[5:7])
        day = __to_int(d[8:10])
        result.append(date(year, month, day))
    return sorted(result)


def extract_distance(comments: List[str]) -> List[float]:
    pattern = re.compile('^(\d?\d),?(\d?\d?).*$')
    result = []
    for c in comments:
        matches = pattern.match(c)
        if len(matches.regs) == 3:
            distance = '{}.{}'.format(matches.group(1), matches.group(2))
            result.append(__to_float(distance))
    return result


def request_all_comments() ->Tuple[List[str], List[str]]:
    key, secret, token = __get_api_keys()
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
                                dates.append(__get_date_string(comment))
                                comments.append(__get_comment_text(comment))
    return (dates, comments)


def __to_int(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        return 0


def __to_float(s: str) -> float:
    try:
        return float(s)
    except ValueError:
        return 0


def __get_comment_text(comment):
    return comment['data']['text']


def __get_date_string(comment):
    return comment['date']


def __get_api_keys():
    with open(os.path.join(os.path.dirname(__file__), 'trello_api.json')) as f:
        j = json.load(f)
        return (j['key'], j['secret'], j['token'])
