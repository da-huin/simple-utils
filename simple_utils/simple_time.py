import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta


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
    return datetime.datetime.now(timezone('Asia/Seoul'))

def get_kst_ymd():
    """
    어떤 환경에서든지 항상 한국 시간의 %Y-%m-%d을 가져오고 싶을 때 사용할 수 있습니다.

    **Example**

    ```
    import simple_utils
    print(simple_utils.time.get_kst_ymd()
    ```

    **Returns**
c
    * **한국시간 %Y-%m-%d** (*str*) --
    """    
    return get_kst().strftime('%Y-%m-%d')
    
def get_month_dt_list(start_dt, last_dt=None, format=None):
    """
    날짜 사이의 날짜들을 월로 구분하여 가져옵니다.

    **Example**

    ```
    import simple_utils
    from datetime import datetime
    print(simple_utils.time.get_month_dt_list(datetime(2015, 1))
    ```

    **Parameters**

    * **[REQUIRED] start_dt** (*datetime.datetime*) --
        
        시작할 날짜입니다.
        
    * **last_dt** (*datetime.datetime*) --
        
        *Default: None*

        종료할 날짜입니다.

    * **format** (*str*) --
        
        *Default: None*

        strftime으로 스트링으로 변환하려면 아래의 매개변수를 입력하세요.

    **Returns**

    * **datetime list** (*list*) --
    """        
    dt = datetime.datetime(start_dt.year, start_dt.month, 1)
    if not last_dt:
        now = datetime.datetime.now()
        last_dt = datetime.datetime(now.year, now.month, 1)
    else:
        last_dt = datetime.datetime(last_dt.year, last_dt.month, 1)
    

    dt_list = []
    while dt <= last_dt:
        dt_list.append(dt)
        dt += relativedelta(months=1)

    if format:
        return [dt.strftime(format) for dt in dt_list]
    
    return dt_list