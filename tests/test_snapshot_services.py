"""Test for the AzureSnapshot class."""
from module_snapshot.services.az_snapshot_services import AzureSnapshot

class TestAzureSnapshot:
    """Test class for the AzureSnapshot class."""

    def test_list_by_subscription_id_when_subscription_id_is_valid(self, mock_snapshot_services, mock_snapshot_list_return):
        """Test the list_snapshot_by_subscription_id method of the AzureSnapshot class when the subscription ID is valid.

         Args:
             mock_snapshot_services: Mock object for snapshot services.
             mock_snapshot_list_return: Mock list of snapshots returned.

         returns:
             None
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.list_snapshot_by_subscription_id('132465789')

        assert expected == mock_snapshot_list_return

    def test_list_by_subscription_id_when_subscription_id_is_not_valid(self, mock_snapshot_services_exception):
        """Test the list_snapshot_by_subscription_id method of the AzureSnapshot class when the subscription ID is not valid.

         Args:
             mock_snapshot_services_exception: Mock object of snapshot services with exception.

         returns:
             None
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.list_snapshot_by_subscription_id('132465789')

        assert expected is None

    def test_list_by_resource_group_when_sub_id_and_rg_name_is_valid(self, mock_snapshot_services, mock_snapshot_list_return):
        """Test the list_snapshot_by_resource_group method of the AzureSnapshot class when the subscription ID and resource group name are valid.

         Args:
             mock_snapshot_services: Mock object for snapshot services.
             mock_snapshot_list_return: Mock list of snapshots returned.

         returns:
             None
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.list_snapshot_by_resource_group('132465789', 'rgtest')

        assert expected == mock_snapshot_list_return

    def test_list_by_resource_group_when_sub_id_or_rg_name_is_not_valid(self, mock_snapshot_services_exception):
        """Test the list_snapshot_by_resource_group method of the AzureSnapshot class when the subscription ID or resource group name is not valid.

         Args:
             mock_snapshot_services_exception: Mock object of snapshot services with exception.

         returns:
             None
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.list_snapshot_by_resource_group('132465789', 'rgtest')

        assert expected is None

    def test_get_snapshot_when_sub_id_and_rg_name_and_snapshot_name_is_valid(self, mock_snapshot_services, mock_snapshot_return):
        """Test the get_snapshot method of the AzureSnapshot class when the subscription ID, resource group name, and snapshot name are valid.

         Args:
             mock_snapshot_services: Mock object for snapshot services.
             mock_snapshot_return: Mock of a returned snapshot.

         returns:
             None
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.get_snapshot('132465789', 'rgtest', 'excluir1')

        assert expected == mock_snapshot_return

    def test_get_snapshot_when_sub_id_or_rg_name_or_snapshot_name_is_not_valid(self, mock_snapshot_services_exception):
        """Test the get_snapshot method of the AzureSnapshot class when the subscription ID, resource group name, or snapshot name is not valid.

         Args:
             mock_snapshot_services_exception: Mock object of snapshot services with exception.

         returns:
             None
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.get_snapshot('132465789', 'rgtest', 'excluir1')

        assert expected is None

    def test_update_tag_when_tag_exist(self, mock_snapshot_services):
        """Tests the update_snapshot_tag method of the AzureSnapshot class when the tag already exists.

         Args:
             mock_snapshot_services: Mock object for snapshot services.

         returns:
             True
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.update_snapshot_tag('132465789', 'rgtest', 'excluir1', 'Responsible - App', 'lucasraugi@gmail.com')

        assert expected is True

    def test_update_tag_when_sub_id_or_rg_name_or_snapshot_name_or_tag_not_exist(self, mock_snapshot_services_exception):
        """Tests the update_snapshot_tag method of the AzureSnapshot class when the subscription ID, resource group name, snapshot name, or tag do not exist.

         Args:
             mock_snapshot_services_exception: Mock object of snapshot services with exception.

         returns:
             False
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.update_snapshot_tag('132465789', 'rgtest', 'excluir1', 'Responsible - App', 'lucasraugi@gmail.com')

        assert expected is False

    def test_delete_snapshot_when_sub_id_and_rg_name_and_snapshot_name_is_valid(self, mock_snapshot_services):
        """Tests the delete_snapshot method of the AzureSnapshot class when the subscription ID, resource group name, and snapshot name are valid.

         Args:
             mock_snapshot_services: Mock object for snapshot services.

         returns:
             True
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.delete_snapshot('132465789', 'rgtest', 'excluir1')

        assert expected is True

    def test_delete_snapshot_when_sub_id_or_rg_name_or_snapshot_name_not_valid(self, mock_snapshot_services_exception):
        """Tests the delete_snapshot method of the AzureSnapshot class when the subscription ID, resource group name, or snapshot name are not valid.

        Args:
            mock_snapshot_services_exception: Mock object of snapshot services with exception.

        returns:
            False
        """
        snapshot_services = AzureSnapshot()
        expected = snapshot_services.delete_snapshot('132465789', 'rgtest', 'excluir1')

        assert expected is False
