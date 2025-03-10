"""
Program that creates a waveform representation of an image for broadcast.
"""

import numpy as np
from PIL import Image
from pathlib import Path
import argparse


class SpectrumPainter():
    """
    Takes a picture as input and converts it to a waveform which, when viewed on a spectrogram, looks like the image.

    Code adapted from - https://github.com/polygon/spectrum_painter
    """

    def __init__(self, fs=1_000000, line_dur=0.008, amplitude_resolution=64):
        self.NFFT = 0
        self.Fs = fs
        self.T_line = line_dur

        if amplitude_resolution == 256:
            self.amp_res = np.complex256
        elif amplitude_resolution == 128:
            self.amp_res = np.complex128
        elif amplitude_resolution == 64:
            self.amp_res = np.complex64

    @property
    def repetitions(self):
        return int(np.ceil(self.T_line * self.Fs / self.NFFT))

    def convert_image(self, filename):
        pic = Image.open(filename)
        pic = pic.convert("L")
        pic = np.array(pic)
        # Set FFT size to be double the image size so that the edge of the spectrum stays clear
        # preventing some bandfilter artifacts
        self.NFFT = 2 * pic.shape[1]

        # Repeat image lines until each one comes often enough to reach the desired line time
        ffts = (np.flipud(np.repeat(pic, self.repetitions, axis=0) / 16.) ** 2.) / 256.

        # Embed image in center bins of the FFT
        fftall = np.zeros((ffts.shape[0], self.NFFT))
        startbin = int(self.NFFT / 4)
        fftall[:, startbin:(startbin + pic.shape[1])] = ffts

        # Generate random phase vectors for the FFT bins, this is important to prevent high peaks in the output
        # The phases won't be visible in the spectrum
        phases = 2 * np.pi * np.random.rand(*fftall.shape)
        rffts = fftall * np.exp(1j * phases)

        # Perform the FFT per image line, then concatenate them to form the final signal
        timedata = np.fft.ifft(np.fft.ifftshift(rffts, axes=1), axis=1) / np.sqrt(float(self.NFFT))
        linear = timedata.flatten()
        linear = linear / np.max(np.abs(linear))

        # Rescale to desired resolution
        linear = linear.astype(self.amp_res)

        return linear


# Command line interface
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='SpecArt',
        description='Encodes pictures into waveform data, which can then be transmitted and viewed over the spectrum')

    parser.add_argument('-i', help='Path of input picture (.jpg or .png)')
    parser.add_argument("-o", help="Path of output file (outputs as complex 64, 128, 256")
    parser.add_argument("-fs", help="Sampling frequency of the output wave. Default: 1000000",
                        type=int, default=1_000_000)
    parser.add_argument("-t", help="How long (in seconds) to encode each line of the picture. Default: 0.008",
                        type=float, default=0.008)
    parser.add_argument("-amp_res", help="Output file resolution. Options are 256, 128 or 64",
                        type=int, default=64, choices=[256, 128, 64])

    args = parser.parse_args()
    input_file = Path(args.i)
    output_file = Path(args.o)
    FS = args.fs
    T = args.t
    amplitude_resolution = args.amp_res

    print(f"Processing {input_file}")

    # Create the spec painter
    spec_painter = SpectrumPainter(fs=FS, line_dur=T, amplitude_resolution=amplitude_resolution)

    # Create the wave from the image
    waveform = spec_painter.convert_image(input_file)

    # Save the wave
    print(f"Saved output to {output_file}")
    waveform.tofile(output_file)



