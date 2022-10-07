import requests
import json
import argparse


introspection_query = """
{
    "query": "query IntrospectionQuery { __schema { queryType { name } mutationType { name } subscriptionType { name } types { ...FullType } directives { name description locations args { ...InputValue } } } } fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } } fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue } fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }"
}
"""

class SpecGenerator:

    def __init__(self):
        pass
    
    @staticmethod
    def _configure_console_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('--url', type=str, help='Graphql server introspection url')
        return parser.parse_args()

    def generate(self, url):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=introspection_query, headers=headers)
        spec_json = response.json()
        with open("spec.json", "w") as outf:
            outf.write(str(json.dumps(spec_json)))


if __name__ == '__main__':
    arguments = PublishApiSpecs._configure_console_parser() 
    publish_api_specs = SpecGenerator()
    publish_api_specs.generate(arguments.url)
