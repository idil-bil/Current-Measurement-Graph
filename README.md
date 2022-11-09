# Live-Current-Graph
Project for my internship in TrioMobil R&D (August 2022)

## Team Members
[@HalilCakir](https://github.com/halilcakir) and Ümit Eren Ayhan

## Explanation
The current measuring circuit (see the [image](https://github.com/idil-bil/Live-Current-Graph/blob/main/breadboard%20for%20esp32.jpg)) is built using an Esp32 module. The power is connected to 3.3 Volts and the resistor on the right is 1 kOhm. The current on the resistor in the left is read through pin 34 with the code written using Arduino ([ReadAnalogCurrent](https://github.com/idil-bil/Live-Current-Graph/blob/main/ReadAnalogCurrent.ino)). The code calculates the average voltage at every 100 values and then calculates the current.

The [GetValue](https://github.com/idil-bil/Live-Current-Graph/blob/main/getvalue.py) file is written to read the data and store it in a .json file every second. Flask is also set up inside to serve an API that displays the data collected previously in a graph.

The graph code is originally downloaded from [this website](https://s7.dosya.tc/server23/pox3ax/sad.rar.html) and [extracted](https://extract.me/). The [modified version](https://github.com/idil-bil/Live-Current-Graph/blob/main/graph%20(modified).html) is a line graph where you can choose a spesific time interval using the scrollbar and view the data measured. 
