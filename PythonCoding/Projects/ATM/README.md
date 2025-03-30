# Elad Uzan

# ATM  application.
# The files are all implemting the basic ATM application as requested in the below exercise. 
# 
# The files are numbered by there iteration number. in each try I have added anouther fix or addition. 
# Some of the files names tailtail about the addition. 
# At the end of most of the .py files there is a comments describing the changes made. 

# THE WAY THE PROGRAM WORKS:
#
#

0. Save several customers in the system 3 like (user1, user2, user3)
with different pin codes and different names and
balances for example ('Avi Cohen', 1234 , 1000), ('Yossi Cohen', 6543 , 500) , ('Yuri Levi', 5852, 800) .

1. Asks the user to input his/her name or (which will have a first name and a last name on it);

2. GREETS THE USER "Welcome to Avi Cohen"

3. Asks the user for her/his pin code (pincode are 4 digits,
need to check if it is correct )

4. Also need to check if it was the users correct pincode

5. IF everything went ok, the user gets a new greeting with the
following options:
"ATM MENU:"
"Press button d to Deposit Money"
"Press button w to Withdraw Money"
"Press button c to Check your Balance";
"Press button q to Quit";

Bonus option: "Press button p to change PIN_CODE"
Bonus option: "Press button R to create RECIPE"
explained in the 11 section.

6. If the user pressed "d" the following menu will appear:
"How much would you like to Deposit?"
it will get the amount from the user and add it to the Balance.
**need to check if the amount is a multiplier of 20 50
or 100 (Because 20 is the lowest bill you can use in ISRAEL)
** for example I cannot deposit 352 because - 300 is fine + 50 is fine
but 2 - can't;
Will print out "OK" or some other conformation and
Then it will get the user back to the "ATM MENU" screen.


7. If the user pressed "w" following menu will appear:
"How much would you like to Withdraw?"
"1 - 50 , 2 - 100 , 3 - 150, 4 - 300, 5 - other "
If pressed "1" 50 will be subtracted from the current Balance amount
same with "2","3" and "4";

But if pressed "5" will be prompt to give own amount and that
amount will be subtracted from the current Balance amount.
 ** Balance cannot go to minus , need to check the subtracted is
 possible (if you have enough money)
 ** If not need to say "sorry, operation could not happen,
 you don't have enough Balance for this operation"
If everything was alright print out "OK" or some other confirmation and
Then it will get the user back to the "ATM MENU" screen.


8. If the user pressed "c" it will show his/hers balance
for example "Your current Balance is 950 NIS".
Then it will get the user back to the "ATM MENU" screen.

9. If the user pressed "q" it will print out "GOODBYE AVI, HAVE A NICE DAY"

10. The project has to use loops, lists, function

11. Bonus Points - Challenge:
    1."Implementing p option to change the pin_code of the Customer to use in the next login to the ATM (need to #     check if it actually works, try to login with it)"
    2."Implementing R option to print the data of the customer
    such as Name and LastName and the current balance of this/hers account "
    Example: """
       Hello Avi Cohen,
      At this moment DATE: 01/03/23 10:00:00 you got 1000 NIS in you account
       Thank you for using your ATM
          """
