from datetime import datetime

from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *


def format_date(date_str):
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%Y-%m-%d %I:%M %p")


def IconNavItem(*d):
    return [Li(A(UkIcon(o[0], uk_tooltip=o[1]))) for o in d]


def IconNav(*c, cls=""):
    return Ul(cls=f"uk-iconnav {cls}")(*c)
