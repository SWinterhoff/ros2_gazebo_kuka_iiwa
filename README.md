Simulation of KUKA iiwa 
- Automated wiring harness mounting
- Simulation environment - Gazebo


Simulation models
- KUKA iiwa Robot
- Electric plug, Molex Stac 64
- (Cable does not have to be simulated yet)


Movement Solutions
1. Move 2 Join Position
    - Move to predefined joint positions (np array, 7 values for 7 joints) 
    - Show movement with trajectory

2. Move 2 TCP (Tool Center Point) Pose
    - Move to predefined Tool Center Point position (np array, 6 values, position and rotation)
    - Solver: MoveIt 2.0

3. Plotfunction
    - Depending on previous methods 7 or 6 predefined functions of the joints and position over time as movementpath
