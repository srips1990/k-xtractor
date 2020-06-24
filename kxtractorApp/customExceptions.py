
def get_validation_exception_obj(error_msg, field_name):
    return {'validation_error': error_msg, 'field_name': field_name}


def get_general_exception_obj(error_msg):
    return {'error': error_msg}
