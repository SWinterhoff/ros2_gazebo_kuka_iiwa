# ROS2 Humble Image
FROM ros:humble

# Source ROS2
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /workspaces/ros2_gazebo_kuka_iiwa/ros2_ws/install/setup.bash" >> ~/.bashrc
RUN echo "source /usr/share/gazebo/setup.sh" >> ~/.bashrc

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

# Set Gazebo Model Path
RUN export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/workspaces/ros2_gazebo_kuka_iiwa/ros2_ws/src/iiwa_ros2

# Set the working directory
WORKDIR /workspaces/ros2_gazebo_kuka_iiwa/ros2_ws

# Set the entrypoint (you can override this when running the container if needed)
CMD ["/bin/bash"]