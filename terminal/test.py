import keyboard
import threading
from time import sleep


def invert_event(key_event):
    if start_event.is_set():
        start_event.clear()
    else:
        start_event.set()

def listen_F3():
    # при опущении зажатой кнопки f3 
    # меняем флаг события на противоположный
    keyboard.on_release_key(key='F3', callback=invert_event)


# объект собития, с его помощью 
# сигнализируем основной поток
# о нажатии клавиши
start_event = threading.Event()
# запускаем поток обработки нажатий
threading.Thread(target=listen_F3).run()
# ждем клавишу
start_event.wait()

while start_event.is_set():
    print('processing...')
    sleep(1)

print('script finished.')
