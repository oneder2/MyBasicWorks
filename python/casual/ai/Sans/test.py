import gym # 环境

import tensorflow as tf # 模型
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import numpy as np # numpy


# """定义训练环境"""
env = gym.make('CartPole-v1')
state_size = env.observation_space.shape[0]
action_size = env.action_space.n


# """定义模型"""
model = Sequential()
model.add(Dense(64, input_shape=(state_size,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(action_size, activation='linear'))


# """定义损失函数和优化器"""
model.compile(optimizer='adam', loss='mse')


# """定义训练循环"""
num_episodes = 1000
gamma = 0.99
for episode in range(num_episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False
    while not done:
        action = np.argmax(model.predict(state))
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        
        target = reward + gamma * np.max(model.predict(next_state))
        target_vec = model.predict(state)[0]
        target_vec[action] = target
        
        model.fit(state, target_vec.reshape(-1, action_size), epochs=1, verbose=0)
        
        state = next_state