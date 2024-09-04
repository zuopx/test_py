""""""
from pysyncobj import SyncObj
from pysyncobj.batteries import ReplCounter, ReplDict

counter1 = ReplCounter()
counter2 = ReplCounter()
dict1 = ReplDict()
syncObj = SyncObj('127.0.0.1:0', [], consumers=[counter1, counter2, dict1])

counter1.set(42, sync=True)  # set initial value to 42, 'sync' means that operation is blocking
counter1.add(10, sync=True)  # add 10 to counter value
counter2.inc(sync=True)  # increment counter value by one
dict1.set('testKey1', 'testValue1', sync=True)
dict1['testKey2'] = 'testValue2'  # this is basically the same as previous, but asynchronous (non-blocking)

print(counter1.get(), counter2.get(), dict1['testKey1'], dict1.get('testKey2')) # 52 1 testValue1 None
