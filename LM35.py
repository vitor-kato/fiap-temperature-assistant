# running in Remote.it

# Importing modules
import sys
import spidev # To communicate with SPI devices
from time import sleep  # To add delay
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# LCD pins
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)

# LCD setup
lcd_columns = 16
lcd_rows = 2
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                                      lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)

SLEEP = 1.5

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
  temp = ((data * 330) / float(1023))
  temp = round(temp, 2)
  return temp


def temperature():
  temp_output = analog_input(0) # Reading from CH0
  temp_volts = convert_volt(temp_output)
  temp = convert_temp(temp_output)
  # result = ('Temp : {} ({}V) {} deg C'.format(temp_output,temp_volts,temp))

  lcd.message = ('Temperature: \n{}'.format(temp))
  return temp


if __name__ == "__main__":
    while True:
      try:
        sleep(SLEEP)
        print(temperature())
      except KeyboardInterrupt:
        lcd.clear()
        print('Exiting...')
        sys.exit(1)
