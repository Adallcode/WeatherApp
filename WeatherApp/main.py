from flask import Flask, request, render_template, redirect, flash
from Weather import Weather


app = Flask(__name__)

'''This is important to work with flash messages'''

app.secret_key = "asd"


# Weather route

@app.route("/")
@app.route("/weather", methods=['POST', 'GET'])
def weather() -> str:

    return render_template('weather.html', the_title= 'Weather')


# Result route

@app.route("/result", methods=['POST'])
def result() -> str:

    if request.method == 'POST':
        try:
            if request.form:
                city = request.form['city']
                # Units is by default iqual to Fahrenheit
                units = request.form['units']

                w = Weather(city, units)
                wT = w.getTemp()

                t = ('Temp', 'Humidity', 'Weather', 'Wind speed')

                return render_template('result.html', teh_tittle="Result", row_table=t, data=wT)
        except Exception as err:
            # This flash msg to let people know that the city could not be found
            flash("The city could not be found", category="error")
            
            return redirect( "/weather")
    

    return redirect( "/weather")


if __name__ == '__main__':
    app.run(debug=True)

