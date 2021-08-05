import heapq


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        # dijkstra
        friend_li = []

        heap = [(0, id)]
        visited = set()

        while len(heap) != 0:
            dis, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            if dis == level:
                friend_li.append(node)

            if dis > level:
                break

            children = friends[node]
            for i in range(len(children)):
                child = children[i]
                if child not in visited:
                    heapq.heappush(heap, (1 + dis, child))

        if len(friend_li) == 0:
            return []
        movies = {}
        for i in range(len(friend_li)):
            temp = watchedVideos[friend_li[i]]
            for j in range(len(temp)):
                movies[temp[j]] = movies.get(temp[j], 0) + 1

        results = [key for key in movies.keys()]
        results.sort()
        results.sort(key=lambda x: movies[x])

        return results