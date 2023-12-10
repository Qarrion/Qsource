import logging
import asyncio

def get_task_name():
    """ 현재 실행 중인 asyncio 태스크의 이름을 반환합니다. """
    task = asyncio.current_task()
    if task is not None:
        return task.get_name()
    return "NoTask"

class CustomFormatter(logging.Formatter):
    def format(self, record):
        """ 로그 레코드를 포맷하는 함수를 재정의합니다. """
        record.task_name = get_task_name()
        return super().format(record)

# 로깅 설정
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = CustomFormatter("%(asctime)s - %(name)s - %(levelname)s - [%(task_name)s] - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# 사용 예시
async def main():
    task1 = asyncio.create_task(some_coroutine(), name="Task1")
    task2 = asyncio.create_task(some_coroutine(), name="Task2")
    await task1
    await task2

async def some_coroutine():
    logger.info("Something happened")

asyncio.run(main())