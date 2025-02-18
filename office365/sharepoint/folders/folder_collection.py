import os

from office365.runtime.paths.service_operation import ServiceOperationPath
from office365.runtime.queries.service_operation_query import ServiceOperationQuery
from office365.sharepoint.base_entity_collection import BaseEntityCollection
from office365.sharepoint.folders.folder import Folder
from office365.sharepoint.internal.paths.entity_resource import EntityPath


class FolderCollection(BaseEntityCollection):
    """Represents a collection of Folder resources."""
    def __init__(self, context, resource_path=None, parent=None):
        super(FolderCollection, self).__init__(context, Folder, resource_path, parent)

    def get(self):
        """
        :rtype: FolderCollection
        """
        return super(FolderCollection, self).get()

    def add_using_path(self, decoded_url, overwrite):
        """
        Adds the folder located at the specified path to the collection.

        :param str decoded_url: Specifies the path for the folder.
        :param bool overwrite:  bool
        """
        parameters = {
            "DecodedUrl": decoded_url,
            "Overwrite": overwrite
        }
        target_folder = Folder(self.context)
        qry = ServiceOperationQuery(self, "AddUsingPath", parameters, None, None, target_folder)
        self.context.add_query(qry)
        return target_folder

    def get_by_path(self, decoded_url):
        """
        Get folder at the specified path.

        :param str decoded_url: Specifies the path for the folder.
        """
        from office365.sharepoint.types.resource_path import ResourcePath as SPResPath
        target_folder = Folder(self.context)
        qry = ServiceOperationQuery(self, "GetByPath", SPResPath(decoded_url), None, "parameters", target_folder)
        self.context.add_query(qry)
        return target_folder

    def ensure_folder_path(self, path):
        """
        Ensures a nested folder hierarchy exist

        :param str path: relative server URL (path) to a folder
        """

        url_component = os.path.normpath(path).split(os.path.sep)
        url_component = [part for part in url_component if part]
        if not url_component:
            raise NotADirectoryError("Wrong relative URL provided")
        child_folder = self
        for url_part in url_component:
            child_folder = child_folder.add(url_part)
        return child_folder

    def add(self, name):
        """Adds the folder that is located at the specified URL to the collection.

        :param str name: Specifies the Name of the folder.
        """
        return_type = Folder(self.context, EntityPath(name, self.resource_path))
        self.add_child(return_type)
        qry = ServiceOperationQuery(self, "Add", [name], None, None, return_type)
        self.context.add_query(qry)
        return return_type

    def get_by_url(self, url):
        """Retrieve Folder resource by url

        :type url: str
        """
        return Folder(self.context, ServiceOperationPath("GetByUrl", [url], self.resource_path))
