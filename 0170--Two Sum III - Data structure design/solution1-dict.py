class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict1 = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """

        self.dict1[number] = self.dict1.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.dict1.keys():
            if self.dict1.get(value - key) is not None:
                if value - key == key:
                    if self.dict1[key] > 1:
                        return True
                    else:
                        continue
                return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)