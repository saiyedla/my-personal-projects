import requests
import pandas as pd

def fetch_json_data(api_url):
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            print("Error: ",response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

api_url_1 = "https://jsonplaceholder.typicode.com/comments"
api_url_2 = "https://jsonplaceholder.typicode.com/posts/1"


json_data_1 = fetch_json_data(api_url_1)
json_data_2 = fetch_json_data(api_url_2)


if json_data_1 and  json_data_2:
    print(json_data_1)
    df_1 = pd.DataFrame(json_data_1)
    df_2 = pd.DataFrame([json_data_2])
    print(df_1)
    print(df_2)
