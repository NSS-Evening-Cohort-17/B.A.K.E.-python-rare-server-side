import sqlite3
import json
from datetime import datetime


def create_post(post):
    """Adds a post to the database when they register

    Args:
        post (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created post
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Post (id, user_id, title, imageUrl, content, publicationDate) values (?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            post['id'],
            post['user_id'],
            post['title'],
            post['imageUrl'],
            post['content'],
            datetime.now()
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })
