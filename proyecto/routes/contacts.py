from flask import Blueprint, render_template

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    return render_template("index.html")


@contacts.route("/new")
def add_contact():
    return "Saving a contact"


@contacts.route("/update")
def update_contact():
    return "Update a contact"


@contacts.route("/delete")
def delete_contact():
    return "Update a contact"
