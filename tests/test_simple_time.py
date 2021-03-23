import datetime
import simple_utils



def test_get_kst():
    print(simple_utils.time.get_kst())

def test_get_kst_ymd():
    print(simple_utils.time.get_kst_ymd())

def get_month_dt_list():
    print(simple_utils.time.get_month_dt_list(datetime.datetime(2015, 1, 1)))

# def get_kst():
#     return datetime.now(timezone('Asia/Seoul'))

# def get_kst_ymd():
#     return get_kst().strftime('%Y-%m-%d')

