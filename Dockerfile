# ROS2 Humble Image
FROM ros:humble

# General Init
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git

# Source ROS2
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Installing Gazebo
RUN curl -sSL http://get.gazebosim.org | sh


