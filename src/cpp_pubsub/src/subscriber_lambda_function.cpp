// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "geometry_msgs/msg/twist.hpp"

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber() : Node("minimal_subscriber")
  {
    //============
    auto topic2_callback = [this](geometry_msgs::msg::Twist::SharedPtr msg) ->void
      {
        RCLCPP_INFO(this->get_logger(), "I heard: %f , %f , %f , %f , %f , %f",  
                msg->linear.x, msg->linear.y, msg->linear.z,
                msg->angular.x, msg->angular.y, msg->angular.z);
      };
    //==============
    
    subscription_2 = this->create_subscription<geometry_msgs::msg::Twist>("cmd_vel", 10, topic2_callback);
  }

private:
    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr subscription_2;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}
