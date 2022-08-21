from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db, proxies
import json
from .webforms import SearchForm
from StockX.api import APIProductSX, APIsearch
from StockX.parser import parser_most_popular
from Restocks.api import APIsearchSKU

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    #shoes = parser_most_popular(2, proxies)
    #APIsearchSKU("DD1391-100", proxies)
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    result = None
    if form.validate_on_submit():
        query = form.searched.data
        result = APIsearch(query, proxies)
        if (result is None):
            print("error")
            return render_template("search.html", searched=result, user=current_user, query=query, captcha=True)
        result.printInfos()
        print("API done")
        return render_template("search.html", searched=result, user=current_user, query=query, captcha=False)
    return redirect(url_for('views.home'))