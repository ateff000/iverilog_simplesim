import os
from sys import platform

if platform == 'linux':
	iverilog = 'iverilog'
	vvp = 'vvp'
	gtkwave = 'gtkwave'

elif platform == "win32":	
	iverilog = r'd:\Other\iverilog\bin\iverilog.exe'
	vvp = r'd:\Other\iverilog\bin\vvp.exe'
	gtkwave = r'd:\Other\iverilog\gtkwave\bin\gtkwave.exe'


testbench = 'Test00.v'
tested = 'SPI_SLAVE_8x.v'

output = 'qqq'


cmd_compil = f'{iverilog} -o {output} {tested} {testbench}'
cmd_sim = f'{vvp} {output}'


os.system(cmd_compil)
os.system(cmd_sim)


while True:
	command = input('>>>')
	if command == 'exit':
		break
	if command == 'run':
		os.system(cmd_compil)
		os.system(cmd_sim)

