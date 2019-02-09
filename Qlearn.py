import numpy as np 
import random
from time import sleep

ground = ["0","=","=","=","=","=","=","=","=","9"]
table = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
def display(new_x):
    ground2 = ["0","=","=","=","=","=","=","=","=","9"]
    p_x = new_x
    if p_x > 8 :
            return 0
    ground2[p_x] = "1"
    for x in ground2:
        print(x,end =' ')
    ground2[p_x] = "="

def update_qtable(c_x,action,r,new_x):
        if(action == 0) :
                table[c_x][0] += r
        else:
                table[c_x][1] += r

def prob_action(current_x):
        if( table[current_x][0] > table[current_x][1]  ) :
               return 0
        else:
                return 1

def rand_action():
        action = random.randint(0,2)      
        return action

def reward(c_x,action):
        x = c_x
        a = action
        f = 1
        if(action == 0):
                x -=1
        else :
                x +=1     
        if x < 0  :
                f = 0
                r = -1
        elif x > len(ground)-1:
                f = 0
                r = -1
        elif(ground[x] == '0' ) :
                f = 0
                r = -1
        elif(ground[x] == '9' ) :
                r = 1
        else :
                r = 0.25
        return r,x,f

def random_move(current_x):
        c_x = current_x
        action = rand_action()#
        r,new_x ,flag= reward(c_x,action)#
        update_qtable(c_x,action,r,new_x)#
        #display(new_x)
        print()
        return new_x,flag

def prob_move(current_x):
        c_x = current_x
        action = prob_action(c_x)
        r,new_x ,flag= reward(c_x,action)
        update_qtable(c_x,action,r,new_x)
        #display(new_x)
        print()
        return new_x,flag

def main():
        limit = 500
        for x in range(0,limit):   
               # sleep(0.15)    
                current_x = 2
                new_x = 0
                flag = 1  #alive
                c = 0
                while(True):
                      #  sleep(0.25)                       
                        thresh = random.random()
                        if thresh > 0.45:
                                new_x ,flag= random_move(current_x)
                                if flag == 0:
                                        break     
                                display(new_x)                               
                                current_x = new_x
                        else :
                                new_x,flag = prob_move(current_x)
                                if flag == 0:
                                        break
                                display(new_x)
                                current_x = new_x
                print("Age :",end = " ")
                print(x)
#    for x in table:
   #            print(x)
      #    current_x = 2
#          new_x = 0
 #         for x in range(0,6):       
                
  #                flag = 1  #alive
     #             c = 0

    
                      #  sleep(0.25)
        #          new_x,flag = prob_move(current_x)
           #       if flag == 0:
              #            break
               #   display(new_x)
                #  current_x = new_x
                #  print("Age :",end = " ")
                #  print(x)
        
main()
