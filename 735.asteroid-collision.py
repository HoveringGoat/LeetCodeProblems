# @before-stub-for-debug-begin
from python3problem735 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def collide(self, leftAsteroids: List[int], rightAsteroids: List[int]) -> List[int]:
        # list of left asteroids moving right and 
        # right asteroids moving left. solve for what is left over
        if len(rightAsteroids) == 0:
            return leftAsteroids
        if len(leftAsteroids) == 0:
            rightAsteroids.reverse()
            return rightAsteroids
        
        maxRight = min(rightAsteroids) * -1
        maxLeft = max(leftAsteroids)

        if maxRight > maxLeft:
            # right asteroids win
            # right asteroids lose everything smaller than maxLeft up to maxRight asteroid
            for i in range(len(rightAsteroids)-1,-1,-1):
                if rightAsteroids[i] * -1 > maxLeft:
                    if i < len(rightAsteroids)-1:
                        rightAsteroids = rightAsteroids[:i+1]
                    break
                if rightAsteroids[i]*-1 == maxLeft:
                    rightAsteroids = rightAsteroids[:i]
                    break
            rightAsteroids.reverse()
            return rightAsteroids
        
        elif maxRight < maxLeft:
            # left asteroids win
            # left asteroids lose everything smaller than maxRight up to maxLeft asteroid
            for i in range(len(leftAsteroids)-1,-1,-1):
                if leftAsteroids[i] > maxRight:
                    if i < len(leftAsteroids)-1:
                        leftAsteroids = leftAsteroids[:i+1]
                    break
                if leftAsteroids[i] == maxRight:
                    leftAsteroids = leftAsteroids[:i]
                    break
            
            return leftAsteroids

        # the max values are equal. delete each side up to the max values
        # then call this again on the remaining values
        
        for i in range(len(leftAsteroids)-1,-1,-1):
            if leftAsteroids[i] == maxRight:
                leftAsteroids = leftAsteroids[:i]
                break
            
        for i in range(len(rightAsteroids)-1,-1,-1):
            if rightAsteroids[i]*-1 == maxLeft:
                rightAsteroids = rightAsteroids[:i]
                break

        if len(rightAsteroids) == 0 or len(leftAsteroids) == 0:
            # we can still finish!
            if len(rightAsteroids) > 0:
                rightAsteroids.reverse()
                return rightAsteroids
            return leftAsteroids

        return self.collide(leftAsteroids, rightAsteroids)
    
    def solveCollisions(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) < 2:
            return asteroids
        
        leftLeftAsteroids = [] # far left asteroids moving left
        leftAsteroids = [asteroids[0]] # group of left asteroids moving right

        # note right asteroids are kept in reverse order since we're "appending" to the end but that end is on the left
        rightAsteroids = [asteroids[len(asteroids)-1]] # groupd of right asteroids moving left
        rightRightAsteroids = [] # far right asteroids moving right
        nextLeftAsteroid = 1
        nextRightAsteroid = len(asteroids)-2

        # do collide
        while nextLeftAsteroid < nextRightAsteroid:
            # move larger asteroid
            if leftAsteroids[-1] > abs(rightAsteroids[-1]):
                if asteroids[nextLeftAsteroid] > 0:
                    # if one to the right is also moving right
                    leftAsteroids.append(asteroids[nextLeftAsteroid])
                    nextLeftAsteroid += 1
                else:
                    # collision!!
                    c = abs(asteroids[nextLeftAsteroid])
                    destroyed = False
                    for i in range(len(leftAsteroids)-1,-1,-1):
                        if leftAsteroids[i] > c:
                            # c is destroyed and left asteroids is now shorted
                            if i < len(leftAsteroids)-1:
                                leftAsteroids = leftAsteroids[:i+1]
                            nextLeftAsteroid += 1
                            destroyed = True
                            break
                        if leftAsteroids[i] == c:
                            leftAsteroids = leftAsteroids[:i]
                            nextLeftAsteroid += 1
                            destroyed = True
                            break

                    if not destroyed:
                        leftLeftAsteroids.append(asteroids[nextLeftAsteroid])
                        leftAsteroids = []
                        nextLeftAsteroid += 1

                    if len(leftAsteroids) == 0:
                        while nextLeftAsteroid < nextRightAsteroid:
                            if asteroids[nextLeftAsteroid] < 0:
                                leftLeftAsteroids.append(asteroids[nextLeftAsteroid])
                                nextLeftAsteroid += 1
                            else:
                                leftAsteroids.append(asteroids[nextLeftAsteroid])
                                nextLeftAsteroid += 1
                                break

                # done operating on left asteroids
                continue

            
            # right asteroid is bigger (or theyre even)
            else:
                if asteroids[nextRightAsteroid] < 0:
                    # next asteroid is also moving left
                    rightAsteroids.append(asteroids[nextRightAsteroid])
                    nextRightAsteroid -= 1
                else:
                    # collision!!
                    c = asteroids[nextRightAsteroid]
                    destroyed = False
                    for i in range(len(rightAsteroids)-1,-1,-1):
                        if rightAsteroids[i] * -1 > c:
                            # c is destroyed and right asteroids is now shorted
                            if i < len(rightAsteroids)-1:
                                rightAsteroids = rightAsteroids[:i+1]
                            nextRightAsteroid -= 1
                            destroyed = True
                            break
                        if rightAsteroids[i]*-1 == c:
                            rightAsteroids = rightAsteroids[:i]
                            nextRightAsteroid -= 1
                            destroyed = True
                            break
                        
                    if not destroyed:
                        rightRightAsteroids.append(c)
                        rightAsteroids = []
                        nextRightAsteroid -= 1

                    if len(rightAsteroids) == 0:
                        while nextRightAsteroid > nextLeftAsteroid:
                            if asteroids[nextRightAsteroid] > 0:
                                rightRightAsteroids.append(asteroids[nextRightAsteroid])
                                nextRightAsteroid -= 1
                            else:
                                rightAsteroids.append(asteroids[nextRightAsteroid])
                                nextRightAsteroid -= 1
                                break


                # done operating on right asteroids
                continue
        
        # the two sides have met
        if nextLeftAsteroid == nextRightAsteroid:
            if asteroids[nextRightAsteroid] > 0:
                leftAsteroids.append(asteroids[nextRightAsteroid])
            else:
                rightAsteroids.append(asteroids[nextRightAsteroid])

        s = self.collide(leftAsteroids, rightAsteroids)
        rightRightAsteroids.reverse()
        return leftLeftAsteroids + s + rightRightAsteroids


    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        startIndex = 0
        endIndex = len(asteroids) - 1

        # first lets ignore the astroids moving left at the start and
        # asteroids moving right at the end. These ones cant hit anything.
        # we can then solve the subset of asteroids and return that
        updated = True
        while updated and startIndex <= endIndex:
            updated = False
            # move start index in if neg
            if asteroids[startIndex] < 0:
                updated = True
                startIndex += 1
            # move end index in if its pos
            if asteroids[endIndex] > 0:
                updated = True
                endIndex -= 1
        if startIndex > endIndex:
            # no collisions return
            return asteroids
        
        start = asteroids[:startIndex]
        end = asteroids[endIndex+1:]
        subset = asteroids[startIndex:endIndex+1]

        subset = self.solveCollisions(subset)

        return start+subset+end
        
# @lc code=end

