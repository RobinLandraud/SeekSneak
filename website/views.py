from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db, proxies
import json
from .webforms import SearchForm

from StockX.api import APIProductSX, APIsearchSX
from StockX.parser import parser_most_popular
from Goat.api import APIsearchG

from Restocks.api import APIProductR, APIsearchR

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
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
        resultSX = APIsearchSX(query, proxies)
        if (resultSX is None):
            print("error StockX")
            return render_template("search.html", searchedSX=resultSX, searchedR=resultR, user=current_user, query=query, captcha=True)
        resultR = APIsearchR(resultSX.styleID, resultSX.gender, resultSX.brand, proxies)
        if resultR is None:
            print("error Restocks")
            return render_template("search.html", searchedSX=resultSX, searchedR=resultR, user=current_user, query=query, captcha=True)
        resultG = APIsearchG(resultSX.styleID, proxies)
        if resultG is None:
            print('error Goat')
            return render_template("search.html", searchedSX=resultSX, searchedR=resultR, user=current_user, query=query, captcha=True)
        print("API done")
        return render_template("search.html", searchedSX=resultSX, searchedR=resultR, searchedG=resultG, user=current_user, query=query, captcha=False)
    return redirect(url_for('views.home'))