from flask import Flask
from flask import render_template
from flask import request

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
	filtered_restaurants = ["Bojangles",
													"Wendy's",
													"Thai Univerity Place",
													"Passage to India"]
	resname = request.args.get('resname')
	print "I have reached the search page"
	return render_template("search.html", 
												 restaurants=filtered_restaurants,
												 res=True)

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
