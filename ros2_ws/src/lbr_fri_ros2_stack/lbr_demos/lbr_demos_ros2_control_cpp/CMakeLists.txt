cmake_minimum_required(VERSION 3.8)
project(lbr_demos_ros2_control_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(control_msgs REQUIRED)
find_package(fri_vendor REQUIRED)
find_package(FRIClient REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(trajectory_msgs REQUIRED)

add_executable(lbr_joint_trajectory_executioner_node
  src/lbr_joint_trajectory_executioner_node.cpp
)

ament_target_dependencies(lbr_joint_trajectory_executioner_node
  control_msgs
  fri_vendor
  rclcpp
  rclcpp_action
  trajectory_msgs
)

target_link_libraries(lbr_joint_trajectory_executioner_node
  FRIClient::FRIClient
)

install(TARGETS
  lbr_joint_trajectory_executioner_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
