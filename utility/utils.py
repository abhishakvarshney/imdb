# -*- coding: utf-8 -*-
from django.conf import settings
import json
# import requests
import re
import sys
import traceback
from Crypto.Cipher import AES
import base64
from utility.log import log
from datetime import datetime
# from dateutil.relativedelta import relativedelta
import uuid
# import dateutil.parser
import time
import os


class GeneralUtils:
    DB_VALUE_DEFAULT = None

    @classmethod
    def encryptData(cls, text):
        """

        @param text:
        @return:
        """
        message = text
        paddingChar = '_'
        obj = AES.new('This_is_a_trackr', AES.MODE_CBC, 'This_is_atracker')
        for i in range(16 - len(text) % 16):
            message += paddingChar
        try:
            cipherText = obj.encrypt(message)
        except:
            cipherText = message
        cipherText = base64.b64encode(cipherText)
        return cipherText.decode('utf-8')


    @classmethod
    def decryptData(cls, text):
        """

        @param text:
        @return:
        """
        text = base64.b64decode(text)
        obj2 = AES.new('This_is_a_trackr', AES.MODE_CBC, 'This_is_atracker')
        try:
            message = obj2.decrypt(text).decode('utf-8')
        except:
            message = ' '
        while True:
            if len(message) > 0 and message[-1] == '_':
                message = message[:-1]
            else:
                break
        return message

