import torch
import random
from collections import deque
import numpy as np
import pickle


class ReplayBuffer():
    def __init__(self):
        self.buffer_size = int(1e6)
        self.batch_size =  32
        self.buffer = deque(maxlen=self.buffer_size)
        self.index = 0

    def __len__(self):
        return len(self.buffer)

    def add(self, experience):
        if len(self.buffer) < self.buffer_size:
            self.buffer.append(experience)
        else:
            self.buffer[self.index] = experience
            self.index = (self.index + 1) % self.buffer_size

    def sample_batch(self):
        batch = random.sample(self.buffer, self.batch_size)
        return batch

    def save_buffer(self, filepath = "buffer.pkl"):
        with open(filepath, 'wb') as f:
            pickle.dump(list(self.buffer), f)
    
    def load_buffer(self, filepath = "buffer.pkl"):
        with open(filepath, 'rb') as f:
            self.buffer = deque(pickle.load(f))


