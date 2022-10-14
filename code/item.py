import sqlite3
from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from constants import DB_PATH


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"item": {"id": row[0], "name": row[1], "price": row[2]}}, 200

    @classmethod
    def insert_item(cls, item):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (NULL, ?, ?)"
        cursor.execute(query, (item["name"], item['price']))
        connection.commit()
        connection.close()

    @classmethod
    def update_item(cls, item):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item["name"]))
        connection.commit()
        connection.close()

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item, 200
        return {"message": "{} not found".format(name)}, 404

    def post(self, name):
        if Item.find_by_name(name):
            return {'item': "An item with name '{}' already exists. ".format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        try:
            Item.insert_item(item)
        except:
            return {"message": "an error occurred inserting item"}, 500
        return item, 201

    @jwt_required()
    def delete(self, name):
        item = Item.find_by_name(name)
        if not item:
            return {'message': "Item not found"}
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {"message": "item successfully deleted"}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = Item.find_by_name(name)
        new_item = {"name": name, "price": data['price']}
        if item is None:
            try:
                Item.insert_item(new_item)
            except:
                return {"message": "an error occurred inserting item"}, 500
        else:
            try:
                Item.update_item(new_item)
            except:
                return {"message": "an error occurred updating item"}, 500
        return new_item, 200


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = [{"id": item[0], "name": item[1], "price": item[2]} for item in result]
        connection.close()

        return items, 200
