"""This is the first file"""

class State():
    """This is my attempt at creating states"""
    def __init__(self, name, color="blank"):
        self.name = name
        self.color = color
        self.neighbors = []

    def __repr__(self):
        msg = self.name + " is " + self.color
        return msg

    def add_state(self, state):
        self.neighbors.append(state)

    def print_state(self):
        print("Name: {0} color: {1}".format(self.name, self.color))
        msg = ""
        for neigh in self.neighbors:
            msg += (neigh.name + " ") 
        print("Neighbors -> " + msg)

        # need to color the state.

    def color_state(self):
        colors = ["red", "blue", "green", "yellow"]
        pallette = []
        for i in self.neighbors:
            pallette.append(i.color) #creates a list of colors
        for color in colors:
            if color not in pallette:  # assigns a color that's not in the list
                self.color = color


#What to do if you can't find a color - recolor it
def recolor(state):
    colors = ["red", "blue", "green", "yellow"]
    existing_color = state.color
    start_index = colors.index(existing_color)
    pallette = []
    success = False
    for neighbor in state.neighbors:
        pallette.append(neighbor.color)
    for i in range(start_index+1,len(colors)-1):
        if colors[i] not in pallette:
            #set the color to the current color
            state.color = colors[i]
            success = True
            return success
    return success






        
#this is a test statement
def create_state_file(statelist):
    with open("statenames.txt", "r") as statefile:
        line = statefile.readline().strip()
        while line != "":
            statelist.append(line)
            line = statefile.readline().strip()
        statefile.close()
         
    return statelist

def clean_state_list(statelist):
    """This creates a split list from the list of strings"""
    new_split_states = []
    for state in statelist:
        new_split_states.append(state.split(", "))

    return new_split_states

def create_states(clean_list):
    """This routine takes a list of states and creates them as State objects """
    pair_dict = {}
    new_state_list = []
    for stateset in clean_list: #This takes the set of states and creates  dictionary with no neighbors
        tempstate = State(stateset[0])
        pair_dict[stateset[0]] = tempstate
#    pair_dict is now populated
#   48 states now exist
# Now, go back through the states and associate the neighbors
    print(len(pair_dict))
    for stateset in clean_list:
        m = 0
        for state in stateset:
            if m == 0:  #this is the firststate and use as reference
                first_state = pair_dict[state]
                new_state_list.append(first_state)
            else:
                neighbor_state = pair_dict[state]
                first_state.add_state(neighbor_state)
            m += 1
    return new_state_list


# Code goes here

#CA = State("California", "blue")
#NV = State("Nevada", "red")
statelist = []

create_state_file(statelist)
#for entry in statelist:
#    print(entry)
#newstates is a squeaky clean version of the statelist
    
newstates = clean_state_list(statelist)
#print(newstates)
#linkedstates is a list of 48 states with attached neighbors
linkedstates = create_states(newstates)
for link in linkedstates:
    link.color_state()
    

    link.print_state()
    if link.color == 'blank':
        print("HERE'S ONE ^^^^^^^^^^")
        for neighbor in link.neighbors:  #Code to help define what to do in this situation
            print(neighbor.name + " " + neighbor.color)

print(len(linkedstates))




