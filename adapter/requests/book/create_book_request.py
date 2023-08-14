from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
import jsonschema
from adapter.validators.name_validator import NameValidator

create_book_validator = {
    'type': 'object',
    'properties': {},
    'required': []
}

create_book_validator['properties'].update(NameValidator.schema())
create_book_validator['required'].append(NameValidator.field())

class CreateBookValidator(Inputs):
    json = [JsonSchema(schema=create_book_validator)]
