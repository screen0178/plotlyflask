"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        from .assets import compile_static_assets

        # Import Dash application
        from .plotlydash.dashboard_like import init_likeDashboard
        app = init_likeDashboard(app)
        from .plotlydash.dashboard_comment import init_commentDashboard
        app = init_commentDashboard(app)

        # Compile static assets
        compile_static_assets(assets)

        return app
