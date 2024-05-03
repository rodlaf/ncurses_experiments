import gymnasium as gym
from gymnasium.utils.play import play
import pygame 

env = gym.make("CartPole-v1", render_mode="rgb_array")

mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 1}

play(env, keys_to_action=mapping, noop=0)
# env.reset()
# while True:
#     action = int(input("Action: "))
#     if action in (0, 1):
#         env.step(action)
#         env.render()