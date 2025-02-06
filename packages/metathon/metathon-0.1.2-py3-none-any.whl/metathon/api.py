#!/usr/bin/env python3
import os
import re
import hmac
import json
import time
import uuid
import base64
import random
import string
import hashlib
import requests
import datetime
import urllib.parse

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.Random import get_random_bytes

from .utils import (
    generate_uuid,
    generate_device_id,
    generate_android_id,
    generate_machine_id,
    generate_timestamp,
    generate_timestamp_to_datetime
)
    
from .device import Device
from .useragent import UserAgent

useragent = UserAgent()

class CookieError(Exception):
    def __init__(self, message: str = None):
        if message is None: message = 'cookie is not valid or have been expired please check your account on instagram app or browsers'
        super().__init__(message)

class Instagram:
    
    web = 'https://www.instagram.com'
    api = 'https://i.instagram.com/api/v1'
    
    def __init__(
            self,
            cookie: str = None,
            device: dict = None,
            device_id: str = None,
            csrftoken: str = None,
            machine_id: str = None,
            user_agent: str = None,
            session: requests.Session = None,
            locale: str = 'ID'
        ):
        
        if cookie is None:
            raise CookieError(
                'cookie cannot be empty '
                'require instagram cookie to access instagram private-api'
            )
        if cookie is not None:
            try: user_id = str(re.search('ds_user_id=(.*?);', cookie).group(1))
            except: raise CookieError(
                'cookie is not valid '
                'cannot find ds_user_id in this cookie'
            )
        
        if device is None:
            d = Device(device_country=locale)
            device = d.get_device_info()
        if device_id is None:
            if 'ig_did' in cookie: device_id = str(uuid.UUID(re.search('ig_did=(.*?);', cookie).group(1)))
            else: device_id = generate_device_id()
        if csrftoken is None:
            if 'csrftoken' in cookie: csrftoken = re.search('csrftoken=(.*?);', cookie).group(1)
            else: csrftoken = generate_machine_id(32)
        if machine_id is None:
            if 'mid' in cookie: mid = re.search('mid=(.*?);', cookie).group(1)
            else: mid = generate_machine_id()
        if user_agent is None: user_agent = useragent.instagram(**device)
        if session is None: session = requests.Session()
        
        self.cookie = cookie
        self.bearer = self.bearer_token_encoder(cookie)
        self.device = device
        self.user_id = user_id
        self.device_id = device_id
        self.csrftoken = csrftoken
        self.machine_id = mid
        self.android_id = generate_android_id(device_id)
        self.user_agent = user_agent
        
        self.session = session
        self.session.cookies.update({'cookie': self.cookie})
        self.session.headers.update({
            'Host': 'i.instagram.com',
            'Authorization': self.bearer,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': '{}, en-US'.format(self.device.get('device_language').replace('_','-')),
            'X-Ig-App-Id': '567067343352427',
            'X-Ig-Device-ID': self.device_id,
            'X-Ig-Android-ID': self.android_id,
            'X-Ig-Connection-Type': 'MOBILE(LTE)',
            'X-Fb-Connection-Type': 'MOBILE.LTE',
            'X-Fb-Http-Engine': 'Liger',
            'X-MID': self.machine_id,
            'User-Agent': self.user_agent
        })
    
    def download(self, url: str = None, name: str = None, path: str = None):
        if not path or not os.path.isdir(path): path = '.'
        filepath = os.path.join(path, name)
        with requests.get(url, stream=True) as session:
            session.raise_for_status()
            with open(filepath, 'wb') as files:
                for chunk in session.iter_content(chunk_size=8192): 
                    files.write(chunk)
        if os.path.isfile(filepath): return filepath
        else: return False
    
    def signature(self, data: dict = None, ig_sig_key: str = 'SIGNATURE', ig_sig_key_version: str = None):
        if ig_sig_key.isdigit():
            return {
                'signed_body': hmac.new(ig_sig_key.encode('utf-8'), json.dumps(data).encode('utf-8'), hashlib.sha256).hexdigest() + '.' + json.dumps(data),
                'ig_sig_key_version': ig_sig_key_version
            }
        else:
            if ig_sig_key_version is not None:
                return {
                    'signed_body': ig_sig_key + '.' + json.dumps(data),
                    'ig_sig_key_version': ig_sig_key_version
                }
            return {
                'signed_body': ig_sig_key + '.' + json.dumps(data)
            }
    
    def cookie_string(self, cookie: dict = None):
        if not 'mid' in cookie: cookie['mid'] = self.machine_id
        if not 'ig_did' in cookie: cookie['ig_did'] = self.device_id.upper()
        return '; '.join([key + '=' + value for key, value in cookie.items()]) if cookie is not None else ''
    
    def bearer_token_encoder(self, cookie: str = None):
        try: return 'Bearer IGT:2:{}'.format(base64.b64encode(str({'ds_user_id': re.search('ds_user_id=(.*?);', str(cookie)).group(1), 'sessionid': re.search('sessionid=(.*?);', str(cookie) + ';').group(1), 'should_use_header_over_cookies': True}).replace("'",'"').replace('True','true').replace(' ','').encode('ascii')).decode('ascii'))
        except: return None
    
    def bearer_token_decoder(self, bearer: str = None):
        cookie = json.loads(base64.urlsafe_b64decode(bearer.split(':')[-1]).decode('utf-8'))
        try: cookie.pop('should_use_header_over_cookies')
        except: pass
        return self.cookie_string(cookie)
    
    def encrypt_password(self, password: str = None, timestamp: str = None, version: str = '4', key_id: int = None, public_key: str = None):
        session_key = get_random_bytes(32)
        iv = get_random_bytes(12)
        key_id = key_id or 41
        timestamp = timestamp if timestamp is not None else str(generate_timestamp())
        recipient_key = RSA.import_key(public_key if public_key is not None else '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvcu1KMDR1vzuBr9iYKW8\nKWmhT8CVUBRkchiO8861H7zIOYRwkQrkeHA+0mkBo3Ly1PiLXDkbKQZyeqZbspke\n4e7WgFNwT23jHfRMV/cNPxjPEy4kxNEbzLET6GlWepGdXFhzHfnS1PinGQzj0ZOU\nZM3pQjgGRL9fAf8brt1ewhQ5XtpvKFdPyQq5BkeFEDKoInDsC/yKDWRAx2twgPFr\nCYUzAB8/yXuL30ErTHT79bt3yTnv1fRtE19tROIlBuqruwSBk9gGq/LuvSECgsl5\nz4VcpHXhgZt6MhrAj6y9vAAxO2RVrt0Mq4OY4HgyYz9Wlr1vAxXXGAAYIvrhAYLP\n7QIDAQAB\n-----END PUBLIC KEY-----\n')
        cipher_rsa = PKCS1_v1_5.new(recipient_key)
        rsa_encrypted = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
        cipher_aes.update(timestamp.encode())
        aes_encrypted, tag = cipher_aes.encrypt_and_digest(password.encode('utf-8'))
        size_buffer = len(rsa_encrypted).to_bytes(2, byteorder='little')
        payload = base64.b64encode(b''.join([b'\x01',key_id.to_bytes(1, byteorder='big'),iv,size_buffer,rsa_encrypted,tag,aes_encrypted]))
        return f'#PWD_INSTAGRAM:{version}:{timestamp[:10]}:{payload.decode()}'
    
    def account(self):
        try:
            user = self.session.get(self.api + f'/users/{self.user_id}/info/').json()['user']
            info = {'id': user['pk_id'], 'email': '', 'phone': '', 'private': user['is_private'], 'verified': user['is_verified'], 'username': user['username'], 'fullname': user['full_name'], 'birthday': '', 'followers': str(user['follower_count']), 'following': str(user['following_count']), 'mediapost': str(user['media_count']), 'biography': user['biography'], 'pictures': user['hd_profile_pic_url_info']['url']}
            user = self.session.get(self.api + '/accounts/current_user/?edit=true').json()['user']
            info['email'] = user['email'] or ''
            info['phone'] = user['phone_number'] or ''
            info['birthday'] = user['birthday'] or ''
            return info
        except:
            return False
    
    def username_info(self, username: str = None):
        try:
            user = self.session.get(self.api + f'/users/{username}/usernameinfo/').json()['user']
            info = {'id': user['pk_id'], 'private': user['is_private'], 'verified': user['is_verified'], 'username': user['username'], 'fullname': user['full_name'], 'followers': str(user['follower_count']), 'following': str(user['following_count']), 'mediapost': str(user['media_count']), 'biography': user['biography'], 'pictures': user['hd_profile_pic_url_info']['url']}
            return info
        except:
            return False
    
    def followers(self, username: str = None):
        if not username.isdigit(): id = self.username_info(username=username)['id']
        else: id = username
        end_cursor = None
        has_next_page = True
        while has_next_page:
            try:
                response = self.session.get(self.web + '/graphql/query/', params={'query_hash': 'c76146de99bb02f6415203be841dd25a', 'id': id, 'first': 100, 'after': end_cursor}).json()
                has_next_page = response['data']['user']['edge_followed_by']['page_info']['has_next_page']
                for user in response['data']['user']['edge_followed_by']['edges']:
                    try:
                        data = {'id': user['node']['id'], 'username': user['node']['username'], 'fullname': user['node']['full_name']}
                        yield data
                    except (requests.exceptions.JSONDecodeError, json.decoder.JSONDecodeError): continue
                if has_next_page: end_cursor = response['data']['user']['edge_followed_by']['page_info']['end_cursor']
            except: break
    
    def following(self, username: str = None):
        if not username.isdigit(): id = self.username_info(username=username)['id']
        else: id = username
        end_cursor = None
        has_next_page = True
        while has_next_page:
            try:
                response = self.session.get(self.web + '/graphql/query/', params={'query_hash': 'd04b0a864b4b54837c0d870b0e77e076', 'id': id, 'first': 100, 'after': end_cursor}).json()
                has_next_page = response['data']['user']['edge_follow']['page_info']['has_next_page']
                for user in response['data']['user']['edge_follow']['edges']:
                    try:
                        data = {'id': user['node']['id'], 'username': user['node']['username'], 'fullname': user['node']['full_name']}
                        yield data
                    except (requests.exceptions.JSONDecodeError, json.decoder.JSONDecodeError): continue
                if has_next_page: end_cursor = response['data']['user']['edge_follow']['page_info']['end_cursor']
            except: break
    
    def media_id(self, url: str = None):
        try:
            media = 0
            base_char = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-_'
            if '/p/' in url: code = re.search(r"/p/([A-Za-z0-9_-]+)/\?", url).group(1)
            elif '/reel/' in url: code = re.search(r"/reel/([A-Za-z0-9_-]+)/\?", url).group(1)
            elif '/story/' in url: code = re.search(r"/story/([A-Za-z0-9_-]+)/\?", url).group(1)
            else: code = ''
            for line in code: media = (media * 64) + base_char.index(line)
            return media
        except:
            return False
    
    def media_info(self, url: str = None):
        try:
            if not url.isdigit(): media_id = self.media_id(url)
            else: media_id = url
            media = []
            media_type = lambda x: 'image' if x == 1 else ('video' if x == 2 else 'carousel')
            items = self.session.get(self.api + f'/media/{media_id}/info/').json()['items']
            for line in items:
                try: caption = line['caption']['text']
                except: caption = ''
                try: id = line['caption']['user']['id']
                except: id = ''
                try: username = line['caption']['user']['username']
                except: username = ''
                try: fullname = line['caption']['user']['full_name']
                except: fullname = ''
                try: has_more_comments = line['has_more_comments']
                except: has_more_comments = False
                try:
                    if media_type(line['media_type']) == 'image':
                        media_url = line['image_versions2']['candidates'][0]['url']
                        media_name = re.search(r'([^/]+\.(jpg|png))', media_url).group(1)
                        media.append({'url': media_url, 'name': media_name})
                    elif media_type(line['media_type']) == 'video':
                        media_url = line['video_versions'][0]['url']
                        media_name = re.search(r'([^/]+\.(mp4))', media_url).group(1)
                        media.append({'url': media_url, 'name': media_name})
                    elif media_type(line['media_type']) == 'carousel':
                        for lines in line['carousel_media']:
                            if media_type(lines['media_type']) == 'image':
                                media_url = lines['image_versions2']['candidates'][0]['url']
                                media_name = re.search(r'([^/]+\.(jpg|png))', media_url).group(1)
                                media.append({'url': media_url, 'name': media_name})
                            elif media_type(lines['media_type']) == 'video': 
                                media_url = lines['video_versions'][0]['url']
                                media_name = re.search(r'([^/]+\.(mp4))', media_url).group(1)
                                media.append({'url': media_url, 'name': media_name})
                except: pass
                return {
                    'id': id,
                    'username': username,
                    'fullname': fullname,
                    'taken_at': generate_timestamp_to_datetime(line['taken_at']),
                    'like': str(line['like_count']),
                    'liked': line['has_liked'],
                    'comment': str(line['comment_count']),
                    'caption': caption,
                    'can_save': line['can_viewer_save'],
                    'can_share': line['can_viewer_reshare'],
                    'can_comment': has_more_comments,
                    'media_id': line['id'],
                    'media_type': media_type(line['media_type']),
                    'media_code': line['code'],
                    'media': media}
        except:
            return False
    
    def upload_id(self, file: str = None, cookie: dict = None, headers: dict = None):
        if not os.path.isfile(file): raise FileNotFoundError(file)
        upload_id = str(int(time.time()) * 1000)
        entity_name = '{}_0_{}'.format(upload_id, random.randint(1000000000, 9999999999))
        params = {'retry_context':'{"num_step_auto_retry": 0, "num_reupload": 0, "num_step_manual_retry": 0}"','media_type':'1','xsharing_user_ids':'[]','upload_id': upload_id,'image_compression':json.dumps({'lib_name':'moz','lib_version':'3.1.m','quality': 80})}
        with open(file,'rb') as f:
            file_data = f.read()
            file_size = str(len(file_data))
        session = requests.Session()
        session.cookies.update(cookie)
        session.headers.update(headers)
        session.headers.update({'Accept-Encoding':'gzip','X-Instagram-Rupload-Params':json.dumps(params),'X_FB_PHOTO_WATERFALL_ID':generate_uuid(),'X-Entity-Type':'image/jpeg','Offset':'0','X-Entity-Name':entity_name,'X-Entity-Length':file_size,'Content-Type':'application/octet-stream','Content-Length':file_size})
        upload_id = session.post('https://i.instagram.com/rupload_igphoto/{}'.format(entity_name), data=file_data).json()['upload_id']
        return upload_id
    
    def change_biography(self, text: str = None):
        try:
            response = self.session.post(
                self.api + '/accounts/set_biography/',
                data = {
                    'logged_in_uids': self.user_id,
                    'device_id': self.device_id,
                    '__uuid': generate_uuid(),
                    'raw_text': text,
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def change_profile_picture(self, file: str = None):
        try:
            if not os.path.isfile(file): raise FileNotFoundError(file)
            upload_id = self.upload_id(file=file, cookie=self.session.cookies.get_dict().copy(), headers=self.session.headers.copy())
            response = self.session.post(
                self.api + '/accounts/change_profile_picture/',
                data = {
                    '_uuid': generate_uuid(),
                    'use_fbuploader': False,
                    'remove_birthday_selfie': False,
                    'upload_id': upload_id
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def remove_profile_picture(self):
        try:
            response = self.session.post(
                self.api + '/accounts/remove_profile_picture/',
                data = {
                    '_uuid': generate_uuid(),
                    'use_fbuploader': False,
                    'remove_birthday_selfie': False,
                    'upload_id': None
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def change_to_public(self):
        try:
            response = self.session.post(self.api + '/accounts/set_public/').json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def change_to_private(self):
        try:
            response = self.session.post(self.api + '/accounts/set_private/').json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def change_password(self, old_password: str = None, new_password: str = None):
        try:
            enc_old_password = self.encrypt_password(old_password)
            enc_new_password = self.encrypt_password(new_password)
            response = self.session.post(
                self.api + '/accounts/change_password/',
                data = {
                    '_uid': self.user_id,
                    '_uuid': self.device_id,
                    '_csrftoken': self.csrftoken,
                    'enc_old_password': enc_old_password,
                    'enc_new_password1': enc_new_password,
                    'enc_new_password2': enc_new_password
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def like(self, url: str = None):
        try:
            if not url.isdigit(): media_id = self.media_id(url)
            else: media_id = url
            response = self.session.post(
                self.api + f'/media/{media_id}/like/',
                data = {
                    'media_id': media_id
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def unlike(self, url: str = None):
        try:
            if not url.isdigit(): media_id = self.media_id(url)
            else: media_id = url
            response = self.session.post(
                self.api + f'/media/{media_id}/unlike/',
                data = {
                    'media_id': media_id
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def block(self, username: str = None):
        try:
            if not username.isdigit(): id = self.username_info(username=username)['id']
            else: id = username
            response = self.session.post(
                self.api + f'/friendships/block/{id}/',
                data = {
                    'surface': 'profile',
                    'is_auto_block_enabled': 'true',
                    'user_id':id,
                    '_uid': self.user_id,
                    '__uuid': self.device_id,
                    'container_module': 'profile'
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def unblock(self, username: str = None):
        try:
            if not username.isdigit(): id = self.username_info(username=username)['id']
            else: id = username
            response = self.session.post(
                self.api + f'/friendships/unblock/{id}/',
                data = {
                    'user_id': id,
                    '_uid': self.user_id,
                    '__uuid': self.device_id,
                    'container_module': 'search_typeahead'
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def follow(self, username: str = None):
        try:
            if not username.isdigit(): id = self.username_info(username=username)['id']
            else: id = username
            response = self.session.post(
                self.api + f'/friendships/create/{id}/',
                data = {
                    'user_id': id
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def unfollow(self, username: str = None):
        try:
            if not username.isdigit(): id = self.username_info(username=username)['id']
            else: id = username
            response = self.session.post(
                self.api + f'/friendships/destroy/{id}/',
                data = {
                    'user_id': id
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def comment(self, url: str = None, text: str = None):
        try:
            if not url.isdigit(): media_id = self.media_id(url)
            else: media_id = url
            text = text if text is not None else random.choice(['Nice post! 👍', 'Good work bro! 💯', 'Alatnya bagus banget, gw suka! 😍', 'Gw kira boongan, ternyata work cuy! 🔥', 'Mantap banget ini alat! 👏', 'Keren banget, auto recommend! 🚀', 'Wih, ini beneran ngebantu banget! 🙌', 'Nice banget, langsung work! 😎', 'Good job! Alatnya oke punya! 💪', 'Ini alat beneran nggak ngecewain! 😁', 'Wah, keren banget! Auto save! 📂', 'Nice, langsung coba dan puas! 😄', 'Alatnya simpel tapi powerful! 💥', 'Gw suka banget sama ini! 👍', 'Ini beneran worth it, cuy! 💸', 'Good work, alatnya beneran ngebantu! 🙏', 'Wih, langsung work tanpa ribet! 🎉', 'Nice post, beneran informatif! 📚', 'Alatnya beneran bagus, gw puas! 😊', 'Keren banget, auto jadi favorit! ⭐', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 💯', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪', 'Nice post, langsung coba dan puas! 😄', 'Alatnya beneran simpel tapi powerful! 💥', 'Gw suka banget sama ini, beneran worth it! 💸', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 🙏', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪', 'Nice post, langsung coba dan puas! 😄', 'Alatnya beneran simpel tapi powerful! 💥', 'Gw suka banget sama ini, beneran worth it! 💸', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 🙏', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪', 'Nice post, langsung coba dan puas! 😄', 'Alatnya beneran simpel tapi powerful! 💥', 'Gw suka banget sama ini, beneran worth it! 💸', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 🙏', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪', 'Nice post, langsung coba dan puas! 😄', 'Alatnya beneran simpel tapi powerful! 💥', 'Gw suka banget sama ini, beneran worth it! 💸', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 🙏', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪', 'Nice post, langsung coba dan puas! 😄', 'Alatnya beneran simpel tapi powerful! 💥', 'Gw suka banget sama ini, beneran worth it! 💸', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 🙏', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪', 'Nice post, langsung coba dan puas! 😄', 'Alatnya beneran simpel tapi powerful! 💥', 'Gw suka banget sama ini, beneran worth it! 💸', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 🙏', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪', 'Nice post, langsung coba dan puas! 😄', 'Alatnya beneran simpel tapi powerful! 💥', 'Gw suka banget sama ini, beneran worth it! 💸', 'Ini beneran nggak boong, work banget! 🔥', 'Good job, alatnya beneran ngebantu! 🙏', 'Wah, langsung suka sama ini! 😍', 'Nice, beneran sesuai ekspektasi! 😎', 'Alatnya beneran nggak ngecewain! 👌', 'Ini beneran keren, auto recommend! 🚀', 'Good work, langsung work tanpa error! 🙌', 'Wih, beneran ngebantu banget! 💪'])
            response = self.session.post(
                self.api + f'/media/{media_id}/comment/',
                data = {
                    'comment_text': text
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def direct_message(self, username: str = None, text: str = None):
        try:
            if not username.isdigit(): id = self.username_info(username=username)['id']
            else: id = username
            text = text if text is not None else 'Hai! pesan ini dikirim menggunakan instahack 👋🏻\n\nhttps://github.com/termuxhackers-id/instahack'
            data = {'action':'send_item','client_context':generate_uuid(),'recipient_users':'[['+id+']]','__uuid':self.device_id}
            if 'https' in str(text):
                path = 'link'
                data.update({'link_text': text})
            else:
                path = 'text'
                data.update({'text': text})
            response = self.session.post(
                self.api + f'/direct_v2/threads/broadcast/{path}/',
                data=data
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def direct_message_photo(self, username: str = None, file: str = None):
        try:
            if not os.path.isfile(file): raise FileNotFoundError(file)
            if not username.isdigit(): id = self.username_info(username=username)['id']
            else: id = username
            upload_id = self.upload_id(file=file, cookie=self.session.cookies.get_dict().copy(), headers=self.session.headers.copy())
            response = self.session.post(
                self.api + f'/direct_v2/threads/broadcast/configure_photo/',
                data = {
                    'action': 'send_item',
                    'send_attribution': 'inbox',
                    'client_context': generate_uuid(),
                    '__uuid': self.device_id,
                    'upload_id': upload_id,
                    'recipient_users':'[['+id+']]',
                    'allow_full_aspect_ratio':'true'
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def upload_photo(self, file: str = None, caption: str = None):
        try:
            if not os.path.isfile(file): raise FileNotFoundError(file)
            upload_id = self.upload_id(file=file, cookie=self.session.cookies.get_dict().copy(), headers=self.session.headers.copy())
            response = self.session.post(
                self.api + '/media/configure/',
                data = {
                    '_uid': self.user_id,
                    '__uuid': self.device_id,
                    'device_id': self.device_id,
                    'custom_accessibility_caption': caption,
                    'caption': caption,
                    'upload_id': upload_id
                }
            ).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False
    
    def upload_photo_story(self, file: str = None, caption: str = None, resolution: tuple[int, int] = (1080, 1920)):
        try:
            if not os.path.isfile(file): raise FileNotFoundError(file)
            upload_id = self.upload_id(file=file, cookie=self.session.cookies.get_dict().copy(), headers=self.session.headers.copy())
            date = datetime.datetime.now()
            data = {
                "supported_capabilities_new": "[{\"name\":\"SUPPORTED_SDK_VERSIONS\",\"value\":\"131.0,132.0,133.0,134.0,135.0,136.0,137.0,138.0,139.0,140.0,141.0,142.0,143.0,144.0,145.0,146.0,147.0,148.0,149.0,150.0,151.0,152.0,153.0,154.0,155.0,156.0,157.0,158.0,159.0\"},{\"name\":\"FACE_TRACKER_VERSION\",\"value\":\"14\"},{\"name\":\"COMPRESSION\",\"value\":\"ETC2_COMPRESSION\"},{\"name\":\"gyroscope\",\"value\":\"gyroscope_enabled\"}]",
                "has_original_sound": "1",
                "camera_entry_point": "12",
                "original_media_type": "1",
                "camera_session_id": generate_uuid(),
                "date_time_digitalized": f"{date.year}:{date.month:02}:{date.day:02} {date.hour:02}:{date.minute:02}:{date.second:02}",
                "camera_model": self.device["device_model"],
                "scene_capture_type": "",
                "timezone_offset": (datetime.datetime.fromtimestamp(date.timestamp() * 1e-3) - datetime.datetime.utcfromtimestamp(date.timestamp() * 1e-3)).seconds,
                "client_shared_at": int(date.timestamp()),
                "story_sticker_ids": "",
                "configure_mode": "1",
                "source_type": "3",
                "camera_position": "front",
                "_uid": self.user_id,
                "device_id": self.device_id,
                "composition_id": generate_uuid(),
                "_uuid": generate_uuid(),
                "creation_surface": "camera",
                "can_play_spotify_audio": "1",
                "date_time_original": f"{date.year}:{date.month:02}:{date.day:02} {date.hour:02}:{date.minute:02}:{date.second:02}",
                "capture_type": "normal",
                "upload_id": upload_id,
                "client_timestamp": int(date.timestamp()),
                "private_mention_sharing_enabled": "1",
                "media_transformation_info": f"{{\"width\":\"{resolution[0]}\",\"height\":\"{resolution[1]}\",\"x_transform\":\"0\",\"y_transform\":\"0\",\"zoom\":\"1.0\",\"rotation\":\"0.0\",\"background_coverage\":\"0.0\"}}",
                "camera_make": self.device["device_brand"],
                "device": {
                    "manufacturer": self.device["device_brand"],
                    "model": self.device["device_model"],
                    "android_version": int(self.device["device_sdk"]),
                    "android_release": self.device["device_version"]
                },
                "edits": {
                    "filter_type": 0,
                    "filter_strength": 1.0,
                    "crop_original_size": [
                        float(resolution[0]),
                        float(resolution[1])
                    ]
                },
                "extra": {
                    "source_width": resolution[0],
                    "source_height": resolution[1]
                }
            }
            if caption: data["caption"] = caption
            response = self.session.post(self.api + '/media/configure_to_story/', data={"signed_body": "SIGNATURE." + json.dumps(data)}).json()
            if response['status'] == 'ok': return True
            else: return False
        except:
            return False