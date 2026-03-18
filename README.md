menyuting dari bro mgi24

di link : https://github.com/mgi24/AudioStreamServerClient

change hardware ke module MAX98357A 
(lebih banyak dan murah di pasaran, di toko ijo dan orange banyak yang jual )

MAX98357A Pin	ESP32 Physical Pin	Function

LRC	 		GPIO 21			Left/Right Clock
BCLK   		GPIO 19			Bit Clock
DIN			GPIO 18			Data Out
GND	 		GND	  			Ground
Vin			5V / VCC			Power 

Atau sesuaikan dengan kebutuhan


Dengan mengedit INO dan Python dengan menambahkan volume control

VOLUME CONTROL 
1.0 = Original Volume
0.1 = Very Quiet
1.5 = Boosted (May cause distortion if original audio is loud)
VOLUME_FACTOR = 0.2

Rubah angka VOLUME FACTOR dan sesuaikan dengan kebutuhan.

Ditambahkan juga visual untuk memastikan music streaming monitoring lebih terlihat
VOLUME LEVEL VISUALIZER



Requirement:

ESP32 V3.0.2 Package arduino IDE
MAX98357A I2S Class-D Mono Amp


How to use:

Download the repo

Open the ino file with Arduino IDE, flash to ESP32

Open server script with python!


Semoga bermanfaat

