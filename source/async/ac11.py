import asyncio
import signal

# 이 함수는 SIGINT 신호를 받았을 때 호출됩니다.
def signal_handler():
    print("SIGINT signal received. Shutting down.")
    loop = asyncio.get_running_loop()
    loop.stop()

async def main():
    # 이벤트 루프에 SIGINT 시그널 핸들러를 설정합니다.
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, signal_handler)

    # 여기서 장시간 실행되는 비동기 작업을 수행할 수 있습니다.
    try:
        while True:
            print("Working...")
            await asyncio.sleep(1)  # 비동기로 1초 대기
    except asyncio.CancelledError:
        # 프로그램이 종료될 때 적절한 정리 작업을 수행합니다.
        print("Cancelled error caught. Cleaning up.")

# 메인 함수를 실행합니다.
asyncio.run(main())