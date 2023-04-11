"""
Homework #3
This program deals with audio data manipulation including loop, flipflop, fade and echo.

Authors: Le Nu Dong Giang, Bui Doan Khanh Quan
Time spent: 5 hours
"""

from csc121.audio import read_wav, write_wav

"""
def loop ():
    audio_name = input("Please enter audio's name (including '.wav'): ")
    repeat_time = input("Please enter the number of times to repeat the audio: ")
    repeat_time = int(repeat_time)
    original_audio = read_wav(audio_name)
    repeated_audio = []
    repeated_audio = original_audio * repeat_time
    write_wav(repeated_audio, 'looped.wav')

def flipflop ():
    audio_name = input("Please enter audio's name (including '.wav'): ")
    original_audio = read_wav(audio_name)
    length = len(original_audio)
    midpoint = length//2
    first_half = original_audio[:midpoint]
    second_half = original_audio[midpoint:]
    swapped_audio = second_half + first_half
    write_wav(swapped_audio, 'flipflopped.wav')


def fade ():
    audio_name = input("Please enter audio's name (including '.wav'): ")
    original_audio = read_wav(audio_name)
    length = len(original_audio)
    faded_audio = []
    POSITION_COUNT = -1
    position = POSITION_COUNT
    for i in original_audio:
        position = position+1
        scaling_factor = 1-position/(length-1)
        faded_audio.append(i*scaling_factor)
    write_wav(faded_audio, 'faded.wav')
 """


def echo():
    audio_name = input("Please enter audio's name (including '.wav'): ")
    original_audio = read_wav(audio_name)
    length = len(original_audio)
    SOFTNESS_FACTOR = 0.3
    softer_audio = []
    for i in original_audio:
        softer_audio.append(i * SOFTNESS_FACTOR)
    shift_length = length // 8
    shift_list = []
    for i in range(shift_length):
        shift_list.append(0)
    original_audio_with_shift = original_audio + shift_list
    softer_audio_with_shift = shift_list + softer_audio
    echoed_audio = [original_audio_with_shift[i] + softer_audio_with_shift[i]
                    for i in range(len(original_audio_with_shift))]
    write_wav(echoed_audio, 'echoed.wav')


echo()
"""
def extra_credit ():
    audio_name = input("Please enter audio's name (including '.wav'): ")
    original_audio = read_wav(audio_name)
    slowdown_audio = []
    SLOWDOWM_FACTOR = 2
    for i in original_audio:
        for j in range(SLOWDOWM_FACTOR):
            slowdown_audio.append(i)
    length = len(slowdown_audio)
    SOFTNESS_FACTOR = 0.3
    softer_audio = []
    for i in slowdown_audio:
        softer_audio.append(i*SOFTNESS_FACTOR)
    shift_length = length//8
    shift_list = []
    for i in range(shift_length):
        shift_list.append(0)
    slowdown_audio_with_shift = slowdown_audio + shift_list
    softer_audio_with_shift = shift_list + softer_audio
    slowdown_echoed_audio = [slowdown_audio_with_shift[i] + softer_audio_with_shift[i]
                             for i in range(len(slowdown_audio_with_shift))]
    write_wav(slowdown_echoed_audio, 'slowdown_echoed.wav')
"""