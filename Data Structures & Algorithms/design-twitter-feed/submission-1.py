class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count-=1
        self.tweetMap[userId].append((self.count,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        userIds = [userId]+ list(self.followMap[userId])
        AllTweets = []
        for _id in userIds:
            AllTweets+=self.tweetMap[_id]
        heapq.heapify(AllTweets)
        res = []
        while k and AllTweets:
            res.append(heapq.heappop(AllTweets)[1])
            k-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
