import numpy as np
import json
import pandas as pd
import simple_utils
from simple_utils.simple_redshift import Column


def test_update_df_type_through_redshift_columns():
    with open('assets/members.json', 'r') as fp:
        members = json.loads(fp.read())

    df = pd.DataFrame(members)
    columns = [Column('id', 'BIGINT'), Column('name', 'VARCHAR(100)'), Column(
        'phone', 'VARCHAR(100)'), Column('created_at', 'TIMESTAMP')]
    dtypes = simple_utils.redshift.update_df_type_through_redshift_columns(df, columns).dtypes

    assert dtypes['id'] == np.int64
    assert dtypes['name'] == np.object
    assert dtypes['phone'] == np.object
    assert dtypes['created_at'] == np.object
