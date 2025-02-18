from office365.runtime.paths.resource_path import ResourcePath
from office365.sharepoint.base_entity import BaseEntity
from office365.sharepoint.sharing.picker_settings import PickerSettings


class SharePointSharingSettings(BaseEntity):
    """This class contains the SharePoint UI-specific sharing settings."""

    @property
    def picker_properties(self):
        """An object containing the necessary information to initialize a client people picker control used
        to search for and resolve desired users and groups."""
        return self.properties.get('PickerProperties',
                                   PickerSettings(self.context, ResourcePath("PickerProperties", self.resource_path)))
