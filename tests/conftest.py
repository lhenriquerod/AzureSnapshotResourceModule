"""Create mocks and fixtures for tests"""
import datetime
from unittest.mock import MagicMock
from pytest import fixture
from module_snapshot.entities.snapshot_model import SnapshotModel
import module_snapshot.infra.azure_cloud_services as mock_az_snapshot_services
from module_snapshot.utils.tag_exception import TagNotFoundException

@fixture(autouse=True)
def mock_env_var(monkeypatch):
    """
    Fixture that sets environment variables for Azure authentication to be used in tests.

    Args:
        monkeypatch: pytest fixture that provides a way to temporarily replace or modify
                     attributes, functions or classes.
    """
    monkeypatch.setenv("AZURE_TENANT_ID", "tenant")
    monkeypatch.setenv("AZURE_CLIENT_ID", "client")
    monkeypatch.setenv("AZURE_CLIENT_SECRET", "secret")

@fixture
def mock_snapshot_services(monkeypatch):
    """Create a mock for snapshot services.

     Args:
         monkeypatch: Object used to patch methods during tests.

     returns:
         MagicMock: Mock object of the snapshot service.
    """

    def mock_snapshot(*args):
        mock_compute_management_client = MagicMock()
        mock_compute_client_snapshots = MagicMock()
        mock_compute_management_client.snapshots = mock_compute_client_snapshots

        snapshots_list = MagicMock()
        snapshots_list.subscription_id = 'b12a52ca-48bb-46a0-870d-239dcd058d7e'
        snapshots_list.resource_group_name = 'RG-LIVE-NSG'
        snapshots_list.id = '/subscriptions/b12a52ca-48bb-46a0-870d-239dcd058d7e/resourceGroups/rgtest/providers/Microsoft.Compute/snapshots/excluir1'
        snapshots_list.name = 'excluir1'
        snapshots_list.location = 'eastus'
        snapshots_list.tags = {'Responsible - App': 'lucasraugi@gmail.com'}
        snapshots_list.type = 'Microsoft.Compute/snapshots'
        snapshots_list.time_created = datetime.datetime(2023, 6, 8, 21, 25, 28, 102399)

        def mock_list(*args, **Kwargs):
            return [snapshots_list]

        def mock_get(*args, **Kwargs):
            return snapshots_list

        def mock_update(*args, **Kwargs):
            return True

        def mock_delete(*args, **Kwargs):
            return True

        mock_compute_client_snapshots.list = mock_list
        mock_compute_client_snapshots.list_by_resource_group = mock_list
        mock_compute_client_snapshots.get = mock_get
        mock_compute_client_snapshots.begin_update = mock_update
        mock_compute_client_snapshots.begin_delete = mock_delete

        return mock_compute_management_client

    monkeypatch.setattr(mock_az_snapshot_services, "ComputeManagementClient", mock_snapshot)

@fixture
def mock_snapshot_services_exception(monkeypatch):
    """Creates a mock for the snapshot services that throws exceptions.

     Args:
         monkeypatch: Object used to patch methods during tests.

     returns:
         MagicMock: Mock object of the snapshot service.
    """

    def mock_snapshot(*args):
        mock_compute_management_client = MagicMock()
        mock_compute_client_snapshots = MagicMock()
        mock_compute_management_client.snapshots = mock_compute_client_snapshots


        def mock_list(*args, **Kwargs):
            return None

        def mock_get(*args, **Kwargs):
            return None

        def mock_update(*args, **Kwargs):
            raise TagNotFoundException('tag_test')

        def mock_delete(*args, **Kwargs):
            raise TagNotFoundException('tag_test')

        mock_compute_client_snapshots.list = mock_list
        mock_compute_client_snapshots.list_by_resource_group = mock_list
        mock_compute_client_snapshots.get = mock_get
        mock_compute_client_snapshots.begin_update = mock_update
        mock_compute_client_snapshots.begin_delete = mock_delete

        return mock_compute_management_client

    monkeypatch.setattr(mock_az_snapshot_services, "ComputeManagementClient", mock_snapshot)

@fixture
def mock_snapshot_list_return():
    """Creates a mock to return a list of snapshots.

     returns:
         list: List of SnapshotModel objects.
    """
    return [SnapshotModel(subscription_id='132465789',
               resource_group_name='rgtest',
               resource_id='/subscriptions/b12a52ca-48bb-46a0-870d-239dcd058d7e/resourceGroups/rgtest/providers/Microsoft.Compute/snapshots/excluir1',
               snapshot_name='excluir1',
               location='eastus',
               tags={'Responsible - App': 'lucasraugi@gmail.com'},
               resource_type='Microsoft.Compute/snapshots',
               created_date='2023-06-08 21:25:28')]

@fixture
def mock_snapshot_return():
    """Create a mock for returning a snapshot.

     returns:
         SnapshotModel: SnapshotModel object.
    """
    return SnapshotModel(subscription_id='132465789',
               resource_group_name='rgtest',
               resource_id='/subscriptions/b12a52ca-48bb-46a0-870d-239dcd058d7e/resourceGroups/rgtest/providers/Microsoft.Compute/snapshots/excluir1',
               snapshot_name='excluir1',
               location='eastus',
               tags={'Responsible - App': 'lucasraugi@gmail.com'},
               resource_type='Microsoft.Compute/snapshots',
               created_date='2023-06-08 21:25:28')
