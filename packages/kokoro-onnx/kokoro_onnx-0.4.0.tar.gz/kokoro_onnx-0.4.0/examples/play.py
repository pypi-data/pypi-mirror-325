"""
Note: on Linux you need to run this as well: apt-get install portaudio19-dev

pip install kokoro-onnx sounddevice

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
python examples/play.py
"""

import sounddevice as sd
from kokoro_onnx import Kokoro

text = """
My seat, to which Bessie and the bitter Miss Abbot had left me riveted, 
was a low ottoman near the marble chimney-piece; the bed rose before me; 
to my right hand there was the high, dark wardrobe, with subdued, broken reflections varying the gloss of its panels; 
to my left were the muffled windows; a great looking-glass between them repeated the vacant majesty of the bed and room. 
I was not quite sure whether they had locked the door; and when I dared move, 
I got up and went to see. Alas! yes: no jail was ever more secure. 
Returning, I had to cross before the looking-glass; my fascinated glance involuntarily explored the depth it revealed. 
All looked colder and darker in that visionary hollow than in reality: and the strange little figure there gazing at me, 
with a white face and arms specking the gloom, and glittering eyes of fear moving where all else was still, had the effect of a real spirit: 
I thought it like one of the tiny phantoms, half fairy, half imp, Bessie’s evening stories represented as coming out of lone, ferny dells in moors, 
and appearing before the eyes of belated travellers. I returned to my stool.
"""


kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
samples, sample_rate = kokoro.create(
    text,
    voice="af_heart",
    speed=1.0,
    lang="en-us",
)
print("Playing audio...")
sd.play(samples, sample_rate)
sd.wait()
