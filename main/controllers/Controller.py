from flask import Blueprint, request, jsonify
from ..services.updates import update_books

payload_controller = Blueprint("payload_controller",__name__)

@payload_controller.route("/",methods=["GET"])
def health_check():
	return jsonify({"status":"success"})

@payload_controller.route("/update_books",methods=["POST"])
def update_books_controller():
	update_books()
	return jsonify({'message':'Books updated'})
