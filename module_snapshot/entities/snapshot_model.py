"""Model for Snapshot data."""
from dataclasses import dataclass

@dataclass
class SnapshotModel:
    subscription_id: str
    resource_group_name: str
    resource_id:str
    snapshot_name:str
    location: str
    tags: dict
    resource_type: str
    created_date: str