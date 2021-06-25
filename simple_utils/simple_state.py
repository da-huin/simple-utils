import json
import boto3
from botocore.exceptions import ClientError

class StateManager():
    def __init__(self, default_state, bucket_name, key, region_name):
        '''
        상태값을 S3에 저장하고 불러오는 클래스입니다.

        **Parameters**

        * **default_state** (*dict*) --

            기본 상태값입니다.

        * **bucket_name** (*dict*) --

            저장할 상태값의 버킷명입니다.

        * **key** (*dict*) --

            저장할 상태값의 S3 경로입니다.

        * **region_name** (*string*) --

            리전명입니다.                    
        '''
        
        if not isinstance(default_state, dict):
            raise ValueError('"default_state" must be of type dict.')

        self._bucket_name = bucket_name
        self._key = key
        self._default_state = default_state
        self._s3_client = boto3.client('s3', region_name=region_name)
        self._state = self.load()
        
    @property
    def state(self):
        return self._state
    
    def init(self):
        self._state = self._default_state
        
    def update(self, key, value):
        self._state[key] = value
        
    def get(self, key):
        return self._state[key]

    def save(self):
        d = self._s3_client.put_object(Bucket=self._bucket_name, Key=self._key, Body=json.dumps(self._state, ensure_ascii=False))    
        return d['ResponseMetadata']['HTTPStatusCode'] == 200
    def load(self):
        try:
            return json.loads(self._s3_client.get_object(Bucket=self._bucket_name, Key=self._key)['Body'].read().decode('utf-8'))
        except ClientError as ex:
            if ex.response['Error']['Code'] == 'NoSuchKey':
                self.init()
            else:
                raise