# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
#from std_msgs.msg import String
import serial


class teleop_serial(Node):

    def __init__(self):
        super().__init__('teleop_serial')

        #setup para

        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)


    def listener_callback(self, msg):
        linear_x = msg.linear.x
        angular_z = msg.angular.z
        command = "f {linear_x}, {angulaer_z}\n"
        self.serial_port.write(command.encode())

def main(args=None):
    rclpy.init(args=args)
    node = teleop_serial()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
