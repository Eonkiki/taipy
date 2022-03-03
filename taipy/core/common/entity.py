from taipy.core.common.reload import set_entity


class Entity:
    MANAGER_NAME: str
    is_in_context = False

    def __enter__(self):
        self.is_in_context = True
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.is_in_context = False
        set_entity(self.MANAGER_NAME, self)
