from datetime import datetime
from pytz import timezone


def get_kst():
    """
    어떤 환경에서든지 항상 한국 시간을 가져오고 싶을 때 사용할 수 있습니다.

    **Example**

    ```
    import simple_utils
    print(simple_utils.time.get_kst()
    ```

    **Returns**

    * **한국시간** (*datetime.datetime*) --
    """
    return datetime.now(timezone('Asia/Seoul'))

def get_kst_ymd():
    """
    어떤 환경에서든지 항상 한국 시간의 %Y-%m-%d을 가져오고 싶을 때 사용할 수 있습니다.

    **Example**

    ```
    import simple_utils
    print(simple_utils.time.get_kst_ymd()
    ```

    **Returns**

    * **한국시간 %Y-%m-%d** (*str*) --
    """    
    return get_kst().strftime('%Y-%m-%d')

