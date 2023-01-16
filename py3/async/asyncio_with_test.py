"""异步上下文管理器

上下文管理协议
-   __enter__()
-   __exit__(exc_type, exc_val, exc_tb)

--------------------------------------------------------------------------------
with EXPR as VAR:
    BLOCK

等价：

mgr = (EXPR)
exit = type(mgr).__exit__  # 并没有调用
value = type(mgr).__enter__(mgr)
exc = True
try:
    try:
        VAR = value  # 如果有"as VAR"
        BLOCK
    except:
        # 这里会处理异常
        exc = False
        if not exit(mgr, *sys.exc_info()):
            raise
        # 如果__exit__返回值是false，异常将被传播；如果返回值是真，异常将被终止
finally:
    if exc:
        exit(mgr, None, None, None)

-------------------------------------------------------------------------------
@contextlib.contextmanager将生成器转化为上下文管理器，示例：

@contextlib.contextmanager
def createContextManager(name):
    print '__enter__ %s' %  name
    yield name
    print '__exit__ %s' % name

with createContextManager('foo') as value:
    print value

#输出
__enter__ foo
foo
__exit__ foo
"""


def main():
    print("hello, world")


if __name__ == "__main__":
    main()
