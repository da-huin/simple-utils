import subprocess

def dynamic_check_output(command):
    """
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
    """

    result = ""
    print(command)
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE)

    for b_line in iter(process.stdout.readline, b''):
        try:
            line = b_line.decode("cp949")
        except:
            try:
                line = b_line.decode("utf-8")
            except:
                pass

        print(line, end="")
        result += line

    return result