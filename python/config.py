import logging

from python.json_manager import JsonManager


class Config:

    BASE_PATH = "/home/pi/deploy/"

    FACE_PIN = 0
    NECK_PIN = 0
    LIGHTS_PIN = 0
    LEFT_PWM_PIN = 0
    LEFT_DIR_PIN = 0
    RIGHT_PWM_PIN = 0
    RIGHT_DIR_PIN = 0

    def __init__(self, json_manager: JsonManager):
        self.json_config = json_manager.get_config()
        self.load()

    def load(self):
        self.load_pins()
        logging.debug(self.__dict__)

    def reload(self):
        self.json_config = JsonManager().get_config()
        self.load()

    def load_pins(self):
        self.NECK_PIN = self.json_config['pins']['neck']
        self.LIGHTS_PIN = self.json_config['pins']['lights']
        self.FACE_PIN = self.json_config['pins']['face']
        self.LEFT_PWM_PIN = self.json_config['pins']['left_pwm']
        self.LEFT_DIR_PIN = self.json_config['pins']['left_dir']
        self.RIGHT_PWM_PIN = self.json_config['pins']['right_pwm']
        self.RIGHT_DIR_PIN = self.json_config['pins']['right_dir']

