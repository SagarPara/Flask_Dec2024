
from flask import Flask, request
import pickle
import sklearn 

app = Flask(__name__)



#load/upload the classifier model into the Project
with open("classifier.pkl", "rb") as file:
    model_pickle = pickle.load(file)




#API Endpoints
@app.route("/")
def hello_world():
    return "<h1>Hi, this is my first Flask page!!!</h1>"

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        return "I will make the prediction"
    else:
        #post request to prediction server"

        loan_req = request.get_json()
        
        if loan_req["Gender"]=="Male":
            Gender=0
        else:
            Gender=1

        
        if loan_req["Married"]=="No":
            Married=0
        else:
            Married=1

        
        ApplicantIncome = loan_req["ApplicantIncome"]
        LoanAmount = loan_req["LoanAmount"]
        Credit_History = loan_req["CreditHistory"]

        input_data = [Gender,Married,Credit_History,LoanAmount,Credit_History]
        result = model_pickle.predict([input_data])
        


        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return {"Loan_approval_status":pred}
                                  


