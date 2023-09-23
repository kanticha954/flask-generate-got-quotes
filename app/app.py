from flask import Flask, render_template, request
import requests

app = Flask(__name__)


#url = "https://api.gameofthronesquotes.xyz/v1/random"
#response = requests.get(url=url)
#print(response.text)

api_url = "https://api.gameofthronesquotes.xyz/v1/random"
@app.route('/')
def welcome():
    return render_template('Welcome.html')
    
#get number of Quote
@app.route('/result', methods=["POST"])
def get_number():
    if request.method == 'POST':
        quat = int(request.form.get('quat'))
        url = f"https://api.gameofthronesquotes.xyz/v1/random/{quat}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            #handle single quote
            if isinstance(data, dict):
                data = [data]
            else: data = data
            print(quat)
            print(response.text)
            return render_template('index.html', quotes=data)
        else:
            return "Error"
    

if __name__ == '__main__':
   app.run(debug = True)
   