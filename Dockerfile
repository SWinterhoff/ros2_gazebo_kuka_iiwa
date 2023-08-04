# ROS2 Humble Image from osrf
FROM osrf/ros:humble-desktop-full

# General Init
RUN apt-get update && apt-get upgrade
RUN apt-get install -y git

# Source ROS2
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Installing Gazebo
RUN curl -sSL http://get.gazebosim.org | sh

