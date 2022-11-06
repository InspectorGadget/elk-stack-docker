class ReprMixin(object):
    def __repr__(self):
        model_name = type(self).__name__
        column_names = [
            column.name
            for column in self.__table__.columns
        ]
        column_values = ', '.join([
            f"{column_name}={getattr(self, column_name).__repr__()}"
            for column_name in column_names
        ])

        return f"<{model_name}({column_values})>"