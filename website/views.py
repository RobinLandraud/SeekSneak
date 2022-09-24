from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Favorite, Note
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
    #if request.method == 'POST':
    #    note = request.form.get('note')
#
    #    if len(note) < 1:
    #        flash('Note is too short!', category='error')
    #    else:
    #        new_note = Note(data=note, user_id=current_user.id)
    #        db.session.add(new_note)
    #        db.session.commit()
    #        flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/add-note', methods=['POST'])
def add_note():
    data = json.loads(request.data)
    note = data['note']
    if len(note) < 1:
        flash('Note is too short!', category='error')
    else:
        new_note = Note(data=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added!', category='success')
    print("test ok")
    return jsonify({})


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

@views.route('/add-favorite', methods=["POST"])
def add_favorite():
    print("ok passing !")
    product = json.loads(request.data)
    for fav in current_user.favorites:
        if fav.style_id == product["styleID"]:
            flash('already in Favorite!', category='success')
            return jsonify({})
    new_favorite = Favorite(style_id=product["styleID"], photo=product["image"], name=product["name"], link=product["link"], user_id=current_user.id)
    db.session.add(new_favorite)
    db.session.commit()
    flash('Favorite added!', category='success')
    return jsonify({})

@views.route('/delete-favorite', methods=['POST'])
def delete_favorite():
    favorite = json.loads(request.data)
    favoriteId = favorite['favoriteId']
    favorite = Favorite.query.get(favoriteId)
    if favorite:
        print("get fav !")
        if favorite.user_id == current_user.id:
            print("id user ok !")
            db.session.delete(favorite)
            db.session.commit()
        else:
            print("id user ko !")
    else:
        print("fav not found !")

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
            return render_template("search.html", user=current_user, query=query, captcha=True)
        resultR = APIsearchR(resultSX.styleID, resultSX.gender, resultSX.brand, proxies)
        resultG = APIsearchG(resultSX.styleID, proxies)
        #return render_template("search.html", searchedSX=resultSX, searchedR=resultR, user=current_user, query=query, captcha=False)
        print("API done")
        return render_template("search.html", searchedSX=resultSX, searchedR=resultR, searchedG=resultG, user=current_user, query=query, captcha=False)
    return redirect(url_for('views.home'))