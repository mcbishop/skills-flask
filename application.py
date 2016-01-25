

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage. It's a good one.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show an application form page."""
    """ grab name, salary, title information."""

    return render_template("application-form.html")


@app.route("/application-response", methods=["POST"])
def application_response():
    """Show an application response page."""
    """ display name, salary, title information from application-form."""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    job_title = request.form.get("job_title")


    return render_template("application-response.html",
                            firstname = firstname,
                            lastname = lastname,
                            salary = salary,
                            job_title = job_title)



if __name__ == "__main__":
    app.run(debug=True)
