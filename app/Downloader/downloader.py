# -*- coding: utf-8 -*-
from urllib2 import urlopen
from urlparse import urlparse, parse_qs
from lxml import etree


class Downloader(object):

    def __init__(self, url, lang='en'):
        self.url = url
        self.video = ''
        self.lang = lang
        self.parse()

    def parse(self):
        parsed_url = urlparse(self.url)
        query = parse_qs(parsed_url.query)
        error = NameError('The url is not valid')
        if parsed_url.netloc == 'www.youtube.com' and query.get('v'):
            self.video = query.get('v')[0]
            if not self.video:
                raise error
        else:
            raise error

    def get_xml(self):
        xml = ''
        url2 = 'http://video.google.com/timedtext?type=track&v={video}' + \
              '&lang={lang}'
        url2 = url2.format(video=self.video, lang=self.lang)
        conf = self.get_config_xml()
        lang_match = next(
            (l for l in conf if l.get('lang_code') == self.lang), None)
        if lang_match:
            if lang_match.get('CC'):
                url2 = url2 + '&name=CC'
            response = urlopen(url2)
            xml = response.read()
        else:
            raise NameError('Language not available')
        return xml

    def get_config_xml(self):
        av_langs = []
        url = 'http://video.google.com/timedtext?type=list&v={video}'
        url = url.format(video=self.video)
        response = urlopen(url)
        pxml = etree.fromstring(response.read())
        tracks = pxml.xpath('//track')
        for track in tracks:
            av_langs.append({\
            'str': track.get('lang_code') + ':' + track.get('lang_translated'),\
            'lang_code': track.get('lang_code'), 'CC': track.get('name', '')})
        return av_langs


    def get_video_title(self):
        import re
        response = urlopen(self.url)
        html = response.read()
        pattern = re.compile('<title.*?>(.+?)</title>')
        title = re.findall(pattern, html)[0].decode('utf-8')
        return title.split(' - YouTube')[0]
