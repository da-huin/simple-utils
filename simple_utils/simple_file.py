import json
from io import StringIO
import csv


def json_to_csv(json_data):
    """\
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

    csv_data == 'hello,abc\\nworld,def\\nsimple,ghi\\n'
    >> True
    ```
    """
    result = ""
    if not isinstance(json_data, list):
        raise ValueError("json data's type must be list.")
    line = StringIO()
    writer = csv.writer(line)

    if len(json_data) > 0:
        csv_rows = []
        csv_rows.append(list(json_data[0].keys()))
        for row in json_data:
            csv_rows.append(row.values())
        writer.writerows(csv_rows)
        result = line.getvalue()

    return result.replace('\r', '')
