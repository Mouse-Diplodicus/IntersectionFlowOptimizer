import timeit

import cityflow
import json
import gym
import gym_cityflow
import numpy as np

class Model:

    def __init__(self, config_path, num_steps):
        self.num_steps = num_steps
        self.env = gym.make('cityflow-v0', configPath=config_path, episodeSteps=num_steps)
        self.env.action_space.seed(42)

    def simulate(self):
        self.env.reset()
        start_time = timeit.default_timer()
        while True :
            observation, reward, done, debug = self.env.step(action=self.env.action_space.sample())
            if done:
                elapsed_time = round(timeit.default_timer() - start_time, 3)
                print(f"Elapsed Time: {elapsed_time} seconds")
                break



if __name__ == '__main__':
    test = Model("examples/config.json", 1000)
    test.simulate()
