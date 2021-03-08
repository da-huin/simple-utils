
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

