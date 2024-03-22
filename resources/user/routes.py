from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort

from schemas import UserSchema
from . import bp

from db import users
from models.user_model import UserModel

from app import db

@bp.route('/user')
class UserList(MethodView):
    
    @bp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all() #.all should return all items
        
    
    # @bp.arguments(UserSchema)
    # @bp.response(201, UserSchema)
    def post(self):
        data = request.get_json()
        print(data, '\n\n\n')
        # try:
        user = UserModel()
        user.from_dict(data)
        # db.session.add(user)
        # db.session.commit()
        user.save_user()
        return {'success': f'{data['username']} added'}, 201
        # except:
        return {'error': 'username or email already taken; try again'}, 400

@bp.route('/user/<int:id>')
class User(MethodView):
    
    @bp.response(200, UserSchema)
    def get(self, id):
        user = UserModel.query.get(id)
        if user:
            return user
        else:
            abort(400, msg='not a valid user')


    @bp.arguments(UserSchema)
    def put(self, data, id):
        user = UserModel.query.get(id)
        if user:
            user.from_dict(data)
            user.save_user()
            return {'message': 'user updated'}, 200
        else:
            abort(400, message='not a valid user')
     

    def delete(self, id):
        user = UserModel.query.get(id)
        if user:
            user.del_user()
            return {'message': 'user deleted'}, 200
        abort(400, message='not a valid user')
        

