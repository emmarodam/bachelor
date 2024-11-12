# 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

# https://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@github.com/emmarodam/uw_exam.git

from bottle import default_app, get, static_file, run, template, request
from icecream import ic
import requests
import x # imports x.py

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")

########################
@get("/script.js")
def _():
    return static_file("script.js", ".")

############################## 
# Defines a route for the home page (`/`). This function sends a POST request to an ArangoDB instance to fetch all crimes and suspects. 
# It then renders the `index` template with the fetched data if available; otherwise, it returns an error message.

@get("/")
def get_all_crimes_suspects():
    url = "http://host.docker.internal:8529/_api/cursor"
   
    # Query to get all crimes, suspects, and people
    query = {
        "query": """
        RETURN {
            crimes: (FOR crime IN crimes RETURN crime),
            suspects: (FOR suspect IN suspects RETURN suspect),
        }
        """
    }
    res = requests.post(url, json=query).json()
   
    if 'result' in res and res['result']:
        data = res['result'][0]
        return template("index", crimes=data['crimes'], suspects=data['suspects'])
    else:
        return {"error": "Data not found"}
        

##############################
@get("/get-crimes")
def get_crimes():
    token = "241097"
    crime_url = f"https://emmarodam.pythonanywhere.com/crimes?token={token}"
 
    try:
        # Make the HTTP GET request
        response = requests.get(crime_url)
 
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Access the JSON data from the response
            crime_data = response.json()
            print(crime_data)  # Output the JSON data
        else:
            return {
                "error": "Failed to fetch data",
                "status_code": response.status_code
            }
 
        res = x.db(query)
        ic(res)
 
        # Check if 'result' key exists in the response
        if 'result' in res:
            return res["result"]
        else:
            return {
                "error": res.get("errorMessage", "Unknown error occurred"),
                "code": res.get("code", "No code available")
            }
    except Exception as e:
        return {
            "error": str(e),
            "status_code": 500
        }



app = default_app()



