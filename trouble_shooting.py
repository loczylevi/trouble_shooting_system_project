import time

def windows_trouble_shooter():
    print("looking for problems... please wait")
    for num in range(1000000):
        time.sleep(0.5)
        print(".",end="")
    print("sorry we dont know the problem")
        
        

print(windows_trouble_shooter())
        
