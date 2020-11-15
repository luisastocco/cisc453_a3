''' Windy Grid World '''

    #####################################################################################

'''1. SARSA - ON-POLICY'''
#Considers all actions associated to the state

def sarsa():
    for i in range(iterations):
        #choose a start state
        #choose a from s using policy from Q
        #for each step:
            while s != goal:
                #takeaction = move(a,s)
                #choose next action from takeaction[0] using policy from Q
                if nextstate != goal:
                    state_action = state_action + learningrate * (reward + (discount * nextstate_nextaction) - state_action)
                elif nextstate == goal:
                    state_action = state_action + learningrate * (reward + (discount * 0) - state_action)
                s = nextstate
                a = nextaction

    ######################################################################################


'''2. Q-Learning - OFF-POLICY
#Considers the maximum value associated with any of the four actions
#undiscounted grid world

def qlearn():

    return'''








import random
import numpy as np



'''Initialize Q(s,a) arbitrarily'''
def stateaction(rows,cols,actions):

    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            actions = []
            for x in range(actions):
                actions.append(0.0) #initiliaze each state-action value
            row.append(actions) 
        grid.append(row)
    return grid
    






'''Based on next state values'''
def bestmove(grid,s_row,s_col,goal,possibilities):
    
    nextstate_vals = []
    best = 0

    for action in range(len(possibilities)):
        
        val = move(action,s_row,s_col,goal)
        
        nextstate_vals.append(val[0])#position of the next state

    if len(set(nextstate_vals)) == 1: #if all values are the same
        x =  random.randint(0,len(possibilities))
        best = possibilities[x] #pick action at random
    else:
        max_ = 0
        index = 0
        for val in range(len(nextstate_vals)):
            if nextstate_vals[val] > max_:
                max_ = nextstate_vals[val]
                index = val
        best = possibilities[index]

    return best


#choose random action every 1 in 10 moves
def greedy(grid, s_row, s_col, episilon, goal):

    possible_actions  = []
    action = 0

    if s_row != 0:
        possible_actions.append(0) #north
    if s_row != 6:
        possible_actions.append(1) #south
    if s_col != 9:
        possible_actions.append(2) #east
    if s_col != 0:
        possible_actions.append(3) #west

    x = random.randint()

    if x < episilon:
        x = random.randint(0,len(possible_actions))
        action = possible_actions[x]
    else:
        action = bestaction(actions[0])


    moved = move(grid,action,s_row,s_col,goal)
    
    grid[s_row][s_col] = action[0] #next state

    return moved


        
def move(grid,action,s_row,s_col,goal):
    
    nextstate = 0
    reward = -1 #because we want the shortest path so we need to punish for moving
    done = False

    if action == 0: #north
        if s_row != 0:
            n_row = s_row - 1
            n_col = s_col
        #otherwise it stays in the same state

    if action == 1: #south
        if s_row != 6:
            n_row = s_row + 1
            n_col = s_col
        #otherwise it stays in the same state

    if action == 2: #east
        if s_col != 9:
            n_row = s_row
            n_col = s_col + 1
        #otherwise it stays in the same state
        
    if action == 3: #west
        if s_col != 0:
            n_row = s_row
            n_col = s_col - 1
        #otherwise it stays in the same state

    #calculate wind        
    if s_col == 3 | s_col == 4 | s_col == 5 | s_col == 8:
        if s_row != 0:
            n_row = n_row - 1 #move one up
            nextstate = grid[n_row][n_col]
            
    if s_col == 6 | s_col == 7:
        if s_row != 0 & s_row != 1:
            n_row = n_row - 2 #move two up
        elif s_row == 1:
            n_row = n_row - 1 #move one up

    nextstate = grid[n_row][n_col]

    if n_row == goal[0] & n_col == goal[1]:
        done = True
        reward = 1

    return [nextstate, n_row, n_row, reward, done]    


'''Initializes an 7x10 grid environment, where each row is an array
    All cells start with a state value of 0 initially'''
def makegrid(rows, cols):

    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0.0) #initiliaze each state value
        grid.append(row)
    return grid

    
def main():

    '''Initialize'''
    goal = [3,7]
    actions = [0,1,2,3] #north, south, east, west
    #episilon = ?
    episilon = 0.1 #take random actual every 1 in 10 steps
    #learningrate = ?
    learningrate = 0.5
    reward = -1 #every step is punished so we find the shortest path or 0 if it doesnt move
    discount = 1 #episodic task

    '''Choose random start state'''
    x = random.randint(0,7) #row
    y = random.randint(0,10) #col
    start = [x,y]

    iterations = 10 #change this later
    done = False #has the agent reached the goal?

    finalrewards = []
    for i in range(iterations):

        grid = makegrid(7,10) #reset
        rewards = []
        state_history = []
        nsteps = 0
        
        while done != True: #has not reached the goal yet

            nsteps += 1
            greedy = greedy()
            rewards.append(greedy[3])
            state_history.append(greedy)

            grid[greedy[1]][greedy[2]] += 1

            if greedy[4] == True: #found goal
                break


        learn(state_history, rewards, nsteps)

            ################???????????????????????????????????

        finalrewards.append(np.sum(rewards))


    #follow optimal
    grid = makegrid(7,10) #reset
    rewards = []
    state_history = []

    #while done != True:
        ##########???????????????
        
    
    #####optimal = optimize() #follow optimal policy
            
        

    

main()
