import sys
import psutil
from collections import namedtuple









if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "cpu":
            namedtupl = str(psutil.cpu_times_percent(interval=1, percpu=False))
            words_list = (namedtupl[namedtupl.find('(')+1:namedtupl.find(')')]).split(',')
            for i in words_list:
                print(i)
             

            
        elif sys.argv[1] == "mem":
            namedtupl = str(psutil.virtual_memory())
            words_list = (namedtupl[namedtupl.find('(')+1:namedtupl.find(')')]).split(',')
            print('Virtual memory:')
            for i in words_list:
                print(i)

            
            namedtupl = str(psutil.swap_memory())
            words_list = (namedtupl[namedtupl.find('(')+1:namedtupl.find(')')]).split(',')
            print('---------------')
            print('Swap memory:')    
            for i in words_list:
                print(i)
           
           

        else:
            print("Please, enter corect parametr: mem or cpu ")
    else:
        print("Please, enter parametr")