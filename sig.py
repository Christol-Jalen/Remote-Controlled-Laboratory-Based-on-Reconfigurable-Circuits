# Import RsInstrument library
from RsInstrument import *
import global_var



# Create an instance of the RsInstrument object
instr = RsInstrument('TCPIP::192.168.1.2::INSTR', True, True)

# Set Parameters

def sigON():

	waveType = global_var.get_value("sigType")
	print("Signal type " + waveType + "is loaded")
	instr.write_str("WGENerator:FUNCtion " + waveType) #waveType itself is a str

	waveFreq = global_var.get_value("sigFreq")
	print("Signal frequnecy " + str(waveFreq) + "is loaded")
	instr.write_str("WGENerator:FREQuency " + str(waveFreq))

	Vpp = global_var.get_value("sigVpp")
	print("Vpp = " + str(Vpp) + "is loaded")
	instr.write_str("WGENerator:VOLTage " + str(Vpp)) 

	instr.write_str("WGENerator:OUTPut:LOAD HIGHz") 
	instr.write_str("WGENerator:OUTPut ON")
	# Close the instrument connection
	instr.close()


def sigOFF():
	instr.write_str("WGENerator:OUTPut OFF")