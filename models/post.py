class Post():
    # def __init__(self, id:int, user_id:int, category_id, title, publication_date, image_URL:str=None, content, approved):

    def __init__(self, id, user_id, category_id, title, publication_date, image_URL, content, approved):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_URL
        self.content = content
        self.approved = approved
        
class Post2():
    # def __init__(self, id:int, user_id:int, category_id, title, publication_date, image_URL:str=None, content, approved):

    def __init__(self, id, user_id, category_id, title, publication_date, image_URL, content, approved, username):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_URL
        self.content = content
        self.approved = approved
        self.username = username