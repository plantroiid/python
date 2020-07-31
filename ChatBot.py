# this is a code for making a chatbot. import the "time" module to have pauses.
import time

print('hello there ! my name is Uoxo123, and i want to have a little chat with you.')
name = input('what is your name?: ')
time.sleep(3) # time for user to read full thing
print('ah,', name, ' is a very nice name.')

# talk about friends. advanced data storing.
friend1 = input('what is one of your firends names?: ')
friend2 = input('what is another one of your friends names?: ')
print('oh, i'd like to meet', friend1, 'and', friend2, ' if thats alright...')
time.sleep(3) # time for user to read the stuff before this.
choice1 = input('can i? y or n?')
if choice1 == 'y' or choice1 == 'Y':
  print('thank you !!')
elif choice1 == 'n' or choice1 == 'N':
  print('awww man. maybe another time, then...')
else:
  print('well, idk what that means, but ok.')

# custom bye-bye. 
print('well,', name, ', it was nice meeting you !!')
print('have an AMAZING DAY :D')

# ok, let's go over this...

# 1. welcome message, introduces.
# 2. the computer asks for user input, which is user's name.
# 3. use the time module, sleep, then say what a nice name it is.
# 4. ask what a friends name is (friend no. 1)
# 5. ask what a friends name is (friend no. 2)
# 6. needs user imput, asks if the computer can meet the 2 friends (friend no. 1 + friend no. 2)
# 7. responds according to answer : if yes, say thank you, if no, say maybe next time, if not Y,y,N,n then says idk what that means.
# 8. custom goodbye msg.

# i will update this later :D
