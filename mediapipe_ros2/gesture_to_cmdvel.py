from ctypes.wintypes import WORD
from turtle import forward
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from rclpy.timer import Timer
from rclpy.time import Time

import threading

class GestureControl(Node):

    def __init__(self):
        super().__init__('GestureControl')
        self.text_subscription = self.create_subscription(
            String,
            '/recognized_gesture',
            self.gesture_listener_callback,
            10)
        self.text_subscription  # prevent unused variable warning

        self.drive_cmd_publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

    def gesture_listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        drive_cmd_msg = Twist()
        speed = 0.5
        if msg.data == "front":

            # your code here
            pass

        if msg.data == "back":

            # your code here
            pass

        if msg.data == "left":

            # your code here
            pass

        if msg.data == "right":

            # your code here
            pass

        if msg.data == "stop":

            # your code here
            pass




def main(args=None):
    rclpy.init(args=args)

    gesture_control = GestureControl()

    rclpy.spin(gesture_control)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gesture_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
