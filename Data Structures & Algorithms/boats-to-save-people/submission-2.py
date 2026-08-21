class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people)-1
        boats = 0

        while l <= r:
            the_sum = people[l] + people[r]

            if the_sum > limit:
                boats += 1
                r -= 1
            elif the_sum <= limit:
                boats += 1
                l += 1
                r -= 1

        return boats                

        