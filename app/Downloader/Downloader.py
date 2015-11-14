import urllib2
from urlparse import urlparse, parse_qs


class Downloader:

    def getxml(self, url):
        xml = ''
        parsed_url = urlparse(url)
        query = parse_qs(parsed_url.query)
        if query.get('v')[0]:
            url2 = 'http://www.youtube.com/api/timedtext?hl=en_US&v={video}' +\
            '&type=track&lang=en&name=CC&kind&fmt=1'
            url2 = url2.format(video=query.get('v')[0])
            response = urllib2.urlopen(url2)
            xml = response.read()
        return xml
