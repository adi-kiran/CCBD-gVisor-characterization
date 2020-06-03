## Container Lifecycle

The container lifecycle is the time spent between setting up the container and tearing it down.


The script lifecycle.py takes in 3 parameters : \[container_type] \[time_per_thread_group] \[max_threads]

The \[conainer_type] can be runc (regular docker containers) or runsc (gVisor)

The \[time_per_thread_group] tells us the time in seconds that each thread in a group must run (default = 120)

The \[max_threads] tells us the number of thread groups [groups starting from 1 thread to max_threads threads] (default = 10)

The recommended max_threads is the number of cores the machine possess.


All the results get written to a file called results.txt. Note : if results.txt already exists in folder it gets overwritten.


# Usage

python3 lifecycle.py \[container_type] \[time_per_thread_group] \[max_threads]

OR

python3 lifecycle.py \[container_type]
(This defaults to time_per_thread_group=120 and max_threads=10)

Usage Example : python3 lifecycle.py runsc 500 6
