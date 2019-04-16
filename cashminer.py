import time
import copy
class cashminer:
    def fileread(self):
            f = open("input.txt")
            line = f.readline()
            self.n = int(line)

            line = f.readline()
            i = int(line)
            line = f.readline()
            wall = []
            while i>0 and line:
                list = line.split(",")
                l = map(int, list)
                wall.append(l)
                i -= 1
                line = f.readline()
            self.wall = wall
          #  print self.wall


            state = [[0 for _ in range(self.n)] for _ in range(self.n)]
          #  print state

            j = int(line)
         #   print j
            line = f.readline()
            terminal = []
            while j>0 and line:
               # print 1
                list = line.split(",")
                l = map(int, list[:2])
                terminal.append(l)
                state[l[0]-1][l[1]-1] = float(list[2])
                j -= 1
                line = f.readline()
            self.terminal = terminal
           # print state


            self.P = float(line)

            line = f.readline()
            self.Rp = float(line)

            line = f.readline()
            self.gama = float(line)
            self.upper = 0.01*(1-self.gama)/self.gama

            for i in range(self.n):
                for j in range(self.n):
                    if (self.check(i+1, j+1)):
                        state[i][j] = self.Rp
                    else:
                        continue
            self.state =state
          #  print state
        #    print self.upper
            f.close()



    def _init_(self, wall, terminal, depth,
               score, n):

        self.wall = wall
        self.terminal = terminal
        self.score = 0


    def renew(self):
        state = self.state
     #   print state
     #   print self.max_value(state, 0, 0)
        while(self.finalState(state) and time.time()-start < 26 ):
            new_state = copy.deepcopy(state)
            for i in range(self.n):
                for j in range(self.n):
                    if self.check(i+1, j+1):
                        new_state[i][j] = self.max_value(state, i, j)
                     #   print self.max_value(state, i, j)
            state = copy.deepcopy(new_state)
        # print state
        f = open("output.txt", "w")

        for i in range(0, self.n):
            for j in range(0, self.n):
                if [i+1, j+1] in self.wall:
                    f.write ("N")
                if [i+1, j+1] in self.terminal:
                    f.write ("E")
                if (self.check(i+1, j+1)):
                    f.write(self.nextstep(state, i, j))
                if (j<self.n-1):
                    f.write (",")

            f.write ("\n")

        f.close()


    def nextstep(self, state, row, column):
        up = 0
        down = 0
        left = 0
        right = 0
        if (row-1>=0 and [row, column+1] not in self.wall):
            up += self.P * state[row-1][column]
        else:
            up += self.P*state[row][column]

        if (row+1<self.n and [row+2, column+1] not in self.wall):
            down += self.P * state[row+1][column]
        else:
            down += self.P*state[row][column]

        if (column+1<self.n and [row+1, column+2] not in self.wall):
            right += self.P * state[row][column+1]
        else:
            right += self.P*state[row][column]

        if (column-1>=0 and [row+1, column] not in self.wall):
            left += self.P*state[row][column-1]
        else:
            left += self.P*state[row][column]

        if (column-1>=0 and row-1>=0 and [row, column] not in self.wall):
            left += (1-self.P)/2*state[row-1][column-1]
            up += (1-self.P)/2*state[row-1][column-1]
        else:
            left += (1-self.P)/2*state[row][column]
            up += (1-self.P)/2*state[row][column]

        if (column-1>=0 and row+1<self.n and [row+2, column] not in self.wall):
            left += (1-self.P)/2*state[row+1][column-1]
            down += (1-self.P)/2*state[row+1][column-1]
        else:
            left += (1-self.P)/2*state[row][column]
            down += (1-self.P)/2*state[row][column]

        if (row-1>=0 and column+1<self.n and [row, column+2] not in self.wall):
            right += (1-self.P)/2*state[row-1][column+1]
            up += (1-self.P)/2*state[row-1][column+1]
        else:
            right += (1-self.P)/2*state[row][column]
            up += (1-self.P)/2*state[row][column]

        if (row+1<self.n and column+1<self.n and [row+2, column+2] not in self.wall):
            right += (1-self.P)/2*state[row+1][column+1]
            down += (1-self.P)/2*state[row+1][column+1]
        else:
            right += (1-self.P)/2*state[row][column]
            down += (1-self.P)/2*state[row][column]
        m = max(up, down, right, left)
        if (left == m):
            #print left
            return "L"
        if (right == m):
            return "R"
        if (up == m):
            return "U"
        return "D"




    def max_value(self, state, row, column):
        up = 0
        down = 0
        left = 0
        right = 0
        if (row-1>=0 and [row, column+1] not in self.wall):
            up += self.P * state[row-1][column]
        else:
            up += self.P*state[row][column]

        if (row+1<self.n and [row+2, column+1] not in self.wall):
            down += self.P * state[row+1][column]
        else:
            down += self.P*state[row][column]

        if (column+1<self.n and [row+1, column+2] not in self.wall):
            right += self.P * state[row][column+1]
        else:
            right += self.P*state[row][column]

        if (column-1>=0 and [row+1, column] not in self.wall):
            left += self.P*state[row][column-1]
        else:
            left += self.P*state[row][column]

        if (column-1>=0 and row-1>=0 and [row, column] not in self.wall):
            left += (1-self.P)/2*state[row-1][column-1]
            up += (1-self.P)/2*state[row-1][column-1]
        else:
            left += (1-self.P)/2*state[row][column]
            up += (1-self.P)/2*state[row][column]

        if (column-1>=0 and row+1<self.n and [row+2, column] not in self.wall):
            left += (1-self.P)/2*state[row+1][column-1]
            down += (1-self.P)/2*state[row+1][column-1]
        else:
            left += (1-self.P)/2*state[row][column]
            down += (1-self.P)/2*state[row][column]

        if (row-1>=0 and column+1<self.n and [row, column+2] not in self.wall):
            right += (1-self.P)/2*state[row-1][column+1]
            up += (1-self.P)/2*state[row-1][column+1]
        else:
            right += (1-self.P)/2*state[row][column]
            up += (1-self.P)/2*state[row][column]

        if (row+1<self.n and column+1<self.n and [row+2, column+2] not in self.wall):
            right += (1-self.P)/2*state[row+1][column+1]
            down += (1-self.P)/2*state[row+1][column+1]
        else:
            right += (1-self.P)/2*state[row][column]
            down += (1-self.P)/2*state[row][column]

     #   print left, right, up, down
   #     print max(left, right, up, down)
        return self.Rp + self.gama * max(up, down, right, left)


    def finalState(self, state):
        count = 0
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                if([i, j] not in self.wall and [i, j] not in self.terminal):
                    count = max(count, abs(self.max_value(state,i-1,j-1)-state[i-1][j-1]))
       # print count
       # print self.sum(state)
        if count < self.upper:
            return False
        else:
            return True


    def check(self, i, j):
        if([i, j] not in self.wall and [i, j] not in self.terminal):
            return True
        return False



start = time.time()
agent = cashminer()
agent.fileread()
agent.renew()


# ps:time abs
