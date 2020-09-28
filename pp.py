from flask import Flask, render_template, request,jsonify, redirect, url_for
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/login', methods=["POST","GET"])
def login(): 
    user = []
    if request.method == 'POST':
        user1 = request.form["a"]
        user2 = request.form["b"]
        user3 = request.form["c"]
        user4 = request.form["d"]
        user5 = request.form["e"]
        user = [user1, user2,user5,user4, user3]
        # for i in range(0, len(user)): 
        #     user[i] = int(user[i]) 
        # int_features = [int(x) for x in request.form.values()]
        # final_features = [np.array(int_features)]
        # return redirect(url_for("user", usr=user))
        for i in user:
            input_vector[i] = 1
        prediction = model.predict([input_vector])
        return render_template('disease.html', pred='{}'.format(prediction))         
    else:
        return render_template("index.html")

@app.route("/<usr>")
def user(usr):
    c = isinstance(usr, str)
    return f"{c}"

if __name__ == "__main__":
    app.run(debug=True)               