<picture align="center">
  <img alt="dsproc logo" src="dsproc_logo.png">
</picture>

------------------

# specArt - Create your own spectrum art!

## What is it?
Encodes pictures into a wave form which can then be transmitted to display your picture in the spectrum using a
waterfall plot or similar visualiser.

------------------

## Minimal example
Use the command line interface
```commandline
python specArt.py -i my_pic.jpg -o complex_wave.64 -fs 1000000 -t 0.008 -amp_res 64
```

For help use the expected:
```commandline
python specArt.py -h
```

## Installation
```commandline
pip install specart
```