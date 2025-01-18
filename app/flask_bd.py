from flask import Blueprint, redirect, url_for, request
from app.db_control import check_exsist, add_rec, get_rec, update_name, update_link, delete_rec

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

@main_bp.route("/add_link", methods=['POST'])
def add_link():
    try:
        data = request.form
        name = data['name']

        if name == None:
            return "name can't be None"

        if check_exsist(name) == True:
            return "your link name not unique", 302
        
        link = data["link"]

        add_rec(link, name)

        return "Link added"

    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/get_link", methods=['GET'])
def get_link():
    try:
        try:
            name = request.args.get('name')
            if name:
                name = get_rec(name)
                return f"{name[0]}"
        except:
            return "The parameter does not exist"
    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/upd_link", methods=['PUT'])
def upd_link():
    try:
        data = request.form
        upd = data['upd']
        
        match upd:
            case "name":
                name = data['name']

                if check_exsist(name) == False:
                    raise Exception

                new_name = data['new_name']
                update_name(name, new_name)

                return "Name updated successfully"
            case "link":
                name = data['name']

                if check_exsist(name) == False:
                    raise Exception

                new_link = data['new_link']
                update_link(name, new_link)

                return "Link updated successfully"

    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/del_link", methods=['DELETE'])
def del_link():
    try:
        data = request.form
        name = data['name']

        if check_exsist(name) == False:
            raise Exception

        delete_rec(name)

        return "Record deleted successfully"
    except:
        return redirect(url_for('backend.error')), 302

@main_bp.route("/error")
def error():
    return "this url not found or an unknown error occurred"