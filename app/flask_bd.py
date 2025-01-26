from flask import Blueprint, redirect, url_for, request, jsonify
from app.db_control import check_exsist, add_rec, get_rec, update_name, update_link, delete_rec
import yaml

main_bp = Blueprint('backend', __name__)

@main_bp.route("/")
def main():
    return redirect(url_for('backend.error')), 302

@main_bp.route("/<name>")
def link(name):
    try:
        link = get_rec(name)

        if link != None:
            return redirect(link[0]), 302
        return "This name does not exsist"

    except:
        return redirect(url_for('backend.error')), 302
    
@main_bp.route("/favicon.ico")
def icon():
    return '', 404

@main_bp.route("/link", methods=['POST'])
def add_link():
    try:
        try:
            data = request.form
            name = data['name']

            if name == None:
                return "name can't be None", 403

            if check_exsist(name) == True:
                return "your link name not unique", 403
            
            try:
                link = data["link"]

                add_rec(link, name)

                return "Link added", 200
            except:
                return "Link was't transmitted", 403
        except:
            return "Name was't transmitted", 403

    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/link/<name>", methods=['GET'])
def get_link(name):
    try:
        try:
            name = get_rec(name)

            if name:
                return f"{name[0]}", 200
            
            return "This name is not in db", 500

        except:
            return "Name was't transmitted", 403
    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/link/<upd>/<name>", methods=['PUT'])
def upd_link(upd, name):
    try:
        data = request.form
        
        match upd:
            case "name":

                if check_exsist(name) == False:
                    return "This name is not in db", 500

                new_name = data['new_name']
                update_name(name, new_name)

                return "Name updated successfully", 200
            case "link":

                if check_exsist(name) == False:
                    return "This name is not in db", 500

                new_link = data['new_link']
                update_link(name, new_link)

                return "Link updated successfully", 200

    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/link/<name>", methods=['DELETE'])
def del_link(name):
    try:
        try:

            if check_exsist(name) == False:
                return "This name is not in db", 500

            delete_rec(name)

            return "Record deleted successfully", 200
        except:
            return "Name was't transmitted", 403
    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/error")
def error():
    return "this url not found or an unknown error occurred"

# Эндпоинт для проверки работы
@main_bp.route('/api', methods=['GET'])
def api_info():
    with open('swagger.yaml', 'r') as file:
        swagger_info = yaml.safe_load(file)
    return jsonify(swagger_info)