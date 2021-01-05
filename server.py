from flask import Flask, redirect, request,render_template
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)

def store_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        writer = csv.writer(database, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        name=data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer.writerow([name,email, subject, message])

@app.route('/submit_msg', methods=['POST', 'GET'])
def submit_msg():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            store_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try Again'