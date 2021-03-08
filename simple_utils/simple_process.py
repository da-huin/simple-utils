import time

class TimeoutError(Exception):
    pass

def retry(proc, argv={}, waiting_time=3, limit=100):
    """
    retry를 해야하는 부분을 직접 작성하지 않고 사용할 수 있도록 도와줍니다.
    
    실패시마다 매개변수 waiting_time 만큼 기다리고, 매개변수 limit만큼 재시도합니다. 

    waiting_time이 3이고 limit가 100이라면 300초가 소요됩니다.

    **Parameters**

    * **[REQUIRED] proc** (*function*) --
    
        실행할 함수입니다.

    * **argv** (dict) --
    
        *Default: {}*

        proc에 매개변수로 넣을 값 입니다.

        ```python
        # 만약 argv가 다음과 같다면...
        {
            'hello': 'world',
            'yellow': 'monkey'
        }

        # 함수는 다음과 같이 만들어질 수 있습니다.
        def proc(hello, yellow):
            pass
        ```

    * **waiting_time** (int) --
    
        *Default: 3*

        한 번 실패시 기다릴 시간 입니다.
    
    * **limit** (int) --
    
        *Default: 100*

        실패 시 재시도할 횟수 입니다.    
    

    **Example**
    ```
    import simple_utils
    simple_utils.notebook.is_notebook()
    ```    

    **Returns**

    * **True | False (*bool*)**


    """    
    result = None
    success = False
    for _ in range(limit):
        try:
            result = proc(**argv)
        except:
            time.sleep(waiting_time)
        else:
            success = True
            break

    if not success:
        raise TimeoutError()

    return result
