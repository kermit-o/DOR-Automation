from flask import jsonify

def example_route():
    return jsonify({"message": "Hello from example route!"})
