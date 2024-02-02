
# Weather Station

For my class of Datascience for IOT I made a weather station. I have used a raspberry pi 4 and a BMP280 sensor. This sensor measures temperature and air pressure. The data is read by the raspberry pi and then sends it to ThingSpeak where it gets put in graphs.


## Demovideo

https://youtu.be/poyPGMRJR-4
## Process

I started with connecting the BMP280 to the raspberry pi and reading out the sensor using [this](https://iotstarters.com/configuring-bmp280-sensor-with-raspberry-pi/) tutorial.
It didn't work at first, but after connecting SD0 pin of the sensor to the ground it did work. \
Then I started on sending data to ThingSpeak and view it. 
After that I combined both parts into one, which became my main code.
## Tutorial

### Hardware
* Raspberry pi
* BMP280

Connect the BMP to the Raspberry pi like the following diagram:

![pinout](https://iotstarters.com/wp-content/uploads/2021/07/rpi_bmp280_bb-min.png)
[source of image](https://iotstarters.com/configuring-bmp280-sensor-with-raspberry-pi/)

Also connect the SD0 pin of the BMP to the black wire/ground.

Run the following command in terminal on the Raspberry pi:
* sudo pip install bmp280

Create a ThingSpeak account and make a channel.\
Add 2 fields: "Temperature (°C)" and "Pressure (hPa)".

Download main.py to the Raspberry pi.\
Copy the Write API Key of the channel.\
Replace the value of writeAPIKey with the copied key.

Run the code and you should be seeing the data in the graphs appearing.
## References

https://iotstarters.com/configuring-bmp280-sensor-with-raspberry-pi/