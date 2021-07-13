import time


class Phone:

    lens = 1
    battery = 1
    chip = 1
    case = 1
    screen = 1

    def __init__(self, OS, make, model, year, battery_full=100):
        self.OS = OS
        self.make = make
        self.model = model
        self.year = year
        self.battery_full = battery_full
        self.battery = battery_full
        self.is_on = True

    def __str__(self):
        return(f"\nOS:{self.OS}\nMake:{self.make}\nModel:{self.model}\nYear:{self.year}\nBattery:{self.battery}%")

    def on(self):
        while self.battery > 0:
            switch = input("\nWould you like to turn your phone on or off? ")
            if switch.lower() == "on":
                print("Your phone is on.")
                self.is_on = True
                break
            elif switch.lower() == "off":
                print("Your phone is off")
                self.is_on = False
                break
            else:
                print("Wrong answer, try again...")

    def use_battery(self):
        if self.is_on:
            self.battery -= float(input("\n{}% BATTERY. How much battery % will you use?: ".format(self.battery)))
            print('{}% battery left.'.format(self.battery))

    def applications(self):
        while self.is_on:
            while self.battery > 0:
                apps = input("\nWhich app would you like to use? (Instagram, Snapchat, YouTube): ")
                if apps.lower() == "instagram":
                    self.battery -= 5
                    print("Browsing IG like a white girl...")
                    print('{}% battery left.'.format(self.battery))
                    # add the method to make it so that there are no decimals here 
                elif apps.lower() == "snapchat":
                    self.battery -= 40
                    print("Draining battery on snap...")
                    print('{}% battery left.'.format(self.battery))
                elif apps.lower() == "youtube":
                    self.battery -= 10
                    print("In tutorial hell on YouTube...")
                    print('{}% battery left.'.format(self.battery))
            self.battery = 0
            print("\nNo battery left")
            print("Phone is now off")
            break

    def recharge(self):
        while self.is_on:
            prompt = input('\nWould you like to recharge your phone (Y/N): ')
            if prompt.lower() == "y":
                print("recharging...")
                time.sleep(5)
                self.battery = self.battery_full
                print("Have fun!")
            else:
                print("Your loss...")
                self.battery = 0


class iPhone(Phone):
    self.self


phone_one = Phone("Android", "Samsung", "A71", 2020)

name = input("What's your name?: ")
print(f'Hello {name}')
phone_one.on()
phone_one.use_battery()
phone_one.applications()
phone_one.recharge()
print(f"\n{name}, this is your phone: " + str(phone_one))


