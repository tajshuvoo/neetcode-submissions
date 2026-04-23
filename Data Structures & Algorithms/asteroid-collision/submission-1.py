class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                if abs(stack[-1]) > abs(ast):
                    break  # current asteroid dies
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()  # both die
                    break
                else:
                    stack.pop()  # stack asteroid dies, keep checking
            else:
                # only runs if while didn't break → asteroid survived
                stack.append(ast)

        return stack