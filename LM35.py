# running in Remote.it

# Importing modules
import spidev # To communicate with SPI devices
from time import sleep  # To add delay

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)

SLEEP = 1

# Read MCP3008 data
def analog_input(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data


# Below function will convert data to voltage
def convert_volt(data):
  volts = (data * 3.3) / float(1023)
  volts = round(volts, 2) # Round off to 2 decimal places
  return volts


# Below function will convert data to temperature.
def convert_temp(data):
  # 3300 mV / (10 mV/deg C) = 330
  # -2 for calibration purpuses
  temp = ((data * 330)/float(1023)) - 2
  temp = round(temp, 2)
  return temp


def temperature():
  temp_output = analog_input(0) # Reading from CH0
  temp_volts = convert_volt(temp_output)
  temp = convert_temp(temp_output)
  #result = ('Temp : {} ({}V) {} deg C'.format(temp_output,temp_volts,temp))
  # Sleep here so we don't fry the board
  sleep(SLEEP)
  return temp


if __name__ == "__main__":
    while True:

      print(temperature())