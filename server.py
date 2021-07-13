from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

print(__name__)


# creating multiple routes on the server:
@app.route('/')
def my_home():
    # render_template() files to be rendered must be in a template folder
    return render_template('index.html')


# dynamic way to accept url page name's, much easier than repeating the route
@app.route('/<string:page_name>')
def html_page(page_name):
    # render_template() files to be rendered must be in a template folder
    return render_template(page_name)


# wrtiting to database.txt:
def write_to_file(data):
    with open('bin/database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(
            f'\n EMAIL: {email}, SUBJECT: {subject}, MESSAGE: {message}')


# writing to database.csv:
def write_to_csv(data):
    with open('bin/database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # method to_dict() turns info from the contact page data fields into a dictionary, the info is then printed to terminal
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong, please try again.'
