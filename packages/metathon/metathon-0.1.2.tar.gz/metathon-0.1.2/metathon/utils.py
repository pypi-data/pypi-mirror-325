#!/usr/bin/env python3
import time
import uuid
import base64
import random
import string
import hashlib
import datetime
import requests

from typing import Union

def generate_uuid(heex: bool = False, seed: Union[str, dict] = None, upper: bool = False):
    if seed is not None:
        hash = hashlib.md5()
        hash.update(seed.encode('utf-8'))
        _uid = uuid.UUID(hash.hexdigest())
    else:
        _uid = uuid.uuid4()
    if heex: return str(_uid.hex).upper() if upper else str(_uid.hex)
    return str(_uid).upper() if upper else str(_uid)

def generate_nonce(seed: str = None):
    seed = seed if seed is not None else '12345'
    seed = base64.b64encode(hashlib.sha256(seed.encode('utf-8')).digest())
    return seed.decode('utf-8')

def generate_jazoest(seed: str = None):
    seed = seed if seed is not None else generate_android_id()
    return f'2{sum(ord(line) for line in seed)}'

def generate_android_id(device_id: uuid.UUID = None):
    device_id = device_id if device_id is not None else generate_device_id()
    seed = str(device_id).replace('-','')
    hash = hashlib.sha256(seed.encode())
    return 'android-' + hash.hexdigest()[:16]

def generate_machine_id(length: int = 28, with_char: bool = False):
    base_char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(base_char + '-_' if with_char else base_char) for _ in range(length))

def generate_device_id():
    return generate_uuid(False)

def generate_family_device_id(upper: bool = False):
    return generate_uuid(upper=upper)

def generate_pigeon_session_id():
    return 'UFS-' + generate_uuid(False) + '-' + random.choice(['0', str(random.randint(1,6))])

def generate_pigeon_raw_client_time():
    return str(round(time.time(), 3))

def generate_timestamp():
    return datetime.datetime.now().timestamp()

def generate_timestamp_to_datetime(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime('%Y-%m-%d %H:%M:%S')

def generate_wordlist(username: str = None, fullname: str = None, combolist: list = ['123','1234','12345'], shuffle: bool = False, capitalize: bool = False):
    wordlist = []
    digit = ''.join([str(line) for line in username if line.isdigit()])
    users = username.replace(digit,'').replace('.','').replace('_','')
    names = ''.join(line.lower() for line in fullname if line.isalpha() or line.isspace())
    if len(digit) > 0: combolist.append(digit)
    for combo in combolist:
        for name in names.split(' '):
            if len(name) > 3: wordlist.append(name + combo)
        wordlist.append(users.replace(' ','') + combo)
        wordlist.append(names.replace(' ','') + combo)
    wordlist = [word for word in wordlist if all(ord(line) < 128 for line in word)]
    wordlist = [word.replace(' ','') for word in wordlist if len(word) >= 8]
    wordlist = sorted(wordlist, key=len)
    if shuffle: random.shuffle(wordlist)
    if capitalize: wordlist = [line.capitalize() for line in wordlist]
    return wordlist