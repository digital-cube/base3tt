import os
import base
from base import test
from base import app, config, registry
import importlib

current_file_folder = os.path.dirname(os.path.realpath(__file__))

random_uuid = '00000000-0000-0000-0420-000000000000'
id_user = '00000000-0000-0000-0000-000000000001'
id_session = '00000000-0000-0000-0000-000000000002'


def token2user(_):
    return {
        'id': id_session,
        'id_user': id_user,
        'permissions': 0
    }


async def reset_test_db():
    from tortoise import Tortoise
    from tortoise.backends.asyncpg import AsyncpgDBClient

    await Tortoise.close_connections()

    for cn in config.tortoise_config()['connections']:
        config.tortoise_config()['connections'][cn]['credentials']['database'] = \
            'test_' + config.tortoise_config()['connections'][cn]['credentials']['database']

    conn_name = 'conn_users'
    db_users = AsyncpgDBClient(
        connection_name=conn_name,
        **config.tortoise_config()['connections'][conn_name]['credentials']
    )

    # conn_name = 'conn_app'
    # db_app = AsyncpgDBClient(
    #     connection_name=conn_name,
    #     **config.tortoise_config()['connections'][conn_name]['credentials']
    # )

    await db_users.create_connection(with_db=False)
    await db_users.db_delete()
    await db_users.db_create()
    await db_users.close()

    # await db_app.create_connection(with_db=False)
    # await db_app.db_delete()
    # await db_app.db_create()
    # await db_app.close()

    await Tortoise.init(
        config=config.tortoise_config()
    )
    await Tortoise.generate_schemas()


class SetUpIntegrationTest(test.BaseTest):

    def setUp(self):
        config.load_from_yaml(current_file_folder + f'/config/config.yaml')
        config.conf['db']['database'] = f"test_{config.conf['db']['database']}"
        self.get_new_ioloop().run_sync(reset_test_db)
        registry.test = True

        importlib.import_module('users.api.users')
        importlib.import_module('app.api.app')

        config.init_logging()
        self.my_app = app.make_app(debug=True)

        super().setUp()
        registry.test_port = self.get_http_port()
