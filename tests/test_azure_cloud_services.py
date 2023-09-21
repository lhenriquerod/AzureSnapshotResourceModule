"Tests for the SnapshotServices class."
from module_snapshot.infra.azure_cloud_services import SnapshotServices

class TestSnapshotServices:
    """Test class for the SnapshotServices class."""

    def test_list_by_subscription_id(self, mock_snapshot_services, mock_snapshot_list_return):
        """Tests the list_by_subscription_id method of the SnapshotServices class.

         Args:
             mock_snapshot_services: Mock object for snapshot services.
             mock_snapshot_list_return: Mock list of snapshots returned.
        """
        snapshot_services = SnapshotServices()
        expected = snapshot_services.list_by_subscription_id('132465789')

        assert expected == mock_snapshot_list_return

    def test_list_by_resource_group(self, mock_snapshot_services, mock_snapshot_list_return):
        """Test the list_by_resource_group method of the SnapshotServices class.

         Args:
             mock_snapshot_services: Mock object for snapshot services.
             mock_snapshot_list_return: Mock list of snapshots returned.

        """
        snapshot_services = SnapshotServices()
        expected = snapshot_services.list_by_resource_group('132465789', 'rgtest')

        assert expected == mock_snapshot_list_return

    def test_get_snapshot(self, mock_snapshot_services, mock_snapshot_return):
        """Test the get_snapshot method of the SnapshotServices class.

         Args:
             mock_snapshot_services: Mock object for snapshot services.
             mock_snapshot_return: Mock of a returned snapshot.

        """
        snapshot_services = SnapshotServices()
        expected = snapshot_services.get('132465789', 'rgtest', 'excluir1')

        assert expected == mock_snapshot_return

    def test_update_tag(self, mock_snapshot_services):
        """Tests the update_tag method of the SnapshotServices class.

         Args:
             mock_snapshot_services: Mock object for snapshot services.

         returns:
             True
        """
        snapshot_services = SnapshotServices()
        expected = snapshot_services.update_tag('132465789', 'rgtest', 'excluir1', 'Responsible - App', 'lucasraugi@gmail.com')

        assert expected is True

    def test_delete_snapshot(self, mock_snapshot_services):
        """Testa o método delete_snapshot da classe SnapshotServices.

        Args:
            mock_snapshot_services: Objeto mock dos serviços de snapshot.

        Returns:
            True
        """
        snapshot_services = SnapshotServices()
        expected = snapshot_services.delete('132465789', 'rgtest', 'excluir1')

        assert expected is True
