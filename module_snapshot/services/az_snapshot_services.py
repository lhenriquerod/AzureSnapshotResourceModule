"""Provide services related to snapshots in Azure."""
from module_snapshot.utils.type_validation import TypeValidation
from module_snapshot.infra.azure_cloud_services import SnapshotServices
from module_snapshot.utils.exception import ExceptionError

class AzureSnapshot:
    """Class responsible for providing services related to snapshots in Azure."""

    def __init__(self):
        self.__type_validation = TypeValidation()
        self.__snapshot_services = SnapshotServices()
        self.__exception_error = ExceptionError()

    def __validate_types(self, params):
        """Validates the types of parameters passed.

         Args:
             params(list): A list of tuples containing (value, name, type) of the parameters.

         Raises:
             TypeError: If any parameter has an invalid type.
        """
        for var, name, type_var in params:
            self.__type_validation.validate_parameter_type(var, name, type_var)

    def list_snapshot_by_subscription_id(self, subscription_id:str):
        """Lists all snapshots of a specific subscription.

         Args:
             subscription_id(str): The subscription ID.

         returns:
             list: A list of SnapshotModel objects containing snapshot information.

         Raises:
             Exception: If an error occurs while listing snapshots.
        """
        self.__validate_types([(subscription_id, 'sub_id', str)])

        try:
            return self.__snapshot_services.list_by_subscription_id(subscription_id)

        except Exception as exception:
            self.__exception_error.exception_error('list_snapshot_by_subscription_id', exception)

    def list_snapshot_by_resource_group(self, subscription_id:str, resource_group_name:str):
        """Lists all snapshots of a given resource group.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.

         returns:
             list: A list of SnapshotModel objects containing snapshot information.

         Raises:
             Exception: If an error occurs while listing snapshots.
        """
        self.__validate_types([
            (subscription_id, 'subscription_id', str),
            (resource_group_name, 'resource_group_name', str)
        ])

        try:
            return self.__snapshot_services.list_by_resource_group(subscription_id, resource_group_name)

        except Exception as exception:
            self.__exception_error.exception_error('list_snapshot_by_resource_group', exception)

    def get_snapshot(self,subscription_id, resource_group_name: str, snapshot_name: str):
        """Get information for a specific snapshot.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.
             snapshot_name (str): The name of the snapshot.

         returns:
             SnapshotModel: A SnapshotModel object containing snapshot information.

         Raises:
             Exception: If an error occurs while obtaining snapshot information.
        """
        self.__validate_types([
            (subscription_id, 'subscription_id', str),
            (resource_group_name, 'resource_group_name', str),
            (snapshot_name, 'snapshot_name', str)
        ])

        try:
            return self.__snapshot_services.get(subscription_id, resource_group_name, snapshot_name)

        except Exception as exception:
            self.__exception_error.exception_error('get_snapshot', exception)

    def update_snapshot_tag(self, subscription_id: str, resource_group_name: str, snapshot_name: str, tag_key:str, new_tag_value:str):
        """Updates the value of a tag in a snapshot.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.
             snapshot_name (str): The name of the snapshot.
             tag_key (str): The key of the tag to be updated.
             new_tag_value(str): The new tag value.

         returns:
             bool: True if the update was successful, False otherwise.

         Raises:
             Exception: If an error occurs while updating the tag.
        """
        self.__validate_types([
            (subscription_id, 'subscription_id', str),
            (resource_group_name, 'resource_group_name', str),
            (snapshot_name, 'snapshot_name', str),
            (tag_key, 'tag_key', str),
            (new_tag_value, 'new_tag_value', str)
        ])

        try:
            return self.__snapshot_services.update_tag(subscription_id, resource_group_name, snapshot_name, tag_key, new_tag_value)

        except Exception as exception:
            self.__exception_error.exception_error('update_snapshot_tag', exception)
            return False

    def delete_snapshot(self,subscription_id, resource_group_name: str, snapshot_name: str):
        """Deletes a snapshot.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.
             snapshot_name (str): The name of the snapshot.

         returns:
             bool: True if deletion was successful, False otherwise.

         Raises:
             Exception: If an error occurs while deleting the snapshot.
        """
        self.__validate_types([
            (subscription_id, 'subscription_id', str),
            (resource_group_name, 'resource_group_name', str),
            (snapshot_name, 'snapshot_name', str)
        ])

        try:
            return self.__snapshot_services.delete(subscription_id, resource_group_name, snapshot_name)

        except Exception as exception:
            self.__exception_error.exception_error('delete_snapshot', exception)
            return False
