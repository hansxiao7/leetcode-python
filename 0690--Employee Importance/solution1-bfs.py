"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # get the importance of everyone
        dict1 = {}
        for e in employees:
            dict1[e.id] = e
            if e.id == id:
                chosen = e

        return dfs(chosen, dict1)


def bfs(e, dict1):
    result = e.importance
    queue = e.subordinates

    while len(queue) != 0:
        curr_e = dict1[queue.pop(0)]
        result += curr_e.importance
        queue.extend(curr_e.subordinates)

    return result


def dfs(e, dict1):
    result = e.importance

    if e.subordinates == []:
        return result

    for i in range(len(e.subordinates)):
        result += dfs(dict1[e.subordinates[i]], dict1)
    return result

