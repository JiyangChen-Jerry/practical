# control.py

class PDController:
    def __init__(self, kp=0.15, kd=0.6):#initialize the controller gains
        self.kp = kp
        self.kd = kd
        self.previous_error = 0

    def compute_control_action(self, reference, output):#compute the control action
        error = reference - output
        derivative = error - self.previous_error
        control_action = self.kp * error + self.kd * derivative
        self.previous_error = error
        return control_action