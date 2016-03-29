from flask import Flask
from flask import render_template
from flask import request
from restaurant_model import Restaurant

app = Flask(__name__)

@app.route('/')
def hello():
	print "home page"
	return render_template("home.html")

@app.route("/search")
def search_page():
	print "loading the search page"
	return render_template("search.html", 
												 restaurants=[],
												 res=False)

@app.route("/search_restaurants", methods=['GET'])
def search_restaurants():
	resname = request.args.get('resname')
	filtered_restaurants = Restaurant.\
												 query.\
												 filter(Restaurant.name.startswith(resname)).all()
	return render_template("search.html", 
												 restaurants=filtered_restaurants,
												 res=True)

@app.route('/all_restaurants')
def all_restaurants():
	filtered_restaurants = Restaurant.query.all()
	return render_template("all_restaurants.html", 
												 restaurants=filtered_restaurants)

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
