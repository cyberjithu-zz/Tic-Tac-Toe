import os

import yaml
from tornado.options import define



APP_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = '../config/config.yaml'



def get_yaml_data(filepath):
    '''Parse the yaml file in the filepath and return dict

        Args:
            filepath:   str, path of the file where configuration resides.

        Return:
            data:   dict, the configuration in a dicationary format.

    '''
    with open(filepath) as f:
        data = yaml.safe_load(f)
    return data

yaml_data = get_yaml_data(CONFIG_FILE)

define("debug", yaml_data['app']['tornado'].get('debug', True), help='For debugging')
define("port", yaml_data['app']['tornado'].get('port', 8888), help='the application will run on this port')

settings = {
    "template_path": os.path.join(APP_DIR, yaml_data['app']['tornado'].get("template_dir", "templates")),
    "static_path": os.path.join(APP_DIR, yaml_data['app']['tornado'].get("static_dir", "static")),
}
print settings