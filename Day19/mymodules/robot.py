import mymodules.intcode as itc

# Robot class
class Robot:
    
    def __init__(self, name=None):
        # Brain of the robot
        self.brain = itc.IntcodeComputer()
        self.name = name if name is not None else 'General Purpose Droid'
        # Variable to track subsequent position of the robot
        self.track_record = [0]
        
    
    # Load software to robot memory
    def load_software(self, software):
        
        self.brain.load_intcode(software)
        
        return
    
    
    # Run brain of the robot once
    def run_brain(self, instr):
                  
        response = self.brain.run(instr)
        
        return response
    
    def greeting(self):
        
        print('Hello, I am a', self.name)
