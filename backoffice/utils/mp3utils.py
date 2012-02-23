from mutagen.mp3 import MP3
from datetime import timedelta

def get_mp3data(mp3path):
    try:
        mp3data = MP3(mp3path)
        mp3len = mp3data.info.length
        #mp3time = str(timedelta(seconds=int(round(mp3data.info.length))))
        mp3time = str(timedelta(seconds=int(mp3data.info.length)))
        if mp3len < 3600:
            mp3time = mp3time[2:len(mp3time)]

        isPerformer = True
        isTitle = True
        try:
            performer = mp3data["TPE1"].text[0].encode('latin1').decode('windows-1251')
        except Exception:
            isPerformer = False
        try:
            title = mp3data["TIT2"].text[0].encode('latin1').decode('windows-1251')
        except Exception:
            isTitle = False

        if isTitle:
            if isPerformer:
                mp3title = u'%s - %s' % (performer, title)
            else:
                performer = u'Not available'
                mp3title = u'%s' % (title)
        else:
            performer = u'Not available'
            title = u'Not available'
            mp3title = u'Not available'
        return dict(mp3performer=performer, mp3title=title, title=mp3title, length=mp3len, time=mp3time)
    except Exception:
        return dict(title='Not available', length=0, time='Undefined')