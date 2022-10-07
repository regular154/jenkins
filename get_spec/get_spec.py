import requests
import json
import argparse
import yaml


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
        parser.add_argument('--title', type=str, help='Title')
        parser.add_argument('--description', type=str, help='Description')
        parser.add_argument('--server', type=str, help='Server url')
        return parser.parse_args()

    def get_spec(self, url):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=introspection_query, headers=headers)
        spec_json = response.json()
        with open("spec.json", "w") as outf:
            outf.write(str(json.dumps(spec_json)))
    
    def modify_config(self, title, description, server):
        with open("config.yml", "r") as stream:
            try:
                config = yaml.safe_load(stream)
                config['info']['title'] = title
                config['info']['description'] = description
                config['servers'].append({'url': server})
            except yaml.YAMLError as exc:
                warnings.warn(f"FAIL: Config file couldn't be modified because - {exc}")
        with open("config_modified.yml", 'w') as outf:
            yaml.dump(config, outf, default_flow_style=False)


if __name__ == '__main__':
    arguments = SpecGenerator._configure_console_parser() 
    publish_api_specs = SpecGenerator()
    publish_api_specs.get_spec(arguments.url)
    publish_api_specs.modify_config(arguments.title, arguments.description, arguments.server)
