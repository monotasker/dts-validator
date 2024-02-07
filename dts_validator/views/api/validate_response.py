from dts_validator.services.DTSResponseValidator import DTSResponseValidator
from flask import request, jsonify
from flask.views import MethodView
import requests


class ValidateResponse(MethodView):
    def get(self):
        test_url_base = request.args["url_base"]
        test_url_endpoint = request.args["endpoint"]
        test_url_args = request.args["arguments"]
        test_request_url = [
            test_url_base,
            test_url_endpoint,
            test_url_args,
        ].join("/")
        test_request_method = request.args["test_method"]

        test_response = requests.request(test_request_method, test_request_url)

        test_evaluation = DTSResponseValidator().evaluate(
            endpoint=test_url_endpoint,
            url_args=test_url_args,
            response=test_response,
        )

        return jsonify({
            "result_body": test_response.data,
            "result_headers": test_response.headers,
            "evaluation": test_evaluation,
        })
