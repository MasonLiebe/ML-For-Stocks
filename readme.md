# ML-For-Stocks

**ML-For-Stocks** is a comprehensive repository featuring a diverse collection of machine learning and deep learning models specifically tailored for stock market forecasting. This repo includes a variety of predictive models, trading bots, and simulations designed to provide insights into stock movements and trading strategies. It serves as a resource for both academic researchers and financial market analysts seeking to apply advanced analytical techniques to the financial markets.

Explore an extensive range of models including LSTM variations, GRUs, Q-learning agents, and more, along with real-time agents and data exploration notebooks.

# Models Implemented So Far

## Agent-Based Models (Reinforcement-Learning)
This is a collection of agent-based models I've put together.  All of these train on the closing prices of the ticker that you chose, but are set up to be adjusted to handle other parameters.  I have them in a general reinforcement learning folder, although some of these agentic strategies are not strictly "reinfocement learning".  I switched from TensorFlow to PyTorch during the building process, so some of the implementations leverage TensorFlow and some leverage Pytorch.
- [Actor-Critic (TensorFlow)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/neuro-evolution-agent-novelty-search.ipynb)
- [Evolution Strategy (PyTorch)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/evolution-strategy-agent.ipynb)
- [Q-Learning (PyTorch and TensorFlow)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/q-learning-agent-pytorch.ipynb)
- [Double Q-Learning (PyTorch)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/double-q-learning-agent.ipynb)
- [Recurrent Q-Learning (PyTorch)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/recurrent-q-learning-agent.ipynb)
- [Moving-Average-Agent (numpy)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/ma-agent.ipynb)
- [Turtle Agent (numpy)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/turtle-agent.ipynb)
- [Signal Rolling Agent (numpy)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/signal-roller.ipynb)
- [Neuro-evolution agent (Self-implemented neural net)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/neuro-evolution-agent.ipynb)
- [Neuro-evolution agent with Novelty Search (Self-implemented neural net)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/reinforcement-learning/neuro-evolution-agent-novelty-search.ipynb)

## Deep Learning Models
This is a collection of deep learning models used for forecasting rather than the RL/Agent models.
- [LSTM (TensorFlow)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/deep-learning/lstm.ipynb)
- [Bidirectional LSTM (TensorFlow)](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/deep-learning/lstm-bidirectional.ipynb)

# Visualization System

I built some visualization tools that leverage plotly to open an interactive browser-based visualizer with some indicators given a user-chosen set of tickers.  The data is fetched leveraging the [yfinance](https://github.com/ranaroussi/yfinance) API, then fed into the visualization system.  Here are some screenshots of the visualizer.

Here's a view of some different metrics computed for AAPL visualized.
![apple_image](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/visualizations/Apple_Statistics_Visualized.png?raw=true)

Here's a visualization of the relative cumulative performace of different tickers
![all_stocks](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/visualizations/Cumulative_Returns_Visualized.png?raw=true)

Here's a violin plot showing the distribution of returns for various equities.
![all_stocks](https://github.com/MasonLiebe/ML-For-Stocks/blob/main/visualizations/Violin-Plot.png?raw=true)
