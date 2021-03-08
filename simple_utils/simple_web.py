import json
import base64


def python_vars_to_javascript(python_vars: dict, without_script_tag=False):
    """
    파이썬 변수를 자바스크립트에서 사용할 수 있게 도와줍니다.

    python_vars에 dict형식으로 변수를 넣으면 javascript 코드를 생성해줍니다.

    Flask와 같은 웹 관련 프레임워크를 사용할 때 도움이 됩니다.

    **Example**

    ```
    simple_utils.web.python_vars_to_javascript({
        'hello': 'world',
        'abc': 'def'
    }, without_script_tag=True)
    ```

    **Parameters**

    * **python_vars** (*dict*) --

        자바스크립트에서 사용할 파이썬 변수들입니다.

    * **without_script_tag** (*bool*) -- 

        <script> 태그를 함께 생성할지 여부입니다.
    """         
    script = ""
    if not without_script_tag:
        script += "<script>"
    script_piece = ""
    for var_name in python_vars:
        value = python_vars[var_name]

        value = json.dumps(value, ensure_ascii=False, default=str)
        encoded_value = base64.b64encode(value.encode("utf-8"))

        script_piece += "var %s = b64DecodeUnicode('%s');\n" % (
            var_name, encoded_value.decode())

        script_piece += "%s = JSON.parse(%s);\n" % (var_name, var_name)

    script += """
        function b64DecodeUnicode(str) {
            return decodeURIComponent(atob(str).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));
        }
    """
    script += script_piece
    if not without_script_tag:
        script += "</script>"

    return script
