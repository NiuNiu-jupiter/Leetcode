"""
    Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
    
    Example:
    
    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1
    m.next(10) = (1 + 10) / 2
    m.next(3) = (1 + 10 + 3) / 3
    m.next(5) = (10 + 3 + 5) / 3

"""
class MovingAverage:
    
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.list = collections.deque()
        self.size = size
        self.sum = 0
    
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.list) >= self.size:
            self.sum -= self.list.popleft()
        self.list.append(val)
        self.sum+=val
        return self.sum /len(self.list)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
