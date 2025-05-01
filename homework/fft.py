import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
def fft_non_recursive(x):
    N = len(x)
    if (N & (N - 1)) != 0:
        raise ValueError("Длина массива должна быть степенью 2")
    j = 0
    for i in range(1, N):
        bit = N >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            x[i], x[j] = x[j], x[i]
    L = 2
    while L <= N:
        angle = -2j * np.pi / L
        w_L = np.exp(angle)
        for k in range(0, N, L):
            w = 1.0
            for j in range(L // 2):
                u = x[k + j]
                v = w * x[k + j + L // 2]
                x[k + j] = u + v
                x[k + j + L // 2] = u - v
                w *= w_L
        L <<= 1
    return x


def ifft_non_recursive(X):
    N = len(X)
    if (N & (N - 1)) != 0:
        raise ValueError("Длина массива должна быть степенью 2")
    j = 0
    for i in range(1, N):
        bit = N >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            X[i], X[j] = X[j], X[i]
    L = 2
    while L <= N:
        angle = 2j * np.pi / L
        w_L = np.exp(angle)
        for k in range(0, N, L):
            w = 1.0
            for j in range(L // 2):
                u = X[k + j]
                v = w * X[k + j + L // 2]
                X[k + j] = u + v
                X[k + j + L // 2] = u - v
                w *= w_L
        L <<= 1
    X = X / N
    return X



def filter_audio(input_file, output_file, cutoff_freq, mode='highpass'):

    sample_rate, audio_data = wavfile.read(input_file)


    if len(audio_data.shape) == 2:
        audio_data = audio_data[:, 0]


    if audio_data.dtype == np.int16:
        audio_data = audio_data / 32768.0


    original_len = len(audio_data)
    N = 1 << (original_len - 1).bit_length()
    padded_audio = np.zeros(N)
    padded_audio[:original_len] = audio_data


    fft_data = fft_non_recursive(padded_audio.copy())


    freqs = np.fft.fftfreq(N, d=1 / sample_rate)


    if mode == 'highpass':
        fft_data[np.abs(freqs) < cutoff_freq] = 0
    elif mode == 'lowpass':
        fft_data[np.abs(freqs) > cutoff_freq] = 0


    filtered_audio = ifft_non_recursive(fft_data).real


    filtered_audio = filtered_audio[:original_len]


    filtered_audio_int = np.int16(filtered_audio * 32768)
    wavfile.write(output_file, sample_rate, filtered_audio_int)

    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.plot(audio_data[:2000], label='Исходный сигнал')
    plt.title('Исходное аудио')

    plt.subplot(122)
    plt.plot(filtered_audio[:2000], label='Фильтрованный сигнал', color='orange')
    plt.title(f'После {mode} ({cutoff_freq} Гц)')

    plt.tight_layout()
    plt.show()



input_wav = 'sample-12s.wav'
output_highpass = 'highpass.wav'
output_lowpass = 'lowpass.wav'

filter_audio(input_wav, output_highpass, cutoff_freq=789, mode='highpass')

filter_audio(input_wav, output_lowpass, cutoff_freq=587, mode='lowpass')