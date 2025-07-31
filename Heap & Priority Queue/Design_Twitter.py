import heapq
class Twitter:

    def __init__(self):
        self.tweets = {} 
        self.following = {} 
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((self.timestamp, tweetId)) 
        else:
            self.tweets[userId] = [(self.timestamp, tweetId)]
        self.timestamp += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        users = self.following.get(userId, set()) | {userId}

        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(max_heap, (-time, tweetId, uid, index))

        feed = []
        while max_heap and len(feed) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(max_heap)
            feed.append(tweetId)
            if index > 0:
                time, next_tid = self.tweets[uid][index - 1]
                heapq.heappush(max_heap, (-time, next_tid, uid, index - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId) 


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)