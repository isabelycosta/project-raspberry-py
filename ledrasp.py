import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
def main():
	x = input("Digite 1 para acionar e 0 para sair: ")
    	if x == 1:
		y = input("Quantas repeticoes voce deseja? ")
		turnOn(y)
	else:
        	turnOff()

def turnOn(rep):
    	while(rep):
	    	print("LED ON\n")
	    	GPIO.output(18,1)
	    	time.sleep(1)
	    	print("LED OFF")
	    	GPIO.output(18,0)
	    	time.sleep(1)
		rep = rep -1
def turnOff():
    		exit(1)
main()
