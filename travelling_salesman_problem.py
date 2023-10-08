"""
Bài toán người du lịch tìm tuyến đường ngắn nhất để đi qua 
các thành phố ở mỹ đúng 1 lần và quay trở lại thành phố xuất phát

Tọa độ trên bản đồ của các thành phố (kinh độ, vĩ độ)
New York City, NY (40.7128° N, 74.0060° W)
Chicago, IL (41.8781° N, 87.6298° W)
San Francisco, CA (37.7749° N, 122.4194° W)
Los Angeles, CA (34.0522° N, 118.2437° W)
Seattle, WA (47.6062° N, 122.3321° W)
Denver, CO (39.7392° N, 104.9903° W)
Dallas, TX (32.7767° N, 96.7970° W)
Miami, FL (25.7617° N, 80.1918° W)
Atlanta, GA (33.7490° N, 84.3880° W)
Boston, MA (42.3601° N, 71.0589° W)

"""
import math
import random
import simulated_annealing as sa

class travelling_salesman_problem(sa.SA_Problem):
    def __init__(self, coords, temp, min_temp, cooling_rate):
        self.coords = coords
        self.n = len(coords)
        self.dist_matrix = [[self.distance(coords[i], coords[j]) for j in range(self.n)] for i in range(self.n)]
        super().__init__(initial_state=list(range(self.n)), temp=temp, min_temp=min_temp, cooling_rate=cooling_rate)
        
    def cost_func(self, state):
        dist = 0
        for i in range(self.n):
            dist += self.dist_matrix[state[i]][state[(i+1)%self.n]]
        return dist
    
    def neighbor_func(self, state):
        # Hoán đổi hai thành phố ngẫu nhiên
        new_state = state.copy()
        i = random.randint(0, self.n-1)
        j = random.randint(0, self.n-1)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state
    
    def distance(self, coord1, coord2):
        """
        Tính khoảng cách (gần đúng) giữa hai tọa độ bằng công thức haversine
        """
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        R = 6371  # Bán kính trái đất tính bằng km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c

if __name__ == "__main__":
    coords = [
        (40.7128, -74.0060),  # New York City, NY
        (41.8781, -87.6298),  # Chicago, IL
        (37.7749, -122.4194),  # San Francisco, CA
        (34.0522, -118.2437),  # Los Angeles, CA
        (47.6062, -122.3321),  # Seattle, WA
        (39.7392, -104.9903),  # Denver, CO
        (32.7767, -96.7970),  # Dallas, TX
        (25.7617, -80.1918),  # Miami, FL
        (33.7490, -84.3880),  # Atlanta, GA
        (42.3601, -71.0589)  # Boston, Ma
    ]
    problem = travelling_salesman_problem(coords=coords, temp=1000, min_temp=0.1, cooling_rate=0.05)
    best_state, best_cost = problem.solve()
    print("Best tour:", [coords[i] for i in best_state])
    print("Best length:", best_cost)

