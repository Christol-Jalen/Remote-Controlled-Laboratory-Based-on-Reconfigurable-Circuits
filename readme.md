# Reconfigurable Circuit Remote-Control Interface Application
To use the application, the following steps should be gone through:
## 1. U2IF Firmware Installation
Download the latest U2IF firmware from https://github.com/execuc/u2if/releases

Plug in the Pico while holding down the BOOTSEL button, then a USB flash storage should appear. Copy uf2 file on it.


## 2. Libraries Installation
Firstly, make sure that Python 3 is installed on your computer.
```Shell
python --version
```
Secondly, install hidapi and Blinka to support for the Pico to run U2IF firmware.
```Shell
pip3 install hidapi
pip3 install adafruit-blinka
```
Thirdly, install Pillow to support GUI's image display feature.
```Shell
pip install Pillow
```
Finally, install RsInstrument to support the programing of Oscilloscope's remote-control function.
```Shell
pip install RsInstrument
```
## 3. Run the Application
Open the Command Prompt, cd to the current directory, and input:
```Shell
set BLINKA_U2IF=1
python gui.py
```
Note: 1. Although the GUI supports cross-platform, this application only support Windows system, because the setup for the U2IF firmware varys between different operating systems. 2. Before running the gui.py, the computer must be correctly connected to the Raspberry Pi Pico (with U2IF Firmware, via USB) and R&S RTB2004 Oscilloscope (via LAN). Otherwise the program will report error.
