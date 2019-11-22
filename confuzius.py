import yaml


class Confuzius:
    configs = {
        'name': 'Confuzius',
        'prefix': 'Conf'
    }

    def getToken(self):
        return self.cfg['Discord']['Token']

    def firstLaunch(self, ymlfileStream):
        yaml.add_representer(type(None), self.represent_none)
        basic = {
            'DB-Settings': {
                'Username': None,
                'Password': None
            },
            'Discord':
                {'Token': None}
        }
        yaml.safe_dump(basic, ymlfileStream, default_flow_style=False)

    def represent_none(self, solf, _):
        return solf.represent_scalar('tag:yaml.org,2002:null', '')

    def __init__(self):
        try:
            with open("config.yml", 'r') as ymlfile:
                cfg = yaml.safe_load(ymlfile)
                # terminal.print(self.configs, 'Loaded Configuration File')
                print('Configuration File loaded')
        except FileNotFoundError as ex:
            # terminal.print(self.configs, 'Could not find Configuration File. Creating config.yml',
            # terminal.COLOR['YELLOW'])
            print('Could not find Configuration File. Creating config.yml')
            with open("config.yml", 'w+') as ymlfile:
                cfg = yaml.safe_load(ymlfile)
                self.firstLaunch(ymlfile)
        self.cfg = cfg


class configException(Exception):
    pass
