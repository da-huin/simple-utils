import hashlib
import jsonschema
import re
import os

class dotdict(dict):
    """
    Dictionary를 dot으로 접근할 수 있게 해줍니다.

    **Example**

    ```python
    import simple_utils

    item = simple_utils.structure.dotdict({'hello':' world'})

    print(item.hello)
    >> world
    ```

    """    
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def make_dict_a_hash(*args):
    """
    dictionary를 hash를 사용해 string으로 변환해줍니다.

    각 dictionary마다 유니크한 값을 만들어줍니다.

    **Example**

    simple_utils.structure.make_dict_a_hash({'hello': 'world', 'a': ['b', 'c']})
    >> 4af49d540ed8112b9bbab8c3b38f001c9fd1451d819b682b42796919be9ad1fb

    **Parameters**

    * **args** (dict) --

        유니크한 값을 만들 dictionary 입니다.

    """
    h = hashlib.sha256()

    for piece in args:
        h.update(str(piece).encode())

    return h.hexdigest()


def set_type(type_name, value):
    """
    string type (예: 'int')를 이용해 그 타입으로 변환해줍니다.

    **Example**
    
    ```
    import simple_utils
    assert simple_utils.structure.set_type('int', '5') == 5
    assert simple_utils.structure.set_type('float', '5.1') == 5.1
    assert simple_utils.structure.set_type('string', '5') == '5'
    assert simple_utils.structure.set_type('bool', 'true') == True
    assert simple_utils.structure.set_type('bool', 'false') == False
    ```

    **Parameters**

    * **type_name** (*string*) --

        string형식의 타입 이름입니다.

    * **value** (*string | dict | int | ...*) --

        type_name을 이용해 변환할 값 입니다.

    """

    if type_name == "int":
        return int(value)
    elif type_name == "float":
        return float(value)
    elif type_name == "string":
        return str(value)
    elif type_name == "bool":
        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            raise ValueError(f"invalid bool value. value is [{value}]")
    else:
        raise ValueError("invalid set type name %s" % (type_name))



def get_validated_obj(obj, schema_item):

    schema = schema_item.get("schema", {})
    properties = schema_item.get("properties", {})

    for name in properties:
        prop = properties[name]

        for key in prop:
            if key == "default":
                default = prop[key]
                if name not in obj:
                    obj[name] = default

        for key in prop:
            value = obj[name]
            if key == "change_type":
                type_name = prop[key]
                obj[name] = set_type(type_name, value)
    try:
        jsonschema.validate(obj, schema)
    except Exception as e:
        raise ValueError(f"validate failed. {e}")

    return obj

def is_match_obj(obj: object, matcher: object):

    for fk in matcher:
        fv = matcher[fk]

        if fk not in obj:
            raise ValueError(
                "matcher key is not in obj. obj -> %s, matcher -> %s" % (str(obj), str(matcher)))

        ov = obj[fk]
        if ov != fv:
            return False

    return True
    
def get_match_objs(objs: list, matcher: object):
    result = []
    for obj in objs:
        try:
            if is_match_obj(obj, matcher):
                result.append(obj)
        except ValueError:
            continue

    return result



def find_all_by_name(start_dir, regex):
    finded_files = []
    compiled_regex = re.compile(regex)

    for root, _, files in os.walk(start_dir):
        for filename in files:
            if compiled_regex.findall(filename):
                finded_files.append(os.path.join(
                    root, filename).replace("\\", "/"))

    return finded_files

def is_obj_looking_for(obj: dict, user_obj: dict):
    o = obj.copy()
    uo = user_obj.copy()

    o.update(uo)

    if o == obj:
        return True

    return False

def is_array_looking_for(array: list, user_array: list):
    a = array.copy()
    ua = user_array.copy()

    a += ua

    if set(a) == set(array):
        return True

    return False

