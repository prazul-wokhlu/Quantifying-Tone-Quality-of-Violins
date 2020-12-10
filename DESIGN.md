# Design of Tonal Recognition Software

We now know that different instruments can play the same note or pitch but still have different ”timbres.” Essentially, although  
the fundamental frequency of the sound is the same, to our ear the quality of sound is different because of the volume of the  
harmonic frequencies. This is how we are able to differentiate between a piano and violin playing the same note. In linear algebra  
terms, we can represent one sound in a vector space with the basis:

β = sin(2π · nt), cos(2π · nt), sin(2π · 2nt), ..., sin(2π · knt), cos(2π · knt)

Where n is the fundamental frequency of the sound (Hz) and k is the number harmonic above the fundamental frequency until infinity.  
So, we can write a singular note as a linear combination of the various sines and cosines of the frequencies. The weights given to  
each sine and cosine is what changes the sound quality, or timbre, of the sound. These relative weights are what tell the difference  
between instruments. Now, if we want to have a singular weight for each frequency rather than one for the sine and cosine, we can  
set it equal to the square root of the sum of each the sine and cosine weights relative to the frequency squared For example,  
suppose we have a linear combination with the following terms in it:

...ansin(2π · 440t) + bncos(2π · 440t)...

Thus, we want to find the weights for each frequency in the linear combination of harmonic vectors that make up the overall sound. These weights
will allow us to quantify the varying timbre between different instruments.
Ultimately however, we want to focus on one instrument and quantify exactly why a beginner’s tone quality will sound worse than a professional’s by
using the same method.

The Fourier Series (similar to the Taylor Series) is a method of representing periodic functions as combinations of sines and cosines.
Since we are trying to differentiate sound, our data will focus on long tones, which is a periodic signal. The Fourier Series works  
well with our problem because we hope to split a long tone into sines and cosines of its harmonics so that we can ultimately find the  
weights of each harmonic.

If you take a look at the two MATLAB files in the "matlab_frequencies" folder, I used that to extract the frequencies to conduct data
analysis and determine if there was a trend between the volume/power of harmonics versus the tone quality of the instrument. This
is just analysis, so I will not go in detail into it because it was not used as a part of the python program.

When we run main.py, the first thing the program checks for is if there is a "longtone" dictionary. If there is not, then the computer  
runs the "load_tones" method. What this does is it takes the mp3 files and does the following one by one:

1. Takes the fourier transform of the audio file, thus breaking it into its harmonics and their relative weights
2. It creates a spectrogram of the harmonics. The spectrogram takes an array of numbers representing the audio file, and
   returns the clipped and logged version of the array that represents values of the spectrogram. Then, this result is put into
   another function that finds the "peaks" of the spectrogram. The local peaks are returned in column-major order for the spectrogram.
   That is, the peaks are ordered by time. That is, we look for nearest neighbors of increasing frequencies at the same times, and
   then move to the next time bin.
3. Then, these peaks are essentially given as the fingerprints of the audio file. These are what the audio file is referencing in the
   dictionary.
4. When the uploading is complete, the program asks for a user input. Now, if we use the test data inside of "longtone_mp3s", we should
   be able to do the similar process for what we did in steps 1-3. We take the user input data, perform a fast fourier transform, find
   the peaks of the spectrogram, assign those as the fingerprints, and compare it to the pre-existing dictionary. It took trial and error
   to figure out what the best condition was for a match. But, once I found it, whenever I gave a user input, I was able to get the
   correct result. If the fingerprints of the inputted sound don't match as well as the condition states, the program takes the closest
   one and states that "it may be ___, but we are not sure". However, I've found that both results give the correct answer.

A more specific explanation for each of the functions is given inside of the code through comment blocks. Feel free to reach out to me if
there are any questions, but I hope you understood how I did this!









