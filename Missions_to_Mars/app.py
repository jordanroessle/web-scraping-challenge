from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

# initialize flask
app = Flask(__name__)

# initalize mongo connection with pymongo
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars')

@app.route("/")
def home():
	# grab data from mongo database
	scraped_data = mongo.db.collection.find_one()

	# return template and data
	return render_template("index.html", scraped_data = scraped_data)


@app.route("/scrape")
def scrape_information():
	# run scrape function
	mars_data = mission_to_mars.scrape()

	# update Mongo database 
	mongo.db.collection.update({}, mars_data, upsert=True)

	# return redirect to home page
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)	