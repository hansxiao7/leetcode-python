class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        # bitmask
        dict1 = {}
        n = len(req_skills)
        target = [1 for _ in range(n)]

        for i in range(n):
            dict1[req_skills[i]] = i

        people_li = []
        for i in range(len(people)):
            p = people[i]
            temp = [0 for _ in range(n)]
            for j in range(len(p)):
                temp[dict1[p[j]]] = 1

            people_li.append(temp)

        # dfs
        self.result = None

        def helper(pos, curr, target):
            if sum(target) == 0:
                if self.result is None or len(curr) < len(self.result):
                    self.result = list(curr)
                return

            if pos == len(people_li):
                return

            for i in range(pos, len(people_li)):
                p = people_li[i]
                temp = list(target)
                for j in range(len(target)):
                    if temp[j] == 0:
                        continue

                    if temp[j] == p[j] == 1:
                        temp[j] = 0

                if sum(temp) < sum(target):
                    curr.append(i)
                    helper(i + 1, curr, temp)
                    curr.pop()

        helper(0, [], target)

        return self.result

