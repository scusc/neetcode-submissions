class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] == -1 * asteroid:
                        stack.pop()
                        break
                    
                    elif stack[-1] < -1 * asteroid:
                        stack.pop()

                    else:
                        break

                else:
                    stack.append(asteroid)        
        return stack