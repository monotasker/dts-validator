from flask import abort, jsonify, request
from flask.views import MethodView
from dts_validator.mocks.collection_responses import (
    SAMPLE_COLLECTION_RESPONSES,
)
from dts_validator.mocks.document_responses import SAMPLE_DOCUMENT_RESPONSES
from dts_validator.mocks.navigation_responses import (
    SAMPLE_NAVIGATION_RESPONSES,
)


class MockAPI(MethodView):

    endpoints = {
        "collection": SAMPLE_COLLECTION_RESPONSES,
        "document": SAMPLE_DOCUMENT_RESPONSES,
        "navigation": SAMPLE_NAVIGATION_RESPONSES,
    }

    def get(self, endpoint):
        if endpoint in self.endpoints.keys():
            response_payloads = [
                s["response_payload"]
                for s in self.endpoints[endpoint]
                if s["request_args"] == request.args
            ]
            if len(response_payloads) > 0:
                return jsonify(response_payloads[0])
            else:
                abort(
                    400,
                    description="The provided request arguments have no mocked"
                    "response prepared",
                )

        abort(
            404,
            description="Invalid endpoint. Endpoints available for this "
            "sample API are 'collection', 'navigation', and 'document'.",
        )
