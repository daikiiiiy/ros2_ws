import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random


class SensorTalker(Node):

    def __init__(self):
        super().__init__('sensor_talker')
        self.publisher_ = self.create_publisher(Int32, 'sensor_value', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(0, 100)  # 疑似センサ値
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sensor value: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = SensorTalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

