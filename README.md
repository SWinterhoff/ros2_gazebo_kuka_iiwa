# Simulation of KUKA iiwa 
- Automated wiring harness mounting
- Simulation environment - Gazebo


### Simulation models
- Robot:            Kuka LBR iiwa 7 R800
- Gripper:          Weiss Robotics WSG 50-110
- Finger:           Weiss Robotics F-WSG-F
- Electric plug:    Molex Stac 64
- Cable:            (does not have to be simulated yet, but needs to be considered)


### Coding
- General approach, consider different joint numbers etc.
- Optimize for calculation time, less loops, consider machine learning


### Movement Solutions
1. Move 2 Joint Position
    - Move to predefined joint positions (np array, 7 values for 7 joints) 
    - Show movement with trajectory

2. Move 2 TCP (Tool Center Point) Pose
    - Move to predefined Tool Center Point position (np array, 6 values, position and rotation)
    - Solver: MoveIt 2.0 (Inverse Kinematics)

3. Plotfunction
    - Depending on previous methods 7 or 6 predefined functions of the joints and position over time as movementpaths



# Using the Workspace
1. 
