class CPU:
    def __init__(self, cpu_type):
        self.cpu_type = cpu_type

class computer:
    def __init__(self, cpu_type):
        self.CPU = CPU(cpu_type)