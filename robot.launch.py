from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package="cpp_pubsub",
            executable="talker"
        )
    ])