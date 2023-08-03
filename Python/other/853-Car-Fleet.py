class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list()
        stack = list()
        for index in range(len(position)):
            cars.append([position[index], speed[index]])

        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        print(cars)

        for car_position, car_speed in cars:
            stack.append((target - car_position) / car_speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


if __name__ == "__main__":
    s = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(s.carFleet(target, position, speed))
