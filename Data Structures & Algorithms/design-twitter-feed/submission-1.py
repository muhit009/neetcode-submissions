class Twitter:

    def __init__(self):
        self.count = 0 #count for get news feed 
        self.tweetMap = defaultdict(list) #[count, tweetId]
        self.followerMap = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count  -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # i need to get the followeeid for most recent tweets
        # get count and tweet id from [count,tweetid] and add it to heap
        # heap will have count, tweetid,index, followeeid (we need followee id to get the next tweet)
        # tooooo much! 
        res = [] # ordered list of 10 recent tweetIds
        minHeap = []
        self.followerMap[userId].add(userId) # an user is following itself
        
        # now the time to get the followeeid for most recent tweets
        # for that I need to go through followerMap and search the tweetMap for the followees

        for followeeId in self.followerMap[userId]: #get the recent tweets for followee
            if followeeId in self.tweetMap: # there might be a chance there is no tweet from the followee
                idx = len(self.tweetMap[followeeId])-1 #last value of the list
                count, tweetId = self.tweetMap[followeeId][idx] #list of count, tweetId
                minHeap.append([count, tweetId, followeeId, idx-1])
        heapq.heapify(minHeap)
        #pop from the heap
        #push things to heap 
        #append the tweeterIds in the res
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx>= 0:
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx-1])
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            return self.followerMap[followerId].remove(followeeId)
