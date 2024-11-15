import rpclib
import sys
import os

from zoodb import *
from debug import *

import hashlib
import secrets

sys.path.append(os.getcwd())
import readconf

def newtoken(db, person):
    hashinput = "%s.%s" % (secrets.token_bytes(16), person.password)
    person.token = hashlib.sha256(hashinput.encode('utf-8')).hexdigest()
    db.commit()
    return person.token

@catch_err
def login(username, password):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('login', username=username, password=password)
    return ret

@catch_err
def register(username, password):
    # Registrar Persona local
    db = person_setup()
    person = db.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username
    #newperson.password = password
    db.add(newperson)
    db.commit()
    # RPC a AUTH
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('register', username=username, password=password)
    return ret

@catch_err
def check_token(username, token):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('check_token', username=username, token=token)
    return ret
