from flask import Flask

def post_route(app: Flask):

    @app.get("/posts")
    def read_posts():
        return ""

    @app.get("/posts/<int:id>")
    def read_post_by_id():
        return ""

    @app.post("/posts")
    def create_post():
        return ""

    @app.patch("/posts/<int:id>")
    def update_post():
        return ""

    @app.delete("/posts/<int:id>")
    def delete_post():
        return ""