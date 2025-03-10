import time
import smbus2
import RPi.GPIO as GPIO

# I2C bus configuration and AS1170 address
I2C_BUS = 3  # Using Raspberry Pi I2C bus 3
I2C_ADDR = 0x30  # AS1170 I2C address

# AS1170 Registers
REG_STROBE_SIGNAL = 0x07
REG_FLASH_TIMER = 0x05
REG_CURRENT_LED1 = 0x01
REG_CURRENT_LED2 = 0x02
REG_CONTROL = 0x06

# STROBE pin configuration
STROBE_PIN = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(STROBE_PIN, GPIO.OUT, initial=GPIO.LOW)

# Initialize I2C bus
bus = smbus2.SMBus(I2C_BUS)

def write_register(register, value):
    """Writes a value to an AS1170 register."""
    bus.write_byte_data(I2C_ADDR, register, value)
    time.sleep(0.01)  # Small delay for stability

class LED:
    """Class to control individual LEDs connected to AS1170."""
    def __init__(self, led_number):
        self.led_register = REG_CURRENT_LED1 if led_number == 1 else REG_CURRENT_LED2

    def on(self, current=0x7F):
        """Turns on the LED with specified current (default ~450mA)."""
        write_register(self.led_register, current)
        write_register(REG_CONTROL, 0x1B)  # Enable flash mode
        GPIO.output(STROBE_PIN, GPIO.HIGH)
        print(f"LED{1 if self.led_register == REG_CURRENT_LED1 else 2} ON")

    def off(self):
        """Turns off the LED."""
        write_register(REG_CONTROL, 0x00)  # Disable LED
        GPIO.output(STROBE_PIN, GPIO.LOW)
        print(f"LED{1 if self.led_register == REG_CURRENT_LED1 else 2} OFF")

# Create LED objects
led = LED(1)

# If used as a standalone script, run a basic test
if __name__ == "__main__":
    try:
        led.on()
        time.sleep(2)  # Keep LED on for 2 seconds
        led.off()
    except KeyboardInterrupt:
        print("Exiting program...")
    finally:
        GPIO.cleanup()
        bus.close()
