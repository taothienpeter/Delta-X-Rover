# Dev_ws/src/cpp_pubsub/src/Deltax.launch.py

from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard'),
        launch_ros.actions.Node(
            package='cpp_pubsub',
            executable='listener'),

])