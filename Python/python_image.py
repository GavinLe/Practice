# -*- coding: utf-8 -*-
import urllib
import re
import os

seed_url = 'http://emberteach.ddlisting.com/'
pic_path = './img'

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def download(html):
    reg = r'src="http://(.+?\.(jpg|gif|png))"'
    img_reg = re.compile(reg)
    img_list = re.findall(img_reg, html)
    print "img_list:{0}".format(img_list)
    img_list_url = [ _[0] for _ in img_list]
    print "img_list_url:{0}".format(img_list_url)
    url_save = os.path.join(pic_path)
    if not os.path.exists(url_save):
        os.makedirs(os.makedirs(url_save))
    x = 0
    image = None
    for img_url in img_list_url:
        target = './img/{0}.jpg'.format(x)
        print 'Downloading image to location: ' + target + '\nurl=' + img_url
        image = urllib.urlretrieve("http://"+img_url, target)
        x+=1
    return image

if __name__ == '__main__':
    try:
        html = getHtml(seed_url)
        download(html)
    except Exception,e:
        print u'错了,智障!'
    else:
        print 'Download has finished.'
    finally:
        print u'退出了'