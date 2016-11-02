# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class DataFormatType(T.Enum):
    """
    One of ['json', 'csv', 'tsv', 'topojson']
    """
    def __init__(self, default_value=T.Undefined, **metadata):
        super(DataFormatType, self).__init__(['json', 'csv', 'tsv', 'topojson'],
                                    default_value=default_value,
                                    **metadata)