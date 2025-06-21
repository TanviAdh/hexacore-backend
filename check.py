import requests

response = requests.post("http://127.0.0.1:8000/api/attendance/create", json={
    "date": "2023-10-01",
    "status": "present",
    "remarks": "On time"
})
print(response.status_code)  # Check if it's 500
print(response.json())  