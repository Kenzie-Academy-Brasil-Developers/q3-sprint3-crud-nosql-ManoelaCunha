import datetime
from app import db

class Post:

    def __init__(self, title: str, author: str, tags: list, content: str, id: int = 1) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
        
    @staticmethod
    def read_all_posts() -> list:
        data_list = db.posts.find()
        return data_list

    @staticmethod
    def read_post_by_id(id) -> dict:
        data = db.posts.find_one({"id": id})
        return data
    
    def create_post(self) -> dict:
        self.created_at = datetime.datetime.now()
        self.updated_at = None
        
        data = self.__dict__
      
        db.posts.insert_one(data)
        
        return data

    @staticmethod
    def update_post(id: int, input_data: dict) -> dict:
        input_data['updated_at'] = datetime.datetime.now()
      
        db.posts.update_one({"id": id}, {"$set": input_data})
        
        updated_data = db.posts.find_one({"id": id})

        return updated_data

    @staticmethod
    def delete_post(id) -> dict:
        data = db.posts.find_one({"id": id})
        db.posts.delete_one(data)

        return data
