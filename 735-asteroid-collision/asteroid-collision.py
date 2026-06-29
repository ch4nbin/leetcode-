class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack collisions only happen when negative is cur val and positive
        # is top of stack (so the most recent element) and basically
        # if negative wins you pop the postivie from stack removing it
        # and if positive wins you just dont append the negative
        # if its eequal youp pop and dont append and whatevers left in the
        # stack is the answer

        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
                
            if a:
                stack.append(a)
        
        return stack