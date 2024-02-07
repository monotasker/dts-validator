from flask import abort, jsonify, request
from flask.views import MethodView


class ValidateEndpoints(MethodView):
    def get(self):
        url_base = request.args.get("url_base")
        if url_base:
            return jsonify({
                "message": f"Confirming that {url_base} provides the required "
                "DTS api endpoints"
            })
        else:
            abort(
                400,
                description="You must supply a valid URL base where "
                "the DTS API endpoints are found.",
            )
