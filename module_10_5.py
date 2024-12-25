# "Многопроцессное программирование"
import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(file.readline())
            line = file.readline()
    print(name, "readed")


filenames = [f'file {number}.txt' for number in range(1, 5)]

#Linear
#start = time.time()
#list(map(read_info, filenames))
#end = time.time()
#print(round(end - start, 4),  "- линейный")

#Multithreading

if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(processes= 4) as pool:
        result = pool.map(read_info, filenames)
    end = time.time()
    print(round(end - start, 4),  "- многопроцессный")