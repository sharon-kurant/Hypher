from flask import Flask, redirect, session,url_for,render_template
from flask import request, jsonify, make_response
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
  searching = 'sharonfdd'
  return render_template("index.html", searching=searching)

@app.route('/SendCountry',methods= ['POST'])
def process():
  countryCode = request.form['countryCode']
  countryName = request.form['countryName']
  output = countryCode+' '+countryName
  if countryCode and countryName:
    print(output)
    return jsonify({'output': output})
  return jsonify({'error' : 'Missing data!'})
  



if __name__ == '__main__':
    app.run(debug= True)
