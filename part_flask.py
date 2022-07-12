from flask import Flask, request, render_template
import api




app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        forecast = api.Wheather(request.form['city_name'])
        data = forecast.error_handler()
        return render_template("weather_info.html",  city = data[0], country=data[1], temp=data[2], wind=data[3], screen_color=data[4])
    return render_template("landing_page.html")




if __name__ == "__main__":
    app.run()



