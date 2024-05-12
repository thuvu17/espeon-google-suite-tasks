from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    # Render the html file from the templates folder
    return render_template('home.html', title='Google Suite Manager Tool')

@app.route('/home_GoogleMeet')
def home_GoogleMeet():
    return render_template('home_GoogleMeet.html', title='Google Meet')

@app.route('/home_GoogleCalendar')
def home_GoogleCalendar():
    return render_template('home_GoogleCalendar.html', title='Google Calendar')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html', title='Sign in')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='127.0.0.1', port=5000)