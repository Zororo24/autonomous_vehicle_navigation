# Autonomous Vehicle Navigation

A deep reinforcement learning project that simulates autonomous vehicles learning to navigate through an environment while avoiding obstacles. The project features two AI-controlled cars that learn simultaneously using Deep Q-Learning Networks (DQN).

## Features

- Real-time simulation of two autonomous vehicles
- Interactive environment where users can draw obstacles
- Deep Q-Learning implementation for autonomous navigation
- Sensor-based obstacle detection
- Experience replay for improved learning
- Save/Load functionality for trained models
- Visual feedback of learning progress

## Prerequisites

- Python 3.7+
- PyTorch
- Kivy
- NumPy
- Matplotlib

## Interface Controls
- Left click and drag to draw obstacles (sand)
- Buttons:
  - `clear`: Removes all obstacles from the map
  - `save`: Saves the current state of both neural networks
  - `load`: Loads previously saved neural networks

## How It Works

### Neural Network Architecture
- Input Layer: 5 neurons (3 sensors + 2 orientation values)
- Hidden Layer: 30 neurons with ReLU activation
- Output Layer: 3 neurons (left, straight, right actions)

### Learning Process
1. Cars receive sensor inputs about their environment
2. Neural network processes inputs to select actions
3. Cars execute actions and receive rewards:
   - -1 for hitting obstacles/walls
   - -0.2 for moving
   - +0.1 for getting closer to the goal
4. Experiences are stored and used for training
5. Goals switch positions when reached

### Cars' Sensors
- Three sensors per car for obstacle detection
- Sensors rotate with the car's orientation
- Detection range: 20x20 pixels around each sensor

## Customization

You can modify various parameters in both files:
- Learning rate (default: 0.001)
- Gamma value (default: 0.9)
- Neural network architecture
- Reward values
- Car speed and rotation angles

## Contact

Abhishek Shinde - abhivshinde24@gmail.com
Project Link: [Autonomous Vehicle Navigation](https://github.com/Zororo24/autonomous_vehicle_navigation)
