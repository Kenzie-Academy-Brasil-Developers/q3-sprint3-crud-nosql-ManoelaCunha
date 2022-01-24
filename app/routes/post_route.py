from flask import Flask
from app.controllers import post_controller

def post_route(app: Flask):

    @app.get("/posts")
    def read_posts():
        return post_controller.read()

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        return post_controller.read_by_id(id)

    @app.post("/posts")
    def create_post():
        return post_controller.create()

    @app.patch("/posts/<int:id>")
    def update_post(id):
        return post_controller.update(id)

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return post_controller.delete(id)
