from crypt import methods
from flask import Blueprint, request, redirect, render_template, session
from models.beer import get_beer, insert_beer, get_all_beer, update_beer, delete_beer


beer_controller = Blueprint(
    "beer_controller", __name__, template_folder="../templates/beer")


@beer_controller.route('/beers')
def beers():
    beer_items = get_all_beer()

    return render_template('beerlist.html', beer_items=beer_items, user_id=session.get("user_id"))

@beer_controller.route('/beers/create')
def create():
    return render_template('create.html')

@beer_controller.route('/beers', methods=["POST"])
def insert():
    # INSERT INTO DB
    print(session.get("user_id"))
    insert_beer(
        session.get("user_id"),
        request.form.get("name"),
        request.form.get("image_url"),
        request.form.get("type"),
        request.form.get("miscellaneous"),
        request.form.get("style")
    )


    return redirect('/')

@beer_controller.route('/beers/<id>')
def show(id):
    beer = get_beer(id)
    return render_template('show.html', beer=beer)

@beer_controller.route('/beers/<id>/edit')
def edit(id):
    beer = get_beer(id)
    print (beer)
    return render_template('edit.html', beer=beer )


@beer_controller.route('/beers/<id>', methods=["POST"])
def update(id):
    name = request.form.get("name")
    image_url = request.form.get("image_url")
    type = request.form.get("type")
    miscellaneous = request.form.get("miscellaneous")
    style = request.form.get("style")
    

    # UPDATE
    
    update_beer(id, name, image_url, type, miscellaneous, style)

    return redirect ('/')


@beer_controller.route('/beers/<id>/delete', methods=["POST"])
def delete(id):
    delete_beer(id)
    return redirect('/')