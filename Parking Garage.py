import time

class parkingGarage():
    
    tickets = [x for x in range(100)]
    parkingSpaces = [x for x in range(100)]
    currentTicket =  {'paid':False}
    ticketCounter =  dict.fromkeys(range(100))

    def takeTicket(self ):
        try:
            number = self.tickets.pop()
            self.parkingSpaces.pop()
            self.ticketCounter[number] = time.time()
            print('You are ticket ' + str(number))

        except:
            print('Sorry, the garage is full.')

    def payForParking(self ):
        z = 1
        ticket_number = ''
        while z == 1 and ticket_number != 'back':
            ticket_number = input('Please provide your ticket number.')
            if ticket_number == 'back':
                z = 0
            else:
                
                try:
                    duration = time.time() - self.ticketCounter[int(ticket_number)]
                    self.ticketCounter[int(ticket_number)] = 'None'
                    cost = duration * .50
                    print('You have been parked for ' + str(round(duration, 2)) + ' seconds. That will be $' + str(round(cost, 2)))
                
                    amount = input('How much would you like to pay?')
                    dif = cost - float(amount)
                    while round(dif, 2) > 0:
                        amount = input('Cheapskate. You still owe me $' + str(round(dif, 2)) + '. Now how much would you like to pay?')
                        dif = dif - float(amount)
                    if round(dif, 2) < 0:
                        print('You have overpaid. Your generosity is appreciated.')
                
                    try:
                        amount = float(amount )
                        print('Your ticket has been paid. You have 15 minutes to leave.')
                        self.currentTicket['paid'] = True
                        z = 0
                    except:
                        print('Please enter only numbers ')
                except:
                    if z == 1:
                        print('That ticket does not seem to be in use. Please try again or type back to return to the previous menu.')
                
    def leaveGarage(self ):
        x = 1
        while x == 1:
            
            self.payForParking()
            
            if self.currentTicket['paid'] == True:
                print('Thank you, have a nice day')
                self.tickets.append(self.tickets[len(self.tickets) - 1] + 1)
                self.parkingSpaces.append(self.parkingSpaces[len(self.parkingSpaces) - 1] + 1)
                x = 0
                self.currentTicket['paid'] =  False
                
            else:
                break
y = 1
print('Hello! Thank you for parking with us. Our rate is 50 cents a second.')
garage = parkingGarage()
while y == 1:
    
    word = input('Please enter 1 for parking, 2 for leaving the garage, or 3 to quit.')
    
    if word == '1':
        garage.takeTicket()
    elif word == '2':
        garage.leaveGarage()
        
    elif word == '3':
        y = 0
    else:
        print("Sorry, I couldn't recognize your input.")
        
