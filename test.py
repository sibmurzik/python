import datetime
import multiprocessing as mt


from PIL import Image
from queue import Empty

def change_size (image_paths, pipe: mt.Pipe, stopEvent: mt.Event):
    for imaage_path in image_paths:
        image = Image.open(imaage_path)
        image = image.resize((200, 300))
        image.save(imaage_path)
        pipe.send(imaage_path)
        stopEvent.set()





def change_color(pipe: mt.Pipe, stopEvent):
    while not stopEvent.is_set():
        image_path = pipe.recv()
        image = Image.open(image_path)
        image = image.convert('L')
        image.save(image_path)

if __name__ == '__main__':
    data = []
    conn1, conn2 = mt.Pipe()
    stopEvent = mt.Event()
    for image in range(1, 160):
        data.append(f'./web/images/img_{image}.JPG')
    print(data)

    resize_process = mt.Process(target= change_size, args=(data, conn1, stopEvent))
    color_process = mt.Process(target=change_color, args=(conn2, stopEvent))
    start = datetime.datetime.now()
    resize_process.start()
    color_process.start()

    resize_process.join()
    color_process.join()
    stop = datetime.datetime.now()
    print (stop - start)
