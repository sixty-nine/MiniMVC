from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ORM:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.engine = create_engine('mysql://%s:%s@%s/%s' % (user, password, host, database))

    def get_session(self):
        Session = sessionmaker(bind = self.engine)
        return Session()

    def __str__(self):
        return "MiniMVC.ORM(%s@%s/%s)" % (self.user, self.host, self.database)
