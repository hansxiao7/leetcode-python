class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        # bitmask
        n_skills = len(req_skills)
        n_people = len(people)

        # index skills
        skill_map = {x: i for i, x in enumerate(req_skills)}

        people_bit = []
        for i in range(len(people)):
            temp = 0
            p = people[i]
            for j in range(len(p)):
                temp |= 1 << skill_map[p[j]]

            people_bit.append(temp)

        cache = {}

        def helper(pos, mask):
            if (pos, mask) in cache:
                return cache[(pos, mask)]
            if mask == 0:
                return []

            if pos == len(people_bit):
                return None

            result = None
            for i in range(pos, len(people_bit)):
                temp = mask & ~people_bit[i]
                if temp == mask:
                    continue
                else:
                    temp2 = helper(i + 1, temp)
                    if temp2 is not None:
                        if result is None or len(temp2) + 1 < len(result):
                            result = [i] + temp2
            cache[(pos, mask)] = result
            return result

        return helper(0, (1 << n_skills) - 1)