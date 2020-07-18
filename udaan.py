'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

class Screen:

    def __init__(self, screen_name, no_of_rows, seats_per_row, aisle_seats_per_row):

        self.screen_name = screen_name
        self.no_of_rows = no_of_rows
        self.seats_per_row = seats_per_row
        self.aisle_seats_per_row = aisle_seats_per_row
        self.reserved_seats = [] #[row,[seats]]
        for i in range(self.no_of_rows):
            
            self.reserved_seats.append([i,[]])
        #print(self.reserved_seats)


        #return True
    def reserve_seats(self,row_number,seats):

        available = True

        if row_number>self.no_of_rows or row_number<0:
            available = False 
            return False

        for i in seats:
            if i>self.seats_per_row:
                available = False
                return False

        for i in range(len(self.reserved_seats)):
            #print(self.reserved_seats[i][0])
            if row_number == self.reserved_seats[i][0]:
                for j in seats:
                    if j in self.reserved_seats[i][1]:
                        available = False
                        break
            
        if available:

            for i in range(len(self.reserved_seats)):
                if row_number == self.reserved_seats[i][0]:
                    for j in seats:
                        self.reserved_seats[i][1].append(j)

            return True
        else:
            return False
    
    def get_unreserved(self,row_number):

        for i in range(len(self.reserved_seats)):

            if self.reserved_seats[i][0] == row_number:
                
                taken_seats = self.reserved_seats[i][1]
                free_seats = []
                for i in range(1, self.seats_per_row+1):
                    if i not in taken_seats:
                        free_seats.append(i)
                return free_seats

    def suggest_contiguos(self,requirement, row_number, choice):

        for i in range(len(self.reserved_seats)):
	

            if self.reserved_seats[i][0] == row_number:

                free_seats = [] 
                
                taken_seats = self.reserved_seats[i][1]
		
                for i in range(1, self.seats_per_row+1):
                    if i not in taken_seats:
                        free_seats.append(i)
                break

        possible = True
        if choice not in free_seats:
            possible = False
            #print('choice is taken_seat')
            return False
        suggestions = []
        if possible:
            #print('possible')
            combination1 = []
            for i in range(choice,choice+requirement):
                combination1.append(i)
            combination1_success = True
            #print(combination1)
            for p in range(len(combination1)):
                if combination1[p] not in free_seats:
                    #print('one of the seats is not free here')
                    combination1_success = False
                if p == len(combination1)-1:
                    pass
                else:
                    if combination1[p] in self.aisle_seats_per_row:
                        if p!=0:
                            #print('one of the seats is an aisle seat')
                            #print(combination1[p])
                            #print(combination1)
                            #print(self.aisle_seats_per_row)
                            
                            combination1_success = False
            c2 = False
            if combination1_success:
                #print('c1 worked')
                
                p_suggestion = combination1
                #c2 = True
                return p_suggestion

            else:

                combination2 = []
                #print('c2')
                for i in range(choice,choice-requirement,-1):
                    
                    combination2.append(i)
                combination2_success = True
                #print(combination2)
                for p in range(len(combination2)):
                    if combination2[p] not in free_seats:
                        #print('one of the seats is not free here')
                        combination2_success = False
                    if p == len(combination2)-1:
                        pass
                    else:
                        if combination2[p] in self.aisle_seats_per_row:
                            if p!=0:
                                #print('one of the seats is an aisle seat')
                                #print(combination2[p])
                                #print(combination2)
                                combination2_success = False
                    
                if combination2_success:
                    suggestions = combination2
                    return suggestions
                else:
                    return False



            



        
        
                







        



t = int(input())

screens = []



for i in range(t):

    command = input().strip().split()
    
    if command[0] == 'add-screen':
        action = 'create'
        name = command[1]
        screen_exists = False
        for names in screens:
            if name == names.screen_name:
                screen_exists = True
        if not screen_exists:
            no_of_rows = int(command[2])
            seats_per_row = int(command[3])
            aisle_seats = []
            for a in range(4,len(command)):
                aisle_seats.append(int(command[a]))
            #print(tuple((name,no_of_rows,seats_per_row,aisle_seats)))
            x = Screen(name,no_of_rows,seats_per_row,aisle_seats)
            screens.append(x)
            print('success')
        else:
            print('failure')
    
    elif command[0] == 'reserve-seat':
        name = command[1]

        screen_exists = True

        for x in screens:
            if x.screen_name == name:
                break
        else:
            screen_exists = False

        if screen_exists:

            row_number = int(command[2])
            seats = [] 
            for i in range(3,len(command)):
                seats.append(int(command[i]))
            
            status = x.reserve_seats(row_number,seats)

            if status:
                print('sucess')
                #print(x.reserved_seats)
            else:
                print('failure')
        else:
            print('failure')
    
    elif command[0] == 'get-unreserved-seats':
        name = command[1]

        screen_exists = True
        
        for x in screens:
            if x.screen_name == name:
                break
        else:
            screen_exists = False

        if screen_exists:
            row_number = int(command[2])

            free_seats = x.get_unreserved(row_number)
            for i in free_seats:
                print(i, end=' ')
            print()
        else:
            print('failure')
            

    elif command[0] == 'suggest-contiguous-seats':
        name = command[1]

        for x in screens:
            if x.screen_name == name:
                break
        requirement = int(command[2])
        row_number = int(command[3])
        choice = int(command[4])

        suggestions = x.suggest_contiguos(requirement,row_number,choice)

        if not suggestions:
            print('none')
        else:
            suggestions.sort()
            for i in suggestions:
                print(i,end=' ')
            print()

        










