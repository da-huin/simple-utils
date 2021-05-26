def list_chunk(target, n):
    """
    리스트를 n개로 분할해줍니다.

    **Example**

    simple_utils.array.list_chunk(your_list, 5)

    **Parameters**

    * **target** (list) --

        분할할 타겟입니다.

    * **n** (int) --

        몇 개씩 분할할지 정합니다.

    """    
    return [target[i:i+n] for i in range(0, len(target), n)]
