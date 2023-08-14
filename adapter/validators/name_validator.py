class NameValidator:
    def schema():
        return {
            'name': {
                'type': 'string',
                'minLength': 3,
                'pattern': '^[^0-9]+$'
            }
        }    
    
    def field():
        return 'name'
    