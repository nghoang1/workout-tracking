import requests
import datetime as dt
import os
APP_ID = os.environ["688babb1"]
API_KEY =os.environ["b66b3b3ff4f94f583816ed046548dc07"]
url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["https://api.sheety.co/e96e248272a374b1226e293195b65768/myWorkouts/sheet1"]
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
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
"Authorization": f"Bearer {os.environ['thisisadrill']}"
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

sheet_response = requests.post(url=sheety_endpoint, json = sheet_inputs,headers=bearer_headers)
print(sheet_response.text)