class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalCustomers = len(customers)
        idle_at = 0
        total_waiting_time = 0
        for i,j in customers:
            if idle_at<=i:
                total_waiting_time+=j
                idle_at = i+j
            else:
                total_waiting_time+=(idle_at-i)+j
                idle_at+=j
        averageTime = total_waiting_time/totalCustomers
        return averageTime
