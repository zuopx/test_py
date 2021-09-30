from concurrent import futures

from flags import save_flag, get_flag, show, main
from flags import BASE_URL, DEST_DIR, POP20_CC

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many1(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executer:
        res = executer.map(download_one, sorted(cc_list))
    return len(list(res))


def download_many2(cc_list):
    '''Futures inspection.'''
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


def download_many3(cc_list):
    '''Futures inspection.'''
    cc_list = cc_list[:1]
    with futures.ThreadPoolExecutor(max_workers=1) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)  # 提交了之后就开始运行
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        future_iter = futures.as_completed(to_do)
        for future in future_iter:
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == "__main__":
    main(download_many3)
