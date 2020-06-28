# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# BSK
# Time complexity: O(4^(N-M)), because for each cell the algorithm checks 4 directions.
# Space complexity: O(N-M), because of tracking visited cells.
# N is a number of cells in the room and M is a number of obstacles.
class Solution:
    def __init__(self):
        self.visited_set = set()
        self.dir_list = [(0, -1), (1, 0), (0, 1), (-1, 0)] # up, right, down, left
        
    def goBack(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
        
    def roamAround(self, robot, cur_x, cur_y, dir):
        # Roam around with an order of directions of up -> right -> down -> left

        for rel_dir in range(4):
            cur_dir = (dir + rel_dir)%4
            next_x = cur_x + self.dir_list[cur_dir][0]
            next_y = cur_y + self.dir_list[cur_dir][1]

            if (next_x, next_y) not in self.visited_set and robot.move():
                robot.clean()
                self.visited_set.add((cur_x, cur_y))   
                self.roamAround(robot, next_x, next_y, cur_dir)
                self.goBack(robot)
            robot.turnLeft()

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        cur_x, cur_y = 0, 0
        robot.clean()
        self.visited_set.add((cur_x, cur_y))
        
        self.roamAround(robot, cur_x, cur_y, dir=0)