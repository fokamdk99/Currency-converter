from django.shortcuts import render
import requests
import json

data = {}

# Create your views here.
def index(request):
    res = requests.get("https://api.exchangeratesapi.io/latest", params = {"format": "json"})
    if res.status_code != 200:
        print(f"nie udalo sie!")
    else:
        currencies = res.json()
        print(f"siema! odpowidz: {currencies['rates']['CAD']}")
        values = currencies['rates']
        values["EUR"] = 1
        print(f"{values}")
        keys = []
        for key in values:
            data[key] = values[key]
            print(f"key: {key}, value: {values[key]}")
            keys.append(key)
            context = {
                "keys":keys
            }
        print(f"{data}")
    return render(request, "pwinside/index.html", context)

def output(request):
    first = request.POST["first"]
    second = request.POST["second"]
    money = request.POST["money"]
    print(f"first currency: {first}, second currency: {second}")
    value1 = data[first]
    value2 = data[second]
    if first == "EUR":
        content = {
            "first": first,
            "second": second,
            "rate": float(money) * value2,
            "money": money
        }
    else:
        content = {
            "first": first,
            "second": second,
            "rate": float(money) * value2 / value1,
            "money": money
        }
    return render(request, "pwinside/response.html", content)