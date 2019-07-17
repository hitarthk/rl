import gym
import time
env = gym.make('CartPole-v0')
env.reset()
count = 0
for i in range(1000):
    state,reward, done, _ = env.step(env.action_space.sample())
    count +=1
    time.sleep(0.015)
    env.render()
    if(done):
        print(f'Run for {count} time steps')
        count= 0
        env.reset()
