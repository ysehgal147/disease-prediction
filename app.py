from flask import Flask, render_template, request,jsonify, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model_pickle","rb"))
df=pd.read_csv("Testing.csv")
X = df.iloc[:,:-1]
symptoms_dict = {}

for index, symptom in enumerate(X):
    symptoms_dict[symptom] = index

input_vector = np.zeros(132)

@app.route('/')
def hello_world():
    return render_template('disease.html')


@app.route('/predict', methods=["POST", "GET"])
def predict(): 
    if request.method == 'POST':
        user1 = request.form["a"]
        user2 = request.form["b"]
        user3 = request.form["c"]
        user4 = request.form["d"]
        user5 = request.form["e"]
        user = [user1, user2,user5,user4, user3]
        input_vector = np.zeros(132)
       
        # return redirect(url_for("user", usr=user))

        for i in user:
            if i in symptoms_dict:
                input_vector[symptoms_dict[i]] = 1
        prediction = model.predict([input_vector])
        return render_template('disease.html', pred='{}'.format(prediction))         
    # else:
    #     return render_template("disease.html")

    	# input_feature = [np.array(input_feature)]
    	# input_feature = [int(x) for x in request.form.values()]

    # 	for i in input_feature:
    # 		input_vector[i] = 1
    # prediction = model.predict([input_vector])
    # return render_template('disease.html', prediction_text='Sales should be $ {}'.format(prediction))
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)        
