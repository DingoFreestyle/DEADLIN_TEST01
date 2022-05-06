from flask import url_for, session, Flask, render_template, request, redirect

application = Flask(__name__)
application.secret_key = "#"

@application.route("/")
def log_in():
    if "userID" in session:
        return render_template("home.html", username = session.get("userID"), login = True)
    else:
        return render_template("home.html", login = False)


@application.route("/login", methods = ["get"])
def login():
    _id_ = request.args.get(userID)


@application.route("/logout")
def logout():
    pass

application.run(host ="0.0.0.0")