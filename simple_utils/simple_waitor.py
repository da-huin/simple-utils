import time
import queue

class Waiter():
    """
    멀티스레드 환경에서 어떤 작업을 기다렸다가 실행해야할 때 사용합니다.

    값이 들어올 때까지 무한히 기다립니다.

    **Example**

    ```
    import simple_utils

    waiter = simple_utils.waitor.Waiter(items=['1','2','3','4','5'])
    assert waiter.get() == '1'
    waiter.put('6')
    assert [waiter.get() for i in range(5)] == ['2', '3', '4', '5', '6']
    ```

    **Parameters**

    * **items** (*list*) --
    
        get함수를 사용했을 때 가져올 값 리스트 입니다. 값들은 Queue에 추가됩니다.

        count가 0이 아니라면 이 값은 무시됩니다.

    * **count** (*int*) -- 

        items 대신 사용할 값 입니다. 
        count가 0이 아니라면 range(count)만큼 Queue에 추가됩니다.

    """     
    def __init__(self, items=[], count=0):
        if count == 0 and len(items) == 0:
            raise ValueError("items or count must be filled.")

        self.q = queue.Queue()

        if count == 0:
            for item in items:
                self.q.put(item)
        else:
            for index in range(count):
                self.q.put(index)

    def get(self, wating_time=1):
        """
        Queue에 추가되었던 값을 가져옵니다. 값이 없다면 무한히 기다립니다.

        **Parameters**

        * **waiting_time** (*int*) --
        
        매 번 가져오기를 실패했을 때 기다릴 시간

        **Returns**
        
        * **큐에 추가되었던 값** (* str | int | list | ...*) --

        """
        item = None
        while True:
            try:
                item = self.q.get(block=False)
            except:
                time.sleep(wating_time)
            else:
                return item

    def put(self, item=""):
        """
        Queue에 값을 추가합니다.

        **Parameters**

        * **item** (* str | int | list | ...*) --

            이후에 get함수에서 가져올 값 입니다.
        """

        
        self.q.put(item)
