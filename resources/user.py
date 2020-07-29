import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be left blank and must be a string",
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field cannot be left blank and must be a string",
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "Username already taken"}

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201