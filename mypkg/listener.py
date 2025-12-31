#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Daiki Okamoto
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


THRESHOLD = 80  # 異常とみなすしきい値


class MonitorListener(Node):

    def __init__(self):
        super().__init__('monitor_listener')
        self.subscription = self.create_subscription(
            Int32,
            'sensor_value',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        if msg.data >= THRESHOLD:
            self.get_logger().warn(
                f'WARNING: Abnormal value detected! ({msg.data})'
            )
        else:
            self.get_logger().info(f'Normal value: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = MonitorListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

