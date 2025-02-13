#!/usr/bin/env python
# coding:utf-8
"""
机械臂驱动节点
"""
import rclpy
from rclpy.node import Node
from uservo.uservo_ex import uservo_ex
from robo_interfaces.srv import ReadData, WriteData
from robo_interfaces.msg import SetAngle
import struct
from sensor_msgs.msg import JointState

ROBO_DRIVER_NODE = "robo_driver_node" + str(uservo_ex.ID)
ROBO_SET_ANGLE_SUBSCRIBER = "set_angle_topic" + str(uservo_ex.ID)



class Arm_contorl(Node):

    def __init__(self):
        super().__init__(ROBO_DRIVER_NODE)
        self.declare_parameter("robo_type", "robo")
        self.declare_parameter("control_mode", "time")
        self.robo_type = (
            self.get_parameter("robo_type").get_parameter_value().string_value
        )
        self.control_mode = (
            self.get_parameter("control_mode").get_parameter_value().string_value
        )
        try:
            self.Servo = uservo_ex(self.robo_type)
        except ValueError as e:
            raise
        self.target_angle = self.Servo.ZERO_ANGLE

        # 初始化串口
        self.interval = [100 for _ in range(self.Servo.srv_num)]
        self.speed = [50 for _ in range(self.Servo.srv_num)]
        self.current_angle = [0.0 for _ in range(self.Servo.srv_num)]
        # 创建话题：发布joint_states
        self.joint_states_publisher = self.create_publisher(
            JointState, "joint_states", 10
        )
        # 创建话题：处理设置角度
        self.angle_subscribers = self.create_subscription(
            SetAngle, ROBO_SET_ANGLE_SUBSCRIBER, self.set_angle_callback, 10
        )
        # 创建服务端：反馈舵机状态消息
        self.srv = self.create_service(
            ReadData, "query_robo_states", self.query_state_callback
        )
        # 创建服务端：写入数据
        self.write_data_srv = self.create_service(
            WriteData, "writedata", self.write_data_callback
        )
        self.timer2 = self.create_timer(0.03, self.timer_callback)
        self.get_logger().info(f"初始化完成")

    def node_close(self):
        self.Servo.servo_all_stop()

    # 新的执行命令
    def set_angle_callback(self, msg):
        for i in range(len(msg.servo_id)):
            id = msg.servo_id[i]
            self.target_angle[id] = int(10*msg.target_angle[i])
            if self.control_mode == "time":
                self.interval[id] = int(msg.time[i])+20
            elif self.control_mode == "speed":
                self.speed[id] = int(msg.speed[i])
                if self.speed[id] < 20:
                    self.speed[id] = 20
                if self.speed[id] > 3000:
                    self.speed[id] = 3000
                    
        if self.control_mode == "time":
            self.arm_move_by_time()
        elif self.control_mode == "speed":
            self.arm_move_by_velocity()

    # 定时任务
    def timer_callback(self):
        self.publish_current_angle()

    # 查询舵机角度发布
    def publish_current_angle(self):
        JointState_msg = JointState()
        JointState_msg.header.stamp = self.get_clock().now().to_msg()
        JointState_msg.velocity = []
        JointState_msg.effort = []
        self.Servo.uservo.send_sync_servo_monitor(self.Servo.servo_ids)

        for i in range(self.Servo.srv_num):
            self.current_angle[i] = self.Servo.uservo.servos[i].angle_monitor
            JointState_msg.name.append(self.Servo.JOINT_[i])
            if self.robo_type == self.Servo.ROBO_TYPE_1:
                JointState_msg.position.append(
                    self.Servo.robo770_servoangle2jointstate(
                        servo_id=i, servo_angle=self.current_angle[i]
                    )
                )
            elif self.robo_type == self.Servo.ROBO_TYPE_2:
                JointState_msg.position.append(
                    self.Servo.servoangle2jointstate(
                        servo_id=i, servo_angle=self.current_angle[i]
                    )
                )
        self.joint_states_publisher.publish(JointState_msg)

    # 默认：控制by时间
    def arm_move_by_time(self):
        print(f'self.target_angle:{self.target_angle}')
        command_data_list = [struct.pack('<BhHH',i,self.target_angle[i], self.interval[i], 0)for i in range(self.Servo.srv_num)]
        self.Servo.set_angle(self.Servo.srv_num,command_data_list)

    # 控制by速度
    def arm_move_by_velocity(self):
        command_data_list = [struct.pack("<BhHHHH", i, self.target_angle[i], self.speed[i], 20, 20, 0)for i in range(self.Servo.srv_num)]
        self.Servo.set_angle_by_velocity(self.Servo.srv_num, command_data_list)

    def write_data_callback(self, request, response):
        command = request.command
        servo_id = request.servo_id
        value1 = request.value1
        match command:
            case "set_torque":
                if value1 == 0:
                    for i in self.Servo.uservo.servos:
                        self.Servo.disable_torque(i)
                    response.result = True
                elif value1 == 1:
                    for i in self.Servo.uservo.servos:
                        self.Servo.enable_torque(i)
                    response.result = True
            case _:
                print("invalid command")
        return response

    # 舵机状态反馈服务
    def query_state_callback(self, request, response):
        command = request.command
        match command:
            case "temperature":
                for i in self.Servo.uservo.servos:
                    response.servo_id.append(i)
                    response.servo_data.append(self.Servo.get_temperature(i))
            case "error_code":
                for i in self.Servo.uservo.servos:
                    response.servo_id.append(i)
                    response.servo_data.append(self.Servo.get_error_code(i))
            case _:
                print("invalid command")
        return response


def main(args=None):
    rclpy.init(args=args)
    try:
        robo_driver_node = Arm_contorl()
    except Exception as e:
        print(e)
        return

    try:
        rclpy.spin(robo_driver_node)
    except KeyboardInterrupt:
        pass
    finally:
        robo_driver_node.node_close()
        robo_driver_node.destroy_node()


if __name__ == "__main__":
    main()
