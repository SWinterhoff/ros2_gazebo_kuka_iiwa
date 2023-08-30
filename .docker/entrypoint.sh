#!/bin/bash

# Build the packages using colcon
#cd /workspaces/ros2_gazebo_kuka_iiwa/ros2_ws
#colcon build

# Install workspace dependencies using rosdep
#rosdep update
#rosdep install -y --from-paths /workspaces/ros2_gazebo_kuka_iiwa/ros2_ws --ignore-src --rosdistro humble

# Run your desired application command here
# For example:
# ros2 run my_package my_node

# Start a shell session to keep the container running
exec /bin/bash