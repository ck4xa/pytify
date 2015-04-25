## IMPORTANT ##
This project is not maintained anymore. If it still works, it is only because of sheer luck. Feel free to contact me if you would like to contribute to pytifys continued existence by becoming a committer.

## Features ##
  * Allows for control of the Spotify media player in Python scripts
  * A simple command line syntax for controlling the Spotify media player from console

## Installing ##
  1. Make sure you have Python installed with the _Python for Windows extensions_. It can be found and downloaded from here: http://sourceforge.net/projects/pywin32/
  1. Unzip the latest pytify zip file that can be downloaded from the **featured downloads** section on this page
  1. Open the console in the directory the files were unzipped to
  1. Type `python setup.py install`

Hopefully, you can now run pytify.py from the command line anywhere in your system.

## How to use ##

### From a Python script ###
```

from pytify import Spotify
spotify = Spotify()

spotify.FUNCTION

```
where **FUNCTION** is one of:
|getCurrentTrack()| Returns title of the current playing track|
|:----------------|:------------------------------------------|
|getCurrentArtist()|Returns artist name for the current playing track|
|isPlaying|returns True if spotify is currently playing, otherwise False|
|playpause()|Play or pause Spotify|
|stop()|Stops playback in Spotify|
|focus()|Giving the Spotify window focus|
|next()|Play next track in queue|
|previous()|Play previous track in queue|
|volumeUp()|Turns volume up|
|volumeDown()|Turns volume down|
|mute()|Mutes Spotify|


### From command line ###
```
python pytify ARGUMENT
```

Where **ARGUMENT** is one of:
|status|Prints the Spotify status|
|:-----|:------------------------|
|playpause|Play or pause Spotify|
|stop|Stop playback|
|next|Play next track in queue|
|previous|Play previous track in queue|
|volup|Turns volume up|
|voldown|Turns volume down|
|mute|Mutes Spotify|
|isplaying|Prints True if spotify is currently playing, otherwise False|
|currenttrack|Prints title of the current track|
|currentartist|Prints artist name for the current track|
|focus|Giving the Spotify window focus|


**This project is completely unofficial and by no means affiliated with spotify.com**

Thanks to zowat@Toastify for publishing the action IDs used when sending messages to the Spotify Window