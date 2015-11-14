from app.Downloader import downloader
from app.SubMaker import submaker
import argparse


def main():
    parser = argparse.ArgumentParser(prog='YTSubPy',
        description='Small program to download subtitles from youtube')
    parser.add_argument('url', help='the url of video')
    r = parser.parse_args()
    url = r.url
    dwnld = downloader.Downloader()
    xml = dwnld.getxml(url)
    sub = submaker.SubMaker()
    sub.fromstring(xml)
    sub.tofile()
    print 'Subtitle file was generated successfully'


if __name__ == '__main__':
    main()
