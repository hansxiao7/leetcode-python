"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n == 0:
            return 0

        x = n // 4
        y = n % 4

        temp = [''] * 4
        for i in range(x):
            n = read4(temp)
            for j in range(n):
                buf[i * 4 + j] = temp[j]
            if n < 4:
                return (i) * 4 + n

        n2 = read4(temp)
        for j in range(min(y, n2)):
            buf[4 * x + j] = temp[j]

        return x * 4 + min(y, n2)


