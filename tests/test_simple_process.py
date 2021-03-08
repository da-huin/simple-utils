import simple_utils

def test_retry():
    # 성공한 경우
    assert simple_utils.process.retry(lambda x: x+1, argv={'x':2}) == 3 
    # 실패한 경우

    try:
        simple_utils.process.retry(lambda x: x+y, argv={'x':5}, waiting_time=1, limit=1)
    except simple_utils.process.TimeoutError:
        pass
    else:
        raise Exception('process - retry 테스트 실패')

