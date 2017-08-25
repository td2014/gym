#
# Simple code to run cartpole in gym
#
import gym
env = gym.make('CartPole-v0')
observation = env.reset()
for iStep in range(100):
    print('iStep: ', iStep)
    print('observation: ', observation)
    env.render()
    action = 1 # env.action_space.sample()
    print('action: ', action)
    observation, reward, done, info = env.step(action) # take a random action
    print('reward: ', reward)
    print()

#
# End of script
#