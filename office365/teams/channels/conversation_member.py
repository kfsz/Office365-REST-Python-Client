from office365.entity import Entity
from office365.runtime.types.string_collection import StringCollection


class ConversationMember(Entity):
    """Represents a user in a team, a channel, or a chat. See also aadUserConversationMember."""

    @property
    def roles(self):
        """The roles for that user."""
        return self.properties.get('roles', StringCollection())


