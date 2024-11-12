import pathlib
from bottle import request, response
import re
import sqlite3
from icecream import ic
import requests

##############################
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

##############################
def db(query, type="cursor"):
    try:
        url = f"http://arangodb:8529/_api/{type}"  # Use f-string to format the URL correctly
        headers = {
            "Content-Type": "application/json"
        }
        res = requests.post(url, json=query, headers=headers)
        ic(res)
        ic(res.text)
        return res.json()
    
    except Exception as ex:
        print(ex)
        return {
            "error": str(ex),
            "code": "exception"
        }
