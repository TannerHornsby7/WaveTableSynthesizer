import numpy as np
import scipy.io.wavfile as wav

def interpolate_linearly(wave_table, index):
    #we want to find the nearest int
    #to the index and then find the weight
    #of the wave_table at these indicies
    #and then return the weighted sum

    #if the given index is out of range, we bring it
    #back into range
    truncated_index = int(np.floor(index))
    #because the indexes are integer values that increment by one,
    #we can describe next index as:
    next_index = (truncated_index + 1) % wave_table.shape[0]

    # I don't understand these two lines yet.
    next_index_weight = index - truncated_index
    truncated_index_weight = 1 - next_index_weight

    return truncated_index_weight * wave_table[truncated_index] + next_index_weight * wave_table[next_index]

def fade_in_out(signal, fade_length=1000):
    fade_in = (1 - np.cos(np.linspace(0, np.pi, fade_length))) * 0.5
    fade_out = np.flip(fade_in)

    signal[:fade_length] = np.multiplty(fade_in, signal[:fade_length])

    signal[-fade_length:] = np.multiply(fade_out, signal[-fade_length:])

def sawtooth(x):
    return (x + np.pi) / np.pi % 2 - 1
def main():
    sample_rate = 44100
    f = 220
    t = 3
    #waveform = np.sin
    waveform = sawtooth

    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))

    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

    output = np.zeros((t * sample_rate,))

    index = 0
    index_increment = f * wavetable_length / sample_rate

    for n in range(output.shape[0]):
        output[n] = interpolate_linearly(wave_table, index)
        #output[n] = wave_table[int(np.floor(index))]
        index += index_increment
        index %= wavetable_length
    
    # scaling the output by a volume converted from a dB val
    gain = -20
    amplitude = 10 ** (gain/ 20)
    output *= amplitude

    wav.write('sawtooth440HzScaledInterpolatedFaded.wav', sample_rate, output.astype(np.float32))
if __name__ == '__main__':
    main() 