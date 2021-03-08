import simple_utils


def test_dotdict():
    dd = simple_utils.structure.dotdict({
        'a': 'b',
        'c': 'd'
    })
    assert dd.a == 'b'
    assert dd.c == 'd'


def test_make_dict_a_hash():
    assert simple_utils.structure.make_dict_a_hash({'hello': 'world', 'a': [
                                                   'b', 'c']}) == '4af49d540ed8112b9bbab8c3b38f001c9fd1451d819b682b42796919be9ad1fb'


def test_set_type():
    assert simple_utils.structure.set_type('int', '5') == 5
    assert simple_utils.structure.set_type('float', '5.1') == 5.1
    assert simple_utils.structure.set_type('string', '5') == '5'
    assert simple_utils.structure.set_type('bool', 'true') == True
    assert simple_utils.structure.set_type('bool', 'false') == False


def test_get_validated_obj():
    schema_item = {
        "schema": {
            "properties": {
                "IMAGEPOOL_DB_USER": {
                    "type": "string"
                },
                "IMAGEPOOL_DB_PORT": {},
            },
            "required": [
                "IMAGEPOOL_DB_USER",
            ]
        },
        "properties": {
            "IMAGEPOOL_DB_PORT": {
                "default": 3306,
                "change_type": "int"
            }
        }
    }

    assert simple_utils.structure.get_validated_obj({
        'IMAGEPOOL_DB_USER': 'hello'
    }, schema_item) == {'IMAGEPOOL_DB_USER': 'hello', 'IMAGEPOOL_DB_PORT': 3306}

    try:
        simple_utils.structure.get_validated_obj({}, schema_item)
    except ValueError as e:
        assert str(e).find("IMAGEPOOL_DB_USER' is a required property") != -1


def test_is_match_obj():
    obj = {
        'hello': 'world',
        'yellow': 'monkey'
    }
    assert simple_utils.structure.is_match_obj(obj, matcher={
        'hello': '?'
    }) == False
    assert simple_utils.structure.is_match_obj(obj, matcher = {
        'hello': 'world'
    }) == True

def test_get_match_objs():
    objs=[{
        'hello': 'world',
        'yellow': 'moneky'
    }, {
        'hello': 'world',
        'color': 'black'
    },
     {
        'hello': '?',
        'color': 'black'
    }]

    assert simple_utils.structure.get_match_objs(objs, matcher={
        'hello': 'world'
    }) == objs[:2]

    
    assert simple_utils.structure.get_match_objs(objs, matcher={
        'color': 'red'
    }) == []

def test_find_all_by_name():
    assert 'assets/message.txt' in simple_utils.structure.find_all_by_name('assets', r'.+\.txt')

def test_is_obj_looking_for():
    obj = {
        'hello': 'world',
        'yellow': 'world'
    }
    assert simple_utils.structure.is_obj_looking_for(obj, user_obj= {'hello': 'world'}) == True
    assert simple_utils.structure.is_obj_looking_for(obj, user_obj= {'hello': '?'}) == False

def test_is_array_looking_for():
    array = ['hello', 'world']
    assert simple_utils.structure.is_array_looking_for(array, user_array=['world']) == True
    assert simple_utils.structure.is_array_looking_for(array, user_array=['oh']) == False

