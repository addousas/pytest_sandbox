import sys
import logging
from pydantic import BaseModel
from datetime import datetime, timezone


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Output to console
        logging.FileHandler(f'run_{datetime.now(timezone.utc).timestamp()}.log')  # Output to file
    ]
)

class Operand(BaseModel):
    pass

class Operation(BaseModel):
    pass

class Instruction(BaseModel):
    pass


class DeviceConfigs:
    def __init__(self):
        logging.info("Device Configs: ")
        logging.warning("test")
        
        pass

class Device:
    def __init__(self):
        self.device_on = True
    
    def pwr_toggle(self):
        logging.info("Device: <toggle state>")
        self.device_on = not self.device_on

    def connect(self):
        if self.device_on:
            logging.info("Device Connect: ")
        


if __name__ == "__main__":
    dut = Device()
    dut.pwr_toggle()
    dut.connect()




