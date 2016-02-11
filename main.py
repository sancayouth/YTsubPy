import argparse
from urllib2 import HTTPError
from app.Downloader import downloader
from app.SubMaker import submaker


def main():
    parser = argparse.ArgumentParser(prog='YTSubPy',\
            description='Small program to download subtitles from youtube')
    parser.add_argument('url', help='the url of video')
    parser.add_argument('-l', help='language', default='en')
    parser.add_argument('-d', help='discover the available languages',
                        action='store_true')
    arg = parser.parse_args()
    url = arg.url
    lang = arg.l
    discover = arg.d
    try:
        dwnld = downloader.Downloader(url, lang)
        if not discover:
            xml = dwnld.get_xml()
            if xml:
                title = dwnld.get_video_title().encode('cp437', 'ignore')
                sub = submaker.SubMaker()
                sub.fromstring(xml)
                sub.tofile(title)
                print 'Subtitle was generated successfully: ' + title
            else:
                raise NameError('Subtitle wasn\'t generated ')
        else:
            langs = dwnld.get_config_xml()
            for lang in langs:
                print lang.get('str')
    except HTTPError as exception:
        print exception
        print 'Subtitle not Found'
    except IOError as exception:
        print 'Subtitle wasn\'t generated : ' , exception
    except Exception as exception:
        print exception

if __name__ == '__main__':
    main()
