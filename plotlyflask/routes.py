"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app
from flask import  redirect

@app.route('/')
def home():
        # app = init_likeDashboard(app)
    # """Landing page."""
    # return render_template(
    #     'index.jinja2',
    #     title='Plotly Dash Flask Tutorial',
    #     description='Embed Plotly Dash into your Flask applications.',
    #     template='home-template',
    #     body="This is a homepage served with Flask."
    # )
    return redirect('/likeDashboard')
