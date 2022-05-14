import sqlite3
import json
from models import Post, Post2

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
        INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved) values (?, ?, ?, ?, ?, ?, 1)
        """, (
            post['user_id'],
            post['category_id'],
            post['title'],
            post['publication_date'],
            post['image_url'],
            post['content']
        ))

        id = db_cursor.lastrowid
        
        post['id'] = id

        return json.dumps(post)


def get_all_posts():
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.username
        FROM Posts p 
        JOIN Users u 
        ON p.user_id = u.id            
        """)
        
    posts = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
        post = Post2(row['id'],
                    row['user_id'],
                    row['category_id'],
                    row['title'],
                    row['publication_date'],
                    row['image_url'],
                    row['content'],
                    row['approved'],
                    row['username'])
        posts.append(post.__dict__)

    return json.dumps(posts)
    
def get_single_post(id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.id = ?       
        """, (id, ))
        
        data = db_cursor.fetchone()
        post = Post(data['id'],
                    data['user_id'],
                    data['category_id'],
                    data['title'],
                    data['publication_date'],
                    data['image_url'],
                    data['content'],
                    data['approved'])

        return json.dumps(post.__dict__)

def update_post(id, new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
               user_id = ?,
               category_id = ?,
               title = ?,
               publication_date = ?,
               image_url = ?,
               content = ?,
               approved = ?
        WHERE id = ?
        """, (new_post['category_id'],
              new_post['title'],
              new_post['publication_date'],
              new_post['image_url'],
              new_post['content'],
              new_post['approved'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True 

        
    
def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))

def get_all_posts_by_user(user_id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.username
        FROM Posts p
        JOIN Users u 
        ON p.user_id = u.id 
        WHERE p.user_id = ?
        """, ( user_id, ))
        
    posts = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
        post = Post2(row['id'],
                    row['user_id'],
                    row['category_id'],
                    row['title'],
                    row['publication_date'],
                    row['image_url'],
                    row['content'],
                    row['approved'],
                    row['username'])
        posts.append(post.__dict__)

    return json.dumps(posts)
