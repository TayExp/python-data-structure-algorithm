from random import randint
from prioqueue import PrioQueue
from SQueue import Squeue

class Simulation:
    def __init__(self, duration):
       self._eventq = PrioQueue()
       self._time = 0
       self._duration = duration

    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            self._time = event.time()
            if self._time > self._duration:
                break
            event.run()

    def add_event(self,event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time


class Customs:
    def __init__(self, gate_num, duration, arrive_interval, check_interval):
        self.simulation = Simulation(duration)
        self.waitline = Squeue()
        self.duration = duration
        self.gates = [0] * gate_num
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrive_interval = arrive_interval
        self.check_interval = check_interval

    def wait_time_acc(self,n):
        """累积等待时间增加"""
        self.total_wait_time += n

    def total_time_acc(self,n):
        """累积时间增加"""
        self.total_used_time += n

    def car_count_1(self):
        """车辆计数加1"""
        self.car_num += 1

    def add_event(self,event):
        self.simulation.add_event(event)

    def cur_time(self):
        return self.simulation.cur_time()

    def enqueue(self,car):
        self.waitline.enqueue(car)

    def has_queued_car(self):
        return not self.waitline.is_empty()

    def next_car(self):
        return self.waitline.dequeue()

    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None