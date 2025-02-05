import os
try:
    import faker
    import requests
    import mechanize
    import json
    import asyncio
    from user_agent import generate_user_agent as ua
    from user_agent import generate_user_agent as us
    from telethon import TelegramClient, functions, errors
    import requests,pycountry,mechanize
    import random,user_agent,re
    import uuid,instaloader,time
    from bs4 import BeautifulSoup
    import string
    from hashlib import md5
    from time import time
    from time import sleep
    import requests,secrets,uuid
except:
        os.system("pip install requests")
        os.system("pip install faker")
        os.system("pip install hashlib")
        os.system("pip install time")
        os.system("pip install secrets")
        os.system("pip install random")
        os.system("pip install user_agent")
        os.system("pip install uuid")
        os.system("pip install instaloader")
        os.system("pip install pycountry")
        os.system("pip install re")
        os.system("pip install string")
        os.system("pip install requests")
        os.system("pip install asyncio")
        os.system("pip install telethon")
        os.system("pip install base64")
        os.system("pip install json")
        import json
        from user_agent import generate_user_agent as us
        import asyncio
        from telethon import TelegramClient, functions, errors
        import requests,pycountry
        from bs4 import BeautifulSoup
        import random,user_agent,re
        import faker
        import uuid,instaloader,time,string

referers = [
        'https://www.instagram.com/accounts/password/reset/?hl=ar',
        'https://www.instagram.com/explore/',
        'https://www.instagram.com/accounts/login/?next=%2F',
        'https://www.instagram.com/',
    ]  
platforms = ['"Windows"', '"macOS"', '"Linux"', '"Android"', '"iOS"']

uuidd = str(uuid.uuid4())
device_id = uuidd.replace("-", "")
hex_chars = string.hexdigits[:16]
cpid = ''.join(random.choice(hex_chars) for _ in range(16))


class Instagram:
    def Check(email):	    
        csrf = md5(str(time()).encode()).hexdigest()
        url = 'https://b.i.instagram.com/api/v1/accounts/login/'
        headers = {
        'User-Agent': "Instagram 136.0.0.34.124 Android (24/7.0; 640dpi; 1440x2560; HUAWEI; LON-L29; HWLON; hi3660; en_US; 208061712)",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": str(csrf),
                }
        data = {
        'username': email,
        'password': "thomas",
        'device_id': f"android-{secrets.token_hex(8)}",
        '_csrftoken' : csrf,
        'phone_id': str(uuid.uuid4()),
        'guid': str(uuid.uuid4()),

                }
        response = requests.post(url, headers=headers, data=data).text
        if "bad_password" in response:
            csrf = md5(str(time()).encode()).hexdigest()
            headers = {
        'X-Pigeon-Session-Id': str(uuid.uuid4()),
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': str(uuid.uuid4().hex),
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': f'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken={csrf}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
            data = {
        'signed_body': '{dd}.{"_csrftoken":"{csrf}","adid":"{uuidd}","guid":"{uuidd}","device_id":"android-{uuiddvice}","query":"'+email+'"}'.replace("{csrf}",csrf).replace("{uuidd}",str(uuid.uuid4())).replace("{uuiddvice}",str(uuid.uuid4().hex)).replace("{dd}",str(uuid.uuid4().hex)),
        'ig_sig_key_version': '4',
    }	
            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data)
            try:
                    rest = response.json()['email']
                    return {'status': 'Good', 'result': 'Account Found', 'Rest':rest ,'dev': 't5omas'}
            except:
                return {'status': 'Good', 'result': 'Account Found' ,'dev': 't5omas'}
        elif "You'll need to update Instagram to the latest version before you can use the app." in response:
            csrf = md5(str(time()).encode()).hexdigest()
            headers = {
        'X-Pigeon-Session-Id': str(uuid.uuid4()),
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': str(uuid.uuid4().hex),
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': f'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken={csrf}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
            data = {
        'signed_body': '{dd}.{"_csrftoken":"{csrf}","adid":"{uuidd}","guid":"{uuidd}","device_id":"android-{uuiddvice}","query":"'+email+'"}'.replace("{csrf}",csrf).replace("{uuidd}",str(uuid.uuid4())).replace("{uuiddvice}",str(uuid.uuid4().hex)).replace("{dd}",str(uuid.uuid4().hex)),
        'ig_sig_key_version': '4',
    }	
            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data)
            rest = response.json()['email']
            return {'status': 'Good', 'result': 'Account Found', 'Rest':rest ,'dev': 't5omas'}
        else:
            return {'status': 'Good', 'result': 'Account Not Found','dev': 't5omas'}
    def Info(user):
                headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-csrftoken': 'bXKL9GTAtK2cYn2IoXBtmQT9J1kEHmQv',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0qFm_PDZfOSVRxZVwKIcwP0xOOG29DNOU5Ec98eOYiANXY',
                'x-instagram-ajax': '1006477071',
                'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
                }
                params = {
                'username': f'{user}',
                }
                requests_info1 = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers)
                requests_info = requests_info1.json()
                try:
                    name = requests_info['data']['user']['full_name']
                except:
                       name = None
                try:
                    username =  requests_info['data']['user']['username']
                except:
                       username=None
                try:
                    Id = requests_info['data']['user']['id']
                except:
                      Id=None
                try:
                    following = requests_info['data']['user']["edge_follow"]["count"]
                except:
                      following=None
                try:
                    followers = requests_info['data']['user']["edge_followed_by"]["count"]
                except:
                      followers=None
                try:
                    post = requests_info['data']['user']["edge_owner_to_timeline_media"]["count"]
                except:
                      post=None
                try:
                    bio = requests_info['data']['user']['biography']
                except:
                      bio=None
                try:
                  if int(Id)>1 and int(Id)<1279000:
                    data=(2010)
                  elif int(Id)>1279001 and int(Id)<17750000:
                    data=(2011)
                  elif int(Id) > 17750001 and int(Id)<279760000:
                    data=(2012)
                  elif int(Id)>279760001 and int(Id)<900990000:
                    data=(2013)
                  elif int(Id)>900990001 and int(Id)< 1629010000:
                    data=(2014)
                  elif int(Id)>1900000000 and int(Id)<2500000000:
                    data=(2015)
                  elif int(Id)>2500000000 and int(Id)<3713668786:
                    data=(2016)
                  elif int(Id)>3713668786 and int(Id)<5699785217:
                    data=(2017)
                  elif int(Id)>5699785217 and int(Id)<8507940634:
                    data=(2018)
                  elif int(Id)>8507940634 and int(Id)<21254029834:
                    data=(2019)
                  else:
                    data=("2020-2023")
                except BaseException as m :
                  date=(m)
                link = (f"https://www.instagram.com/{username}/")
                return {'Username':username,'Name':name,'Date':data,'Id':Id,'Following':following,'Followers':followers,"Post":post,'Bio':bio,'Account_Link':link,'dev': 't5omas'}
    def getoldusers():
        try:
            lsd=''.join(random.choice('2ULwtVInskNgB5QAG8IdQQfY1jVdyRSkg02fn5DXJR4Uuge4db2od8j6BFl0') for _ in range(16))
            id=str(random.randrange(10000,739988755))

            headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/0s9s/',
            'user-agent': str(user_agent.generate_user_agent()),
            'x-fb-lsd': 'insta'+lsd,
            'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        }
            data = {
            'lsd': 'insta'+lsd,
            'variables': '{"id":"'+id+'","relay_header":false,"render_surface":"PROFILE"}',
            'doc_id': '7397388303713986',
        }
            user= requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']
            return {'Username':user,'dev': 't5omas'}

        except Exception as e:
            return None
    def sessionid(username,password):
            headers = {"accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "ar,en;q=0.9",
                "content-length": "317",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": "mid=Yemn3AAEAAGx56yZBU5-oiVvPQ4e; ig_did=B8C62C92-A3F7-418B-8F2D-7552C1467C20; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com;",
                "origin": "https://www.instagram.com",
                "referer": "https://www.instagram.com/accounts/login/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": user_agent.generate_user_agent(),
                "x-csrftoken": "dlVqZxJJmbq22SfBTTC3pPlEcsDkptlj",
                "x-ig-app-id": "936619743392459",
                "x-ig-www-claim": "hmac.AR1cXkJeUEqtcGbsTBzJrMSHrjfv-gbYYkqfI4FZCDO_-3mb",
                "x-instagram-ajax": "1c61e9255248",
                'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
                "x-requested-with": "XMLHttpRequest"
                }
            data={'username': username,'enc_password': "#PWD_INSTAGRAM_BROWSER:0:&:"+password,}

            response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
            try:
                ses = response.cookies.get_dict()['sessionid']
                return {'sessionid':{ses},'dev': 't5omas'}
            except:
                return 'ERROR : Username Or Password Wrong'
    def following(target,sessionid):
        info=requests.get('https://anonyig.com/api/ig/userInfoByUsername/'+target,headers={'user-agent': user_agent.generate_user_agent()}).json()['result']
        id=info['user']['pk']
        count = info['user']['following_count']
        cookies = {
                    'ig_did': '9669EE3D-9AA8-4A7D-84B9-2738EFE07C31',
                    'ig_nrcb': '1',
                    'mid': 'ZuydJgALAAHgHrsiGEXlJTLU8ZBg',
                    'datr': 'Jp3sZu-JWHb3PPSORdl09M0f',
                    'csrftoken': 'BSTqYpml9ApETJCc7SJXCeJUnVQSkKJ3',
                    'ds_user_id': '61133585536',
                    'sessionid': sessionid,
                    'shbid': '"2476\\05461133585536\\0541758318862:01f7b68aa989e19c1d450206cf928099068ab69a3655a60bae81d706b0f0a14eb0d3719a"',
                    'shbts': '"1726782862\\05461133585536\\0541758318862:01f7589e936c303fd72c884e0d071569c031b18b6b56bc6dd0973129f42f56c86570904e"',
                    'wd': '1365x945',
                    'rur': '"RVA\\05461133585536\\0541758318911:01f7085bff8a402a2e6f6e8ab8036052f1cc56e83bd2fca92ea06db3482b5e1af1ddbcbb"',
                }

        headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    # 'cookie': 'ig_did=9669EE3D-9AA8-4A7D-84B9-2738EFE07C31; ig_nrcb=1; mid=ZuydJgALAAHgHrsiGEXlJTLU8ZBg; datr=Jp3sZu-JWHb3PPSORdl09M0f; csrftoken=BSTqYpml9ApETJCc7SJXCeJUnVQSkKJ3; ds_user_id=61133585536; sessionid=61133585536%3AHw3xTTAs2kNoTf%3A24%3AAYfiMml6NV2u7puMNfqKlVJl58xFXkLhErVCUATuZw; shbid="2476\\05461133585536\\0541758318862:01f7b68aa989e19c1d450206cf928099068ab69a3655a60bae81d706b0f0a14eb0d3719a"; shbts="1726782862\\05461133585536\\0541758318862:01f7589e936c303fd72c884e0d071569c031b18b6b56bc6dd0973129f42f56c86570904e"; wd=1365x945; rur="RVA\\05461133585536\\0541758318911:01f7085bff8a402a2e6f6e8ab8036052f1cc56e83bd2fca92ea06db3482b5e1af1ddbcbb"',
                    'priority': 'u=1, i',
                    'referer': 'https://www.instagram.com/d_r_n/following/',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                    'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.59", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.59"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': user_agent.generate_user_agent(),
                    'x-asbd-id': '129477',
                    'x-csrftoken': 'BSTqYpml9ApETJCc7SJXCeJUnVQSkKJ3',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR09bdfDA0NvG62iAuVQekRHtbPWBf_SQkZdzBIbvmg_JDTd',
                    'x-requested-with': 'XMLHttpRequest',
                    'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
                }

        params = {
                    'count': count,
                }

        response = requests.get(
                    f'https://www.instagram.com/api/v1/friendships/{id}/following/',
                    params=params,
                    cookies=cookies,
                    headers=headers,
                ).json()
        for i in range(count):
            try:
                username = response['users'][i]['username']
                print({'username':username,'dev':'@t5omas'})
            except Exception as e:
                        return 'Your sessionid Got Banned Try Again Later'
    def followers(username,password,target):
        L = instaloader.Instaloader()
        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, target)
        for followee in profile.get_followers():
                try:
                    name1 = str(followee)
                    name2 = name1.split('Profile ')[1]
                    name3 = name2.split(' (')[0]
                    time.sleep(60)
                    print({'username':name3,'dev':'@t5omas'})
                except:
                    return 'Your sessionid Got Banned Try Again Later'
    def login(username,password):
        random_uuid = uuid.uuid4()
        device_id = str(random_uuid).replace("-", "")
        url = "https://i.instagram.com/api/v1/accounts/login/"

        headers = {
                            "Accept-Encoding": "gzip",
                            "Accept-Language": "en-US",
                            "Connection": "Keep-Alive",
                            "Content-Length": "330",
                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                            "Cookie": "mid=Zq_SxQABAAFwUCIa9KHIn1rlOIiN; csrftoken=SuzlAHVsab8fEuBhnK51ksCUjZLKCkyV",
                            "Cookie2": "$Version=1",
                            "Host": "i.instagram.com",
                            "User-Agent": "Instagram 6.12.1 Android (33/13; 450dpi; 1080x2009; samsung/xiaomi; M2012K11C; a13ve; mt6768; en_US)",
                            "X-IG-Capabilities": "AQ==",
                            "X-IG-Connection-Type": "WIFI",
                            'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
                        }

        data = {
                            "ig_sig_key_version": "4",
                            "signed_body": "f4ef46b2c12815ec0c5b7866b08fa96ea392fe9b233add6a058a6236b8ca515b.{\"username\":\"{1}\",\"password\":\"{2}\",\"device_id\":\"android-{id}\",\"guid\":\"{guid}\",\"_csrftoken\":\"SuzlAHVsab8fEuBhnK51ksCUjZLKCkyV\"}".replace("{1}",username).replace("{2}",password).replace("{id}",device_id[:16]).replace("{guid}",str(uuid.uuid4())
            )
                        }

        response = requests.post(url, headers=headers, data=data).text
        try:
            if "logged_in_user" in response:
                return {'status':'ok','logged_in_user':True,'dev':'@t5omas'}
            elif "checkpoint_required" in response:
                return {'status':'ok','logged_in_user':'checkpoint','dev':'@t5omas'}
            else:
                return {'status':'ok','logged_in_user':False,'dev':'@t5omas'}
        except:
            return 'FIELD EMPTY or error with requests Please Try Again'
    def getrandomuser(word):
        try:
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'ig_did=9669EE3D-9AA8-4A7D-84B9-2738EFE07C31; ig_nrcb=1; mid=ZuydJgALAAHgHrsiGEXlJTLU8ZBg; datr=Jp3sZu-JWHb3PPSORdl09M0f; shbid="2476\\05461133585536\\0541758318862:01f7b68aa989e19c1d450206cf928099068ab69a3655a60bae81d706b0f0a14eb0d3719a"; shbts="1726782862\\05461133585536\\0541758318862:01f7589e936c303fd72c884e0d071569c031b18b6b56bc6dd0973129f42f56c86570904e"; csrftoken=c3K96JBD7YHr5oYZveanDWW1YWpOx12m; ds_user_id=64540361093; sessionid=64540361093%3AMIHM28oD3SQWj6%3A3%3AAYcSpICOayKuw4mlqCNdXCe7GQrsHqsaAXPAdWS4QQ; wd=1172x945; rur="CLN\\05464540361093\\0541758325017:01f7187a749c954124ea0e896dbc33a93b69f6de91de98509ba2653e16dcda3664f3d925"',
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/z.yyz3/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.59", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.59"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'x-asbd-id': '129477',
                'x-bloks-version-id': '45949a58ec060709d5054d638e57729a553188c614b175e79022df638c465743',
                'x-csrftoken': 'c3K96JBD7YHr5oYZveanDWW1YWpOx12m',
                'x-fb-friendly-name': 'PolarisSearchBoxRefetchableQuery',
                'x-fb-lsd': 'Jz_QNPAPuDFR5P9okyB4bV',
                'x-ig-app-id': '936619743392459',
                'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
            }

            data = {
                'av': '17841464352817545',
                '__d': 'www',
                '__user': '0',
                '__a': '1',
                '__req': '15',
                '__hs': '19985.HYP:instagram_web_pkg.2.1..0.1',
                'dpr': '1',
                '__ccg': 'UNKNOWN',
                '__rev': '1016645849',
                '__s': 'as7rpz:2gmi86:rm8nyd',
                '__hsi': '7416502291445634002',
                '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awgo9oO0n24oaEnxO1ywOwv89k2C1Fwc60D87u3ifK0EUjwGzEaE2iwNwmE7G4-5o4q3y1Sx-0lKq2-azqwt8d-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubxKi2K7E5yqcxK2K1ew',
                '__csr': 'gigqYp2AYoxvf4lFbTjj8AQGOJkGL-lQn9HF9ruFRihJk9P6LAuGiCDAZpdx2-GKBpGmufGiKAEzKqQgwFfV-qWByUOi8K2mA4utrmaGWyGGVtoCFHDxdAKuVogAhe4Fp9E88kw04SCw3HEujxSKawAwWOwsE5yqu3q0FVEC3AE0bbV4ea6EZbgggjS0J4l3U8Q2CdyFEpwhUk8VRCYOw4MIAWj8mA4N8G2Twe63F8weax1hY9wlWwyg6505sIC0zES1Nx-0bdhpQ9EE5O3Z3po07Be0dUw1KK',
                '__comet_req': '7',
                'fb_dtsg': 'NAcNHbQHE80tz7psai4UxdmKO_ZiBeUGnFvioBxfOSNad9sIVdTlycA:17864789131057511:1726786920',
                'jazoest': '26452',
                'lsd': 'Jz_QNPAPuDFR5P9okyB4bV',
                '__spin_r': '1016645849',
                '__spin_b': 'trunk',
                '__spin_t': '1726789002',
                'qpl_active_flow_ids': '1056839232',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisSearchBoxRefetchableQuery',
                'variables': '{"data":{"context":"blended","include_reel":"true","query":"{1}","rank_token":"1726789012137|acf5baaa3e8bd63b19c2aaf21b458a92f6719c73d09cee164d9bdebbf7545d37","search_surface":"web_top_search"},"hasQuery":true}'.replace("{1}",word),
                'server_timestamps': 'true',
                'doc_id': '7935512656557707',
            }

            response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
        except:
             return 'FIELD Word EMPTY or error with requests Please Try Again'
        usr = response['data']['xdt_api__v1__fbsearch__topsearch_connection']['users'][1]['user']['username']
        return {'username':usr,'dev':'@t5omas'}
class TikTok:
      def GetRandomUser():
                device_id = random.randint(1000000000000000000, 9999999999999999999)
                iid = random.randint(1000000000000000000, 9999999999999999999)
                openudid = cpid
                ts = str(random.randint(1000000000, 9999999999))
                region = random.choice(['US', 'IQ', 'CA', 'UK'])
                build_number = f"{random.randint(30, 40)}.{random.randint(0, 9)}.{random.randint(0, 9)}"

                url = f"https://api22-normal-c-alisg.tiktokv.com/tiktok/feed/explore/v1?device_platform=android&os=android&ssmix=a&_rticket={ts}106&cdid=f5b31c42-4518-42ed-b1a9-53b6e6cfca14&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360204&version_name=36.2.4&manifest_version_code=2023602040&update_version_code=2023602040&ab_version=36.2.4&resolution=900*1600&dpi=320&device_type=SM-G965N&device_brand=samsung&language=en&os_api=28&os_version=9&ac=wifi&is_pad=0&current_region=US&app_type=normal&sys_region=US&last_install_time=1718636614&mcc_mnc=31002&timezone_name=Africa%2FNairobi&carrier_region_v2=310&residence={region}&app_language=en&carrier_region={region}&timezone_offset=10800&host_abi=arm64-v8a&locale=en&ac2=wifi5g&uoo=0&op_region={region}&build_number={build_number}&region={region}&ts={ts}&iid={iid}&device_id={device_id}&openudid={openudid}"

                headers = {
                    "Accept-Encoding": "gzip",
                    "Connection": "Keep-Alive",
                    "Content-Length": "88",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": "store-idc=alisg; store-country-code=iq; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=VBdfaKOGXtpOVbcY75NbTPxJzIsH5wPkfgZK87yPs6xlCmPVtdrfi-YW16Gal6A25-swsHMnNufQCEzDcWGtkoMchVFvbivEyZF4oG4leBL9rMOhq5NBKRDVq65sLS4VqixG-U-Zcri6wV7FatdO1gBth_Eb2Lcv2tKMoKkCvJmCovheIs1gIfDvGDignkPFH_kgl_xQk0ytDqLn_uWtUH5QlR1afkj7hmHmNra4PZqK-OukrMaNs5dS5KlEykIJfZpZWofIND8Yay8y7nrjDJYdRNjBRl-QTOTu-k760L-_K4HPGYJoA4SYU2Nbhsc04RI18cfH84xPT9UiiFyKmBE4b7FVkVS1YThBZOsSjZ45RzUHZ4P6qWJJdY3...",
                    "Host": "api22-normal-c-alisg.tiktokv.com",
                    "passport-sdk-version": "6030490",
                    "sdk-version": "2",
                    "User-Agent": f"com.zhiliaoapp.musically/{build_number} (Linux; U; Android 9; en; SM-G965N; Build/QP1A.190711.020;tt-ok/3.12.13.4-tiktok)",
                    "X-Argus": "kLoxy/8ao3NT8csOzLQq8Dm2HZ0EsyeTSSyji+8/kgNF6C/QgjBNl7+wIFLzBf4pBenwqQ1O5RRe+M2vJdkTS3Ou/fQsPwso3QHAGVyNexGdwGSYakfba0RP+3haL61DBOZZ42mnD8TK6hRffqp/XvIq97xxB5QErTAVGknVj+TmJVvXzGFl/oTPYOY8fuO84nnYkK8R32lO5mj7peOIOKNQzXm28YXu3WNTS9WnpsncNJm5TI/4UjlVcoajJ0xvjOKMoPXUfxzT1/G+Thz9hTYsXfNeOJoDRfp/Abg7ihU4NrTKkwa+73WfE27DUOhWRxSrOrpD+3t5tVxcitDQcogsxLxMKtznI86hbFEF58AUyOyQipVAokS0mynVvt//qezLEYcAF6czaVd1DqsFeDT8EdayzfP4Nemntf2HzHTFPVdNCvW3tprOpauN+dFVhBTbSPywCECrw7dvK+aACQt+PoxMmd20uTv3dyknqu...",
                    "x-bd-client-key": "#UHZZTJtjXutzfn6E75ApLG6WykzTUs46M6Q4iJlFm/LVt4wXcWPNtQh5Cw44PQ88ZUl7LtEOyDTtSL0M",
                    "x-bd-kmsv": "0",
                    "X-Gorgon": "8404c04d400063966322baafb4ffe6fabb7ac8ec2f35fbcd734f",
                    "X-Khronos": "1724791172",
                    "X-Ladon": "IpIwGSEj+FdhYm+jSiOzRQ2CdDSNiVkKoHf+DR6dsz5Bk+3H",
                    "x-metasec-event-source": "native",
                    "x-metasec-pns-event-id": "291",
                    "X-SS-REQ-TICKET": f"{ts}107",
                    "X-SS-STUB": "9A7DA7A830589EA4C0D266DF151E9870",
                    "x-tt-dm-status": "login=1;ct=1;rt=1",
                    "x-tt-request-tag": "n=0",
                    "x-tt-store-region": "iq",
                    "x-tt-store-region-src": "uid",
                    "X-Tt-Token": "030a54167a4814d6c4276755bb0f576b9c0468a878de78fa1993692180dfb4e8c9064e3f85cd527cec2615206b366758cac244b35b4117d0b70f49cf77be3f6862d6f01715358fd8fe1b4d026ce1d1f1b24d277da86912eae72da7f2e54f01c8e2c35-1.0.1",
                    "x-vc-bdturing-sdk-version": "2.3.8.i18n",
                    'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
                }

                data = {
                    "count": "8",
                    "tab_type": "2",
                    "interacted_ids": "{}",
                    "pull_type": "1",
                    "non_personalized": "false",
                    "enter_from": "0"
                }

                response = requests.post(url, headers=headers, data=data)
                unique_id = response.json()['awemes'][0]['author']['unique_id']
                return {'usernamer':unique_id,'dev':'@t5omas'}
        
      def Info(username):
                patre = {
                "Host": "www.tiktok.com",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "\"Android\"",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
                
            }

                tikinfo = requests.get(f'https://www.tiktok.com/@{username}', headers=patre).text
                getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
                try:
                    id = str(getting.split('id":"')[1]).split('",')[0]
                except:
                    id = ""
                try:
                    name = str(getting.split('nickname":"')[1]).split('",')[0]
                except:
                    name = ""
                try:
                    bio = str(getting.split('signature":"')[1]).split('",')[0]
                except:
                    bio = ""
                try:
                    country = str(getting.split('region":"')[1]).split('",')[0]
                except:
                    country = ""
                try:
                    private = str(getting.split('privateAccount":')[1]).split(',"')[0]
                except:
                    private = ""
                try:
                    followers = str(getting.split('followerCount":')[1]).split(',"')[0]
                except:
                    followers = ""
                try:
                    following = str(getting.split('followingCount":')[1]).split(',"')[0]
                except:
                    following = ""
                try:
                    like = str(getting.split('heart":')[1]).split(',"')[0]
                except:
                    like = ""
                try:
                    video = str(getting.split('videoCount":')[1]).split(',"')[0]
                except:
                    video = ""
                try:
                    secid = str(getting.split('secUid":"')[1]).split('"')[0]
                except:
                    secid = ""
                try:
                    countryn = pycountry.countries.get(alpha_2=country).name
                except:
                    countryn = ""
                try:
                    countryf = pycountry.countries.get(alpha_2=country).flag
                except:
                    countryf = ""
                try:
                  return {"username": username,"secuid": secid,"name": name,"followers": followers,"following": following,"like": like,"video": video,"private": private,"country": countryn,"flag": countryf,"id": id,"bio": bio,"status": "ok","dev": "@t5omas"}
                except:
                    return 'ERROR : invalid Username '
                    
                    
                    
class Facebook:
    def Login_v1(ids,pas):
            session = requests.Session()
            ua = user_agent.generate_user_agent()
            head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            MD=session.cookies.get_dict().keys()
            try:
                if "c_user" in MD:
                        return {'status':'ok','logged_in_user':True,'dev':'@t5omas'}
                elif "checkpoint" in MD:
                    return {'status':'ok','logged_in_user':'checkpoint','dev':'@t5omas'}
                else:
                        return {'status':'ok','logged_in_user':False,'dev':'@t5omas'}
            except:
                return 'FIELD EMPTY or error with requests Please Try Again'
                
                
                
    def Login_v2(ids, pas):
      try:
        agent = user_agent.generate_user_agent()
        session = requests.Session()
        url = "https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&locale2=ar_AR&refid=8"
        headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23127PN0CC"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': agent,
    'viewport-width': '980',
}

        response = session.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        hidden_inputs = soup.find_all("input", type="hidden")
        data = {input.get('name'): input.get('value') for input in hidden_inputs if input.get('name')}
        data['email'] = ids
        data['pass'] = pas

        req = session.post(url, data=data, headers=headers, allow_redirects=False)

        if "m_page_voice" in req.cookies:
            return {'status':'ok','logged_in_user':True,'dev':'@t5omas'}
        elif "Unsupported Browser" in req.text or "<title>Error Facebook</title>" in req.text or "خطأ" in req.text:
            return {'status':'ok','logged_in_user':'Bad UserAgent','dev':'@t5omas'}
                
        elif "checkpoint" in req.cookies:
            return {'status':'ok','logged_in_user':'checkpoint','dev':'@t5omas'}
        else:            
            return {'status':'ok','logged_in_user':False,'dev':'@t5omas'}
      except:
            return {'status':'ok','logged_in_user':False,'dev':'@t5omas'}
            
            
            
    def Login_v3(ids,pas):
        url = "https://b-graph.facebook.com/auth/login"

        payload = f"email={ids}&password={pas}&credentials_type=password&error_detail_type=button_with_disabled&format=json&device_id=1590ae20-130f-4979-b0c2-3b9d09b4b29f&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&method=POST"

        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; 23116PN5BC Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/338.0.0.3.102;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/436638506;FBCR/Yemen Mobile;FBMF/Xiaomi;FBBD/Redmi;FBDV/23116PN5BC;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2220};]",
            'Connection': "Keep-Alive",
            'Authorization': "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
        }

        response = requests.post(url, data=payload, headers=headers)
        if "Invalid username or email address" in response.text:
            return {'status':'ok','logged_in_user':False,'dev':'@t5omas'}
        elif "Go to the app store on your device and update the Messenger app to log in." in response.text:
            return 'ERROR CHECK ID OR TALK TO @t5omas'
        else:
            return {'status':'ok','logged_in_user':True,'dev':'@t5omas'}
            
    def check(email):
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=N0XjZk_xaveMEDIenIAJEXZ_; datr=N0XjZh8iQ9roQcjFSpSZ_NDn; ps_l=1; ps_n=1; fr=1byMbkzmqLuiE4Nw0.AWVD7E62mfZfmIJswB6kRHB_57w.Bm5eqc..AAA.0.0.Bm6VRS.AWWt0sb7J9E; wd=1089x945',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.138", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent.generate_user_agent(),
            'x-asbd-id': '129477',
            'x-fb-lsd': 'AVpCsFS0jaU',
            'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
        }

        data = {
            'jazoest': '2934',
            'lsd': 'AVpCsFS0jaU',
            'email': email,
            'did_submit': '1',
            '__user': '0',
            '__a': '1',
            '__req': '4',

        }

        response = requests.post(
            'https://www.facebook.com/ajax/login/help/identify.php',
            headers=headers,
            data=data,
        )
        sh = response.cookies.get_dict()
        try:
            if 'sfiu' in sh:
                return {'status': 'Good', 'result': 'Account Found', 'dev': 't5omas'}
            else:
                return {'status': 'Good', 'result': 'Account Not Found', 'dev': 't5omas'}
        except:
            return 'FIELD EMPTY'
            
            
class Email_services:
    def Gmail(Email):
        if not "@" in Email:
            Email = Email + "@gmail.com"
        else:
            Email = Email
        gm = mechanize.Browser()
        gm.set_handle_robots(False)
        gm.addheaders = [
            ('User-Agent', us()),
            ('Accept-Language', 'en-US,en;q=0.9'),
            ('Accept-Encoding', 'gzip, deflate, br'),
            ('Connection', 'keep-alive'),
            ('Upgrade-Insecure-Requests', '1'),
            ('X-Forwarded-For', f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}")
        ]
        gm.open("https://accounts.google.com/v3/signin/recoveryidentifier?checkConnection=youtube:511&checkedDomains=youtube&ddm=0&dsh=S-418804429:1719166987007523&flowName=WebLiteSignIn&hl=en&pstMsg=1&service=mail")
        gm._factory.is_html = True
        gm.select_form(nr=0)
        if len(Email.split("@")[0]) >= 6:
            if "_" not in Email:
                gm['identifier'] = Email
                jgm = gm.submit().read()
                soup = BeautifulSoup(jgm, 'html.parser')
                res = soup.get_text()            
                if "Couldn’t find your Google AccountNextForgot email" in str(res):   
                    return {"type":"Gmail","isAvailable":True,'dev':'@t5omas'}    
                else:
                    return {"type":"Gmail","isAvailable":False,'dev':'@t5omas'}
            else:
                return " Bad With Requests "
        else:
            return " Email is too short "



    def Hotmail(username):
        random_ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        cookies = {
            'MicrosoftApplicationsTelemetryDeviceId': str(uuid.uuid4),
            'MSFPC': f'GUID=f{str(uuid.uuid4().hex)}&HASH=5a8b&LV=202409&V=4&LU=1726708584502',
            'MUID': str(uuid.uuid4().hex),
            '_pxvid': str(uuid.uuid4),
            'logonLatency': 'LGN01=638630045570418108',
            'amsc': '3/kyc9AFFGTjBmKvC/6jLJ7joCAK0jkV7rZFltiHV+cwAUZpHHY3eju+6CZKM3Cj0coXcS5TrzcxkWaAP98OD0Az29X8zhV7YdcPkSJDFrCXHs7CyDibJfucUIcPPGkCivtUp6iTRC1PmEdG4h8V2N1hPS806YzopEmWRIQx7Pl2cMFOKKUOKXhx7WBZwRNdlMUhj+Ez+mhIs/G6eH8Vnc7AaLG4sxSykoaM0uifU0L1+gxei1ED79i8mUEvkpmRySj2n8JyCzhOlYIb265TcDPxvwX+eBzMuZb+jgBt8Wk=:2:3c',
            'ai_session': 'x86SXzMmuaa9CgpoR4cgo8|1727407773082|1727407773082',
            'fptctx2': 'taBcrIH61PuCVH7eNCyH0I1otfYAPn9VOPY9aMX8tO1RkWgq2m174KN7LvQacI4UeqMh2BXGzaobu8W%252brBibMn8CDVBG%252byTSM%252f25JTka9bOnNYF1Xgkj9VD4mL2g1VXDAA7D4XjS5PiTIoH5MkL9p8d8x63%252fHvrQC1JHaE%252fnhOlWw37nb1DvfX3%252f0njCoqm7QgG2vs0SnR%252bEANOG7IhUPVneOLLIOhAq8vHDnFl8QLHZH8%252b1pa3fu5MbITkKfXo9SREyEEz6Frky4mLwzgWGq2V5znUbsRjv2rf4pC0FFMCaboaKEhb9wX82Qq414do2ZNUhJb1gIxZMRZ5uWT7wvA%253d%253d',
            '_px3': '7aa5ea4913c79ec9118bfa44e5a369d0b223d9e2f0735e547e7f990e3ba2939b:EazFbSlOCxSBnNAroaNaXvalNK8IALR3s98Yf7oav7DgtwxxwxbZbIqUMygntTyk/RqSieu9c6lQjcMrnKMARg==:1000:C0yRLFfD6Su+qOXUvCIfLqHO0xCXeZnqoqduLR3r9N/0tsUTamHaGJVqwfWjvA6hx1KhIeZ6K1/sWrI66uqRHO82/KHTwlpCEHEprv2osGMWxH8SMy7Re3q9LQRlKjI7pNC8U5gcDN85aslPOmvYMrbtml5tbr3l6Yu6PEbKIBdscZeejhq8pnzFHESBmVBUWVX2wHYI6pLG4ejwtcx6OPfVPEw8Aj7Pg/ZJ13OvcBU=',
            '_pxde': f'{str(uuid.uuid4().hex)}:eyJ0aW1lc3RhbXAiOjE3Mjc0MDc3NjI1MDksImZfa2IiOjAsImlwY19pZCI6W10sImluY19pZCI6WyI2ZDJkODk4ZjUzMGM0ODgxMWY1MTViNjAxMDE4YmY1YSJdfQ==',
        }

        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'canary': 'WazYOCBz6qpSoc3FKOJdRcaSsfB5Pf0hdquKurp5d5nqxi4fC2lc3BFKr2TViKaQA0Z7sBymXMGUV2WF86nHHngJ8uzQDuhmWzSF29hMxV9EXDkZuyVTiSYWPKy2fLvcxKF2aoio9yns8cdoQKEDJuLQ8EwsxKRNbZcWx/SeYmoT1ltGTJgF8XRfSfVDBTiNX6OMFkJIwYOiYT0Q/ampBRfhBm272wr4t7AUSyOmo8ueElA8Eqf5XeFjfje7EYEw:2:3c',
            'client-request-id': str(uuid.uuid4().hex),
            'content-type': 'application/json; charset=utf-8',
            # 'cookie': 'MicrosoftApplicationsTelemetryDeviceId=23a7892a-f083-436c-b495-ec907e200965; MSFPC=GUID=5a8b6ceb2df14ead8624d9617dbd7f29&HASH=5a8b&LV=202409&V=4&LU=1726708584502; MUID=dd50173a7a8842cb86eab584e65ebed0; _pxvid=e46b5923-776f-11ef-b1d0-847f940ff0e1; logonLatency=LGN01=638630045570418108; amsc=3/kyc9AFFGTjBmKvC/6jLJ7joCAK0jkV7rZFltiHV+cwAUZpHHY3eju+6CZKM3Cj0coXcS5TrzcxkWaAP98OD0Az29X8zhV7YdcPkSJDFrCXHs7CyDibJfucUIcPPGkCivtUp6iTRC1PmEdG4h8V2N1hPS806YzopEmWRIQx7Pl2cMFOKKUOKXhx7WBZwRNdlMUhj+Ez+mhIs/G6eH8Vnc7AaLG4sxSykoaM0uifU0L1+gxei1ED79i8mUEvkpmRySj2n8JyCzhOlYIb265TcDPxvwX+eBzMuZb+jgBt8Wk=:2:3c; ai_session=x86SXzMmuaa9CgpoR4cgo8|1727407773082|1727407773082; fptctx2=taBcrIH61PuCVH7eNCyH0I1otfYAPn9VOPY9aMX8tO1RkWgq2m174KN7LvQacI4UeqMh2BXGzaobu8W%252brBibMn8CDVBG%252byTSM%252f25JTka9bOnNYF1Xgkj9VD4mL2g1VXDAA7D4XjS5PiTIoH5MkL9p8d8x63%252fHvrQC1JHaE%252fnhOlWw37nb1DvfX3%252f0njCoqm7QgG2vs0SnR%252bEANOG7IhUPVneOLLIOhAq8vHDnFl8QLHZH8%252b1pa3fu5MbITkKfXo9SREyEEz6Frky4mLwzgWGq2V5znUbsRjv2rf4pC0FFMCaboaKEhb9wX82Qq414do2ZNUhJb1gIxZMRZ5uWT7wvA%253d%253d; _px3=7aa5ea4913c79ec9118bfa44e5a369d0b223d9e2f0735e547e7f990e3ba2939b:EazFbSlOCxSBnNAroaNaXvalNK8IALR3s98Yf7oav7DgtwxxwxbZbIqUMygntTyk/RqSieu9c6lQjcMrnKMARg==:1000:C0yRLFfD6Su+qOXUvCIfLqHO0xCXeZnqoqduLR3r9N/0tsUTamHaGJVqwfWjvA6hx1KhIeZ6K1/sWrI66uqRHO82/KHTwlpCEHEprv2osGMWxH8SMy7Re3q9LQRlKjI7pNC8U5gcDN85aslPOmvYMrbtml5tbr3l6Yu6PEbKIBdscZeejhq8pnzFHESBmVBUWVX2wHYI6pLG4ejwtcx6OPfVPEw8Aj7Pg/ZJ13OvcBU=; _pxde=7772a0b37bf604b90b3694fcf0948ee02c5701da67096f4d8f7a8b96ced01e19:eyJ0aW1lc3RhbXAiOjE3Mjc0MDc3NjI1MDksImZfa2IiOjAsImlwY19pZCI6W10sImluY19pZCI6WyI2ZDJkODk4ZjUzMGM0ODgxMWY1MTViNjAxMDE4YmY1YSJdfQ==',
            'correlationid': str(uuid.uuid4().hex),
            'hpgact': '0',
            'hpgid': '200225',
            'origin': 'https://signup.live.com',
            'priority': 'u=1, i',
            'referer': 'https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=161&ct=1727407757&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3dd357c20b-59f3-c41a-e87b-1d06e3dd99ed&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&lic=1&uaid=11d20b56cc384acca1a82598b93a26d4',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'X-Forwarded-For': random_ip
        }

        json_data = {
            'includeSuggestions': True,
            'signInName': f'{username}@hotmail.com',
            'uiflvr': 1001,
            'scid': 100118,
            'uaid': '11d20b56cc384acca1a82598b93a26d4',
            'hpgid': 200225,
        }

        response = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames?lcid=1033&wa=wsignin1.0&rpsnv=161&ct=1727407757&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3dd357c20b-59f3-c41a-e87b-1d06e3dd99ed&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&lic=1&uaid=11d20b56cc384acca1a82598b93a26d4',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        response_json = response.json()
        try:
            if '"isAvailable":true' in response.text:
                at = response_json['isAvailable']
                return {"type":"hotmail","isAvailable":at,'dev':'@t5omas'}
            elif '"isAvailable":false':
                af = response_json['isAvailable']
                return {"type":"hotmail","isAvailable":af,'dev':'@t5omas'}
        except:
            microsoft_app_id = str(uuid.uuid4())
            uaid = str(uuid.uuid4())
            msfpc_guid = str(uuid.uuid4())
            muid = ''.join(random.choice('0123456789abcdef') for _ in range(32))
            mscc = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}-IQ"
            msfpc = f"GUID={msfpc_guid}&HASH={''.join(random.choice('0123456789abcdef') for _ in range(4))}&LV={random.randint(202301, 202412)}&V=4&LU={random.randint(1600000000000, 1800000000000)}"
            cookies = {
                'MUID': muid,
                'MSCC': mscc,
                'MicrosoftApplicationsTelemetryDeviceId': microsoft_app_id,
                'MSFPC': msfpc,
                'MSPBack': '0',
                'logonLatency': f"LGN01={random.randint(100000000000000000, 999999999999999999)}",
                'uaid': uaid,
                'MSPRequ': 'id=292841&lt=1727198966&co=0',
                'MSPOK': '$uuid-bcd56121-cb0b-47fa-afef-125ee97242c3',
                'OParams': ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!*') for _ in range(200)),
                'amsc': ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/') for _ in range(150)) + ":2:3c",
                'ai_session': f"{str(uuid.uuid4())}|{random.randint(1600000000000, 1800000000000)}|{random.randint(1600000000000, 1800000000000)}",
                'fptctx2': ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%') for _ in range(100)),
            }
            client_request_id = str(uuid.uuid4())
            correlation_id = str(uuid.uuid4())

            headers = {
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-type': 'application/json; charset=utf-8',
                'Origin': 'https://login.live.com',
                'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=161&ct=1727198965&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26deeplink%3dowa%252f%26RpsCsrfState%3d12fa363f-dee8-af36-da7a-8bda7a184fdc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'client-request-id': client_request_id,
                'correlationId': correlation_id,
                'hpgact': '0',
                'hpgid': str(random.randint(1, 100)),
                'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'X-Forwarded-For': random_ip
            }


            params = [
                ('opid', str(uuid.uuid4()).replace('-', '').upper()),
                ('id', '292841'),
                ('cobrandid', str(uuid.uuid4())), 
                ('mkt', 'EN-US'),
                ('lc', '1033'),
                ('uaid', str(uuid.uuid4())),
            ]
            flow_token = f'-Dm*IVWKvkpi2U!rCGO8Dx1iFSIxIF5kgaReQI*d59ThpSaUtjnZBbF7N30v3S2jsFQyGwyLEcdUDJ6Czjospau5JDwRLPqydt68cHjFVRv0MI863h6YNK7rTpTaOKjIPsytA8hTd68KS2klGeXGmK6PgqwS!MNPLDnEXeagWQjftxzH88TlkEZjpVO5DHI235fDlQGvvys3tnagFr6XpjRsEN15veMTur1ImyiToxnW6ECDiH2yCa7yQLEVprA5Yfkr9NiVa5Jxp0mXFn5KGSmU${uuid.uuid4().hex}'
            json_data = {
                'checkPhones': False,
                'country': '',
                'federationFlags': 3,
                'flowToken': flow_token,
                'forceotclogin': False,
                'isCookieBannerShown': False,
                'isExternalFederationDisallowed': False,
                'isFederationDisabled': False,
                'isFidoSupported': True,
                'isOtherIdpSupported': True,
                'isRemoteConnectSupported': False,
                'isRemoteNGCSupported': True,
                'isSignup': False,
                'originalRequest': '',
                'otclogindisallowed': False,
                'uaid': str(uuid.uuid4()), 
                'username': f'{username}@hotmail.com',
            }

            response = requests.post(
                'https://login.live.com/GetCredentialType.srf',
                params=params,
                cookies=cookies,
                headers=headers,
                json=json_data,
            )
            if '"IfExistsResult":1' in response.text:
                return {"type":"hotmail","isAvailable":True,'dev':'@t5omas'}
            elif '"IfExistsResult":0':
                return {"type":"hotmail","isAvailable":False,'dev':'@t5omas'}
            else:
                return 'Error With request please Send to --> @t5omas '
                
                
                
    def Outlook(username):
        random_ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        cookies = {
            'MicrosoftApplicationsTelemetryDeviceId': str(uuid.uuid4),
            'MSFPC': f'GUID=f{str(uuid.uuid4().hex)}&HASH=5a8b&LV=202409&V=4&LU=1726708584502',
            'MUID': str(uuid.uuid4().hex),
            '_pxvid': str(uuid.uuid4),
            'logonLatency': 'LGN01=638630045570418108',
            'amsc': '3/kyc9AFFGTjBmKvC/6jLJ7joCAK0jkV7rZFltiHV+cwAUZpHHY3eju+6CZKM3Cj0coXcS5TrzcxkWaAP98OD0Az29X8zhV7YdcPkSJDFrCXHs7CyDibJfucUIcPPGkCivtUp6iTRC1PmEdG4h8V2N1hPS806YzopEmWRIQx7Pl2cMFOKKUOKXhx7WBZwRNdlMUhj+Ez+mhIs/G6eH8Vnc7AaLG4sxSykoaM0uifU0L1+gxei1ED79i8mUEvkpmRySj2n8JyCzhOlYIb265TcDPxvwX+eBzMuZb+jgBt8Wk=:2:3c',
            'ai_session': 'x86SXzMmuaa9CgpoR4cgo8|1727407773082|1727407773082',
            'fptctx2': 'taBcrIH61PuCVH7eNCyH0I1otfYAPn9VOPY9aMX8tO1RkWgq2m174KN7LvQacI4UeqMh2BXGzaobu8W%252brBibMn8CDVBG%252byTSM%252f25JTka9bOnNYF1Xgkj9VD4mL2g1VXDAA7D4XjS5PiTIoH5MkL9p8d8x63%252fHvrQC1JHaE%252fnhOlWw37nb1DvfX3%252f0njCoqm7QgG2vs0SnR%252bEANOG7IhUPVneOLLIOhAq8vHDnFl8QLHZH8%252b1pa3fu5MbITkKfXo9SREyEEz6Frky4mLwzgWGq2V5znUbsRjv2rf4pC0FFMCaboaKEhb9wX82Qq414do2ZNUhJb1gIxZMRZ5uWT7wvA%253d%253d',
            '_px3': '7aa5ea4913c79ec9118bfa44e5a369d0b223d9e2f0735e547e7f990e3ba2939b:EazFbSlOCxSBnNAroaNaXvalNK8IALR3s98Yf7oav7DgtwxxwxbZbIqUMygntTyk/RqSieu9c6lQjcMrnKMARg==:1000:C0yRLFfD6Su+qOXUvCIfLqHO0xCXeZnqoqduLR3r9N/0tsUTamHaGJVqwfWjvA6hx1KhIeZ6K1/sWrI66uqRHO82/KHTwlpCEHEprv2osGMWxH8SMy7Re3q9LQRlKjI7pNC8U5gcDN85aslPOmvYMrbtml5tbr3l6Yu6PEbKIBdscZeejhq8pnzFHESBmVBUWVX2wHYI6pLG4ejwtcx6OPfVPEw8Aj7Pg/ZJ13OvcBU=',
            '_pxde': f'{str(uuid.uuid4().hex)}:eyJ0aW1lc3RhbXAiOjE3Mjc0MDc3NjI1MDksImZfa2IiOjAsImlwY19pZCI6W1s0sImluY19pZCI6WyI2ZDJkODk4ZjUzMGM0ODgxMWY1MTViNjAxMDE4YmY1YSJdfQ==',
        }

        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'canary': 'WazYOCBz6qpSoc3FKOJdRcaSsfB5Pf0hdquKurp5d5nqxi4fC2lc3BFKr2TViKaQA0Z7sBymXMGUV2WF86nHHngJ8uzQDuhmWzSF29hMxV9EXDkZuyVTiSYWPKy2fLvcxKF2aoio9yns8cdoQKEDJuLQ8EwsxKRNbZcWx/SeYmoT1ltGTJgF8XRfSfVDBTiNX6OMFkJIwYOiYT0Q/ampBRfhBm272wr4t7AUSyOmo8ueElA8Eqf5XeFjfje7EYEw:2:3c',
            'client-request-id': str(uuid.uuid4().hex),
            'content-type': 'application/json; charset=utf-8',
            # 'cookie': 'MicrosoftApplicationsTelemetryDeviceId=23a7892a-f083-436c-b495-ec907e200965; MSFPC=GUID=5a8b6ceb2df14ead8624d9617dbd7f29&HASH=5a8b&LV=202409&V=4&LU=1726708584502; MUID=dd50173a7a8842cb86eab584e65ebed0; _pxvid=e46b5923-776f-11ef-b1d0-847f940ff0e1; logonLatency=LGN01=638630045570418108; amsc=3/kyc9AFFGTjBmKvC/6jLJ7joCAK0jkV7rZFltiHV+cwAUZpHHY3eju+6CZKM3Cj0coXcS5TrzcxkWaAP98OD0Az29X8zhV7YdcPkSJDFrCXHs7CyDibJfucUIcPPGkCivtUp6iTRC1PmEdG4h8V2N1hPS806YzopEmWRIQx7Pl2cMFOKKUOKXhx7WBZwRNdlMUhj+Ez+mhIs/G6eH8Vnc7AaLG4sxSykoaM0uifU0L1+gxei1ED79i8mUEvkpmRySj2n8JyCzhOlYIb265TcDPxvwX+eBzMuZb+jgBt8Wk=:2:3c; ai_session=x86SXzMmuaa9CgpoR4cgo8|1727407773082|1727407773082; fptctx2=taBcrIH61PuCVH7eNCyH0I1otfYAPn9VOPY9aMX8tO1RkWgq2m174KN7LvQacI4UeqMh2BXGzaobu8W%252brBibMn8CDVBG%252byTSM%252f25JTka9bOnNYF1Xgkj9VD4mL2g1VXDAA7D4XjS5PiTIoH5MkL9p8d8x63%252fHvrQC1JHaE%252fnhOlWw37nb1DvfX3%252f0njCoqm7QgG2vs0SnR%252bEANOG7IhUPVneOLLIOhAq8vHDnFl8QLHZH8%252b1pa3fu5MbITkKfXo9SREyEEz6Frky4mLwzgWGq2V5znUbsRjv2rf4pC0FFMCaboaKEhb9wX82Qq414do2ZNUhJb1gIxZMRZ5uWT7wvA%253d%253d; _px3=7aa5ea4913c79ec9118bfa44e5a369d0b223d9e2f0735e547e7f990e3ba2939b:EazFbSlOCxSBnNAroaNaXvalNK8IALR3s98Yf7oav7DgtwxxwxbZbIqUMygntTyk/RqSieu9c6lQjcMrnKMARg==:1000:C0yRLFfD6Su+qOXUvCIfLqHO0xCXeZnqoqduLR3r9N/0tsUTamHaGJVqwfWjvA6hx1KhIeZ6K1/sWrI66uqRHO82/KHTwlpCEHEprv2osGMWxH8SMy7Re3q9LQRlKjI7pNC8U5gcDN85aslPOmvYMrbtml5tbr3l6Yu6PEbKIBdscZeejhq8pnzFHESBmVBUWVX2wHYI6pLG4ejwtcx6OPfVPEw8Aj7Pg/ZJ13OvcBU=; _pxde=7772a0b37bf604b90b3694fcf0948ee02c5701da67096f4d8f7a8b96ced01e19:eyJ0aW1lc3RhbXAiOjE3Mjc0MDc3NjI1MDksImZfa2IiOjAsImlwY19pZCI6W10sImluY19pZCI6WyI2ZDJkODk4ZjUzMGM0ODgxMWY1MTViNjAxMDE4YmY1YSJdfQ==',
            'correlationid': str(uuid.uuid4().hex),
            'hpgact': '0',
            'hpgid': '200225',
            'origin': 'https://signup.live.com',
            'priority': 'u=1, i',
            'referer': 'https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=161&ct=1727407757&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3dd357c20b-59f3-c41a-e87b-1d06e3dd99ed&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&lic=1&uaid=11d20b56cc384acca1a82598b93a26d4',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'X-Forwarded-For': random_ip
        }

        json_data = {
            'includeSuggestions': True,
            'signInName': f'{username}@outlook.com',
            'uiflvr': 1001,
            'scid': 100118,
            'uaid': '11d20b56cc384acca1a82598b93a26d4',
            'hpgid': 200225,
        }

        response = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames?lcid=1033&wa=wsignin1.0&rpsnv=161&ct=1727407757&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3dd357c20b-59f3-c41a-e87b-1d06e3dd99ed&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&lic=1&uaid=11d20b56cc384acca1a82598b93a26d4',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        response_json = response.json()
        try:
            if '"isAvailable":true' in response.text:
                at = response_json['isAvailable']
                return {"type":"hotmail","isAvailable":at,'dev':'@t5omas'}
            elif '"isAvailable":false':
                af = response_json['isAvailable']
                return {"type":"hotmail","isAvailable":af,'dev':'@t5omas'}
        except:
            microsoft_app_id = str(uuid.uuid4())
            uaid = str(uuid.uuid4())
            msfpc_guid = str(uuid.uuid4())
            muid = ''.join(random.choice('0123456789abcdef') for _ in range(32))
            mscc = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}-IQ"
            msfpc = f"GUID={msfpc_guid}&HASH={''.join(random.choice('0123456789abcdef') for _ in range(4))}&LV={random.randint(202301, 202412)}&V=4&LU={random.randint(1600000000000, 1800000000000)}"
            cookies = {
                'MUID': muid,
                'MSCC': mscc,
                'MicrosoftApplicationsTelemetryDeviceId': microsoft_app_id,
                'MSFPC': msfpc,
                'MSPBack': '0',
                'logonLatency': f"LGN01={random.randint(100000000000000000, 999999999999999999)}",
                'uaid': uaid,
                'MSPRequ': 'id=292841&lt=1727198966&co=0',
                'MSPOK': '$uuid-bcd56121-cb0b-47fa-afef-125ee97242c3',
                'OParams': ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!*') for _ in range(200)),
                'amsc': ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/') for _ in range(150)) + ":2:3c",
                'ai_session': f"{str(uuid.uuid4())}|{random.randint(1600000000000, 1800000000000)}|{random.randint(1600000000000, 1800000000000)}",
                'fptctx2': ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%') for _ in range(100)),
            }
            client_request_id = str(uuid.uuid4())
            correlation_id = str(uuid.uuid4())

            headers = {
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-type': 'application/json; charset=utf-8',
                'Origin': 'https://login.live.com',
                'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=161&ct=1727198965&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26deeplink%3dowa%252f%26RpsCsrfState%3d12fa363f-dee8-af36-da7a-8bda7a184fdc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'client-request-id': client_request_id,
                'correlationId': correlation_id,
                'hpgact': '0',
                'hpgid': str(random.randint(1, 100)),
                'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'X-Forwarded-For': random_ip
            }


            params = [
                ('opid', str(uuid.uuid4()).replace('-', '').upper()),
                ('id', '292841'),
                ('cobrandid', str(uuid.uuid4())), 
                ('mkt', 'EN-US'),
                ('lc', '1033'),
                ('uaid', str(uuid.uuid4())),
            ]
            flow_token = f'-Dm*IVWKvkpi2U!rCGO8Dx1iFSIxIF5kgaReQI*d59ThpSaUtjnZBbF7N30v3S2jsFQyGwyLEcdUDJ6Czjospau5JDwRLPqydt68cHjFVRv0MI863h6YNK7rTpTaOKjIPsytA8hTd68KS2klGeXGmK6PgqwS!MNPLDnEXeagWQjftxzH88TlkEZjpVO5DHI235fDlQGvvys3tnagFr6XpjRsEN15veMTur1ImyiToxnW6ECDiH2yCa7yQLEVprA5Yfkr9NiVa5Jxp0mXFn5KGSmU${uuid.uuid4().hex}'
            json_data = {
                'checkPhones': False,
                'country': '',
                'federationFlags': 3,
                'flowToken': flow_token,
                'forceotclogin': False,
                'isCookieBannerShown': False,
                'isExternalFederationDisallowed': False,
                'isFederationDisabled': False,
                'isFidoSupported': True,
                'isOtherIdpSupported': True,
                'isRemoteConnectSupported': False,
                'isRemoteNGCSupported': True,
                'isSignup': False,
                'originalRequest': '',
                'otclogindisallowed': False,
                'uaid': str(uuid.uuid4()), 
                'username': f'{username}@outlook.com',
            }

            response = requests.post(
                'https://login.live.com/GetCredentialType.srf',
                params=params,
                cookies=cookies,
                headers=headers,
                json=json_data,
            )
            if '"IfExistsResult":1' in response.text:
                return {"type":"hotmail","isAvailable":True,'dev':'@t5omas'}
            elif '"IfExistsResult":0':
                return {"type":"hotmail","isAvailable":False,'dev':'@t5omas'}
            else:
                return 'Error With request please Send to --> @t5omas '
    def yahoo(username):
        cookies = {
            'A3': 'd=AQABBCp862YCECC0g7K9RZaxT9XeIYd0L98FEgEBAQHN7Gb1Zlx0yyMA_eMAAA&S=AQAAAuyGDHe0H4pgkpGm7O60qTU',
            'A1': 'd=AQABBCp862YCECC0g7K9RZaxT9XeIYd0L98FEgEBAQHN7Gb1Zlx0yyMA_eMAAA&S=AQAAAuyGDHe0H4pgkpGm7O60qTU',
            'A1S': 'd=AQABBCp862YCECC0g7K9RZaxT9XeIYd0L98FEgEBAQHN7Gb1Zlx0yyMA_eMAAA&S=AQAAAuyGDHe0H4pgkpGm7O60qTU',
            'cmp': 't=1726850748&j=0&u=1---',
            'gpp': 'DBAA',
            'gpp_sid': '-1',
            'tbla_id': uuid.uuid4(),
            'axids': 'gam=y-BmUBYKFE2uJAwiJGVjvQZplkTW9.HRyP~A&dv360=eS1RR2lrQTZCRTJ1R0pjSU9nRjhPZHJDVldxVzBubklqSn5B&ydsp=y-0DWl0phE2uIYXYqTyKdPWj9GQDqThO2g~A&tbla=y-H7I421tE2uIZm8oLAFyn54ZGSEN2Y8rA~A',
            'AS': 'v=1&s=Du4NAl7c&d=A66eef852|kPMHFar.2SokL7CT9.OkEiC8OxRFHF1f0sduk_kWsGX5U_VYvWaTPnbn0Csf5ErDyJ.U3ewusEL3Wxq5w2uFYQ0sg9buel677xITg5Od4NH64nIYmCekHxdvlX4AKLyrrhyFFw5.LtgwIDtR5GhVuswgTZ0sTvI0HjuFGmlsycbAHymxSAfT9NOXbDyA74CVywQMYPMdOxBzBWx5JBUZDl2PEtZbg6.4RsUe7FBVm9eeRVcf6s1VmW1SCsZGLuC6.zdnUWL_VluWcSN1Z27T2NVKZBI0jQ.gklm2oF6hAGDmH.h7IKk5USgZPlipYGkrb11a_yFF7zOJBzDQqb9wmtc8EyTciXo30m7_D0lRELgGA83hy29zL9bJPtjKppgNy45.T20GPJOYAyFOFTfgZgG5HgTx5lJZF8Zxzr1Hii_7iyLRpjxwrBNLBVp6UzQrFlNwQ86kmZiUK2N_lw1C39VXRL3_Z5bCsf72iOED.fIeC9UhTSAs0G2DXP4RJfjixeXHocrfVr4ym9OaULklx0axzaKoWebAOhC3chjK8j__BgYQ7rRpEPwAcE_bHfkHL9RvGYDagHrNZZU7NlNf1xt6sef0b9_iZ9.tsELjG8zKjCimgDCsGtoVq6O0Xhn0xaMFcbdFnrFHR0NyE0vYnrEvlNgeSMasIoaD6D6H2XpPKSq1ID_5crSgZxMH7FyjZNGMIAMWT5Hk3Wt0EDZyO3GPu0anZ8lg2pRhOUsESC6EgMVX3uX25mN9mHac_AUrTI9CIAC8kr_lv3548PIPDd6jccEdIWmBWeoVFQXMNOgv0APhugwSqSb7T.FFemaoQgK8o2sh4zqGv_vKXoTLRl6q3ZKEgFs-~A|B66eef865|n4TueIz.2TpbTzY4mTtUKMG56ABvyIWzWX4DVvwR0odHaaDkvO3zp_vsCx6QX_ac.FCxQ.vKet.bFUZTtbk_70aWAcM5QwQK_E7IDa.HmOYknCNBTRzO.HRh8ZslDv4aKIJPdCWwvwg6P0blaJehYLv0QpNU1_zVoIMiILJOtahyIgT63lvh37d2ohsHSWVNuunsDyNxfrFLe5VkJFb_r8TNEIhvVC64KLoqG1K4zt1qdehsmW7NwVOKEZtWKmtoYusDnRiEDSoZ0xK9NdwvYZDxaIBir11i2WploW_pKNYe57RsepFXQpVISicbEeLh0zWZ2E8ZrjsyqJpwf.9GMHEB_Jc9Iyvnns1iR.m93Qw14vkjiSiDhGdSzeDZZjHE9COP7xpijrxmzReEpLRXdQ0YBxIk.z6Z3UXmwOc3WDGhjgyzQc1ue6KvFYYSI6m4pMA6nX94EkONy2R_ihO1z02bxiz0JnRzl4n3It1oYaOJkEV8iD6GLnVOSVhdwVksWqmftZutpPow8xxi8eZ7K88XHL9.H7BgtS_957_quto8SUPZPf_tOtVkZqz4onSahNF8xAUnezlLbQNw4Fll1F1W3VQBakPRpmDVaQxCMcpDiPrdgXHfMer5Dx4pHd5Sfq2LjRuB4EC.7casX9VY33HmwvVX8phbEep.8bmKGoo048Dg..nMs10QUTdKaCf8tZTLeaG33gqcsjO6v6hucKThasWBzGCd92iynN1Hpz_npdrT_0bbCfdJATi95OgKiZhVdVLXEnp3S1KpuB07GEiSrf6XIlAiSUiUoVqrwsZ7cR1YQe9tUTRnABseI3Xh1QtvbwlQ2T7clDr8cf_t_2u._LXyw8Jkbbzp_BVzbur78dtL2xZKFNxijep9ZkLKL06sYfPAjH7NfYRMJ69HW_yg2mP715xg7V._NUspYTedcl3iiMX4wqG_2miA_Oy6eorINZ.s7jYz59ch9uYRMazkoEhl7HMhuui0MUFpGfK7g7KR~A',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'A3=d=AQABBCp862YCECC0g7K9RZaxT9XeIYd0L98FEgEBAQHN7Gb1Zlx0yyMA_eMAAA&S=AQAAAuyGDHe0H4pgkpGm7O60qTU; A1=d=AQABBCp862YCECC0g7K9RZaxT9XeIYd0L98FEgEBAQHN7Gb1Zlx0yyMA_eMAAA&S=AQAAAuyGDHe0H4pgkpGm7O60qTU; A1S=d=AQABBCp862YCECC0g7K9RZaxT9XeIYd0L98FEgEBAQHN7Gb1Zlx0yyMA_eMAAA&S=AQAAAuyGDHe0H4pgkpGm7O60qTU; cmp=t=1726850748&j=0&u=1---; gpp=DBAA; gpp_sid=-1; tbla_id=cd49cae0-21a4-4008-bffa-a74bdd28dbeb-tuctde501ea; axids=gam=y-BmUBYKFE2uJAwiJGVjvQZplkTW9.HRyP~A&dv360=eS1RR2lrQTZCRTJ1R0pjSU9nRjhPZHJDVldxVzBubklqSn5B&ydsp=y-0DWl0phE2uIYXYqTyKdPWj9GQDqThO2g~A&tbla=y-H7I421tE2uIZm8oLAFyn54ZGSEN2Y8rA~A; AS=v=1&s=Du4NAl7c&d=A66eef852|kPMHFar.2SokL7CT9.OkEiC8OxRFHF1f0sduk_kWsGX5U_VYvWaTPnbn0Csf5ErDyJ.U3ewusEL3Wxq5w2uFYQ0sg9buel677xITg5Od4NH64nIYmCekHxdvlX4AKLyrrhyFFw5.LtgwIDtR5GhVuswgTZ0sTvI0HjuFGmlsycbAHymxSAfT9NOXbDyA74CVywQMYPMdOxBzBWx5JBUZDl2PEtZbg6.4RsUe7FBVm9eeRVcf6s1VmW1SCsZGLuC6.zdnUWL_VluWcSN1Z27T2NVKZBI0jQ.gklm2oF6hAGDmH.h7IKk5USgZPlipYGkrb11a_yFF7zOJBzDQqb9wmtc8EyTciXo30m7_D0lRELgGA83hy29zL9bJPtjKppgNy45.T20GPJOYAyFOFTfgZgG5HgTx5lJZF8Zxzr1Hii_7iyLRpjxwrBNLBVp6UzQrFlNwQ86kmZiUK2N_lw1C39VXRL3_Z5bCsf72iOED.fIeC9UhTSAs0G2DXP4RJfjixeXHocrfVr4ym9OaULklx0axzaKoWebAOhC3chjK8j__BgYQ7rRpEPwAcE_bHfkHL9RvGYDagHrNZZU7NlNf1xt6sef0b9_iZ9.tsELjG8zKjCimgDCsGtoVq6O0Xhn0xaMFcbdFnrFHR0NyE0vYnrEvlNgeSMasIoaD6D6H2XpPKSq1ID_5crSgZxMH7FyjZNGMIAMWT5Hk3Wt0EDZyO3GPu0anZ8lg2pRhOUsESC6EgMVX3uX25mN9mHac_AUrTI9CIAC8kr_lv3548PIPDd6jccEdIWmBWeoVFQXMNOgv0APhugwSqSb7T.FFemaoQgK8o2sh4zqGv_vKXoTLRl6q3ZKEgFs-~A|B66eef865|n4TueIz.2TpbTzY4mTtUKMG56ABvyIWzWX4DVvwR0odHaaDkvO3zp_vsCx6QX_ac.FCxQ.vKet.bFUZTtbk_70aWAcM5QwQK_E7IDa.HmOYknCNBTRzO.HRh8ZslDv4aKIJPdCWwvwg6P0blaJehYLv0QpNU1_zVoIMiILJOtahyIgT63lvh37d2ohsHSWVNuunsDyNxfrFLe5VkJFb_r8TNEIhvVC64KLoqG1K4zt1qdehsmW7NwVOKEZtWKmtoYusDnRiEDSoZ0xK9NdwvYZDxaIBir11i2WploW_pKNYe57RsepFXQpVISicbEeLh0zWZ2E8ZrjsyqJpwf.9GMHEB_Jc9Iyvnns1iR.m93Qw14vkjiSiDhGdSzeDZZjHE9COP7xpijrxmzReEpLRXdQ0YBxIk.z6Z3UXmwOc3WDGhjgyzQc1ue6KvFYYSI6m4pMA6nX94EkONy2R_ihO1z02bxiz0JnRzl4n3It1oYaOJkEV8iD6GLnVOSVhdwVksWqmftZutpPow8xxi8eZ7K88XHL9.H7BgtS_957_quto8SUPZPf_tOtVkZqz4onSahNF8xAUnezlLbQNw4Fll1F1W3VQBakPRpmDVaQxCMcpDiPrdgXHfMer5Dx4pHd5Sfq2LjRuB4EC.7casX9VY33HmwvVX8phbEep.8bmKGoo048Dg..nMs10QUTdKaCf8tZTLeaG33gqcsjO6v6hucKThasWBzGCd92iynN1Hpz_npdrT_0bbCfdJATi95OgKiZhVdVLXEnp3S1KpuB07GEiSrf6XIlAiSUiUoVqrwsZ7cR1YQe9tUTRnABseI3Xh1QtvbwlQ2T7clDr8cf_t_2u._LXyw8Jkbbzp_BVzbur78dtL2xZKFNxijep9ZkLKL06sYfPAjH7NfYRMJ69HW_yg2mP715xg7V._NUspYTedcl3iiMX4wqG_2miA_Oy6eorINZ.s7jYz59ch9uYRMazkoEhl7HMhuui0MUFpGfK7g7KR~A',
            'origin': 'https://login.yahoo.com',
            'priority': 'u=1, i',
            'referer': 'https://login.yahoo.com/account/create?.lang=en-US&src=homepage&specId=yidregsimplified&activity=ybar-signin&pspid=2023538075&.done=https%3A%2F%2Fwww.yahoo.com%2F&done=https%3A%2F%2Fwww.yahoo.com%2F&intl=xa&context=reg',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': us(),
            'x-requested-with': 'XMLHttpRequest',
            'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        }

        params = {
            'validateField': 'userId',
        }

        data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A12%2C%22timezoneOffset%22%3A-180%2C%22timezone%22%3A%22Asia%2FBaghdad%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(NVIDIA)~ANGLE%20(NVIDIA%2C%20NVIDIA%20GeForce%20RTX%203060%20(0x00002544)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221920%22%2C%22h%22%3A%221080%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%221032%22%2C%22h%22%3A%221920%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1726851820742%2C%22render%22%3A1726851823402%7D%7D&specId=yidregsimplified&context=REGISTRATION&cacheStored=&crumb=icEW92SPRieKouPo1kWRuQ&acrumb=Du4NAl7c&sessionIndex=Qg--&done=https%3A%2F%2Fwww.yahoo.com%2F&googleIdToken=&authCode=&attrSetIndex=0&specData=&tos0=oath_freereg%7Cxa%7Cen-JO&multiDomain=&firstName=gfevdqattgfq&lastName=dtgqdtgqatg&userid-domain=yahoo&userId={username}&password=&mm=&dd=&yyyy=&signup='

        response = requests.post('https://login.yahoo.com/account/module/create', params=params, cookies=cookies, headers=headers, data=data)
        try:
            if '"userId","error":"IDENTIFIER_NOT_AVAILABLE"' in response.text:
                return {"type":"yahoo","isAvailable":False,'dev':'@t5omas'}
            else:
                return {"type":"yahoo","isAvailable":True,'dev':'@t5omas'}
        except:
            return 'FIELD EMPTY'
    def aol(username):
        cookies = {
            'A1': 'd=AQABBLSm7WYCEO1Xq1EdjejuwjJWxMPEZ3wFEgEBAQH47mb3Zlx0yyMA_eMAAA&S=AQAAAsyJsX_CRm9sEdlOdBb9LEs',
            'A3': 'd=AQABBLSm7WYCEO1Xq1EdjejuwjJWxMPEZ3wFEgEBAQH47mb3Zlx0yyMA_eMAAA&S=AQAAAsyJsX_CRm9sEdlOdBb9LEs',
            'A1S': 'd=AQABBLSm7WYCEO1Xq1EdjejuwjJWxMPEZ3wFEgEBAQH47mb3Zlx0yyMA_eMAAA&S=AQAAAsyJsX_CRm9sEdlOdBb9LEs',
            'cmp': 't=1726850748&j=0&u=1---',
            'gpp': 'DBAA',
            'gpp_sid': '-1',
            'weathergeo': '%2233.33%7C44.39%7CBaghdad%7CBaghdad%7CIraq%7C0%7C56055276%22',
            'axids': 'gam=y-BmUBYKFE2uJAwiJGVjvQZplkTW9.HRyP~A&dv360=eS1RR2lrQTZCRTJ1R0pjSU9nRjhPZHJDVldxVzBubklqSn5B&ydsp=y-0DWl0phE2uIYXYqTyKdPWj9GQDqThO2g~A&tbla=y-H7I421tE2uIZm8oLAFyn54ZGSEN2Y8rA~A',
            'tbla_id': uuid.uuid4(),
            'AS': 'v=1&s=bArfTXR6&d=A66eef85b|R5gtDLT.2Sq1nqPxLFmXYctRjCnGjF3CKLUFnqJAwlyNk.8l4N97Gn6kasj_MwWYlbM.45ixiU65lI2M5UEAzoYzpNhlcL2jxN9Wd6Q1ll4vhQjOJoZD1AUBS7w6oY4T.MIix9BL0dbQTe0dT7NShK4uto0eaCGwZm6itS3eQr1ly_fzO1fa3iODFW5lprDhwdZSWkgLrm2QrcmtcWU2QwB343uNp1p6vsuZYdJU8Jdr4580SaSS4Zes3IJmU5EWN8nh7y4bCPp93MK7XJqEzVqFvbKPAjYU1CHmSlO7_5gVS6bMswgDU5JWXuN3eH00bdhZgccEdFXN8s1J_wfSJlhNJMoKgT4pN5fnuORlqHuCBxj5MjOlQWBo1Sux37et_vAwDP_o2GeYXO.7MaZnh27H1hbhfm1u.hn28vrZ8R0NufkLRHLRU30PrTQwtQR9PlSCrklna3_4jtJ2zqEGtteL0U8d6J4J36kVjtVpDxVpdiJg_ylAGrGjSFRIp2t2kg5r0EDP.x02iZKWrGAY5xBIByjxii8QbOG74XWlewNyEZq3y1E6oSV75bhugYCV3tqDF.PMpdNA.AmvpaOaNG3IB0TiVg5EfdwOsKHZIWtj5PcvZTrwn7tB7j852cvCtbt.4Snm41UevHI1.bhOUzCGWDQvC07a69Youtv3oTvRcuDrogkGR3xna24RKcrl9PeE0eN..Rn9bKrUvkV6w2U1N_3ehzpF3EAicDM1yuaLPcVTQdzT.CJuxUgRlR7nWzV8T7ejWNvS5WY9sd9D3mKRQqmgt4CvwKQLORsQfRXKbMvq2HhYkHXz6kJxmYFknZRk.fd3tckQ9uHlnam2oqrg_2QG76yCtHXRwOhLfQduR2wJ1vzNnm9BjS.5gnZiKrx19G1C~A|B66eef867|B6VfVSL.2To8kHlfqUvPWpgJoQY46ZDRdyy_YvHszw0gIyd29a0eTuCk51xDKfmSuBR..IkD5iyZmnljzQvXcIXAjL8NyQ1dkSwPgQoEEOWo0kF6vc_cLhj_btKp8OQTVRn7Bbu.vDjB5ZeSDkyJsROP0_ozFpYYDdfkb1JTIcej2V3FzSveQOHIqIakU434406D0s9l2HH0BpTsSbyz8nXciTit6bjKKXTCk7iwP_B8B4BETERIUSGzxNDE8m_2SZmRyZ_4h6wkT1RqEt9Yde_o23lx1bz0sbgjZG8hkvScdC53zurUnPInoq7E0t4sgKzH5YE9k_cneWt6p4oHNiB6uX0Sq4ZE5TghsOGCSodYfjWNEufMkc4f1K2zuXGVJIbAaUuRcRvdHqFCRd4zkFRU8P1aQvpxa32QB.psaNWgQRZc0rfTvEP0TT8KsU9tjbRXuYDKgwqseZW6RfshvcBP7YKFIttuizCl0amlN0dVC6ECE9q_AKUoSXudi6pxt7pdQ4tIx7ijZGaDJOhec6ASTjZSJUKDs2ZHmvfWU6j_3OpkMwUXUr7kwtU.jHf5y7ExHFGXaC3A4mpfLCQastGnEnq3aYUHQw_vVVtQawuiZvBrMJ44SNgsQ5aOe8wjwO731_ClnQ9Ro1ezHCn04W_wUK7QyOilB59wMIsF61lUwuCFYPtBmiGIs.bD8MSAHChGPrfKzk6ZyeDtF6faUdy6iXjIzsA3bLbdkbYl9kBPOnIO8mqUbJ2vnkVSJEPqREGzYILQYjB0nvZLw757ZZ17r_eWSjb1dL52xxkfchMutoH.HS4UgRFmKyF2UxTzjGCmatlckmQ4qWJw1ke6l2nny35MwoYVTCu6tO73MnkIUhulJ8ZrGs.t_60Qn2ZL0hZFbysxpN0JKv77jX1rm7hD79fyePVggmNd_0eV.KnJlvk0p852_jvILXRQFBRBJXx.g75L5zSF0X5XW236uUpub.gbrGzq9FIwEyZ.qOG2gA--~A',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'A1=d=AQABBLSm7WYCEO1Xq1EdjejuwjJWxMPEZ3wFEgEBAQH47mb3Zlx0yyMA_eMAAA&S=AQAAAsyJsX_CRm9sEdlOdBb9LEs; A3=d=AQABBLSm7WYCEO1Xq1EdjejuwjJWxMPEZ3wFEgEBAQH47mb3Zlx0yyMA_eMAAA&S=AQAAAsyJsX_CRm9sEdlOdBb9LEs; A1S=d=AQABBLSm7WYCEO1Xq1EdjejuwjJWxMPEZ3wFEgEBAQH47mb3Zlx0yyMA_eMAAA&S=AQAAAsyJsX_CRm9sEdlOdBb9LEs; cmp=t=1726850748&j=0&u=1---; gpp=DBAA; gpp_sid=-1; weathergeo=%2233.33%7C44.39%7CBaghdad%7CBaghdad%7CIraq%7C0%7C56055276%22; axids=gam=y-BmUBYKFE2uJAwiJGVjvQZplkTW9.HRyP~A&dv360=eS1RR2lrQTZCRTJ1R0pjSU9nRjhPZHJDVldxVzBubklqSn5B&ydsp=y-0DWl0phE2uIYXYqTyKdPWj9GQDqThO2g~A&tbla=y-H7I421tE2uIZm8oLAFyn54ZGSEN2Y8rA~A; tbla_id=cd49cae0-21a4-4008-bffa-a74bdd28dbeb-tuctde501ea; AS=v=1&s=bArfTXR6&d=A66eef85b|R5gtDLT.2Sq1nqPxLFmXYctRjCnGjF3CKLUFnqJAwlyNk.8l4N97Gn6kasj_MwWYlbM.45ixiU65lI2M5UEAzoYzpNhlcL2jxN9Wd6Q1ll4vhQjOJoZD1AUBS7w6oY4T.MIix9BL0dbQTe0dT7NShK4uto0eaCGwZm6itS3eQr1ly_fzO1fa3iODFW5lprDhwdZSWkgLrm2QrcmtcWU2QwB343uNp1p6vsuZYdJU8Jdr4580SaSS4Zes3IJmU5EWN8nh7y4bCPp93MK7XJqEzVqFvbKPAjYU1CHmSlO7_5gVS6bMswgDU5JWXuN3eH00bdhZgccEdFXN8s1J_wfSJlhNJMoKgT4pN5fnuORlqHuCBxj5MjOlQWBo1Sux37et_vAwDP_o2GeYXO.7MaZnh27H1hbhfm1u.hn28vrZ8R0NufkLRHLRU30PrTQwtQR9PlSCrklna3_4jtJ2zqEGtteL0U8d6J4J36kVjtVpDxVpdiJg_ylAGrGjSFRIp2t2kg5r0EDP.x02iZKWrGAY5xBIByjxii8QbOG74XWlewNyEZq3y1E6oSV75bhugYCV3tqDF.PMpdNA.AmvpaOaNG3IB0TiVg5EfdwOsKHZIWtj5PcvZTrwn7tB7j852cvCtbt.4Snm41UevHI1.bhOUzCGWDQvC07a69Youtv3oTvRcuDrogkGR3xna24RKcrl9PeE0eN..Rn9bKrUvkV6w2U1N_3ehzpF3EAicDM1yuaLPcVTQdzT.CJuxUgRlR7nWzV8T7ejWNvS5WY9sd9D3mKRQqmgt4CvwKQLORsQfRXKbMvq2HhYkHXz6kJxmYFknZRk.fd3tckQ9uHlnam2oqrg_2QG76yCtHXRwOhLfQduR2wJ1vzNnm9BjS.5gnZiKrx19G1C~A|B66eef867|B6VfVSL.2To8kHlfqUvPWpgJoQY46ZDRdyy_YvHszw0gIyd29a0eTuCk51xDKfmSuBR..IkD5iyZmnljzQvXcIXAjL8NyQ1dkSwPgQoEEOWo0kF6vc_cLhj_btKp8OQTVRn7Bbu.vDjB5ZeSDkyJsROP0_ozFpYYDdfkb1JTIcej2V3FzSveQOHIqIakU434406D0s9l2HH0BpTsSbyz8nXciTit6bjKKXTCk7iwP_B8B4BETERIUSGzxNDE8m_2SZmRyZ_4h6wkT1RqEt9Yde_o23lx1bz0sbgjZG8hkvScdC53zurUnPInoq7E0t4sgKzH5YE9k_cneWt6p4oHNiB6uX0Sq4ZE5TghsOGCSodYfjWNEufMkc4f1K2zuXGVJIbAaUuRcRvdHqFCRd4zkFRU8P1aQvpxa32QB.psaNWgQRZc0rfTvEP0TT8KsU9tjbRXuYDKgwqseZW6RfshvcBP7YKFIttuizCl0amlN0dVC6ECE9q_AKUoSXudi6pxt7pdQ4tIx7ijZGaDJOhec6ASTjZSJUKDs2ZHmvfWU6j_3OpkMwUXUr7kwtU.jHf5y7ExHFGXaC3A4mpfLCQastGnEnq3aYUHQw_vVVtQawuiZvBrMJ44SNgsQ5aOe8wjwO731_ClnQ9Ro1ezHCn04W_wUK7QyOilB59wMIsF61lUwuCFYPtBmiGIs.bD8MSAHChGPrfKzk6ZyeDtF6faUdy6iXjIzsA3bLbdkbYl9kBPOnIO8mqUbJ2vnkVSJEPqREGzYILQYjB0nvZLw757ZZ17r_eWSjb1dL52xxkfchMutoH.HS4UgRFmKyF2UxTzjGCmatlckmQ4qWJw1ke6l2nny35MwoYVTCu6tO73MnkIUhulJ8ZrGs.t_60Qn2ZL0hZFbysxpN0JKv77jX1rm7hD79fyePVggmNd_0eV.KnJlvk0p852_jvILXRQFBRBJXx.g75L5zSF0X5XW236uUpub.gbrGzq9FIwEyZ.qOG2gA--~A',
            'origin': 'https://login.aol.com',
            'priority': 'u=1, i',
            'referer': 'https://login.aol.com/account/create?intl=us&src=fp-us&activity=default&pspid=1197803361&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3Dyxv4WzEx5CXDrdK1htgNs8z2herQ6bhf%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bguce-w%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E&specId=yidregsimplified',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': us(),
            'x-requested-with': 'XMLHttpRequest',
            'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        }

        params = {
            'validateField': 'userId',
        }

        data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A12%2C%22timezoneOffset%22%3A-180%2C%22timezone%22%3A%22Asia%2FBaghdad%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(NVIDIA)~ANGLE%20(NVIDIA%2C%20NVIDIA%20GeForce%20RTX%203060%20(0x00002544)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221920%22%2C%22h%22%3A%221080%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%221032%22%2C%22h%22%3A%221920%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1726850791543%2C%22render%22%3A1726850794222%7D%7D&specId=yidregsimplified&context=REGISTRATION&cacheStored=&crumb=ZfXuy9kqN0PbaanqqIOpg&acrumb=bArfTXR6&sessionIndex=Qg--&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3Dyxv4WzEx5CXDrdK1htgNs8z2herQ6bhf%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bguce-w%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E&googleIdToken=&authCode=&attrSetIndex=0&specData=&tos0=oath_freereg%7Cus%7Cen-US&multiDomain=&firstName=&lastName=&userid-domain=yahoo&userId={username}&password=&mm=&dd=&yyyy=&signup='

        response = requests.post('https://login.aol.com/account/module/create', params=params, cookies=cookies, headers=headers, data=data)
        try:
            if '"userId","error":"IDENTIFIER_EXISTS"' in response.text:
                return {"type":"aol","isAvailable":False,'dev':'@t5omas'}
            else:
                return {"type":"aol","isAvailable":True,'dev':'@t5omas'}
        except:
            return 'FIELD EMPTY'
            
            
class Telegram:
    def User_Checker(username_list, api_id, api_hash,sesname):
        async def change_username(session_name, api_id, api_hash, new_username):
            async with TelegramClient(session_name, api_id, api_hash) as app:
                try:
                    await app(functions.account.UpdateUsernameRequest(username=new_username))
                    return {
                            'State': 'Good',
                            'Username': new_username,
                            'changed': True
                            }
                except errors.UsernameOccupiedError:
                    return {
                            'State': 'Good',
                            'Username': new_username,
                            'changed': False
                            }
                except Exception as e:
                    return{'State': 'Good', 'Username': new_username, 'changed': False}

        async def main():
            for userfinlly in username_list:
                cookies = {
                    'stel_ssid': '68deb5a64807bebcd3_3801354700860422975',
                    'stel_dt': '-180',
                }

                headers = {
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://fragment.com',
                    'priority': 'u=1, i',
                    'referer': 'https://fragment.com/',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': str(us()),
                    'x-requested-with': 'XMLHttpRequest',
                    'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
                }

                params = {
                    'hash': 'f4a417f70135439a08',
                }

                data = {
                    'type': 'usernames',
                    'query': userfinlly,
                    'filter': '',
                    'sort': '',
                    'method': 'searchAuctions',
                }

                response = requests.post('https://fragment.com/api', params=params, cookies=cookies, headers=headers, data=data)
                if "Unavailable" in response.text:
                    change_result = await change_username(sesname, api_id, api_hash, userfinlly)
                    print(change_result)
                else:
                    print({'State': 'Good','Username':userfinlly,'State':'Unavailable'})
        return asyncio.run(main())
    def MakeSes(api_id,api_hash,sesname):
        client = TelegramClient(sesname, api_id, api_hash)
        async def main():
            await client.start()
            return "DONE"
        with client:
            client.loop.run_until_complete(main())
            
            
class insta_app_follower:
    def perfectfollower(username, password):
        headers = {
            "User-Agent": "Dart/3.1 (dart:io)",
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "Authorization": "Bearer kasper",
            "Content-Type": "application/x-www-form-urlencoded",
            'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        }
        data = {'username': username, 'password': password}
        response_json= requests.post("https://perfectfollow.app/api/v1/login", headers=headers, data=data).json()
        if "token" in response_json:
                token = response_json['token']
                return {'status': 'Good', 'Login': 'True', 'dev': 't5omas', 'token': token}
        else:
            return {'status': 'Good', 'Login': 'false', 'dev': 't5omas'}
    def blackfollowe(username, password):
        url = "https://blackfollow.online/api/v1/login"

        payload = f"password={password}&email={username}"

        headers = {
        'User-Agent': "okhttp/3.9.1",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/x-www-form-urlencoded",
        'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        }

        response = requests.post(url, data=payload, headers=headers)
        if '"ok":"1"' in response.text:
            return {'status': 'Good', 'Login': 'True', 'dev': 't5omas'}
        else:
            return {'status': 'Good', 'Login': 'false', 'dev': 't5omas'}


        
        
        
class GPT:
    def chat18(ask):
        url = "https://api.binjie.fun/api/generateStream"
        payload = json.dumps({
            "prompt": ask,
            
            "network": True,
            "system": "",
            "withoutContext": False,
            "stream": False
        }, ensure_ascii=False).encode('utf-8')  
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'Content-Type': "application/json",
    'sec-ch-ua': "\"Not)A;Brand\";v=\"99\", \"Android WebView\";v=\"127\", \"Chromium\";v=\"127\"",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua-mobile': "?1",
    'origin': "https://chat18.aichatos8.com",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://chat18.aichatos8.com/",
    'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i"

        }

        response = requests.post(url, data=payload, headers=headers)
        content = response.content.decode('utf-8')
        return {'content':content,'dev':'@t5omas'}
    def GPT(ask):
        url = "https://us-central1-amor-ai.cloudfunctions.net/chatWithGPT"

        payload = json.dumps({
        "data": {
            "messages": [
            {
                "role": "user",
                "content": ask
            }
            ]
        }
        })

        headers = {
        'User-Agent': "okhttp/5.0.0-alpha.2",
        'Accept-Encoding': "gzip",
        'content-type': "application/json; charset=utf-8"
        }

        response = requests.post(url, data=payload, headers=headers)

        content = response.json()['result']['choices'][0]['message']['content']
        return {'content':content,'dev':'@t5omas'}
        
        
        
        
class TempSocial:
    def __init__(self):
        url = "https://www.1secmail.com/api/v1/"
        params = {
            'action': "genRandomMailbox",
            'count': "1"
        }
        headers = {
            'User-Agent': "okhttp/3.9.1",
            'Accept-Encoding': "gzip"
        }
        req = requests.get(url, params=params, headers=headers).text
        self.email = req.split('["')[1].split('"]')[0]
        print(f" oluşturuldu ✅: {self.email}")
    def refresh_messages(self):
        name = self.email.split('@')[0]
        dom = self.email.split('@')[1]

        url = "https://www.1secmail.com/api/v1/"
        params = {
            'action': "getMessages",
            'login': name,
            'domain': dom,
        }
        headers = {
            'User-Agent': "okhttp/3.9.1",
            'Accept-Encoding': "gzip"
        }
        response = requests.post(url, params=params, headers=headers)
       
    def Temp_Email(self,time):
        while True:
                sleep(time)
                self.refresh_messages()