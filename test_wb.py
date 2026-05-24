class Solve:
    def __init__(self, populations: list[int]):
      
        self.initial_pops = populations
        
        self.current_pops = populations.copy()
        
    def route_person(self):
       
        best_city = -1
        min_ratio = float('inf')
        
        for i in range(len(self.current_pops)):
            
            if self.initial_pops[i] == 0:
                continue 
                
            
            ratio = self.current_pops[i] / self.initial_pops[i]
            
            
            if ratio < min_ratio:
                min_ratio = ratio
                best_city = i
                
        
        if best_city != -1:
            self.current_pops[best_city] += 1
            
        return best_city



