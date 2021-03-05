"""
Write a function that when given a URL as a string, parses out 
just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""

import re

def domain_name(url):
    if url.find('www') >= 0:
        pattern = 'www.(.*?)\.'
    elif url.find("://") >= 0:
        pattern = '://(.*?)\.'
    elif url.find(".") >= 0:
        #print(url)
        pattern = '(^.+)\.'
    else:
        pattern = '(.*?)'
    match = re.search(pattern, url).group(1)
    print("{}   {}".format(url, match))
    return match

domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")
domain_name("icann.org")
domain_name("url")
