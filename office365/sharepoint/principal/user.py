from office365.runtime.queries.service_operation_query import ServiceOperationQuery
from office365.runtime.paths.resource_path import ResourcePath
from office365.sharepoint.alerts.alert_collection import AlertCollection
from office365.sharepoint.principal.principal import Principal
from office365.sharepoint.principal.user_id_info import UserIdInfo


class User(Principal):
    """Represents a user in Microsoft SharePoint Foundation. A user is a type of SP.Principal."""

    def get_personal_site(self):
        """Get personal site"""
        from office365.sharepoint.sites.site import Site
        site = Site(self.context)

        def _user_loaded():
            from office365.sharepoint.userprofiles.peopleManager import PeopleManager
            people_manager = PeopleManager(self.context)
            person_props = people_manager.get_properties_for(self.login_name)

            def _person_props_loaded(resp):
                site.set_property("NewSiteUrl", person_props.properties['PersonalUrl'])
            self.context.after_execute(_person_props_loaded)

        self.ensure_property("LoginName", _user_loaded)
        return site

    def get(self):
        """
        :rtype: User
        """
        return super(User, self).get()

    @property
    def groups(self):
        """Gets a collection of group objects that represents all of the groups for the user."""
        from office365.sharepoint.principal.group_collection import GroupCollection
        return self.properties.get('Groups',
                                   GroupCollection(self.context, ResourcePath("Groups", self.resource_path)))

    @property
    def alerts(self):
        return self.properties.get('Alerts',
                                   AlertCollection(self.context, ResourcePath("Alerts", self.resource_path)))

    @property
    def is_site_admin(self):
        """Gets or sets a Boolean value that specifies whether the user is a site collection administrator."""
        return self.properties.get('isSiteAdmin', None)

    @property
    def user_id(self):
        """Gets the information of the user that contains the user's name identifier and the issuer of the
         user's name identifier."""
        return self.properties.get('UserId', UserIdInfo())

    def expire(self):
        qry = ServiceOperationQuery(self, "Expire")
        self.context.add_query(qry)
        return self
