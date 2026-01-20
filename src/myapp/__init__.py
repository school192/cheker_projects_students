from flask import Flask


def create_app(config_object=None):
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="templates",
        static_folder="static",
    )
    app.config.from_mapping(SECRET_KEY="dev")

    if config_object:
        app.config.from_object(config_object)

    from .extensions import init_extensions

    init_extensions(app)

    from .routers import register_routers

    register_routers(app)

    return app
