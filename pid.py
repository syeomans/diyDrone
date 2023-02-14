import time 
import random

print("Hello world")

class pid:
    def __init__(self, setpoint, Kp=1, Ki=1, Kd=1, dt=0.01):
        self.setpoint = setpoint
        self.Kp = Kp 
        self.Ki = Ki 
        self.Kd = Kd 
        self.dt = dt 
        self.previousError = 0
        self.integral = 0
        self.processVar = 0
        self.controlVar = 0
        self.running = True

    def updateControl(self):
        error = self.setpoint - self.processVar
        proportional = error
        self.integral += error * self.dt 
        derivative = (error - self.previousError) / self.dt
        self.controlVar = self.Kp*proportional + self.Ki * self.integral + self.Kd * derivative
        self.previousError = error

    def updateProcess(self):
        # Return a random number for now
        self.processVar = random.randrange(1,10)

    def setSetpoint(self, setpoint):
        self.setpoint = setpoint

    def setKp(self, Kp):
        self.Kp = Kp
    
    def setKi(self, Ki):
        self.Ki = Ki 
    
    def setKd(self, Kd):
        self.Kd = Kd

    def setRunning(self, running):
        self.running = running

    def loop(self):
        while self.running:
           self.updateProcess()
           self.updateControl()
           time.sleep(self.dt) 
