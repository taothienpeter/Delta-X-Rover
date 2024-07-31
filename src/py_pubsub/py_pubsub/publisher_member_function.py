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

from std_msgs.msg import String


class step_driver(Node):

    def __init__(self):
        super().__init__('step_driver')

        #setup para

        self.declare_parameter('loop_rate', value =0)
        if (self.get_parameter('loop_rate').value == 0):
            print("WARNING! loop rate set to 0!")

        self.declare_parameter('serial_port', value = "dev/ttyUSB0")
        self.serial_port = self.get_parameter('serial_port').value 

        self.declare_parameter('baud_rate', value = 9600)
        self.baud_rate = self.get_parameter('baud_rate').value

        self.declare_parameter('cmd', value='0')
        

    def timer_callback(self):
        pass
    def close_conn(self):
        self.conn.close()
        
    

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = step_driver()
    rclpy.spin(step_driver)
    step_driver.close_conn()
    step_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
