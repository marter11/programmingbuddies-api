from flask import request, jsonify
from api import app
from api.controllers import projectController

@app.route("/projects", methods=['POST'])
def post_project():
    project = projectController.create_project(**request.get_json())

    return jsonify(project.as_dict()), 201

@app.route("/projects/<id>", methods=['GET'])
def get_project(id):
    project = projectController.get_project(id=id)

    if project:
        return jsonify(project.as_dict()), 200
    else:
        return "", 404

@app.route("/projects", methods=['GET'])
def get_all_projects():
    all_projects = projectController.get_all_projects()

    projects = [ project.as_dict() for project in all_projects ]

    return jsonify(projects), 200

@app.route("/projects/<id>", methods=['DELETE'])
def delete_project(id):
    project = projectController.delete_project(id)

    if project:
        return "", 202
    else:
        return "", 404