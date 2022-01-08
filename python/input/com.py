from python.input.message import Message
import serial
import logging

from python.input.file_watcher import FileWatcher


class Com:
    arduino_enable = True
    arduino = serial.Serial("/dev/serial0", 115200, timeout=1)
    # arduino = serial.Serial("/dev/ttyAMA0", 115200, timeout=1)
    # arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
    # time.sleep(0.1)  # wait for serial to open
    watcher = FileWatcher()

    def get_msg(self) -> Message:
        if self.watcher.changed():
            return self.watcher.get_last_key()

        if self.arduino_enable & self.arduino.isOpen():
            # logging.info("{} connected!".format(self.arduino.port))
            if self.arduino.inWaiting() > 0:
                msg = self.arduino.readline().decode('utf-8').rstrip()
                self.arduino.flushInput()  # remove data after reading
                logging.info('received from arduino' + msg)
                return self.decode(msg)
        return None

    def send_msg(self, msg):
        if self.arduino.isOpen():
            self.arduino.write(msg)

    def decode(self, msg: str):
        if msg.startswith(Message.PREFIX) and msg.endswith(Message.POSTFIX):
            return Message(msg[1], msg[2], msg[3], msg[4] + msg[5])
        else:
            logging.error("wrong message : \"" + msg + "\"")
            return None

