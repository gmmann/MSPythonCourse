# # # this code won't run at all
# x = 42
# y = 206
# if x == y,
#     print('Success!!')
    


    
# this code will fail when run 
# x = 42
# y = 4
# # print(x / y)



# try: 
#     print(x / y)
# except ZeroDivisionError as e:
#     # Optionally, log e somewhere
#     print('Sorry, something went wrong')
# except:
#     print('Something really went wrong')    
# finally:
#     print('This always runs on success or failure')



# # this code won't run at all
# x = 206
# y = 42
# if x < y:
#     print(str(x) + ' is greater than ' + str(y))




# # this code WILL run .  changing the greater than/less than
# x = 206
# y = 42
# if x > y:
#     print(str(x) + ' is greater than ' + str(y))


# this code will fail when run 
x = 42
y = 0
print()
try:
    print (x /y )
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
    print()
# except SyntaxError as s:
#     print('Check YO SYNTAX!!')    
else:
    print('Something else went wrong')
    print()
finally:
    print('This is our cleanup code')
    print()


    