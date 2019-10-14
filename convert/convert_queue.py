import queue, threading, logging


from convert.convert_video import ffmpeg_convert_video_to_mp4

def convert_queue(args):
    logging.basicConfig(filename='convert.log',
                        format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S')
    logging.info('Convert queue is staring...')

    q = queue.Queue()
    # 用queue和threading处理处理待转码任务
    def worker():
        while True:
            item = q.get()
            if item is None:
                break
            print('Doing convert %s' % item[0])
            # time.sleep(5)
            ffmpeg_convert_video_to_mp4(item[0], item[1])
            q.task_done()
            logging.info('%s --> convert finished.' % item[0])

    convert_queue = args
    for item in convert_queue:
        q.put(item)

    threads = []
    # 启动的线程数（同时转码的数量）
    num_worker_threads = 2

    # 启动转码线程
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # block until all tasks are done
    q.join()

    # stop workers
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()
