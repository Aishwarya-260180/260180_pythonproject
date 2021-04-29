
print("-----Program for Student Information-----")
D = dict()

#define function to add student details
def enter_details():
    n = int(input('How many student record you want to store?? '))
  
# Add student information 
# to the dictionary
    for i in range(0,n):
        x, y = input("Enter the complete name (First and last name) of student: ").split()
        z = input("Enter contact number: ")
        m = input('Enter Marks: ')
        D[x, y] = (z, m)
    f = open('Student.txt', 'a')
    data = str(D)
    f.write('\n')
    f.write(data)
    f.close()

      
# define a function for sorting 
# based on first name
def sort():
    ls = list()
    # fetch key and value using 
    # items() method
    for sname,details in D.items(): 
        
        # store key parts as an tuple
        tup = (sname[0],sname[1]) 
          
        # add tuple to the list
        ls.append(tup)    
          
    # sort the final list of tuples
    ls = sorted(ls)    
    for i in ls:
        
        # print first name and second name
        print(i[0],i[1]) 
    return
    
# define a function for  finding the minimum marks in stored data
def minmarks():
    ls = list()
    # fetch key and value using
    # items() methods
    for sname,details in D.items(): 
        ls.append(details[1])    
    # sort the list elemnts    
    ls = sorted(ls)    
    print("Minimum marks: ", min(ls))
    return
    
# define a function for searching student contact number
def searchdetail(fname):
    ls = list()
      
    for sname,details in D.items():
        
        tup=(sname,details)
        ls.append(tup)
          
    for i in ls: 
        if i[0][0] == fname:
            print(i[1][0])
    return
 
    
#  funtion for asking the options to user From here the user can execute program
def option():
    
        choice = int(input('Enter the operation detail: \n \
        1: Enter Student Details: \n \
        2: Finding Minimum marks \n \
        3: Search contact number using first name: \n \
        4: List all details of Student File\n \
        5: Sorting using first name\n \
        6: Exit\n \
        Option: '))
      
        if choice == 1:
        # call function sort to sort the details of student
            enter_details()
            option()
        
            
        elif choice == 2:
        # call function minmarks to find minimum marks in the details of student
            minmarks()
            option()
        
          
        elif choice == 3:
        # call function searchdetail by passing first name of student 
        # whose contact number should be fetched back as output to user
            first = input('Enter first name of student: ')
            searchdetail(first)
            option()
       

        elif choice == 4:
        #open file and fetch back the details of students stored in text file
            with open('Student.txt') as f:
                 data = f.read()
            print("Data of students in textfile is\n : ", data)
            option()
        
      
        elif choice==5:
        #call sort function to sort the details of student based on marks
            sort()
            option()
          
        
        else:
            print('Thanks for executing me!!!!')
            exit()
          
option()