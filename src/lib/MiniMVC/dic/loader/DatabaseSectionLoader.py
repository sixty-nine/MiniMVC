from MiniMVC.orm.ORM import ORM

class DatabaseSectionLoader(object):

    def load(self, container, name, config):
        
        if name != 'database':
            return False
        
        if not 'type' in config or not 'host' in config or not 'user' in config or not 'password' in config or not 'database' in config:
            return False
            
        orm = ORM(config['type'], config['host'], config['user'], config['password'], config['database'])
        container.set_param('sys.orm', orm)
        return True
