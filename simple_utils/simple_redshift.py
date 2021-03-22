class Column():
    """
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
    """
    def __init__(self, name, column_type, attr="", comment=""):
        self.name = name
        self.column_type = column_type
        self.attr = attr
        self.comment = comment


def update_df_type_through_redshift_columns(df, columns):
    """
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
    """

    wdf = df.copy()
    case_insensitive_check = lambda x, word: word.lower() in [s.lower() for s in x]
    for column in columns:
        if case_insensitive_check(["BIGINT", "INT", "SMALLINT"], column.column_type):
            wdf[column.name] = wdf[column.name].astype(int)
        elif case_insensitive_check(["FLOAT"], column.column_type):
            wdf[column.name] = wdf[column.name].astype(float)
        elif column.column_type.upper().startswith("VARCHAR"):
            wdf[column.name] = wdf[column.name].astype(str)
        elif case_insensitive_check(["BOOLEAN"], column.column_type):
            wdf[column.name] = wdf[column.name].astype(bool)            
        elif column.column_type in ["DATE", "TIMESTAMP"]:
            pass
        else:
            raise ValueError(f"Unknown type {column.column_type}")

    return wdf
