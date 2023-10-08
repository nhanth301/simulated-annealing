import math
import random
class SA_Problem:
    def __init__(self,initial_state,temp,min_temp,cooling_rate):
        self.initial_state = initial_state
        self.temp = temp
        self.min_temp = min_temp
        self.cooling_rate = cooling_rate
        
    def cost_func():
        pass
    
    def neighbor_func():
        pass
    
    def solve(self):
        current_state = self.initial_state
        current_cost = self.cost_func(current_state)
        best_state = current_state
        best_cost = current_cost
        temp = self.temp
        while temp > self.min_temp:
            neighbor = self.neighbor_func(current_state)
            neighbor_cost = self.cost_func(neighbor)
            delta_cost = neighbor_cost - current_cost
            acceptance_prob = math.exp(-delta_cost / temp)
            if delta_cost < 0:
                current_state = neighbor
                current_cost = neighbor_cost
            elif random.uniform(0, 1) < acceptance_prob:
                current_state = neighbor
                current_cost = neighbor_cost
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost
            temp *= (1-self.cooling_rate)
        return best_state, best_cost
