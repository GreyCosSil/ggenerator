from pytest import fixture


def pandas_dataframe(data):
    from pandas import DataFrame

    dataframe = DataFrame(data=data)

    return dataframe


@fixture
def pandas_dataframe_with_data():
    data = [{"Column": "Value_1", "Column2": "Value_12"},
            {"Column": "Value_2", "Column2": "Value_12"},
            {"Column": "Value_3", "Column2": "Value_12"},
            {"Column": "Value_4", "Column2": "Value_12"},
            {"Column": "Value_5", "Column2": "Value_12"},
            {"Column": "Value_6", "Column2": "Value_12"}]
    return pandas_dataframe(data=data)


@fixture
def pandas_dataframe_without_data():
    return pandas_dataframe(data=[])
