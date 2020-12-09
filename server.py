"""
Server file
"""


from flask import render_template


import config



connex_app = config.connex_app


connex_app.add_api("swagger.yml")



@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")



@connex_app.route("/people")
@connex_app.route("/people/<int:person_id>")
def people(person_id=""):
    """
    This function just responds to the browser URL
    localhost:5000/people
    :return:        the rendered template "people.html"
    """
    return render_template("people.html", person_id=person_id)


if __name__ == "__main__":
    connex_app.run(debug=True)
