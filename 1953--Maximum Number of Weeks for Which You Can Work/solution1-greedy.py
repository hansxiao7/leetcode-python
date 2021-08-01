class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        if len(milestones) == 1:
            return 1

        _sum = sum(milestones)
        _max = max(milestones)

        _rest = _sum - _max

        if _rest >= _max:
            return _sum
        else:
            return 2 * _rest + 1

