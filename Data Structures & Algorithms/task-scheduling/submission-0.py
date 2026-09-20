class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        all_tasks=[-cnt for cnt in c.values()]
        heapq.heapify(all_tasks)
        time=0
        q=deque()
        while all_tasks or q:
            time+=1
            if not all_tasks:
                time=q[0][1]
            else:
                cnt=1+heapq.heappop(all_tasks)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(all_tasks,q.popleft()[0])
        return(time)
