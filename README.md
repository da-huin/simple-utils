<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./static/icon.png" alt="Project logo" ></a>
 <br>

</p>

<h3 align="center">Simple Utils</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/da-huin/aws_glove.svg)](https://github.com/jaden-git/simple-utils/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/da-huin/aws_glove.svg)](https://github.com/jaden-git/simple-utils/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 자주 사용하는 함수들을 모아두었습니다.
    <br> 
</p>

# 🦊 Usage

## 🍀 Simple File



### 🌱 *(method)* `json_to_csv`

json을 csv string으로 만듭니다.

**Parameters**

* **json_data** (*list*) --

    csv로 만들 list형식의 json 데이터 입니다.

**Returns**

* **csv string (*string*)**

**Example**
```
import simple_utils
csv_data = simple_utils.file.json_to_csv([
    {
        'hello': 'world',
        'abc':'def'
    },
    {
        'hello': 'simple',
        'abc':'ghi'
    }
])

csv_data == 'hello,abc\nworld,def\nsimple,ghi\n'
>> True
```



## 🍀 Simple Notebook



### 🌱 *(method)* `is_notebook`

현재 실행되는 곳이 주피터 노트북인지 확인합니다.

**Example**

```
import simple_utils
simple_utils.notebook.is_notebook()
```    

**Returns**

* **True | False (*bool*)**

### 🌱 *(method)* `parse_arguments`

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



## 🍀 Simple Process



### 🌱 *(method)* `retry`

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



## 🍀 Simple Random



### 🌱 *(method)* `get_uuid`

uuid를 가져옵니다.

**Example**
```
import simple_utils
simple_utils.random.get_uuid()
```
**Returns**

* **uuid.uuid4** (*string*)

### 🌱 *(method)* `make_uuid_including_time`

시간(time_ns)를 포함한 uuid를 가져옵니다.

**Example**
```
import simple_utils
simple_utils.make_uuid_including_time()
```
**Returns**

* **time_ns를 포함한 uuid** (*string*)



## 🍀 Simple Redshift



### 🌱 *(class)* `Column`

Database Column의 속성을 담고 있는 클래스입니다.

**Parameters**

* **name** (*string*) --

    컬럼명

* **column_type** (*string*) --

    컬럼 타입(BIGINT, VARCHAR(100), etc.)

* **attr** (*string*) --

    컬럼 속성(DEFAULT CURRENT_TIMESTAMP, etc.)

* **comment** (*string*) --

    코멘트

### 🌱 *(method)* `update_df_type_through_redshift_columns`

Pandas DataFrame과 Columns를 이용해 Pandas DataFrame의 타입을 업데이트합니다.

**Example**

```python
import simple_utils
from simple_utils.simple_redshift import Column

members = [
    {
        "id": 1,
        "name": "park",
        "phone": "01020203030",
        "created_at": "2020-01-01"
    },
    {
        "id": 2,
        "name": "kim",
        "phone": "01020203031",
        "created_at": "2020-01-02"
    },
    {
        "id": 3,
        "name": "han",
        "phone": "01020203032",
        "created_at": "2020-01-03"
    }]

df = pd.DataFrame(members)
columns = [Column('id', 'BIGINT'), Column('name', 'VARCHAR(100)'), Column(
    'phone', 'VARCHAR(100)'), Column('created_at', 'TIMESTAMP')]
dtypes = simple_utils.redshift.update_df_type_through_redshift_columns(df, columns).dtypes

assert dtypes['id'] == np.int64
assert dtypes['name'] == np.object
assert dtypes['phone'] == np.object
assert dtypes['created_at'] == np.object
```

**Parameters**

* **df** (*pandas.DataFrame*) --

    변환 할 padnas dataframe 입니다.

* **columns** (*list*) --

    simple_utils.redshift.Column을 포함하고 있는 list입니다.

**Returns**

* **변환된 데이터프레임** (*pandas.DataFrame*) --



## 🍀 Simple Shell



### 🌱 *(method)* `dynamic_check_output`

결과값을 모두 실행한 후 봐야하는 check_output을 개선시킨 함수입니다.

check_output이 실행되는 도중에 진행 상황을 볼 수 있습니다.

**Example**

```
import simple_utils
simple_utils.shell.dynamic_check_output('ls')
```

**Parameters**

* **[REQUIRED] command** (*string*) --

    실행시킬 명령어



## 🍀 Simple Structure



### 🌱 *(class)* `dotdict`

Dictionary를 dot으로 접근할 수 있게 해줍니다.

**Example**

```python
import simple_utils

item = simple_utils.structure.dotdict({'hello':' world'})

print(item.hello)
>> world
```

### 🌱 *(method)* `make_dict_a_hash`

dictionary를 hash를 사용해 string으로 변환해줍니다.

각 dictionary마다 유니크한 값을 만들어줍니다.

**Example**

simple_utils.structure.make_dict_a_hash({'hello': 'world', 'a': ['b', 'c']})
>> 4af49d540ed8112b9bbab8c3b38f001c9fd1451d819b682b42796919be9ad1fb

**Parameters**

* **args** (dict) --

    유니크한 값을 만들 dictionary 입니다.

### 🌱 *(method)* `set_type`

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



## 🍀 Simple Text



### 🌱 *(method)* `get_random_string`

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

### 🌱 *(method)* `set_var`

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

### 🌱 *(method)* `get_var`

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

### 🌱 *(method)* `is_unchanged_var_exists`

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

### 🌱 *(method)* `parse_at_txt`

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



## 🍀 Simple Time



### 🌱 *(method)* `get_kst`

어떤 환경에서든지 항상 한국 시간을 가져오고 싶을 때 사용할 수 있습니다.

**Example**

```
import simple_utils
print(simple_utils.time.get_kst()
```

**Returns**

* **한국시간** (*datetime.datetime*) --

### 🌱 *(method)* `get_kst_ymd`

어떤 환경에서든지 항상 한국 시간의 %Y-%m-%d을 가져오고 싶을 때 사용할 수 있습니다.

**Example**

```
import simple_utils
print(simple_utils.time.get_kst_ymd()
```

**Returns**

* **한국시간 %Y-%m-%d** (*str*) --



## 🍀 Simple Waitor



### 🌱 *(class)* `Waiter`

멀티스레드 환경에서 어떤 작업을 기다렸다가 실행해야할 때 사용합니다.

값이 들어올 때까지 무한히 기다립니다.

**Example**

```
import simple_utils

waiter = simple_utils.waitor.Waiter(items=['1','2','3','4','5'])
assert waiter.get() == '1'
waiter.put('6')
assert [waiter.get() for i in range(5)] == ['2', '3', '4', '5', '6']
```

**Parameters**

* **items** (*list*) --

    get함수를 사용했을 때 가져올 값 리스트 입니다. 값들은 Queue에 추가됩니다.

    count가 0이 아니라면 이 값은 무시됩니다.

* **count** (*int*) -- 

    items 대신 사용할 값 입니다. 
    count가 0이 아니라면 range(count)만큼 Queue에 추가됩니다.

### 🌱 *(method)* `Waiter - get`

Queue에 추가되었던 값을 가져옵니다. 값이 없다면 무한히 기다립니다.

**Parameters**

* **waiting_time** (*int*) --

매 번 가져오기를 실패했을 때 기다릴 시간

**Returns**

* **큐에 추가되었던 값** (* str | int | list | ...*) --

### 🌱 *(method)* `Waiter - put`

Queue에 값을 추가합니다.

**Parameters**

* **item** (* str | int | list | ...*) --

    이후에 get함수에서 가져올 값 입니다.




## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Title icon made by [Freepik](https://www.flaticon.com/kr/authors/freepik).

- If you have a problem. please make [issue](https://github.com/jaden-git/simple-utils/issues).

- Please help develop this project 😀

- Thanks for reading 😄