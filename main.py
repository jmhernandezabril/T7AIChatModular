from flask import render_template
import config

def register_routes(app):

    @app.route("/")
    def index():
        return render_template(
            "base.html",
            app_name=config.APP_NAME,
            ai_model=config.AI_MODEL,
            font_family=config.FONT_FAMILY,
            saludo_inicial=config.SALUDO_INICIAL
        )