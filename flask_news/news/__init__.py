import os
from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='secret-key-goes-here'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # from news.utils import get_news
    # from news.forms import SelectForm
    from . import utils
    from . import forms

    @app.route("/", methods=["GET", "POST"])
    @app.route("/home", methods=["GET", "POST"])
    def home():
        form = forms.SelectForm()
        if form.validate_on_submit(): 
            query = form.query.data 
            language = form.language.data
            category = form.category.data 
            country = form.country.data 
            sort_by = form.sort_by.data
            result = utils.get_news(query, language, category, country, sort_by)
            return render_template("home.html", form=form, result=result)

        return render_template("home.html", form=form)

    return app