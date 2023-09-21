"""Provide services related to snapshots"""
from azure.mgmt.compute import ComputeManagementClient
from module_snapshot.infra.authenticate import AzureAuthenticate
from module_snapshot.entities.snapshot_model import SnapshotModel
from module_snapshot.utils.tag_exception import TagNotFoundException


class SnapshotServices:
    """Class responsible for providing services related to snapshots."""

    def __init__(self):
        self.__az_authenticate = AzureAuthenticate()
        self.__credential = self.__az_authenticate.client_credentials()


    def list_by_subscription_id(self, subscription_id:str):
        """Lists all snapshots of a specific subscription.

         Args:
             subscription_id(str): The subscription ID.

         returns:
             list: A list of SnapshotModel objects containing snapshot information.
        """
        compute_client = ComputeManagementClient(self.__credential, subscription_id)

        snapshots_list = compute_client.snapshots.list()
        snapshot_list = []
        for snapshot in snapshots_list:
            resource_group_name = snapshot.id.split("/")[4]
            created_time = snapshot.time_created.strftime("%Y-%m-%d %H:%M:%S")
            snapshot_list.append(SnapshotModel(
                                subscription_id,
                                resource_group_name,
                                snapshot.id,
                                snapshot.name,
                                snapshot.location,
                                snapshot.tags,
                                snapshot.type,
                                created_time)
                            )

        return snapshot_list


    def list_by_resource_group(self, subscription_id:str, resource_group_name:str):
        """Lists all snapshots of a given resource group.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.

         returns:
             list: A list of SnapshotModel objects containing snapshot information.
        """
        compute_client = ComputeManagementClient(self.__credential, subscription_id)
        snapshot_list = []
        snapshots_list = compute_client.snapshots.list_by_resource_group(resource_group_name)

        for snapshot in snapshots_list:
            created_time = snapshot.time_created.strftime("%Y-%m-%d %H:%M:%S")
            snapshot_list.append(SnapshotModel(
                                subscription_id,
                                resource_group_name,
                                snapshot.id,
                                snapshot.name,
                                snapshot.location,
                                snapshot.tags,
                                snapshot.type,
                                created_time)
                            )

        return snapshot_list


    def get(self,subscription_id, resource_group_name: str, snapshot_name: str):
        """Get information for a specific snapshot.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.
             snapshot_name (str): The name of the snapshot.

         returns:
             SnapshotModel: A SnapshotModel object containing snapshot information.
        """
        compute_client = ComputeManagementClient(self.__credential, subscription_id)
        snapshot = compute_client.snapshots.get(resource_group_name, snapshot_name)
        created_time = snapshot.time_created.strftime("%Y-%m-%d %H:%M:%S")

        return SnapshotModel(
                            subscription_id,
                            resource_group_name,
                            snapshot.id,
                            snapshot.name,
                            snapshot.location,
                            snapshot.tags,
                            snapshot.type,
                            created_time
                        )


    def update_tag(self, subscription_id: str, resource_group_name: str, snapshot_name: str, tag_key:str, new_tag_value:str):
        """Updates the value of a tag in a snapshot.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.
             snapshot_name (str): The name of the snapshot.
             tag_key (str): The key of the tag to be updated.
             new_tag_value(str): The new value for the tag.

         returns:
             bool: True if the update was successful, False otherwise.

         Raises:
             TagNotFoundException: If the specified tag does not exist in the snapshot.
        """
        compute_client = ComputeManagementClient(self.__credential, subscription_id)
        snapshot = compute_client.snapshots.get(resource_group_name, snapshot_name)

        existing_tags = snapshot.tags

        if tag_key in existing_tags:
            existing_tags[tag_key] = new_tag_value
            result = compute_client.snapshots.begin_update(resource_group_name, snapshot_name, snapshot)

        else:
            raise TagNotFoundException(tag_key)

        return bool(result)


    def delete(self,subscription_id, resource_group_name: str, snapshot_name: str):
        """Deletes a snapshot.

         Args:
             subscription_id(str): The subscription ID.
             resource_group_name (str): The name of the resource group.
             snapshot_name (str): The name of the snapshot.

         returns:
             bool: True if deletion was successful, False otherwise.
        """
        compute_client = ComputeManagementClient(self.__credential, subscription_id)
        result = compute_client.snapshots.begin_delete(resource_group_name, snapshot_name)

        return bool(result)
