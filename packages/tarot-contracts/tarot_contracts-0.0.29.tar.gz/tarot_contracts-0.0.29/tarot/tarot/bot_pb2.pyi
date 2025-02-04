from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MESSAGE_ACTION_TYPE_UNSPECIFIED: _ClassVar[MessageActionType]
    MESSAGE_ACTION_TYPE_URL: _ClassVar[MessageActionType]
    MESSAGE_ACTION_TYPE_CALLBACK: _ClassVar[MessageActionType]
    MESSAGE_ACTION_TYPE_CALLBACK_PARAMETRIZED: _ClassVar[MessageActionType]

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MESSAGE_TYPE_UNSPECIFIED: _ClassVar[MessageType]
    MESSAGE_TYPE_MESSAGE: _ClassVar[MessageType]
    MESSAGE_TYPE_SPREAD_RESULT: _ClassVar[MessageType]

class SentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SENT_STATUS_UNSPECIFIED: _ClassVar[SentStatus]
    SENT_STATUS_SENT: _ClassVar[SentStatus]
    SENT_STATUS_ERROR: _ClassVar[SentStatus]
    SENT_STATUS_USER_BLOCKED: _ClassVar[SentStatus]
MESSAGE_ACTION_TYPE_UNSPECIFIED: MessageActionType
MESSAGE_ACTION_TYPE_URL: MessageActionType
MESSAGE_ACTION_TYPE_CALLBACK: MessageActionType
MESSAGE_ACTION_TYPE_CALLBACK_PARAMETRIZED: MessageActionType
MESSAGE_TYPE_UNSPECIFIED: MessageType
MESSAGE_TYPE_MESSAGE: MessageType
MESSAGE_TYPE_SPREAD_RESULT: MessageType
SENT_STATUS_UNSPECIFIED: SentStatus
SENT_STATUS_SENT: SentStatus
SENT_STATUS_ERROR: SentStatus
SENT_STATUS_USER_BLOCKED: SentStatus

class MessageAction(_message.Message):
    __slots__ = ["title", "url", "callback", "callback_param"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_PARAM_FIELD_NUMBER: _ClassVar[int]
    title: str
    url: str
    callback: str
    callback_param: str
    def __init__(self, title: _Optional[str] = ..., url: _Optional[str] = ..., callback: _Optional[str] = ..., callback_param: _Optional[str] = ...) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ["message", "actions", "recipient_ids", "type"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    actions: _containers.RepeatedCompositeFieldContainer[MessageAction]
    recipient_ids: _containers.RepeatedScalarFieldContainer[int]
    type: MessageType
    def __init__(self, message: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[MessageAction, _Mapping]]] = ..., recipient_ids: _Optional[_Iterable[int]] = ..., type: _Optional[_Union[MessageType, str]] = ...) -> None: ...

class MessageSentStatus(_message.Message):
    __slots__ = ["recipient_id", "status"]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    recipient_id: int
    status: SentStatus
    def __init__(self, recipient_id: _Optional[int] = ..., status: _Optional[_Union[SentStatus, str]] = ...) -> None: ...

class SendMessageResponse(_message.Message):
    __slots__ = ["statuses"]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedCompositeFieldContainer[MessageSentStatus]
    def __init__(self, statuses: _Optional[_Iterable[_Union[MessageSentStatus, _Mapping]]] = ...) -> None: ...
