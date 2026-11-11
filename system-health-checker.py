import psutil
import pynvml
import datetime as dt

##Get & Store the collected data:
##- Disk Usage
disk_usage = psutil.disk_usage('C:\\')
disk_result = disk_usage.percent

##- CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
cpu_result = cpu_usage

##- Memory Usage
mem_usage = psutil.virtual_memory()
mem_result = mem_usage.percent

##- GPU Usage
device_count = 0
gpu_result = None
gpu_initialize = False

try:
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()
    total_util = 0
    gpu_initialize = True

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        total_util = util.gpu + total_util
        

    if device_count > 0:
        gpu_result = total_util / device_count
        
    else:
        gpu_result = None

except pynvml.NVMLError as error:
    print(f"NVIDIA monitoring is unavailable {error}")
    
finally:
     if gpu_initialize:
        pynvml.nvmlShutdown()

##Check each metric:
##- If usage is 99% or 100%, increase the count
##- If usage is below 99%, do not increase the count
counter = 0

if disk_result >= 99:
    counter = counter + 1

if cpu_result >= 99:
    counter = counter + 1

if mem_result >= 99:
    counter = counter + 1

if gpu_result is not None:
    if gpu_result >= 99:
        counter = counter + 1


##Save the system health result to a text file
with open ("system_health_report.txt", "w") as file:
    #Date today and generate to report
    today = dt.datetime.now()
    time_today = today.strftime("%m/%d/%Y %I:%M %p")
    file.write(f"Report Generated: {time_today} \n\n")

    file.write("System Health Status\n\n")
    file.write(f"Disk Usage: {disk_usage.percent}%\n")
    file.write(f"CPU Usage: {cpu_usage}%\n")
    file.write(f"Memory Usage: {mem_usage.percent}%\n")

    if gpu_result is None:
        file.write(f"GPU Usage: N/A\n")
        file.write(f"GPU monitoring was unavailable\n\n")
    else:
        file.write(f"GPU Usage: {gpu_result}%\n\n")

##Determine system status:
##- Count = 0 → Healthy
##- Count = 1 → Warning
##- Count = 2 → Severe
##- Count = 3 or 4 → Critical

    if counter == 0:
        file.write("System is Healthy, all resources does not exceed 99% threshold")
    elif counter == 1:
        file.write("Warning, 1 of the resources exceeds 99% treshold")
    elif counter == 2:
        file.write("Severe, 2 of the resources exceeds 99% threshold")
    elif counter >= 3 :
        file.write("Critical, 3 or more 1 of the resources exceeds 99% treshold")

##Print "Done checking" in the terminal
print("Done checking")