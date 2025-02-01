from flask import Blueprint, request, jsonify
from app.utils.database import get_db

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/", methods=["GET"])
def get_users():
    db = get_db()
    users = db.execute("SELECT * FROM users").fetchall()
    return jsonify([dict(user) for user in users])

@bp.route("/", methods=["POST"])
def create_user():
    db = get_db()
    data = request.json
    db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
               (data["name"], data["email"], data["password"]))
    db.commit()
    return jsonify({"message": "User created successfully"}), 201
