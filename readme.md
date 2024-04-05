# Meteo Pixel
Dirty as hay, learn python with this file at your own risks.
TheDarkTiger 2024


## The script
Generates an audio fake weather forecast / bulletin from a text file.

## How to use install?

### Classic python install

* Install Python >=3
* Run "pip install -r requirements.txt"
* Install [espeak](https://espeak.sourceforge.net/download.html), and make sure it is available in the PATH.
* Install [sox](https://sourceforge.net/projects/sox/files/latest/download), and make sure it is available in the PATH.

You should be able to run the script "MeteoPixel.py"

### Windows executable
Not yet available


## How to use?

* Edit "bulletin.txt"
* Run the script by using "python MeteoPixel.py"

The script will stitch each lines one after the other to generate the final audio in the generated folder as "out.ogg".
As an example, [bulletin.txt](/bulletin.txt) should generate something akind to [bulletin.ogg](/res/bulletin.ogg)

By now, it can either add a sound or synthetize voice, nothing else (no efects, no mixing, etc.).


## Tip and Tricks

### bulletin format

Any line staring by \[ and ending by \] indicates the audio file to add to the bulletin.
Any other line will be send to the speech synthetizer.

> [!WARNING]
> No check as for the content of the files will be done, if you specify a broken audio file, or other kind of file, sox may not like it.


## Future work
No garanty of future work.
See [TODO.txt](/TODO.txt).
