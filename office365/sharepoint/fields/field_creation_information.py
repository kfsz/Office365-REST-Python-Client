from office365.runtime.client_value import ClientValue
from office365.runtime.client_value_collection import ClientValueCollection
from office365.sharepoint.fields.field_type import FieldType


class FieldCreationInformation(ClientValue):

    def __init__(self, title, field_type_kind, description=None,
                 lookup_list_id=None, lookup_field_name=None, lookup_web_id=None,
                 required=False, formula=None):
        """
        Represents metadata about fields creation.

        :param str lookup_web_id: Specifies the identifier of the site (2) that contains the list that is the
            source for the field (2) value.
        :param bool required: Specifies whether the field (2) requires a value.
        :type lookup_field_name: str
        :param str lookup_list_id: A CSOM GUID that specifies the target list for the lookup field (2).
        :type title: str
        :param int field_type_kind: Specifies the type of the field (2).
        :type description: str or None
        :type formula: str or None
        """
        super(FieldCreationInformation, self).__init__()
        self.Title = title
        self.FieldTypeKind = field_type_kind
        self.Description = description
        self.Choices = ClientValueCollection(str) \
            if field_type_kind == FieldType.MultiChoice or field_type_kind == FieldType.Choice else None
        self.LookupListId = lookup_list_id
        self.LookupFieldName = lookup_field_name
        self.LookupWebId = lookup_web_id
        self.Required = required
        self.Formula = formula

    @property
    def entity_type_name(self):
        return "SP.FieldCreationInformation"
