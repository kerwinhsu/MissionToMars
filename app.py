from flask import Flask, render_template
from flask_pymongo import PyMongo
import pymongo
#import scrape_mars


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")



@app.route("/")
def home(): 
    mars_data=mongo.db.collection.find_one()
    print(mars_data)
    return render_template("C:Users/KerwinH/Documents/Data Analytics/Homework/Mission To Mars/templates/index.html", info_on_mars= mars_data)
    
@app.route("/scrape/")
def scrape(): 
    mars = mongo.db.mars
    mars_info= scrape_mars.scrape()
    mars.update({}, mars_info, upsert = True)
    return "Scraping done!"

if __name__ == "__main__":
    app.run( debug=True)

    