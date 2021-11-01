here are new things

sudo="sudo"
command="fdisk"
commandArgument="-l"
print(f'Gathering partition information with command: {sudo} {command} {commandArgument}')
subprocess.run([sudo,command,commandArgument])
