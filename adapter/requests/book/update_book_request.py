from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
import jsonschema
from adapter.validators.name_validator import NameValidator

update_book_validator = {
    'type': 'object',
    'properties': {},
    'required': []
}

update_book_validator['properties'].update(NameValidator.schema())
update_book_validator['required'].append(NameValidator.field())

class UpdateBookRequest(Inputs):
    json = [JsonSchema(schema=update_book_validator)]
