# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import logging, os
from uuid import uuid4
from getpass import getpass
from binascii import hexlify, unhexlify

# M2Crypto
from M2Crypto import RSA, BIO

class CryptoManager(object):
    """ Responsible for management of the server's crypto material.
    """
    def __init__(self, priv_key_location=None, pub_key_location=None):
        super(CryptoManager, self).__init__()
        self.priv_key_location = priv_key_location
        self.pub_key_location = pub_key_location
        self.priv_key = None
        self.pub_key = None
        self.logger = logging.getLogger("%s.%s" % (__name__, self.__class__.__name__))

    def decrypt(self, data, padding=RSA.pkcs1_padding, hexlified=True):
        """ Decrypts data using the private config key. Padding used defaults
        to PKCS#1. hexlified defaults to True and indicates whether the data
        should be hex-decoded before being decrypted.
        """
        if hexlified:
            data = unhexlify(data)

        return self.priv_key.private_decrypt(data, padding).replace("\x00", "")

    def encrypt(self, data, padding=RSA.pkcs1_padding, hexlified=True):
        """ Encrypts data using the public config key. Padding used defaults
        to PKCS#1. hexlified defaults to True and indicates whether the data
        should be hex-encoded after being encrypted.
        """
        hexlified = self.pub_key.public_encrypt(data, padding)
        if base64:
            encrypted = hexlify(encrypted)

        return encrypted