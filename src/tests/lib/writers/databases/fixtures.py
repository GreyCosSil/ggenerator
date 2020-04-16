from pytest import fixture


@fixture
def mysql_specification():
    return {
        "type": "sql",
        "options": {
            "engine": "mysql",
            "method": "cli",
            "host": "",
            "port": 3306,
            "database": "",
            "schema": "",
            "username": "",
            "password": ""
        }
    }


@fixture
def postgres_specification():
    return {
        "type": "sql",
        "options": {
            "engine": "postgres",
            "method": "direct",
            "host": "",
            "port": 3306,
            "database": "",
            "schema": "",
            "username": "",
            "password": ""
        }
    }


@fixture
def sql_formatter():
    return {
        'options': {
            'table_name': 'mytable',
            "mode": "truncate",
            'batch_size': 2,
            'schema': {
                'Column': {'quoted': True}
            }
        }
    }


@fixture
def dataframe():
    dt = {[
        {
            "id": 1,
            "nome": "Heloísa Silva",
            "titulo_eleitoral": "475543834826",
            "idade": 1,
            "peso": 200.3713,
            "trabalho": "Bartender",
            "data": 1588165835
        },
        {
            "id": 2,
            "nome": "Clara Jesus",
            "titulo_eleitoral": "999946747776",
            "idade": 110,
            "peso": 225.8265369163,
            "trabalho": "Espeleologista",
            "data": 1588778349
        },
        {
            "id": 3,
            "nome": "Júlia da Rosa",
            "titulo_eleitoral": "418677955948",
            "idade": 12,
            "peso": 125.9,
            "trabalho": "Mensageiro",
            "data": 1589157184
        },
        {
            "id": 4,
            "nome": "Stephany das Neves",
            "titulo_eleitoral": "366536047757",
            "idade": 110,
            "peso": 0.79,
            "trabalho": "Psicomotricista",
            "data": 1588607518
        },
        {
            "id": 5,
            "nome": "Olivia Campos",
            "titulo_eleitoral": "841082824437",
            "idade": 102,
            "peso": 75.92,
            "trabalho": "Profissional de relações públicas",
            "data": 1588220548
        }
    ]}
    return dt
