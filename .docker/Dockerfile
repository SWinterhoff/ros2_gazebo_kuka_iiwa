# ROS2 Humble Image
FROM ros:humble

# Source ROS2
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /workspaces/ros2_gazebo_kuka_iiwa/ros2_ws/install/setup.bash" >> ~/.bashrc
RUN echo "source /usr/share/gazebo/setup.sh" >> ~/.bashrc
RUN echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/workspaces/ros2_gazebo_kuka_iiwa/ros2_ws/src/iiwa_ros2' >> ~/.bashrc

# Set the working directory
WORKDIR /workspaces/ros2_gazebo_kuka_iiwa/ros2_ws

# General Init
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git
RUN apt-get install -y ros-humble-gazebo-ros-pkgs
RUN apt-get install -y ros-humble-moveit
RUN apt-get install -y python3-rosdep
RUN apt-get install -y ros-humble-controller-interface
RUN apt-get install -y ros-humble-controller-manager
RUN apt-get install -y ros-humble-moveit-servo
RUN apt-get update


### Using only Docker ###
# Copy the entrypoint script into the image
#COPY .docker/entrypoint.sh /tmp/entrypoint.sh

# Give execute permissions to the script
#RUN chmod +x /tmp/entrypoint.sh

# Set the entrypoint to the script
#ENTRYPOINT ["/tmp/entrypoint.sh"]



### Using devcontainer ###
# Set the entrypoint (Default commands when container starts are already included in entrypoint.sh)
CMD ["/bin/bash"]