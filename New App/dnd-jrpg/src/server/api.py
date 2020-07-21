# from flask import Flask
# from flask_restful import Resource, Api

# 
# app = Flask(__name__)
# api = Api(app)

def simple_func():
    print("this is a function from api.py")
    return "this is a function from api.py"


def func(x):
    return x + 1
# 
# class Student(Resource):
#     def get(self, name):
#       return {'student':name}
# 
#api.add_resource(Student, '/student/<string:name>')
# 
# app.run(port=5000)