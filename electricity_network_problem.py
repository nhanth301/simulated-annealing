"""
Bài toán tối ưu hóa mạng lưới điện. Bài toán này yêu cầu tìm cách cấu hình hệ thống
mạng lưới điện sao cho chi phí vận hành của hệ thống là thấp nhất
"""

import math
import random
import simulated_annealing as sa

class electricity_network_problem(sa.SA_Problem):
    def cost_func(self,state):
        total_cost = 0
        for component in state:
            power_usage = component["power_usage"]
            unit_price = component["unit_price"]
            cost = power_usage * unit_price
            total_cost += cost
        return total_cost
    
    def neighbor_func(self,state):
        new_state = state.copy()
        component_idx = random.randint(0, len(new_state) - 1)
        component = new_state[component_idx]
        component_type = component["type"]
        if component_type == "power_line":
            # Thay đổi công suất sử dụng của đường dây điện
            new_power_usage = random.uniform(0.5, 1.5) * component["power_usage"]
            new_state[component_idx]["power_usage"] = new_power_usage
        elif component_type == "lighting":
            # Thay đổi loại bóng đèn được sử dụng
            new_bulb_type = random.choice(["incandescent", "fluorescent", "LED"])
            new_state[component_idx]["bulb_type"] = new_bulb_type
        return new_state

if __name__ == "__main__":
    initial_state = [{"type": "power_line", "power_usage": 1000, "unit_price": 0.1},    
                     {"type": "power_line", "power_usage": 500, "unit_price": 0.1},    
                     {"type": "power_line", "power_usage": 2000, "unit_price": 0.1},    
                     {"type": "lighting", "bulb_type": "incandescent", "power_usage": 100, "unit_price": 0.2},    
                     {"type": "lighting", "bulb_type": "incandescent", "power_usage": 150, "unit_price": 0.2},    
                     {"type": "lighting", "bulb_type": "fluorescent", "power_usage": 80, "unit_price": 0.15},    
                     {"type": "lighting", "bulb_type": "LED", "power_usage": 50, "unit_price": 0.3}]
    problem = electricity_network_problem(initial_state = initial_state, temp= 1000, min_temp = 0.1, cooling_rate = 0.05)
    best_state, best_cost = problem.solve()
    print("Best state:", best_state)
    print("Best cost:", best_cost)