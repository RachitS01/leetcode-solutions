class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque()
        visited = set()
        ans = []

        queue.append(id)
        visited.add(id)


        for _ in range(level):
            k = len(queue)
            for _ in range(k):
                person = queue.popleft()

                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
          

        freq = Counter()
        for people in queue:
            for videos in watchedVideos[people]:
                freq[videos] += 1
        freq= sorted(freq.keys(),key=lambda x : (freq[x],x) )
        print(freq)

        return freq
