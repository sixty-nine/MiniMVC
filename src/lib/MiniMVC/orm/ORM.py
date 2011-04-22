from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ORM(object):

    def __init__(self, type, host, user, password, database):
        self.type = type
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.engine = create_engine('%s://%s:%s@%s/%s' % (type, user, password, host, database))

    def get_session(self):
        Session = sessionmaker(bind = self.engine)
        return Session()

    def __str__(self):
        return "MiniMVC.ORM(%s://%s@%s/%s)" % (self.type, self.user, self.host, self.database)
#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ORM(object):

    def __init__(self, type, host, user, password, database):
        self.type = type
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.engine = create_engine('%s://%s:%s@%s/%s' % (type, user, password, host, database))

    def get_session(self):
        Session = sessionmaker(bind = self.engine)
        return Session()

    def __str__(self):
        return "MiniMVC.ORM(%s://%s@%s/%s)" % (self.type, self.user, self.host, self.database)
