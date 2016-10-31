from flask import Flask, render_template
app = Flask(__name__)

def get_date():
   import time
   return time.strftime("%d/%m/%Y")

def get_time():
   import time
   return time.strftime("%I:%M:%S")


@app.route('/date')
def print_date():
   return render_template("date.html", cdate=get_date())

@app.route('/time')
def print_time():
   return render_template("time.html", cdate=get_time())

 
if __name__ == '__main__':
    try:
        app.run(debug=False,host="0.0.0.0")
    except KeyboardInterrupt:
        pass

