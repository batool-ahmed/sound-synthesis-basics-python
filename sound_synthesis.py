import numpy as np
import sounddevice as sd

def main():
    ''' Generate a sound '''

    # # White noise
    # my_sound = white_nose()

    # # Single sine wave
    # my_sound = sine_tone()

    '''  Generate multiple sine waves with varying frequencies and amplitudes, and combining them '''

    # sine_1 = sine_tone(200, 1, 0.6)
    # sine_2 = sine_tone(400, 1, 0.3)
    # sine_3 = sine_tone(800, 1, 0.2)
    # my_sound = sum([sine_1, sine_2, sine_3])

    # # Harmonic frequency
    # sines = [sine_tone(frequency = 200 * i, amplitude = 0.7 / i) for i in range(1, 31, 2)]
    # my_sound = sum(sines)

    # # Inharmonic frequency (added a value to the multiple)
    # sines = [sine_tone(frequency = 200 * i + 50, amplitude = 0.7 / i) for i in range(1, 31, 2)]
    # my_sound = sum(sines)


    # # Beating effect (two waves with very close frequencies)
    # sines = [sine_tone(200, 1.0, 0.6), sine_tone(205, 1, 0.6)]
    # my_sound = sum(sines)
    
    # Play the sound
    # sd.play(my_sound)
    # sd.wait()

def sine_tone(
    frequency: int = 440,
    duration: float = 1.0, 
    amplitude: float = 0.5, 
    sample_rate: int = 44100
) -> np.ndarray:
    ''' Generate a sine tone '''

    # Calculate the number of samples needed
    n_samples = int(duration * sample_rate)

    # Create an array of time points
    time_points = np.linspace(0, duration, n_samples, False)

    # Create the sine wave
    sine = np.sin(2 * np.pi * frequency * time_points)

    # Apply amplitude
    sine *= amplitude

    return sine

def white_nose(
    duration: float = 1.0, 
    amplitude: float = 0.5, 
    sample_rate: int = 44100
) -> np.ndarray : 
    ''' Generate white noise '''

    # Calculate the number of samples needed
    n_samples = int(duration * sample_rate)

    # Generate white noise with values between -1 and 1
    noise = np.random.uniform(-1, 1, n_samples)

    # Scale by amplitude
    noise *= amplitude

    return noise

if __name__ == "__main__":
    main()