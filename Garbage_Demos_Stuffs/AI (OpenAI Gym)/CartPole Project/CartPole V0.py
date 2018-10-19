# Basic CartPole Simulations - OpenAI project

import gym

env = gym.make('CartPole-v0')  # This creates the enviroment for the simulation


def basic_policy(obs):  # Determines what basic action to take
    angle = obs[2]  # Angle is the angle of the pole
    return 0 if angle < 0 else 1  # 0 is to go left, 1 is to go right


totals = []  # list of the total reward accumulated for each episode

for episode in range(20):  # Run 10 Simulations
    episode_rewards = 0  # The reward for the episode, for staying alive
    obs = env.reset()  # This resets the poles postion, carts postion, angle of the pole, ect. to (0,0) based on observations {obs}
    action = 1  # Move the cart Left or Right
    for step in range(500):  # Run simulation for 500 time steps, not forever
        action = basic_policy(obs)  # Carry out action based on observation and policy from the enviroment
        env.render()  # Renders the enviroment of the simulation
        obs, reward, done, info = env.step(action)  # Observation, Reward, Done {Boolean Value}, Info {Debbuging Data, Must be there}
        episode_rewards += reward  # Adds a reward at each time step that pole hasn't fallen over
        if done:  # When the  simulation end and done = True
            totals.append(episode_rewards)  # Append the episode rewards to the totals list
            break  # Break out of step loop

print("\n~~~~~~~~~~~~~~~~~~~~\n")
print(totals)
print('The longest number of timesteps the pole was balanced:' + str(max(totals)))
print("\n~~~~~~~~~~~~~~~~~~~~\n")
