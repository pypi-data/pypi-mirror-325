"""
舵机转手臂控制通用类
"""

import math
import struct
import serial
from uservo.uservo import UartServoManager
from robo_interfaces.srv import ReadData, WriteData
import time


class writedata:
    def __init__(self, command, servo_id=255, value=0):
        if command == None:
            return
        WriteData_ = WriteData()
        WriteData_.command = command
        WriteData_.servo_id = servo_id
        WriteData_.value = value
        return WriteData_


class uservo_ex:
    ROBO_TYPE_1 = "robo_770"
    ROBO_TYPE_1_JOINT_ = [
        "joint1",
        "joint2",
        "joint3",
        "joint4",
        "joint5",
        "joint6",
        "joint7_right",
    ]
    ROBO_TYPE_1_INDEX_JOINT_ = {
        value: index for index, value in enumerate(ROBO_TYPE_1_JOINT_)
    }

    ROBO_TYPE_2 = "robo_280"
    ROBO_TYPE_2_JOINT_ = [
        "robot_joint1",
        "robot_joint2",
        "robot_joint3",
        "robot_joint4",
        "hand_joint",
        "grippers_joint",
        "right_joint",
    ]
    ROBO_TYPE_2_INDEX_JOINT_ = {
        value: index for index, value in enumerate(ROBO_TYPE_2_JOINT_)
    }

    SERVO_PORT_NAME = "/dev/ttyAMA1"  # 舵机串口号 <<< 修改为实际串口号
    SERVO_BAUDRATE = 500000  # 舵机的波特率
    ID = 0  # 多手臂时区分话题ID
    servo_ids = list()

    # 参数
    # PORT_NAME: 设置舵机串口号，默认使用/dev/ttyUSB0，当需要在同一个设备上使用多个机械臂时，需要修改该参数
    # SET_ZERO: 是否回到零位，默认回到零位
    # CHECK_ANGLE: 是否检查上电舵机角度，默认检查，确保初始化状态一致性。
    def __init__(self, robo_type, PORT_NAME=None, SET_ZERO=True, CHECK_ANGLE=True):
        self.ROBO_TYPE = robo_type
        if self.ROBO_TYPE == self.ROBO_TYPE_1:
            self.JOINT_ = self.ROBO_TYPE_1_JOINT_
            self.INDEX_JOINT_ = self.ROBO_TYPE_1_INDEX_JOINT_
        elif self.ROBO_TYPE == self.ROBO_TYPE_2:
            self.JOINT_ = self.ROBO_TYPE_2_JOINT_
            self.INDEX_JOINT_ = self.ROBO_TYPE_2_INDEX_JOINT_
        else:
            raise ValueError("未知的机器人类型")
        self.INDEX_JOINT_ = {value: index for index, value in enumerate(self.JOINT_)}

        # 初始化串口
        success = False
        while not success:
            try:
                if PORT_NAME == None:
                    self.uart = serial.Serial(
                        port=self.SERVO_PORT_NAME,
                        baudrate=self.SERVO_BAUDRATE,
                        parity=serial.PARITY_NONE,
                        stopbits=1,
                        bytesize=8,
                        timeout=0,
                    )
                else:
                    self.uart = serial.Serial(
                        port=PORT_NAME,
                        baudrate=self.SERVO_BAUDRATE,
                        parity=serial.PARITY_NONE,
                        stopbits=1,
                        bytesize=8,
                        timeout=0,
                    )
                success = True  # 如果成功初始化，则设置成功标志
            except serial.SerialException as e:
                print(f"串口初始化失败: {e}")
                time.sleep(0.1)  # 暂停 1 秒后重试
        try:
            self.uservo = UartServoManager(self.uart, srv_num=7)
        except Exception as e:
            raise

        self.servo_ids = list(self.uservo.servos.keys())
        self.srv_num = len(self.uservo.servos)

        if self.ROBO_TYPE == self.ROBO_TYPE_1:
            if self.srv_num != 7:
                raise ValueError(f"舵机数量错误 只有{self.srv_num}")
        elif self.ROBO_TYPE == self.ROBO_TYPE_2:
            if self.srv_num != 6:
                raise ValueError(f"舵机数量错误 只有{self.srv_num}")

        self.ZERO_ANGLE = [0 for _ in range(self.srv_num)]

        time.sleep(1)
        if CHECK_ANGLE:
            for id in range(self.srv_num):
                start_angle = self.query_servo_current_angle(id)
                if start_angle < -180 or start_angle > 180:
                    self.reset_multi_turn_angle(id)
                    time.sleep(0.1)
                    print(f"{id}号舵机当前为{start_angle}，已重设")
        if SET_ZERO:
            print(f"正在回到零位")
            self.move_to_zero()
        time.sleep(3)
        print(f"{self.ROBO_TYPE} driver init")

    # 返回虚拟关节的名称
    @classmethod
    def fake_joint_name(cls):
        return "right_joint"

    # 将弧度转为角度
    @classmethod
    def radians_to_degrees(cls, radians):
        degrees = radians * (180 / math.pi)
        return degrees

    # 将米转为角度
    @classmethod
    def meters_to_degrees(cls, meters):
        degrees = (meters / 0.027) * 50
        return degrees

    # 将角度转为弧度
    @classmethod
    def degrees_to_radians(cls, degrees):
        radians = degrees * (math.pi / 180)
        return radians

    # 将角度转为米
    @classmethod
    def degrees_to_meters(cls, degrees):
        meters = (degrees / 50) * 0.027
        return meters

    @classmethod
    def jointstate2servoangle(cls, servo_id, joint_state):
        if servo_id == 0:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 1:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 2:
            return cls.radians_to_degrees(-joint_state)
        elif servo_id == 3:
            return cls.radians_to_degrees(-joint_state)
        elif servo_id == 4:
            return cls.radians_to_degrees(-joint_state)
        elif servo_id == 5:
            return cls.meters_to_degrees(joint_state)
        else:
            return 0

    @classmethod
    # 将舵机角度转换为关节位置
    def servoangle2jointstate(cls, servo_id, servo_angle):
        if servo_id == 0:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 1:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 2:
            return -cls.degrees_to_radians(servo_angle)
        elif servo_id == 3:
            return -cls.degrees_to_radians(servo_angle)
        elif servo_id == 4:
            return -cls.degrees_to_radians(servo_angle)
        elif servo_id == 5:
            return -cls.degrees_to_meters(servo_angle)

    @classmethod
    def robo770_jointstate2servoangle(cls, servo_id, joint_state):
        if servo_id == 0:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 1:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 2:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 3:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 4:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 5:
            return cls.radians_to_degrees(joint_state)
        elif servo_id == 6:
            return cls.meters_to_degrees(joint_state)
        else:
            return 0

    @classmethod
    # 将舵机角度转换为关节位置
    def robo770_servoangle2jointstate(cls, servo_id, servo_angle):
        if servo_id == 0:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 1:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 2:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 3:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 4:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 5:
            return cls.degrees_to_radians(servo_angle)
        elif servo_id == 6:
            return cls.degrees_to_meters(servo_angle)

    def write_500k_bandrate(self):
        softstart_bytes = struct.pack("<B", 7)
        # 将数据写入内存表
        for i in self.uservo.servos:
            self.uservo.write_data(4, 36, softstart_bytes)
        self.uservo.write_data(9, 36, softstart_bytes)

    # 移动到零点
    def move_to_zero(self):
        command_data_list = [
            struct.pack("<BhHH", i, int(self.ZERO_ANGLE[i] * 10), 3000, 0)
            for i in range(self.srv_num)
        ]
        self.uservo.send_sync_angle(self.srv_num, command_data_list)

    # 设置角度
    def set_angle(self, size, command_data_list):
            self.uservo.send_sync_angle(size, command_data_list)

    # 设置角度（指定转速）
    def set_angle_by_velocity(self, size, command_data_list):
            self.uservo.send_sync_anglebyvelocity(size, command_data_list)

    # 设置角度（指定转速）
    def set_angle_by_interval(self, size, command_data_list):
            self.uservo.send_sync_anglebyinterval(size, command_data_list)

    def set_single_angle(self, servo_id, angle, velocity=30):
            self.uservo.set_servo_angle(servo_id, angle, velocity=velocity)

    # 查询角度
    def query_servo_current_angle(self, servo_id):
        if servo_id in self.uservo.servos:
            return self.uservo.query_servo_angle(servo_id)

    # 失能舵机
    def disable_torque(self, servo_id):
        self.servo_stop(servo_id)

    def enable_torque(self, servo_id):
        current_angle = self.uservo.query_servo_angle(servo_id)
        self.set_single_angle(servo_id, current_angle)

    # 查询一次温度
    def get_temperature(self, servo_id):
        if servo_id in self.uservo.servos:
            return self.uservo.query_temperature(servo_id)

    # 查询错误码
    def get_error_code(self, servo_id):
        if servo_id in self.uservo.servos:
            code = self.uservo.query_status(servo_id)
            if code <= 1:
                return 0
            else:
                return code

    # 重设所有舵机多圈圈数
    def reset_all_servo_multi_turn_angle(self):
        for i in self.uservo.servos:
            self.reset_multi_turn_angle(i)

    # 重设指定舵机多圈圈数
    def reset_multi_turn_angle(self, servo_id):
        self.uservo.disable_torque(servo_id)
        time.sleep(0.05)
        self.uservo.reset_multi_turn_angle(servo_id)

    # 返回舵机数量
    def servo_num(self):
        if self.srv_num:
            return self.srv_num
        return 0

    def servo_stop(self, servo_id, mode=2, power=500):
        self.uservo.stop_on_control_mode(servo_id, mode, power)

    def servo_all_stop(self, mode=2, power=500):
        for id in range(self.srv_num):
            self.servo_stop(id, mode, power)
            time.sleep(0.05)


    #舵机停止释放锁力
    def servo_stop_lock(self, servo_id):
        self.uservo.stop_on_control_mode(servo_id,0,500)
    #舵机保持锁力
    def servo_keep_lock(self, servo_id):
        self.uservo.stop_on_control_mode(servo_id,1,50000)

    #舵机设置原点
    def servo_set_origin_point(self, servo_id):
        self.uservo.set_origin_point(servo_id)
    #发送0°角度命令
    def servo_set_zero_angle(self, servo_id, angle, interval, power):
        self.uservo.set_servo_angle(servo_id,angle,interval,power)

    #读取内存表数据
    def servo_read_data(self, servo_id, address):
        self.uservo.read_data(servo_id,address)

    #写入内存表数据
    def servo_write_data(self, servo_id, address, content):
        self.uservo.write_data(servo_id,address,content)

