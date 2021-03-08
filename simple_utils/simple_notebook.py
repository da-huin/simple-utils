from . import simple_structure
import argparse

def is_notebook():
    """
    현재 실행되는 곳이 주피터 노트북인지 확인합니다.

    **Example**

    ```
    import simple_utils
    simple_utils.notebook.is_notebook()
    ```    

    **Returns**

    * **True | False (*bool*)**


    """
    try:
        get_ipython()
        return True
    except NameError:
        return False

def parse_arguments(param={}, description=""):
    """
    .ipynb 파일을 .py으로 변환하여 동작시키려고 하고, .py에서는 유저 입력값(sys.argv)를 받아야 할 때 사용할 수 있습니다.

    아래의 예제를 .py파일로 변환시킨다면 python3 {filename}.py --kind="history" --include_table="order" 와 같은 방식으로 사용할 수 있습니다.

    그리고 주피터에서는 default값으로 사용할 수 있습니다.

    **Example**

    ```
    import simple_utils
    argv = simple_utils.structure.dotdict({})

    argv.kind = {
        'default': 'redshift',
        'required': False
    }

    argv.target_date = {
        'default': '',
        'required': False
    }

    argv.include_table = 'ABC'

    argv = simple_utils.notebook.parse_arguments(argv)    


    print(argv.kind)
    >> redshift
    ```

    **Parameters**

    * **param** (*simple_utils.structure.dotdict*) --
        
        param의 어떤 값이 dict 형식이라면, ArgumentParser.add_argument함수에 --{name}, **{value} 옵션으로 추가됩니다.

        param의 어떤 값이 string 형식이라면 required: True로 추가되고 기본값은 {value} 이 됩니다.

    * **description** (*string*) --

        전체적인 설명 입니다.

    """    
    namespace = {}

    default_args = {
        "help": "",
        "required": True
    }
    
    for name, user_args in param.items():
        if not isinstance(user_args, dict):
            param[name] = {
                "default":user_args
            }

    if not is_notebook():
        parser = argparse.ArgumentParser(description=description)

        for name, user_args in param.items():
            args = default_args.copy()
            args.update(user_args)
            print(args)

            parser.add_argument(f"--{name}", **args)

        namespace = parser.parse_args()

    else:
        for name, user_args in param.items():
            namespace[name] = user_args["default"]
            
        namespace = simple_structure.dotdict(namespace)

    return namespace
