from app.Downloader import Downloader
from app.SubMaker import SubMaker
import argparse


def main():
    parser = argparse.ArgumentParser(prog='YTSubPy',
        description='Small program to download subtitles from youtube')
    parser.add_argument('url', help='the url of video')
    r = parser.parse_args()
    url = r.url
    dwnld = Downloader.Downloader()
    xml = dwnld.getxml(url)
    sub = SubMaker.SubMaker()
    sub.fromstring(xml)
    sub.tofile()
    print 'Subtitle file was generated successfully'


if __name__ == '__main__':
    main()
