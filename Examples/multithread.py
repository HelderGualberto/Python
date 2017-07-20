import multiprocessing

def function(param1,param2):

p = multiprocessing.Process(target=function,args=(param1,param2),)
p.start()

