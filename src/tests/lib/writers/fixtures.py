from pytest import fixture


def pandas_dataframe(data):
    from pandas import DataFrame

    dataframe = DataFrame(data=data)

    return dataframe


@fixture
def pandas_dataframe_with_data():
    data = [{"Column1": "Value_1", "Column2": "Value_12"},
            {"Column1": "Value_2", "Column2": "Value_12"},
            {"Column1": "Value_3", "Column2": "Value_12"},
            {"Column1": "Value_4", "Column2": "Value_12"},
            {"Column1": "Value_5", "Column2": "Value_12"},
            {"Column1": "Value_6", "Column2": "Value_12"}]
    return pandas_dataframe(data=data)


@fixture
def pandas_dataframe_without_data():
    return pandas_dataframe(data=[])


@fixture
def specification():
    from os.path import abspath
    from uuid import uuid4

    absolute_path = abspath(".")
    file_name = uuid4()

    return {'uri': f"{absolute_path}/{file_name}"}


@fixture
def sql_specification_format():
    def _spec(table_name, index=False, index_label=None):
        return {
            'options': {
                'table_name': table_name,
                'batch_size': 2,
                'schema': {
                    'Column1': {
                        'quoted': True
                    }
                },
                'mode': 'replace',
                'index': index,
                'index_label': index_label
            }
        }
    return _spec


@fixture
def sql_specification_writer():
    return {
        'options': {
            'engine': 'mysql',
            'method': 'direct',
            'host': 'dbhost',
            'port': 3306,
            'database': 'mydb',
            'username': 'root'
        }
    }
