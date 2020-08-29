class PlatformException(Exception):
    def __init__(self, *args, **kwargs):
        if hasattr(self, 'status_code') is False:
            self.status_code = 500
        if hasattr(self, 'message') is False:
            self.message = 'PlatformException'
        Exception.__init__(self, *args, **kwargs)


class PlatformException404(PlatformException):
    def __init__(self, *args, **kwargs):
        if hasattr(self, 'status_code') is False:
            self.status_code = 404
        if hasattr(self, 'message') is False:
            self.message = 'PlatformException404'
        PlatformException.__init__(self, *args, **kwargs)


class PlatformException403(PlatformException):
    def __init__(self, *args, **kwargs):
        if hasattr(self, 'status_code') is False:
            self.status_code = 403
        if hasattr(self, 'message') is False:
            self.message = 'PlatformException403'
        PlatformException.__init__(self, *args, **kwargs)


class PlatformException400(PlatformException):
    def __init__(self, *args, **kwargs):
        if hasattr(self, 'status_code') is False:
            self.status_code = 400
        if hasattr(self, 'message') is False:
            self.message = 'PlatformException400'
        PlatformException.__init__(self, *args, **kwargs)


# Exceptions
class ArgumentMissingException(PlatformException400):
    def __init__(self, msg):
        # self.message = 'ArgmentMissingException '+str(msg)
        self.message = str(msg)
        PlatformException400.__init__(self)


class InvalidAPIArgumentException(PlatformException400):
    def __init__(self, msg):
        # self.message = 'InvalidAPIArgumentException '+str(msg)
        self.message = str(msg)
        PlatformException400.__init__(self)


class NotImplementedException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NotImplementedException '+str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class InvalidFieldNameException(PlatformException):
    def __init__(self, msg):
        # self.message = 'InvalidFieldNameException '+str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class InvalidClassNameException(PlatformException):
    def __init__(self, msg):
        # self.message = 'InvalidClassNameException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class NoSuchAPIException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NoSuchAPIException '+ str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class NoPlatformConfigurationException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NoPlatformConfigurationException '+ str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class NoPlatformConfigurationKeyException(PlatformException):
    def __init__(self, msg):
        self.message = str(msg)
        # self.message = 'NoPlatformConfigurationKeyException '+str(msg)
        PlatformException.__init__(self)


# Database Exceptions
class DatabaseException(PlatformException):
    def __init__(self, msg):
        # self.message = 'DatabaseException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class NoDataException(DatabaseException):
    def __init__(self, msg):
        # self.message = 'NoDataException '+ str(msg)
        self.message = str(msg)
        DatabaseException.__init__(self)


class ConstraintViolationException(PlatformException):
    def __init__(self, msg):
        # self.message = 'ConstraintViolationException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class DatabaseException(PlatformException):
    def __init__(self, msg):
        # self.message = 'DatabaseException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class NoSuchDatabaseInstanceException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NoSuchDatabaseInstanceException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


# Service Exceptions
class UnsupportedServiceException(PlatformException):
    def __init__(self, msg):
        # self.message = 'UnsupportedServiceException '+str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class ServiceNotSetException(PlatformException):
    def __init__(self, msg):
        # self.message = 'ServiceNotSetException' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class UnsupportedServiceActionException(PlatformException):
    def __init__(self, msg):
        # self.message = 'UnsupportedServiceActionException' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


# Asset Exceptions
class NoSuchAssetTypeIdException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NoSuchAssetTypeIdException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class InvalidUserAssetException(PlatformException):
    def __init__(self, msg):
        # self.message = 'InvalidUserAssetException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


# User Exception
class NoSuchUserException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NoSuchUserException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


# Notification Exception
class NotificationInvalidEventException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NotificationInvalidEventException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class NotificationParameterMissingException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NotificationParameterMissingException '+str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


# Application Exception
class NoSuchApplicationException(PlatformException):
    def __init__(self, msg):
        # self.message = 'NoSuchApplicationException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class ApplicationPermissionDeniedException(PlatformException):
    def __init__(self, msg):
        # self.message = 'ApplicationPermissionDeniedException ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)


class ApplicationAssetMissingException(PlatformException):
    def __init__(self, msg):
        # self.message = 'Application Asset Missing Exception ' + str(msg)
        self.message = str(msg)
        PlatformException.__init__(self)
