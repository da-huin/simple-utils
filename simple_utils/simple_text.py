
import json
import re
import random


def get_random_string(length=10):
    """
    랜덤으로 스트링을 생성해줍니다.

    소스는 a-z, A-Z, 0-9 입니다.

    **Example**

    ```
    import simple_utils
    simple_utils.text.get_random_string(length=10)
    ```

    **Parameters**

    * **length** (*int*) --

        *Default: 10*

        랜덤으로 생성할 길이
    """

    random_box = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    random_box_length = len(random_box)
    result = ""
    for _ in range(length):
        result += random_box[int(random.random()*random_box_length)]

    return result

def set_var(target, dictionary: dict):
    """
    str 또는 dict 형식의 target를 dictionary 통해 값을 변환합니다.

    **Example**

    ```
    import simple_utils
    print(simple_utils.text.set_var('hello {{name}}', {'name': 'jun'}))
    >>> hello jun
    ```

    **Parameters**

    * **[REQUIRED] target** (*str | dict*) --

        변환 할 값

    * **[REQUIRED] dictionary** (*dict*) --

        target을 변환시킬 사전
    """    
    temp = ""
    if isinstance(target, dict):
        temp = json.dumps(target, ensure_ascii=False, default=str)
    elif isinstance(target, str):
        temp = target
    else:
        raise ValueError(f"invalid target type {type(target)}")

    for key in dictionary:
        value = dictionary[key]
        temp = temp.replace("{{"+key+"}}", value)

    if isinstance(target, dict):
        temp = json.loads(temp)

    return temp

def get_var(target):
    """
    target에서 {{}} 형식이 있는지 찾아서 배열로 반환합니다.

    **Example**

    ```
    import simple_utils
    print(simple_utils.text.get_var('my name is {{name}}, and {{hello}}'))
    >> ['{{name}}', '{{hello}}']
    ```

    **Parameters**

    * **[REQUIRED] target** (*str | dict*) --

        변환 할 것이 있는지 확인할 값

    **Returns**

    * **찾은 결과값 배열** (*list*) --

    """        
    temp = ""
    if isinstance(target, dict):
        temp = json.dumps(target, ensure_ascii=False, default=str)
    elif isinstance(target, str):
        temp = target
    else:
        raise ValueError(f"invalid target type {type(target)}")

    return re.findall(r"{{.+?}}", temp)

def is_unchanged_var_exists(target):
    """
    target에서 {{}} 형식이 있으면 True를 반환합니다.

    **Example**

    ```
    import simple_utils
    print(simple_utils.text.is_unchanged_var_exists('my name is {{name}}, and {{hello}}'))
    >> True
    ```

    **Parameters**

    * **[REQUIRED] target** (*str | dict*) --

        변환 할 것이 있는지 확인할 값

    **Returns**

    * **True | False** (*bool*) --
    """            
    if isinstance(target, dict):
        temp = json.dumps(target, ensure_ascii=False, default=str)
    elif isinstance(target, str):
        temp = target
    else:
        raise ValueError(f"invalid target type {type(target)}")

    return len(re.findall(r"{{.+?}}", temp)) != 0

def parse_at_txt(txt, return_type='dict'):
    """


    아래의 형식을 파싱하여 dict, list 형태로 돌려줍니다.
    @start_date=2020-01-01 @end_date=2020-02-01

    **Example**

    ```
    import simple_utils
    print(simple_utils.text.parse_at_txt('@start_date=20200101 @end_date=20200101'))
    >> {'start_date': '20200101', 'end_date': '20200101'}
    ```

    **Parameters**

    * **[REQUIRED] txt** (*str*) --
        타겟 텍스트 입니다.

    * **[REQUIRED] return_type** (*str*) --
        dict | list
        
        *Default: dict*

        중복된 키를 처리해야 하는 경우 list로 반환할 수 있습니다.

    **Returns**

    * **파싱된 결과 값** (*dict | list*) --
    """                
    data = [[e[0], '='.join(e[1:])] for e in [s.strip().split('=') for s in txt.split('@') if s]]
    if return_type == 'array':
        return data
    elif return_type == 'dict':
        return {key: value for key, value in data}
    else:
        raise ValueError(f"invalid return_type {return_type}")

