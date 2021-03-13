class Solution:
    def isPathCrossing(self, path: str) -> bool:

        nx = [-1, 1, 0, 0]
        ny = [0, 0, 1, -1]
        route = [(0, 0)]
        x, y = 0, 0

        for i in path:

            if i == 'N':

                x += nx[0]
                y += ny[0]

            elif i == 'S':

                x += nx[1]
                y += ny[1]

            elif i == 'E':

                x += nx[2]
                y += ny[2]

            elif i == 'W':

                x += nx[3]
                y += ny[3]

            if (x, y) in route:
                return True

            route.append((x, y))

        return False