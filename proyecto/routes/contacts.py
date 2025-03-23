from flask import Blueprint, render_template, request, redirect, url_for

from models.contact import Contact
from utils.db import get_db_connection


#contacts = Blueprint("contacts", __name__, url_prefix="/contacts")

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contact;')
    contacts_data = cur.fetchall()
    print("contacts: ", contacts_data)
    contacts = [Contact(id,fullname, email, phone) for id, fullname, email, phone in contacts_data]
    cur.close()
    conn.close()
    return render_template("index.html", contacts=contacts)


@contacts.route("/new",  methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    contact = Contact(None,fullname, email, phone)

    print("Contact: ", contact)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO contact (fullname, email, phone)'
                'VALUES (%s, %s, %s)',
                (fullname, email, phone))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('contacts.home'))


@contacts.route("/update/<id>")
def update_contact(id):


    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contact WHERE id = %s;', (id,))
    contact_db = cur.fetchone()
    contact = None

    if contact_db:
        # Crear un objeto Contact con los datos de la tupla
        contact = Contact(
            id=contact_db[0],
            fullname=contact_db[1],
            email=contact_db[2],
            phone=contact_db[3]
        )

    cur.close()
    conn.close()
    return render_template("edit.html", contact = contact)

@contacts.route("/update", methods=["POST"])
def update_contact_post():
    id = request.form["id"]
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contact WHERE id = %s;', (id,))
    contact_db = cur.fetchone()

    cur.execute(
        'UPDATE contact SET fullname = %s, email = %s, phone = %s WHERE id = %s;',
        (fullname, email, phone, id))

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('contacts.home'))




@contacts.route("/delete/<id>")
def delete_contact(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM contact WHERE id = %s;', (id,))
    conn.commit()

    cur.close()
    conn.close()
    return redirect(url_for('contacts.home'))
