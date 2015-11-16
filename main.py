from app.Downloader import downloader
from app.SubMaker import submaker
from urllib2 import HTTPError
import argparse


def main():
    parser = argparse.ArgumentParser(prog='YTSubPy',
        description='Small program to download subtitles from youtube')
    parser.add_argument('url', help='the url of video')

    r = parser.parse_args()
    url = r.url
    try:
        dwnld = downloader.Downloader()
        xml = dwnld.get_xml(url)
        if xml:
            sub = submaker.SubMaker()
            sub.fromstring(xml)
            sub.tofile()
            print 'Subtitle was generated successfully'
        else:
            raise NameError('Subtitle wasn\'t generated ')
    except HTTPError as e:
        print e
        print 'Subtitle not Found'
    except IOError as e:
        print 'Subtitle wasn\'t generated : ' + e
    except Exception as e:
        print e


if __name__ == '__main__':
    main()
