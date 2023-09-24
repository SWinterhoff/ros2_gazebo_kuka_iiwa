# ROS2 Humble Hawksbill Image
FROM osrf/ros:humble-desktop-full

# Source ROS2
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /workspaces/ros2_gazebo_kuka_iiwa/ros2_ws/install/setup.bash" >> ~/.bashrc

# Source Gazebo
RUN echo "source /usr/share/gazebo/setup.sh" >> ~/.bashrc
RUN echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/workspaces/ros2_gazebo_kuka_iiwa/lbr_fri_ros2_stack_ws/src/lbr_fri_ros2_stack' >> ~/.bashrc

# Set the PYTHONPATH environment variable to include custom package path
ENV PYTHONPATH="/opt/ros/humble/lib/python3.10/site-packages:/opt/ros/humble/local/lib/python3.10/dist-packages:/workspaces/ros2_gazebo_kuka_iiwa/ros2_ws/install:$PYTHONPATH"

# Set environment variables
ENV ROS_DISTRO humble

# Install dependencies
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get install -y git 
RUN apt-get install -y python3-rosdep
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y ros-humble-rviz2
RUN apt-get install -y ros-humble-xacro
RUN apt-get install -y ros-humble-controller-manager
RUN apt-get install -y ros-humble-joint-state-publisher
RUN apt-get install -y ros-humble-ros2-controllers
RUN apt-get install -y ros-humble-ros2-control
RUN apt-get install -y ros-humble-gazebo-ros2-control
RUN apt-get install -y ros-humble-gazebo-ros-pkgs
RUN apt-get install -y ros-humble-pilz-industrial-motion-planner
RUN apt-get install -y ros-humble-moveit-ros-planning
RUN apt-get install -y ros-humble-moveit-planners-ompl
RUN apt-get install -y ros-humble-cv-bridge
RUN apt-get install -y ros-humble-moveit-ros-move-group
RUN apt-get install -y ros-humble-moveit-simple-controller-manager
RUN apt-get install -y ros-humble-moveit-servo
RUN apt-get install -y ros-humble-moveit-msgs
RUN apt-get install -y ros-humble-moveit-common
RUN apt-get install -y ros-humble-moveit-core
RUN apt-get install -y ros-humble-moveit-ros-visualization
RUN apt-get install -y ros-humble-moveit-kinematics
RUN apt-get install -y ros-humble-moveit-planners
RUN apt-get install -y ros-humble-joint-state-publisher-gui
RUN apt-get install -y ros-humble-moveit-configs-utils
RUN apt-get install -y ros-humble-moveit-setup-assistant
RUN apt-get install -y ros-humble-rviz-common
RUN apt-get install -y ros-humble-rviz-default-plugins
RUN apt-get install -y ros-humble-controller-interface
RUN apt-get install -y ros-humble-hardware-interface
RUN apt-get install -y ros-humble-control-toolbox
RUN apt-get install -y ros-humble-realtime-tools
RUN apt-get install -y ros-humble-control-msgs
RUN apt-get install -y ros-humble-joy
RUN apt-get install -y ros-humble-ros2-control-test-assets
RUN apt-get install -y ros-humble-joint-state-broadcaster
RUN apt-get install -y ros-humble-joint-trajectory-controller
RUN apt-get update

# Create a directory in the container for your code
WORKDIR /workspaces

# Copy your code into the container
RUN git clone https://github.com/SWinterhoff/ros2_gazebo_kuka_iiwa.git
#COPY ../../ros2_gazebo_kuka_iiwa /workspaces/ros2_gazebo_kuka_iiwa

# Start a shell session by default
CMD ["/bin/bash"]