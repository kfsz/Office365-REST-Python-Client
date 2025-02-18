from office365.runtime.queries.service_operation_query import ServiceOperationQuery
from office365.sharepoint.base_entity_collection import BaseEntityCollection
from office365.sharepoint.usercustomactions.user_custom_action import UserCustomAction


class UserCustomActionCollection(BaseEntityCollection):

    def __init__(self, context, resource_path=None):
        """Specifies a collection of custom actions."""
        super(UserCustomActionCollection, self).__init__(context, UserCustomAction, resource_path)

    def clear(self):
        """
        Deletes all custom actions in the collection.

        Exceptions:
        - 2130575305 Microsoft.SharePoint.SPException Custom action was modified on the server  in a way that
             prevents changes from being committed, as determined by the protocol server.
        """
        qry = ServiceOperationQuery(self, "Clear")
        self.context.add_query(qry)
        return self
