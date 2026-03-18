menyuting dari bro mgi24

di link : https://github.com/mgi24/AudioStreamServerClient


change hardware ke module MAX98357A 
(lebih banyak dan murah di pasaran, di toko ijo dan orange banyak yang jual )

dengan mengedit INO dan Python dengan menambahkan volume control

--- VOLUME CONTROL ---
1.0 = Original Volume
0.1 = Very Quiet
1.5 = Boosted (May cause distortion if original audio is loud)

VOLUME_FACTOR = 0.2


Rubah angka VOLUME FACTOR dan sesuaikan dengan kebutuhan.

Ditanbahkan juga visual untuk memastikan music streaming monitoring lebih terlihat



Requirement:

ESP32 V3.0.2 Package arduino IDE


How to use:

Download the repo

Open the ino file with Arduino IDE, flash to ESP32

Open server script!


Semoga bermanfaat
