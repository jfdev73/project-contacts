from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.contact import Contact

from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():

    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    contact = Contact(fullname, email, phone)
    db.session.add(contact)
    db.session.commit()

    flash("Contact addded successfully !")

    return redirect(url_for('contacts.home'))


@contacts.route("/update/<id>")
def update_contact(id):
    contact = Contact.query.get(id)
    return render_template("edit.html", contact=contact)

@contacts.route("/update",methods=["POST"])
def update_contact_post():
    id = request.form["id"]
    contact = Contact.query.get(id)
    contact.fullname = request.form["fullname"]
    contact.email = request.form["email"]
    contact.phone = request.form["phone"]

    db.session.commit()

    flash("Contact updated successfully !")
    return redirect(url_for('contacts.home'))


@contacts.route("/delete/<id>")
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts.home'))
