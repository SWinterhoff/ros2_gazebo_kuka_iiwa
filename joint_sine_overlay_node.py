import math
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sensor_msgs.msg import JointState

class JointSineOverlayNode(Node):
    def __init__(self, node_name: str) -> None:
        super().__init__(node_name)
        self.amplitude_ = 0.04  # rad
        self.frequency_ = 0.25  # Hz
        self.phase_ = 0.0

        # Create publisher for joint trajectory
        self.joint_trajectory_pub_ = self.create_publisher(
            JointTrajectory,
            "/position_trajectory_controller/follow_joint_trajectory",
            QoSProfile(depth=10)  # Adjust the depth as needed
        )

        # Create subscription to joint states (simulated robot)
        self.joint_state_sub_ = self.create_subscription(
            JointState,
            "/joint_states",
            self.on_joint_states,
            QoSProfile(depth=10)  # Adjust the depth as needed
        )

    def on_joint_states(self, joint_states: JointState) -> None:
        # Ensure the joint_states message contains at least 4 positions
        if len(joint_states.position) >= 4:
            # Modify joint 3's position based on a sine wave
            joint_trajectory = JointTrajectory()
            joint_trajectory.joint_names = joint_states.name

            point = JointTrajectoryPoint()
            point.positions = joint_states.position
            point.velocities = [0.0] * len(joint_states.position)
            point.accelerations = [0.0] * len(joint_states.position)

            # Adjust the modification to the desired joint (e.g., joint 3)
            joint_index_to_modify = 3
            point.positions[joint_index_to_modify] += self.amplitude_ * math.sin(self.phase_)

            # Update the phase for the next iteration
            self.phase_ += 2 * math.pi * self.frequency_

            point.time_from_start.sec = 0
            point.time_from_start.nanosec = int(1e9 * (1.0 / self.frequency_))

            joint_trajectory.points.append(point)
            self.joint_trajectory_pub_.publish(joint_trajectory)

def main(args=None):
    rclpy.init(args=args)
    node = JointSineOverlayNode("joint_sine_overlay_node")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
