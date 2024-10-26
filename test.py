import requests

data = {
    "request_type": "update_med",
    "email": "example4@gmail.com",
    "Med_data":{'id':124,
                "name":"paracetamol",
                "brand":"Dr.Reddy",
                "quantity":1000}
}
response = requests.post("http://127.0.0.1:8000/api/medicine", json=data)
print(response.text)