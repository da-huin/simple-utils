import random
import uuid
import time
from . import simple_text

def get_uuid():
    """
    uuid를 가져옵니다.

    **Example**
    ```
    import simple_utils
    simple_utils.random.get_uuid()
    ```
    **Returns**

    * **uuid.uuid4** (*string*)
    """

    return str(uuid.uuid4())


def make_uuid_including_time():
    """
    시간(time_ns)를 포함한 uuid를 가져옵니다.

    **Example**
    ```
    import simple_utils
    simple_utils.random.make_uuid_including_time()
    ```
    **Returns**

    * **time_ns를 포함한 uuid** (*string*)
    """    
    return str(time.time_ns()) + "_" + simple_text.get_random_string(5)


def get_element(arr):
    """
    원소 중 하나를 랜덤으로 가져옵니다.

    **Example**
    ```
    import simple_utils
    arr = ['a','b','c']
    simple_utils.random.get_element(arr)
    ```
    **Returns**

    * **원소 중 하나**
    """        
    return arr[random.randint(0, len(arr) - 1)]
