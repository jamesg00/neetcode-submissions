class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted(zip(position,speed), reverse=True)

        count = 0
        slowed = 0

        for pos, spd in car:
            time = (target - pos) / spd
            if time > slowed:
                count += 1
                slowed = time

        return count 
