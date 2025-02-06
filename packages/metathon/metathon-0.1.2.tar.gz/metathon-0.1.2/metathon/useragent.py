#!/usr/bin/env python3
import random
from .device import Device, DEVICE_LIST, COUNTRY_LIST
from .constants import (
    THREADS,
    FACEBOOK,
    INSTAGRAM
    )

class UserAgent:

    def get_chrome_version(self):
        return str(random.randint(80,112)) + '.0.' + str(random.randint(2024,3058)) + '.0' + str(random.randint(10,99))
    
    def get_threads_version(self):
        return random.choice(THREADS)
    
    def get_facebook_version(self):
        return random.choice(FACEBOOK)
    
    def get_instagram_version(self):
        return random.choice(INSTAGRAM)
    
    def dalvik(self, device_brand: str = None, device_model: str = None, device_build: str = None, device_version: str = None, **kwargs):
        device_brand = device_brand if device_brand is not None else random.choice(DEVICE_LIST)
        device = Device(device_brand).get_device_info()
        device_build = device_build if device_build is not None else device['device_build']
        device_model = device_model if device_model is not None else device['device_model']
        device_version = device_version if device_version is not None else device['device_version']
        return f'Dalvik/2.1.0 (Linux; U; Android {device_version}; {device_model} Build/{device_build})'
    
    def chrome(self, device_brand: str = None, device_model: str = None, device_build: str = None, device_version: str = None, chrome_version: str = None, webview: bool = False, **kwargs):
        device_brand = device_brand if device_brand is not None else random.choice(DEVICE_LIST)
        device = Device(device_brand).get_device_info()
        device_build = device_build if device_build is not None else device['device_build']
        device_model = device_model if device_model is not None else device['device_model']
        device_version = device_version if device_version is not None else device['device_version']
        chrome_version = chrome_version if chrome_version is not None else self.get_chrome_version()
        return f'Mozilla/5.0 (Linux; Android {device_version}; {device_model} Build/{device_build}{"; wv" if webview else ""}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
    
    def threads(self, device_brand: str = None, device_model: str = None, device_board: str = None, device_vendor: str = None, device_version: str = None, device_language: str = None, device_sdk: str = None, device_dpi: str = None, threads_code: str = None, threads_version: str = None, **kwargs):
        device_brand = device_brand if device_brand is not None else random.choice(DEVICE_LIST)
        device = Device(device_brand).get_device_info()
        device_model = device_model if device_model is not None else device['device_model']
        device_board = device_board if device_board is not None else device['device_board']
        device_vendor = device_vendor if device_vendor is not None else device['device_vendor']
        device_version = device_version if device_version is not None else device['device_version']
        device_language = device_language if device_language is not None else device['device_language']
        device_dpi = device_dpi if device_dpi is not None else device['device_dpi']
        device_sdk = device_sdk if device_sdk is not None else device['device_sdk']
        threads = self.get_threads_version()
        threads_code = threads_code if threads_code is not None else threads['code']
        threads_version = threads_version if threads_version is not None else threads['version']
        return f'Barcelona {threads_version} Android ({device_sdk}/{device_version}; {device_dpi}; {device_brand}; {device_model}; {device_board}; {device_vendor}; {device_language}; {threads_code})'
    
    def facebook(self, device_brand: str = None, device_model: str = None, device_version: str = None, device_language: str = None, device_armeabi: str = None, device_density: str = None, device_operator: str = None, facebook_code: str = None, facebook_version: str = None, facebook_package: str = None, dalvik: bool = False, **kwargs):
        device_brand = device_brand if device_brand is not None else random.choice(DEVICE_LIST)
        device = Device(device_brand).get_device_info()
        device_model = device_model if device_model is not None else device['device_model']
        device_version = device_version if device_version is not None else device['device_version']
        device_language = device_language if device_language is not None else device['device_language']
        device_armeabi = device_armeabi if device_armeabi is not None else device['device_armeabi']
        device_density = device_density if device_density is not None else device['device_density']
        device_operator = device_operator if device_operator is not None else device['device_operator']
        facebook = self.get_facebook_version()
        facebook_code = facebook_code if facebook_code is not None else facebook['code']
        facebook_version = facebook_version if facebook_version is not None else facebook['version']
        facebook_package = facebook_package if facebook_package is not None else 'com.facebook.katana'
        facebook_user_agent = f'[FBAN/FB4A;FBAV/{facebook_version};FBBV/{facebook_code};FBDM/{device_density};FBLC/{device_language};FBRV/0;FBCR/{device_operator};FBMF/{device_brand};FBBD/{device_brand};FBPN/{facebook_package};FBDV/{device_model};FBSV/{device_version};FBOP/1;FBCA/{device_armeabi}:;]'
        return self.dalvik(device_brand=device_brand, device_build=device['device_build'], device_model=device['device_model'], device_version=device['device_version']) + ' ' + facebook_user_agent if dalvik else facebook_user_agent
    
    def instagram(self, device_brand: str = None, device_model: str = None, device_board: str = None, device_vendor: str = None, device_version: str = None, device_language: str = None, device_sdk: str = None, device_dpi: str = None, instagram_code: str = None, instagram_version: str = None, **kwargs):
        device_brand = device_brand if device_brand is not None else random.choice(DEVICE_LIST)
        device = Device(device_brand).get_device_info()
        device_model = device_model if device_model is not None else device['device_model']
        device_board = device_board if device_board is not None else device['device_board']
        device_vendor = device_vendor if device_vendor is not None else device['device_vendor']
        device_version = device_version if device_version is not None else device['device_version']
        device_language = device_language if device_language is not None else device['device_language']
        device_dpi = device_dpi if device_dpi is not None else device['device_dpi']
        device_sdk = device_sdk if device_sdk is not None else device['device_sdk']
        instagram = self.get_instagram_version()
        instagram_code = instagram_code if instagram_code is not None else instagram['code']
        instagram_version = instagram_version if instagram_version is not None else instagram['version']
        return f'Instagram {instagram_version} Android ({device_sdk}/{device_version}; {device_dpi}; {device_brand}; {device_model}; {device_board}; {device_vendor}; {device_language}; {instagram_code})'