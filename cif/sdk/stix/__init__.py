__version__ = '0.0.0a0'

import time
from stix.indicator import Indicator
from stix.core import STIXPackage, STIXHeader
from cybox.common import Hash
from cybox.objects.file_object import File
from cybox.objects.address_object import Address
import re

import pprint
pp = pprint.PrettyPrinter()

class Stix(object):
    def __init__(self,description='unknown',*args,**kwargs):
        self._description = description
        
        stix_package = STIXPackage()
        stix_header = STIXHeader()
        stix_header.description = self._description
        stix_package.stix_header = stix_header
        
        self._handle = stix_package
        
    def create_indicator(self, keypair=None,*args,**kwargs):
        indicator = Indicator()
        indicator.set_producer_identity(keypair.get('provider'))
        indicator.set_produced_time(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(keypair.get('reporttime'))))
    
        indicator.description = ','.join(keypair.get('tags'))
        
        otype = keypair.get('otype')
    
        if otype == 'md5':
            f = _md5(keypair)
        elif otype == 'sha1':
            f = _sha1(keypair)
        elif otype == 'sha256':
            f = _sha256(keypair)
        else:
            f = _address(keypair)
            
        indicator.add_object(f)
        
        return indicator
    
    def to_xml(self):
        return self._handle.to_xml()
        
    def _md5(self,keypair):
        shv = Hash()
        shv.simple_hash_value = keypair.get('observable')
        
        f = File()
        h = Hash(shv, Hash.TYPE_MD5)
        f.add_hash(h)
        return f
        
    def _sha1(self,keypair):
        shv = Hash()
        shv.simple_hash_value = keypair.get('observable')
        
        f = File()
        h = Hash(shv, Hash.TYPE_SHA1)
        f.add_hash(h)
        return f
    
    def _sha256(self,keypair):
        shv = Hash()
        shv.simple_hash_value = keypair.get('observable')
        
        f = File()
        h = Hash(shv, Hash.TYPE_SHA256)
        f.add_hash(h)
        return f
    
    def _address(self,keypair):
        address = keypair.get('observable')
        if _address_fqdn(address):
            return Address(address,'fqdn')
        elif _address_ipv4(address):
            return Address(address,'ipv4-addr')
        elif _address_url(address):
            return Address(address,'url')
    
    def _address_ipv4(self,address):
        if re.search('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}',address):
            return 1  
    
    def _address_fqdn(self,address):
        if re.search('^[a-zA-Z0-9.\-_]+\.[a-z]{2,6}$',address):
            return 1
    
    def _address_url(self,address):
        if re.search('^(ftp|https?):\/\/',address):
            return 1