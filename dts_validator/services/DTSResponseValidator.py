import json
from pyld import jsonld

# from pprint import pprint


def getContext() -> json:
    """
    Read the DTS JSON-LD context file and return JSON object
    """
    with open("specifications/context/1.0.0draft-2.json") as context_file:
        context_object = json.load(context_file)
    return context_object


class DTSResponseValidator:
    """
    Validators for DTS-compliant endpoint response documents.
    """

    def __init__(self, collection_schema, navigation_schema):
        self.collection_schema = collection_schema
        self.navigation_schema = navigation_schema

    def validate_collection(self):
        """
        Validates the JSON-LD object returned from a DTS-compliant
        Collection endpoint GET request
        """

        # TODO: can we declare schema for "dublincore" object?
        # TODO: in "references" members must be links to the
        # Navigation API route for the object
        # TODO: "passage" uri must be url for the Documents API for the object
        pass

    def validate_document(self):
        """
        Validates the XML document returned from a DTS-compliant
        Collection endpoint GET request
        """
        pass

    def validate_navigation(self):
        """
        Validates the JSON-LD object returned from a DTS-compliant
        Collection endpoint GET request
        """
        pass

    if __name__ == "__main__":
        context = getContext()
        jsonld.set_document_loader(jsonld.requests_document_loader())

        compacted = jsonld.compact(sample, context)
        print(json.dumps(compacted, indent=4))

        expanded = jsonld.expand(sample, context)
        print(json.dumps(expanded, indent=4))

        # validate some Dublincore
