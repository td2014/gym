#
# Simple code to run cartpole in gym
#
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    s = env.step(env.action_space.sample()) # take a random action
    print(s)

#
# End of script
#
