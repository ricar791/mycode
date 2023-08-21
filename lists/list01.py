#!/usr/bin/env python3

'''Alta3 Research | RZFeeser
   Lists are created with square brackets, [], and organize data into an ordered series.
   Each item in the series is given an index position starting at 0. Data will remain in that position until an instruction to (re)move it.

   L[0] - returns the first item in the list
   L[-1] - returns the last item in the list

   L.append(item) - adds an item to the end of the list'''
def main():
       '''exploring lists with networking data'''

       interface = ["192.168.0.5", 5060, "UP"] # create a list called "interface"

       # the print(), or "print function", displays whatever it is passed to standard out
       # first item in the list is in position 0
       print("The first item in the list (IP):", interface[0])

       print("The second item int the list (port):", interface[1])

       print("The last item in the list (state):", interface[2])

       # add an item to the end of the list
       interface.append("SIP telephone server")

       print("A new item has been added to the list:",interface[3])

       print("The last indexed item is always found at -1:", interface[-1])

if __name__ == "__main__":
       main()     #calls the "main" function to run

