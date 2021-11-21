import requests



# Units: metric = Fahrenheit, imperial = Celsius

class Weather:
    def __init__(self, city: str, units: str = "") -> None:
        self.city = city
        self.units = units
        
    def getTemp(self) -> tuple:

        dic = { "APPID": "7a48ec450df61a100a3c1bf5cf1bb00c", "q": self.city, "units": self.units }

        url = "http://api.openweathermap.org/data/2.5/weather?"

        res = requests.get(url, params=dic)
        # Convert the data into a json 
        js = res.json()

        mTuple = (js['main']['temp'], js['main']['humidity'], js['weather'][0]['main'], js['wind']['speed'])
        return mTuple
    

