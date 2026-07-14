import threading
import time

print("bachelor room app")

class bachelor_room():
    def __int__(self):
        pass


    def Washing_Clothes(self):
        print("friend 1 started washing clothes")
        time.sleep(10)
        print("washing finished")
        print("friend 1 next ena kupudatha")

    def Making_Tea(self):
        print("friend 2 making tea")
        time.sleep(3)
        print("tea preapared")

br_obj=bachelor_room()
wc=threading.Thread(target=br_obj.Washing_Clothes)
mt=threading.Thread(target=br_obj.Making_Tea)

wc.start()
mt.start()

wc.join()
mt.join()


print("bachalor room work finished")


# In python threading is the one of the concept. using thread we will create task for each function.

# using thread we will be able to execute multiple funciton at the same time which is called thread. 

# if we creating mutiple thread in the same python script file which is called multithreading
 