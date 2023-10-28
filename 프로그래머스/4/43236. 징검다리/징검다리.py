def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    minDistance = 1
    maxDistance = distance
    answer = 0

    while minDistance <= maxDistance:
        midDistance = (minDistance + maxDistance) // 2
        minRockDistance = float('inf')
        current = 0
        removed_rocks = 0

        for rock in rocks:
            if rock - current < midDistance:
                removed_rocks += 1
            else:
                minRockDistance = min(minRockDistance, rock - current)
                current = rock

        if removed_rocks > n:
            maxDistance = midDistance - 1
        else:
            minDistance = midDistance + 1
            answer = minRockDistance

    return answer


