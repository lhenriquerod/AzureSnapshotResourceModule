"""Validate parameter"""
class TypeValidation:
    """Class that has methods to validate the type of parameter."""

    def validate_parameter_type(self, param, param_name, type):
        """Validate the type of parameter."""
        if isinstance(param, type):
            return True
        else:
            raise TypeError(f'The "{param_name}" parameter must be {type}.')
        
