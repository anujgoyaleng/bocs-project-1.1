# count=1   
# while count <= 5 :
#       print("hello")
#       count += 1
      
# i=1
# while i <=5:
#     print("apna collage",i)
#     i+=1

#print number 1 to 5

# i=1
# while i<= 5:
#     print(i)
#     i+=1
    
# print("Loop ended")   

#qs1 print number from 1 to 100.
# i=100
# while i>=1: #stopping condn
#     print(i)
#     i-= 1
    
 #qs2 print number from 100 to 1.
# i=1
# while i<=100: #stopping condn
#     print(i)
#     i+= 1

#qs3 print the multiplication table of number n.
# n=3
# i=1
# while i <=10:
#     print(n*i) 
#     i+=1   

#qs4 print the element of the following list using a loop
#nums=  1,4,9,16,25,36,49,64,81,100.
# i=1
# while i <=10:
#     print(i*i)
#     i+=1
    
#second approch
# nums=[1,4,9,26,25,36,49,64,81,100]
# idx=0
# while idx < len(nums):
#     print(nums[idx]) 
#     idx+=1

#qs5 search for a number x in the tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]
# nums=(1,4,9,16,25,36,49,64,81,100,36)
# x=36

# i=0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx",i)
#     else:
#         print(("Finding..."))    
        
#     i += 1    
    
 #break & continue
# break: used to terminate the loop when encountered
# continue: terminates exicution in the current iteration & continues execution of the loop with the next iteration       

# Write Python 3 code in this online editor and run it.
n = int(input())
nums= list(map(int,input().split()))
ans=[]
for i in range (len(nums)):
    ans.append(nums[nums[i]])
print("a",*ans)