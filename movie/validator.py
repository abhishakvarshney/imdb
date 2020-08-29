from voluptuous import Schema, Required, MultipleInvalid, Any


def validate_add_student(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('studentId'): str,
            Required('password'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_update_student(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('studentId'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_delete_student_account(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('studentId'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_student_delete_teacher(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('teacherId'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}

def validate_add_teacher(data):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('teacherId'): str,
            Required('password'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_update_teacher(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('teacherId'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_delete_teacher_account(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('teacherId'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_teacher_delete_student(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('studentId'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_mark_student(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('studentId'): str,
            Required('teacherId'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
