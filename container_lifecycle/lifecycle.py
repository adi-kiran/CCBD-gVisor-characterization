import threading
import time
import os
import sys

def lifecycle_rate(name,run_time,container_type):
    global start_times
    global end_times
    global threadwise_lifecycle
    global count
    if container_type == "runc":
        cmd = '''docker run -it --rm ubuntu /bin/sh -c "exit"'''
    elif container_type == "runsc":
        cmd = '''docker run --runtime=runsc -it --rm ubuntu /bin/sh -c "exit"'''
    start_times.append(time.time())
    while((time.time()-min(start_times))<run_time):
        begin = time.time()
        os.system(cmd)
        end = time.time()
        count+=1
        threadwise_lifecycle[name].append([begin,end,count])
        start_times.append(begin)
        end_times.append(end)
        ctr.append(count)

if __name__ =="__main__":
    # by default we shall run 10 threads for 120s each
    threadcount = 10
    run_time = 120
    container_type = str(sys.argv[1])
    # if user provides explicit time_per_thread and threadcount, we shall use those values
    if len(sys.argv) == 4:
        run_time = int(str(sys.argv[2]))
        threadcount = int(str(sys.argv[3]))
    # display specifications to user
    print("Container Type : ",container_type)
    print("Test time per thread collection : ",run_time)
    print("No of thread collections 'n' (starting from 1 thread to n threads) : ",threadcount)
    # we approximate total time that the measurment may take
    print("Approximate Total Time : ",(threadcount*run_time)+(threadcount*10))
    # All results shall be written to results.txt
    f = open("results.txt","w")
    # begin measurements, from a single thread, to 'threadcount' number of simultaneous threads creating and deleting containers
    for i in range(threadcount):
        c = 1
        threads=[]
        start_times=[]
        end_times = []
        threadwise_lifecycle={}
        ctr = []
        count = 0
        print("**************")
        print("No of Threads : ",i+1,file=f)
        print("No of Threads : ",i+1)
        print("Approximate time : ",run_time+10," seconds")
        # create the threads
        for j in range(i+1):
            t = threading.Thread(target=lifecycle_rate, args=("Thread-"+str(c),run_time,container_type,))
            threads.append(t)
            threadwise_lifecycle["Thread-"+str(c)] = []
            c+=1
        # start the threads
        for t in threads:
            t.start()
        # wait for them to finish/terminate
        for t in threads:
            t.join()
        # print results
        x = []
        for i in threadwise_lifecycle:
            for j in threadwise_lifecycle[i]:
                x.append([j[1]-j[0], j[2], i])
        x.sort(key=lambda x : x[1])
        end_times.sort()
        print("Containers Created : ",count,"during Time Interval (end-start): ",max(end_times)-min(start_times),file=f)
        print("Containers Created : ",count,"during Time Interval (end-start): ",max(end_times)-min(start_times))
        print("Start : ",min(start_times),"End : ",max(end_times),file=f)
        print("Start : ",min(start_times),"End : ",max(end_times))
        print("Rate (containers/sec) : ",count/(max(end_times)-min(start_times)),file=f)
        print("Rate (containers/sec) : ",count/(max(end_times)-min(start_times)),"\n")
        print("Lifecycle Time (finish time - begin time) || Container No || Thread No : ",file=f)
        for i in x:
            print(i, file=f)
        print("**************")
        print("**************",file=f)
        print()
    f.close()