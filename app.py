from flask import Flask, render_template, request
import util
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    vehicle = util.get_vehicles()
    return render_template("carprice.html", vehicle = vehicle)

@app.route("/estimatedResult", methods = ["POST"])
def estimatedResult():
    try:
        year = int(request.form["year"])
        present_price = float(request.form["show_room_price"])
        kms = int(request.form["kilometers"])
        vehicle = request.form["vehicle"]
        owner = int(request.form["owner"])
        fuel = request.form["fuel"]
        seller = request.form["seller"]
        transmission = request.form["transmission"]

        diesel = 0
        petrol = 0
        individual = 0
        manual = 0

        year = datetime.now().year - year

        if fuel == "diesel":
            diesel = 1
        elif fuel == "petrol":
            petrol = 1

        if seller == "individual":
            individual = 1

        if transmission == "manual":
            manual = 1

        result = util.predict_price(year, present_price, kms, owner, diesel, petrol, individual, manual, vehicle)

        if result == 1:
            return "Something is wrong please fill proper input!!"
        else:
            return str(round(float(result), 2)) + " lakh rupees"
    except:
        return "Something is wrong please fill proper input!!"         


if __name__ == "__main__":
    app.run()
