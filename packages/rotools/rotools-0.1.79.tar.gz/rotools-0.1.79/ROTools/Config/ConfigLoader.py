import os

from ROTools.Config.Config import Config
from ROTools.Helpers.DictObj import DictObj


def _config_constructor(loader, node):
    fields = loader.construct_mapping(node, deep=True)
    for item in fields.items():
        if isinstance(item[1], dict):
            fields[item[0]] = DictObj(item[1])
    return Config(**fields)


def load_yaml( file_name, tag=None):
    import yaml
    yaml.add_constructor(tag, _config_constructor)

    with open(file_name, 'r') as file:
        content = file.read()
    return yaml.load(content, Loader=yaml.FullLoader)


class ConfigBuilder:
    def __init__(self, config_directory, config_file):
        files = os.listdir(config_directory)
        files = [a for a in files if not a.startswith("_")]
        files = [file for file in files if os.path.isfile(os.path.join(config_directory, file))]
        files = [os.path.join(config_directory, a) for a in files if a.endswith(('.yaml', '.yml'))]

        main_file_name = os.path.join(config_directory, config_file)
        if main_file_name not in files:
            raise Exception("Config file not found!")

        files = [a for a in files if a != main_file_name]

        self.config = load_yaml(main_file_name, tag='!Config')
        for file in files:
            sub_config = load_yaml(file, tag='!Config')
            for key, value in sub_config.items():
                self.config.set(key, value)


