from  urllib2 import urlopen, HTTPError
from urlparse import urlparse, parse_qs
from lxml import etree


class Downloader:

    def get_xml(self, url):
        xml = ''
        parsed_url = urlparse(url)
        query = parse_qs(parsed_url.query)
        v = query.get('v')[0]
        if v:
            url2 = 'http://www.youtube.com/api/timedtext?hl=en_US&v=' + \
                    '{video}&type=track&lang=en&fmt=1'
            code = self.get_config_xml(v)
            if code == 'CC':
                url2 = url2 + '&name=CC'
            url2 = url2.format(video=v)
            response = urlopen(url2)
            xml = response.read()
        else:
            raise NameError('Parameter v doesn\'t exists, check the url')
        return xml

    def get_config_xml(self, video):
        v = video
        code = ''
        try:
            url = 'https://www.youtube.com/api/timedtext?caps=asr&v={video}' +\
                '&key=yttt1&hl=en_US&type=list&tlangs=1&fmts=0&vssids=1&asrs=1'
            url = url.format(video=v)
            response = urlopen(url)
            pxml = etree.fromstring(response.read())
            track = pxml.xpath('//track[@lang_code=\'en\']')
            code = track[0].attrib.get('name')
        except HTTPError as e:
            print e
        return code
