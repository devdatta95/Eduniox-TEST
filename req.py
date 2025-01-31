import requests
import json

url = "http://192.168.31.91:8081/api/prediction"

payload = json.dumps({
  "Gender": 1,
  "Married": 1,
  "Dependents": 20,
  "Education": 1,
  "Self_Employed": 0,
  "ApplicantIncome": 1,
  "CoapplicantIncome": 0,
  "LoanAmount": 556,
  "Loan_Amount_Term": 36,
  "Credit_History": 0,
  "Property_Area": 2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
