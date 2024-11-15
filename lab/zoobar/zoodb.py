from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
import os
from debug import *

PersonBase = declarative_base()
TransferBase = declarative_base()
CredBase = declarative_base()

class Person(PersonBase):
    __tablename__ = "person"
    username = Column(String(128), primary_key=True)
    zoobars = Column(Integer, nullable=False, default=10)
    profile = Column(String(5000), nullable=False, default="")

class Cred(CredBase):
    __tablename__ = "cred"
    username = Column(String(128), primary_key=True)
    password = Column(String(128))
    salt = Column(String(128))
    token = Column(String(128))

class Transfer(TransferBase):
    __tablename__ = "transfer"
    id = Column(Integer, primary_key=True)
    sender = Column(String(128))
    recipient = Column(String(128))
    amount = Column(Integer)
    time = Column(String)

def dbsetup(name, base):
    thisdir = os.path.dirname(os.path.abspath(__file__))
    dbdir   = os.path.join(thisdir, "db", name)
    if not os.path.exists(dbdir):
        os.makedirs(dbdir)

    dbfile  = os.path.join(dbdir, "%s.db" % name)
    engine  = create_engine('sqlite:///%s' % dbfile,
                            isolation_level='SERIALIZABLE')
    base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    return session()

def person_setup():
    return dbsetup("person", PersonBase)

def transfer_setup():
    return dbsetup("transfer", TransferBase)

def cred_setup():
    return dbsetup("cred", CredBase)

