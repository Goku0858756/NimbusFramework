__author__ = 'N05F3R4TU'
from flask import Flask, redirect, render_template, flash, request, url_for
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user, fresh_login_required
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json

app = Flask(__name__)
app.secret_key = "senna is een blije baby"
mongo = MongoClient(host="localhost", port=27017, connect=True)

Breadcrumbs(app=app)
colors = {"bg": "#252830", "menu":  "#30343e", "blue":  "#42a5f5", "green": "#1bc98e", "red":   "#e64759", "line":  "#434857", "else": "#444851", "panel_bg_text": "#c0c2c5"}
login_manager = LoginManager()
login_manager.init_app(app=app)
users = {'test@user.com': {'pw': 'secret'}}




""" --------------------------------------------------------- """
"""                     Dashboard :: View                     """
""" --------------------------------------------------------- """

@app.route("/")
@app.route("/home")
@app.route("/index")
@app.route("/dashboard")
@login_required
@fresh_login_required
def index():
    user = current_user.id
    return render_template("index.html", user=user)

@app.route("/scans", methods=['GET', 'POST'])
@login_required
def scans():

    if request.method == 'GET':
        print("Do Something with GET")
    elif request.method == "POST":
        print("Do a POST")
    else:
        print("Else something")

    nr = mongo["targets"]["nr"].find_one({'_id': '12345'})
    print(nr)
    return render_template("scans.html", nr=nr)




""" --------------------------------------------------------- """
"""           Targets, Schedule, Templates  :: Views          """
""" --------------------------------------------------------- """
# @app.route('/scan')
# @app.route('/scan/<int:id>')
# @app.route('/scan/ip/<ip>')
# @app.route('/scan/url/<url>')
# @app.route('/scan/name/<name>')
# @login_required
# @fresh_login_required
# def scan(id=None, ip=None, url=None, name=None):
#
#     context = {'id': id, 'ip': ip, 'name': name, 'url': url}
#     return render_template('scan.html', **context)


@app.route('/victim/<name>', methods=["POST", "GET"])
def victim(name=None):

    if request.method == 'POST':

        try:
            target = mongo['nimbus']['targets'].insert_one({
                "name":request.form['name'],
                "description":request.form['description'],
                "ip": [request.form['target']]
            })
            print(target.inserted_id)
        except Exception as e:
            print("[ VICTIM ]" + str(e))
        finally:
            mongo.close()

    else:
        if name == "overview":
            return render_template('victims.html')

    return render_template('victim.html', name=name)


@app.route('/template/<state>')
@app.route('/template/<state>/<id>')
def template(state, id=None):

    if state == "create":
        return render_template('modules.html')
    elif state == 'edit' and id != None:
        return "Edit existing template"
    else:
        return "Unknown State"





""" --------------------------------------------------------- """
"""           Filter, Os, CMS, Proto ...  :: Views            """
""" --------------------------------------------------------- """

@app.route("/filter/<category>")
@login_required
@fresh_login_required
def filter(category):

    context = ""
    if category == "cms":
        context = "CMS Data"
    else:
        context = "Other Data then CMS"

    return render_template("filter.html", category=category, context=context)





""" --------------------------------------------------------- """
"""           Add, Edit, Delete, Overview  :: Views           """
""" --------------------------------------------------------- """
@app.route('/add/<component>')
def add(component):
    """
    Add <component> :: Targets, Templates(modules(plugins)), Schedules(target, template)
    """
    return render_template('add.html', component=component)


@app.route('/edit/<component>/<id>')
def edit(component, id):
    return render_template('edit.html', component=component, id=id)

@app.route('/overview/<component>')
def overview(component):

    return render_template('overview.html', component=component)





""" --------------------------------------------------------- """
"""                Login, Register, Logout  :: Views          """
""" --------------------------------------------------------- """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='pw' id='pw' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
               '''

    email = request.form['email']
    if request.form['pw'] == users[email]['pw']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))
    else:
        return 'Bad login'

# @app.route('/login', methods=["POST", "GET"])
# def login(error=None):
#
#     if request.method == "POST":
#         user = mongo['nimbus']['users'].find_one({"username":request.form['username']})
#
#         if user != None and user["passwd"] == request.form['password']:
#             print("logged IN")
#             # user = User()
#             # user.id = request.form['username']
#             # login_user(user)
#             # return redirect(url_for('protected'))
#             return redirect(url_for('index'))
#         else:
#             print("Logged In Else")
#             error = "The given Username and/or password is invalid"
#             return render_template('login.html', error=error)
#
#     elif request.method == "GET":
#         print("Print Request")
#         return render_template('login.html', error=error)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'


class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user


""" --------------------------------------------------------- """
"""                Redirect Forms  :: Views                   """
""" --------------------------------------------------------- """

@app.errorhandler(404)
def page_not_found(error):
    # return render_template('page_not_found.html'), 404
    return redirect(url_for('index'))

@app.route('/protected')
@login_required
def protected():
    # return 'Logged in as: ' + current_user.id
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return redirect(url_for('index'))

@app.route('/save', methods=["POST"])
def save():
    # return render_template('save.html')
    print(json.dumps(dict(request.form.items())))
    return "Saved"


""" --------------------------------------------------------- """
"""                     WorldMap  :: View                     """
""" --------------------------------------------------------- """
@app.route("/map")
@login_required
@fresh_login_required
def worldmap():
    return render_template('worldmap.html')



def start_web(host='localhost', port=8000, debug=True):
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    start_web()
