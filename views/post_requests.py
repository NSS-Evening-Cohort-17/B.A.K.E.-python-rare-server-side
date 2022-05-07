# import sqlite3
# import json
# from datetime import datetime


# def create_post(post):
#     """Adds a post to the database when they register

#     Args:
#         post (dictionary): The dictionary passed to the register post request

#     Returns:
#         json string: Contains the token of the newly created post
#     """
#     with sqlite3.connect('./db.sqlite3') as conn:
#         # conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         INSERT INTO Post (title, image_Url, content) values (?, ?, ?)
#         """, (
#             post['title'],
#             post['image_Url'],
#             post['content']
#         ))

#         id = db_cursor.lastrowid
        
#         post['id'] = id

#         return json.dumps(post)


import sqlite3
import json
from models import Post

def create_post(post):
    """Adds a post to the database when they register

    Args:
        post (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created post
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        # conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Post (user_id, category_id, title, publication_date, image_url, content, approved) values (?, ?, ?, ?, ?, ?, 1)
        """, (
            post['user_id'],
            post['category_id'],
            post['title'],
            post['publication_date'],
            post['image_url'],
            post['content'],
            post['approved']
        ))

        id = db_cursor.lastrowid
        
        post['id'] = id

        return json.dumps(post)