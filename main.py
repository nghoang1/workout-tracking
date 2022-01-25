import requests
import datetime as dt
import config

url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": config.APP_ID,
    "x-app-key": config.API_KEY,
}
activity = input("Which exercise did you do?")
parameters = {
    "query": activity,
    "gender":"male",
    "weight_kg":64.5,
    "height_cm":169.00,
    "age":27

}

response = requests.post(url=url_endpoint, headers=headers, json=parameters)
result = response.json()
#print(result["exercises"][0]["name"])
bearer_headers = {
"Authorization": F"Bearer {config.TOKEN}"
}
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=config.sheety_endpoint, json = sheet_inputs,headers=bearer_headers)
print(sheet_response.text)