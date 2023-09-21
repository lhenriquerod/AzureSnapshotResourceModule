class TagNotFoundException(Exception):
    """Exceção lançada quando uma tag não é encontrada."""

    def __init__(self, tag_key):
        self.tag_key = tag_key
        message = f"The '{tag_key}' tag does not exist."
        super().__init__(message)