class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        friend_set = set(friends)

        result = []

        for person in order:

            if person in friend_set:
                result.append(person)

        return result