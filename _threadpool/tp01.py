import concurrent.futures
import time
import random
import logging

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG) 
handler = logging.StreamHandler() 
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s.%(msecs)03d ::: [%(levelname)-7s] %(name)s @ %(message)s [%(threadName)s]')
handler.setFormatter(formatter)
logger.addHandler(handler)

def worker(id):
    while True:
        time.sleep(1)  # 무작위 시간 동안 대기
        if random.random() < 0.1:  # 10% 확률로 예외 발생
            logger.info('do error')
            raise Exception(f"Worker {id}: 오류 발생!")
        else:
            logger.info('do work')


with concurrent.futures.ThreadPoolExecutor(max_workers=3, thread_name_prefix='worker') as executor:
    futures = [executor.submit(worker, i) for i in range(3)]
    # 오류를 출력하는 부분
    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()  # 결과를 얻거나 예외를 발생시킵니다.
        except Exception as e:
            print(e)  # 오류 출력

# 2023-12-03 09:25:55,149.149 ::: [INFO   ] test @ do work [worker_0]
# 2023-12-03 09:25:55,150.150 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:25:55,150.150 ::: [INFO   ] test @ do work [worker_1]
# 2023-12-03 09:25:56,150.150 ::: [INFO   ] test @ do work [worker_0]
# 2023-12-03 09:25:56,150.150 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:25:56,150.150 ::: [INFO   ] test @ do error [worker_1]
# 2023-12-03 09:25:57,150.150 ::: [INFO   ] test @ do work [worker_0]
# 2023-12-03 09:25:57,151.151 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:25:58,151.151 ::: [INFO   ] test @ do error [worker_0]
# 2023-12-03 09:25:58,151.151 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:25:59,152.152 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:26:00,152.152 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:26:01,153.153 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:26:02,153.153 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:26:03,154.154 ::: [INFO   ] test @ do work [worker_2]
# 2023-12-03 09:26:04,154.154 ::: [INFO   ] test @ do error [worker_2]