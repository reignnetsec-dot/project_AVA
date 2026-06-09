# from modules.pass_manager import PassMan
import pandas as pd
import random


feature = 2
target = 10
learning_rate = 0.08
weight = 0.3            # change this to 6.0 to test overshoot correction


class Brain:
    def __init__(self, feature: int, target: int, learning_rate: float, weight: float):
        self.feature = feature
        self.target = target
        self.learning_rate = learning_rate
        self.weight = weight

    def train(self):
        while True:
            # Forward pass: linear unit with bias
            output = self.weight * self.feature + 1
            error = self.target - output          # positive if too low, negative if too high

            print(f"Feature: {self.feature}, Output: {output:.4f}, Error: {error:.4f}")

            # Unified update rule: move weight in direction of error,
            # with step proportional to error magnitude
            self.weight += self.learning_rate * error * self.feature

            # Recompute after update to check stopping condition on new state
            new_output = self.weight * self.feature + 1
            new_error = self.target - new_output

            if abs(new_error) < 0.1:              # close enough
                print(f"Converged: Output = {new_output:.4f}, Weight = {self.weight:.4f}")
                break

            print(f"Weight updated to: {self.weight:.4f}\n")


# Instantiate and train
ava = Brain(feature, target, learning_rate, weight)
ava.train()