import pyvisa
import time
import logging

logger = logging.getLogger(__name__)


class AxisError(Exception):
        # COEF = 10 (pulse/mm)

    MESSAGES = {
        "X": "Command or parameter errors",
        "K": "Normal state",
        "L": "First-axis stopped at LS",
        "W": "First and second axes stopped at LS",
    }

    def __init__(self, error_code):
        self.message = self.MESSAGES[error_code]


class GSC:
    default_units = ' '

    def __init__(self, rsrc_name):
        self._actuator = None
        self.rsrc_name = rsrc_name
        self.position = [0, 0] 
        self.speed_ini = [0, 0]
        self.speed_fin = [0, 0]
        self.accel_t = [0, 0]
        

    def connect(self):
        try:
            rm = pyvisa.ResourceManager()
            self._actuator = rm.open_resource(self.rsrc_name)
            self._actuator.write_termination = "\r\n"
            self._actuator.read_termination = "\r\n"
            self._actuator.baud_rate = 9600
            logger.info(f"Connection to {self._actuator} successful")
        except Exception as e:
            logger.error(f"Error connecting to {self.rsrc_name}: {e}")
        
#### Below are methods based on updating the GUI units 
    def convert_units(self, units, value, coeff):
        """Convert value based on the units. Coefficient is taken through the GUI"""
        if units == " " or units == "pulse":
            return value
        elif units == "um":
            return value*(coeff) 
    
    def set_unit(self, unit): 
        """Set the unit pulse based on the GUI needed"""
        if unit == "pulse": 
            return " "
        else: 
            return unit
    def get_unit_position(self, unit, channel): 
        """Gets the actuator position based on the unit."""
        if unit == 'um': 
            self.position[channel-1] = (self.position[channel-1])/2 
        else: 
            pass
### End of the block of code that updates the unit of GUI
    def move(self, position, channel):
        """Move the specified channel to the position."""

        print(position, "pulses in move method")

        if position >= 0:
            self._actuator.write(f"A:{channel}+P{position}")
        else:
            self._actuator.write(f"A:{channel}-P{abs(position)}")
        self._actuator.write("G:")
        self.wait_for_ready()
        
        self.position[channel - 1] = position

    def move_rel(self, position, channel):
        """Move the specified channel to the relative position."""
        if position >= 0:
            self._actuator.write(f"M:{channel}+P{position}")
        else:
            self._actuator.write(f"M:{channel}-P{abs(position)}")
        self._actuator.write("G:")
        self.wait_for_ready()
        self.position[channel - 1] = position + self.position[channel - 1]

    def stop(self, channel):
        """Stop the specified channel."""
        self._actuator.write(f"L:{channel}")

    def get_position(self, channel):
        """Get the position of the specified channel."""
        if self.position[channel - 1] is None:
            return logger.error("Position is None")
        return self.position[channel - 1]

    def home(self, channel):
        """Move the specified channel to the home position."""
        self._actuator.write(f"H:{channel}")
        self.wait_for_ready()
        self.position[channel - 1] = 0

    def set_speed(self, speed_ini, speed_fin, accel_t, channel):
        """Set the speed of the specified channel"""
        if speed_ini >= 0 and speed_fin >= 0 and accel_t >= 0:
            self._actuator.write(f"D:{channel}S{speed_ini}F{speed_fin}R{accel_t}")
            self.speed_ini[channel - 1] = speed_ini
            self.speed_fin[channel - 1] = speed_fin
            self.accel_t[channel - 1] = accel_t
        else:
            logger.error("Speed, acceleration, and deceleration must be positive")

    def get_speed(self, channel):
        """Get the speed of the specified channel"""
        if self.speed_ini[channel - 1] is None:
            return logger.error("Speed is None")
        return self.speed[channel - 1]

    def close(self):
        pyvisa.ResourceManager().close()

    def check_error(self):
        """Checks for the errors and returns the error message."""
        error = self._actuator.query("Q:")
        error = error.split(",")[2]
        if error != "K":
            logger.error(f"Error: {error}")
            AxisError(error)

    def read_state(self):
        """Read the state of the specified channel."""
        state = self._actuator.query(f"!:") 
        return state

    def wait_for_ready(self):
        time0 = time.time()
        while self.read_state() != "R":
            time1 = time.time() - time0
            if time1 >= 60:
                logger.error("Timeout error")
                self.check_error()
                break
            time.sleep(0.2)