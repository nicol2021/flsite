from flask import Flask, render_template, make_response, url_for, request, session
import datetime
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c8f529015ad2c25260e883db23bf381521351191'
app.permanent_session_lifetime = datetime.timedelta(days=10)

@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # обновление данных сессии
    else:
        session['visits'] = 1  # запись данных в сессию
 
    return f"<h1>Main Page</h1>Число просмотров: {session['visits']}"
 
data = [1,2,3,4]
@app.route("/session")
def session_data():
   session.permanent = True   #False
   if 'data' not in session:
      session['data'] = data
   else:
      session['data'][1] += 1
      session.modified = True

   return f"session['data']: {session['data']}"
 
if __name__ == "__main__":
   app.run(debug=True)
