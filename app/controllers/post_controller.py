from app.models.post_model import Post
from flask import request, jsonify
from http import HTTPStatus

def read():
    data_list = list(Post.read_all_posts())

    for data in data_list:
        del data["_id"]

    return jsonify(data_list), HTTPStatus.OK


def read_by_id(id):
    try:
        data = Post.read_post_by_id(id)

        del data["_id"]

        return jsonify(data), HTTPStatus.OK

    except TypeError:
        return dict(error="Post inexistente!"), HTTPStatus.NOT_FOUND


def create():
    try:
        data = request.get_json()
        data_list = list(Post.read_all_posts())
        
        if data_list != []:
            data['id'] = data_list[-1].get('id') + 1
            
        post = Post(**data)
        post.create_post()

        del post.__dict__["_id"]
                
        return jsonify(post.__dict__), HTTPStatus.CREATED

    except TypeError:
        return dict(error="Chaves incorretas!"), HTTPStatus.BAD_REQUEST


def update(id):
    try:
        input_data = request.get_json()

        if input_data['title'] and input_data['author'] and input_data['tags'] and input_data['content']:
       
            updated_data = Post.update_post(id, input_data)
      
            del updated_data["_id"]

            return jsonify(updated_data), HTTPStatus.OK
              
    except KeyError:
        return dict(error="Chaves incorretas!"), HTTPStatus.BAD_REQUEST

    except TypeError:
        return dict(error="Post inexistente!"), HTTPStatus.NOT_FOUND


def delete(id):
    try:
        data = Post.delete_post(id)
    
        del data["_id"]

        return jsonify(data), HTTPStatus.NO_CONTENT
    
    except TypeError:
        return dict(error="Post inexistente!"), HTTPStatus.NOT_FOUND
