class MySqrt:
    @staticmethod
    def geron_sqrt(value):
        sqrt = 3
        while True:
            buff = sqrt
            sqrt = 0.5 * (sqrt + value / sqrt)
            if buff == sqrt:
                break
        return sqrt

if __name__ == '__main__':
    result = MySqrt.geron_sqrt(100)
    print(result)
