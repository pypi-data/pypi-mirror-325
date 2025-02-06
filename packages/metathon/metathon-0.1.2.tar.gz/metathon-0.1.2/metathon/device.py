#!/usr/bin/env python3
import random

from .constants import (
    DEVICE,
    DEVICE_LIST,
    COUNTRY,
    COUNTRY_LIST
    )

class DeviceNotFound(Exception):
    def __init__(self, message):
        self.message = message + ' not found ! to check what device are available use: metathon.device.DEVICE_LIST'
        super().__init__(self.message)

class CountryNotFound(Exception):
    def __init__(self, message):
        self.message = message + ' not found ! to check what country are available use: metathon.device.COUNTRY_LIST'
        super().__init__(self.message)

class Device:
    
    def __init__(
            self,
            device_brand: str = None,
            device_country: str = None
        ):
        self.device_brand = device_brand if device_brand is not None else random.choice(DEVICE_LIST)
        self.device_country = device_country if device_country is not None else random.choice(COUNTRY_LIST)
        
    def get_dpi(self):
        return random.choice(['480dpi; 1080x2400','480dpi; 720x1600','480dpi; 720x1560','480dpi; 1080x2376','480dpi; 1080x2404','480dpi; 1080x2408','320dpi; 1080x2340','560dpi; 1440x3040','560dpi; 1440x3088','560dpi; 1080x2400','320dpi; 1600x2560','320dpi; 720x1568','560dpi; 1440x2560','480dpi; 1344x2772'])
    
    def get_build(self):
        return '{}.{}'.format(random.choice(['SP1A','QP1A','RP1A','TP1A','RKQ1','SKQ1']), str(random.randint(200999,220905)) + '.0{}'.format(random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16'])))
    
    def get_armeabi(self):
        return random.choice(['arm64-v8a','armeabi-v8a:armeabi','armeabi-v7a:armeabi','x86_64:x86:x86_64','x86_64:arm64-v8a:x86_64'])
    
    def get_density(self):
        return random.choice(['{density=3.0,width=1080,height=2068}','{density=3.0,width=1080,height=1920}','{density=2.3,width=2149,height=1117}','{density=1.0,width=2060,height=1078}','{density=1.8,width=1582,height=558}','{density=3.0,width=1080,height=1920}','{density=2.0,width=720,height=1193}','{density=2.1,width=1814,height=1023}'])
    
    def get_device_info(self):
        if self.device_brand.upper() in DEVICE_LIST:
            if self.device_country.upper() in COUNTRY_LIST:
                d = random.choice(DEVICE[self.device_brand.upper()])
                c = COUNTRY[self.device_country.upper()]
                return {
                    'device_brand': self.device_brand.capitalize(),
                    'device_model': d['model'],
                    'device_board': d['board'],
                    'device_build': self.get_build(),
                    'device_vendor': d['vendor'],
                    'device_version': d['version'],
                    'device_armeabi': self.get_armeabi(),
                    'device_density': self.get_density(),
                    'device_dpi': self.get_dpi(),
                    'device_sdk': str(19 + int(d['version'])),
                    'device_number': c['number'],
                    'device_country': self.device_country,
                    'device_language': c['language'],
                    'device_operator': random.choice(c['operator'])
                }
            raise CountryNotFound(self.device_country)
        raise DeviceNotFound(self.device_brand)

