#!/usr/bin/python

'''
KakaoTalk PC-style Login PoC

Author: Brian Pak (bpak.org)

'''

import requests
import json
import urllib2
import sys

# Fill these in before you use it
EMAIL = ''
PASSWORD = ''
COMP_NAME = ''
ONCE = 'false'
DUUID = ''

LOGIN_URL = 'https://sb-talk.kakao.com/win32/account/login.json'
SETTINGS_URL = 'https://sb-talk.kakao.com/win32/account/more_settings.json?since=0&lang=en'
BLOCKED_URL = 'https://sb-talk.kakao.com/win32/friends/blocked.json?'
UPDATE_URL = 'https://sb-talk.kakao.com/win32/friends/update.json'

headers = {'User-Agent': 'KakaoTalk Win32 1.0.3',
           'Host': 'sb-talk.kakao.com',
           'A': 'win32/1.0.3/en',
           'Content-Type': 'application/x-www-form-urlencoded',
           }

data = {'email': EMAIL,
        'password': PASSWORD,
        'device_uuid': DUUID,
        'model': '',
        'name': COMP_NAME}


def login_step1():
    r = requests.post(LOGIN_URL, data=data, headers=headers)
    j = json.loads(r.text)
    if j['status'] != -100:
        print
        'Error in step 1'
        sys.exit()
    else:
        print
        'Step 1 Success!'


def login_step2():
    data['once'] = ONCE
    r = requests.post(LOGIN_URL, data=data, headers=headers)
    j = json.loads(r.text)
    if j['status'] != 0:
        print
        'Error in step 2'
        sys.exit()
    else:
        print
        'Step 2 Success!'


def login_step3():
    data['forced'] = 'false'
    data['passcode'] = raw_input('passcode? => ')
    r = requests.post(LOGIN_URL, data=data, headers=headers)
    j = json.loads(r.text)
    if j['status'] != 0:
        print
        'Error in step 3'
        sys.exit()
    else:
        print
        'Step 3 Success!'
        print
        'Got sessionKey: %s' % j['sessionKey']
        print
        'Device UUID: %s' % DUUID
        headers['S'] = '%s-%s' % (j['sessionKey'], DUUID)


def get_settings():
    r = requests.get(SETTINGS_URL, headers=headers)
    print
    r.text


def get_blocked():
    r = requests.get(BLOCKED_URL, headers=headers)
    print
    r.text


def get_update():
    update_data = {'contacts': '[]',
                   'removed': '[]',
                   'phone_number_type': 1,
                   'token': 0,
                   'type': 'f'}
    r = requests.post(UPDATE_URL, data=update_data, headers=headers)
    print
    r.text


# main
login_step1()
login_step2()
login_step3()
get_settings()
get_blocked()
get_update()
