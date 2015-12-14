from  urllib2 import urlopen, HTTPError
from urlparse import urlparse, parse_qs
from lxml import etree


class Downloader:

    def __init__(self, url, lang='en'):
        self.url = url
        self.v = ''
        self.lang = lang
        self.parse()

    def parse(self):
        parsed_url = urlparse(self.url)
        query = parse_qs(parsed_url.query)
        error = NameError('The url is not valid')
        if parsed_url.netloc == 'www.youtube.com' and query.get('v'):
            self.v = query.get('v')[0]
            if not self.v:
                raise error
        else:
            raise error

    def get_xml(self):
        xml = ''
        url2 = 'https://www.youtube.com/api/timedtext?hl=en_US&v=' + \
                '{video}&type=track&lang={lang}&fmt=1'
        conf = self.get_config_xml()
        lang_match = next(
            (l for l in conf if l.get('lang_code') == self.lang), None)        
        if lang_match:
            if lang_match.get('CC'):
                url2 = url2 + '&name=CC'
            url2 = url2.format(video=self.v, lang=self.lang)
            response = urlopen(url2)
            xml = response.read()
        else:
            raise NameError('Language not available')
        return xml

    def get_config_xml(self, discover=False):
        av_langs = []
        url = 'https://www.youtube.com/api/timedtext?caps=asr&v={video}' +\
            '&key=yttt1&hl=en_US&type=list&tlangs=1&fmts=0&vssids=1&asrs=1'
        url = url.format(video=self.v)
        response = urlopen(url)
        pxml = etree.fromstring(response.read())
        tracks = pxml.xpath('//track')
        for track in tracks:
            av_langs.append({
            'str':track.get('lang_code') + ':' + track.get('lang_translated'),
            'lang_code':track.get('lang_code'), 'CC':track.get('name','')})
        return av_langs
