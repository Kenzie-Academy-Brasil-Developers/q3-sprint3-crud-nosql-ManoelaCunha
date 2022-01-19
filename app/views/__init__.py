from flask import Flask

def init_app(app: Flask):

    from app.views.posts.post_route import post_route
    post_route(app)
