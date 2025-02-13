import pytest

from shade import Shade

# ToDo - do something better w this once we add it to GH actions
API_KEY = 'sk_965a8a31cbf49c8ecc842082d40d5fa8cc529aa78a217788536cbeff5cf56ab3'
REMOTE_URL = 'http://127.0.0.1:9082'
TEST_DOMAIN = 'testshadeinc'


@pytest.fixture
def shade():
    return Shade(remote_url=REMOTE_URL, api_key=API_KEY)


# @pytest.fixture
# def test_workspace(shade: Shade):
#     workspace_data = {
#         'name': "Clarkson's Farm",
#         'description': 'Clarkson and his team are back on the farm',
#         'thumbnail': 'manymanybytez',
#         'domain': 'testshadeinc',
#     }
#     try:
#         test_workspace = shade.workspace.get_workspace_by_domain(
#             workspace_data.get('domain')
#         )
#     except ValueError as e:
#         if 'No workspace with domain' in e.args[0]:
#             test_workspace = shade.workspace.create_workspace(**workspace_data)
#         else:
#             raise e
#
#     return test_workspace
#
#


@pytest.fixture
def test_workspace(shade: Shade):
    workspace_data = {
        'name': "Clarkson's Farm",
        'description': 'Clarkson and his team are back on the farm',
        'thumbnail': 'manymanybytez',
        'domain': TEST_DOMAIN,
    }
    test_workspace = None

    try:
        test_workspace = shade.workspace.get_workspace_by_domain(
            workspace_data.get('domain')
        )

    except Exception as e:
        if 'No workspace with domain' in e.args[0]:
            # All good, workspace doesn't exist
            pass
        else:
            # some other error, raise
            raise e

    if test_workspace is not None:
        shade.workspace.delete_workspace(test_workspace.get('id'))

    test_workspace = shade.workspace.create_workspace(**workspace_data)

    return test_workspace


@pytest.fixture
def test_drive(test_workspace: dict, shade: Shade):
    # drive_identifier = 'sdk-drive'

    drive = shade.drive.create_drive(
        test_workspace.get('id'), name='TestDrive', description='description'
    )

    shade.workspace.init_workspace_for_tests(TEST_DOMAIN, drive.get('identifier'))

    return drive
