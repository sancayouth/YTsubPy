YTSubPy
=================
*Small program to download subtitles from youtube (WIP)*

SETUP
------------
$ pip install -r requirements.txt

USAGE
------------

### discover mode:
*Discover the available languages*  
$ python main.py youtube_video_url -d  
'English':'en'  
'French':'fr'  
'Portuguese (Brazil)':'pt-BR'  
'Russian':'ru'  
'Spanish':'es'  

## download subtitle:
$ python main.py youtube_video_url -l es  
Subtitle was generated successfully

TODO
------------
-download automatic subtitles

LICENSE
------------
Licensed under the MIT License.
