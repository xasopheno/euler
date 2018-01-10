class Euler014:
    def __init__(self, maximum=1000000):
        self.maximum = maximum
        self.cache = self.populate_cache()
        self.longest_path = {0: 0}

    def populate_cache(self):
        cache = {}
        for i in range(self.maximum):
            cache[i] = 0
        return cache

    @staticmethod
    def even(n):
        return n/2

    @staticmethod
    def odd(n):
        return 3*n + 1

    def collatz(self, n):
        if n % 2 == 0:
            return self.even(n)
        else:
            return self.odd(n)

    def max_collatz_path_length(self):
        for i in range(2, self.maximum):
            path_length = 0
            current_value = i
            while current_value != 1:
                new_value = self.collatz(current_value)
                path_length += 1
                try:
                    _ = self.cache[new_value]
                except:
                    self.cache[new_value] = 0
                if self.cache[new_value] and self.cache[new_value] != 0:
                    self.cache[i] = path_length + self.cache[new_value]
                    break
                elif new_value == 1:
                    self.cache[i] = path_length
                    break
                else:
                    current_value = new_value


def euler_014_answer():
    euler014 = Euler014()
    euler014.max_collatz_path_length()
    answer = max(euler014.cache.keys(), key=(lambda key: euler014.cache[key]))
    return answer
