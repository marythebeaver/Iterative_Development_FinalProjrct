from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

#for multi threads
session = scoped_session(sessionmaker(bind=engine))
@app.teardown_request
def remove_session(ex=None):
    session.remove()


@app.route('/')
@app.route('/restaurants')
def showRestaurants():


    return render_template('restaurants.html', restaurants = restaurants)


@app.route('/restaurant/new')
def newRestaurants():


    return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurants(restaurant_id):


    return render_template('editRestaurant.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurants(restaurant_id):


    return render_template('deleteRestaurant.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):


    return render_template('menu.html', restaurant = restaurant, items = items)


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):


    return render_template('newMenuItem.html', restaurant = restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id,menu_id):


    return render_template('editMenuItem.html', restaurant = restaurant, item = item)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id,menu_id):


    return render_template('deleteMenuItem.html', restaurant = restaurant, item = item)





if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
