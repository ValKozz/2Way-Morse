import time
import numpy, pygame, math


def calculate_sine_pos(amplitude, frequency, time_):
    """Calculate the x position of the wave in time"""
    x_pos = amplitude * math.sin(2 * numpy.pi * frequency * time_)
    x_pos = int(round(x_pos))
    return x_pos


class Beeper:
    def __init__(self, frequency, dot_time):
        self.freq = frequency
        self.dot_time = dot_time
        self.dah_time = self.dot_time * 3
        self.l_pause = self.dah_time
        self.w_pause = self.dot_time * 7

        # Init pygame
        pygame.init()
        self.bits = 16
        self.sample_per_sec = 44100

        pygame.mixer.pre_init(self.sample_per_sec, self.bits)

    def play(self, tone):
        if tone == '.':
            duration = self.dot_time
        else:
            duration = self.dah_time

        num_samples = int(round(duration * self.sample_per_sec))
        buffer = numpy.zeros((num_samples, 2), dtype=numpy.int16)  # 2 zeros per channel, len of samples
        amp = 2 ** (self.bits - 1) - 1

        for sample in range(num_samples):
            time_ = float(sample) / self.sample_per_sec

            sine = calculate_sine_pos(amplitude=amp, frequency=self.freq, time_=time_)
            # Assign speaker to sign buffer (L - 0, R - 1)
            buffer[sample][1] = sine
            buffer[sample][0] = sine

        sound = pygame.sndarray.make_sound(buffer)

        sound.play(loops=1, maxtime=int(duration * 1000))
        time.sleep(duration)
