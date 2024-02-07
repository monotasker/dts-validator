from flask import Flask, Blueprint
from dts_validator.views.ui.index import Index
from dts_validator.views.api.mock_api import MockAPI
from dts_validator.views.api.validate_response import ValidateResponse
from dts_validator.views.api.validate_endpoints import ValidateEndpoints

app = Flask(__name__)

# Index blueprint
index_blueprint = Blueprint("index", __name__)
index_blueprint.add_url_rule("/", view_func=Index.as_view("index"))

app.register_blueprint(index_blueprint)

# API blueprint
api_blueprint = Blueprint("api", __name__)

api_blueprint.add_url_rule(
    "/mock/<string:endpoint>",
    view_func=MockAPI.as_view("mock_api"),
)
api_blueprint.add_url_rule(
    "/validate/response",
    view_func=ValidateResponse.as_view("validate_response"),
)
api_blueprint.add_url_rule(
    "/validate/endpoints",
    view_func=ValidateEndpoints.as_view("validate_endpoints"),
)

app.register_blueprint(api_blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
