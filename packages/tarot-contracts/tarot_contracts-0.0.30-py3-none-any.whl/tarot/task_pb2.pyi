from tarot import bot_pb2 as _bot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TASK_STATUS_UNSPECIFIED: _ClassVar[TaskStatus]
    TASK_STATUS_PENDING: _ClassVar[TaskStatus]
    TASK_STATUS_IN_PROGRESS: _ClassVar[TaskStatus]
    TASK_STATUS_COMPLETED: _ClassVar[TaskStatus]
    TASK_STATUS_FAILED: _ClassVar[TaskStatus]

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TASK_TYPE_UNSPECIFIED: _ClassVar[TaskType]
    TASK_TYPE_SEND_MESSAGE: _ClassVar[TaskType]
    TASK_TYPE_SEND_BATCH_MESSAGE: _ClassVar[TaskType]
TASK_STATUS_UNSPECIFIED: TaskStatus
TASK_STATUS_PENDING: TaskStatus
TASK_STATUS_IN_PROGRESS: TaskStatus
TASK_STATUS_COMPLETED: TaskStatus
TASK_STATUS_FAILED: TaskStatus
TASK_TYPE_UNSPECIFIED: TaskType
TASK_TYPE_SEND_MESSAGE: TaskType
TASK_TYPE_SEND_BATCH_MESSAGE: TaskType

class SendMessagePayload(_message.Message):
    __slots__ = ["message", "recipient_id", "action", "type"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    recipient_id: int
    action: _bot_pb2.MessageAction
    type: _bot_pb2.MessageType
    def __init__(self, message: _Optional[str] = ..., recipient_id: _Optional[int] = ..., action: _Optional[_Union[_bot_pb2.MessageAction, _Mapping]] = ..., type: _Optional[_Union[_bot_pb2.MessageType, str]] = ...) -> None: ...

class SendMessageBatchPayload(_message.Message):
    __slots__ = ["message", "recipient_ids", "action", "type"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    recipient_ids: _containers.RepeatedScalarFieldContainer[int]
    action: _bot_pb2.MessageAction
    type: _bot_pb2.MessageType
    def __init__(self, message: _Optional[str] = ..., recipient_ids: _Optional[_Iterable[int]] = ..., action: _Optional[_Union[_bot_pb2.MessageAction, _Mapping]] = ..., type: _Optional[_Union[_bot_pb2.MessageType, str]] = ...) -> None: ...

class ScheduleTaskRequest(_message.Message):
    __slots__ = ["name", "type", "send_message_payload", "send_batch_message_payload", "due_timestamp"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SEND_BATCH_MESSAGE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DUE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: TaskType
    send_message_payload: SendMessagePayload
    send_batch_message_payload: SendMessageBatchPayload
    due_timestamp: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[TaskType, str]] = ..., send_message_payload: _Optional[_Union[SendMessagePayload, _Mapping]] = ..., send_batch_message_payload: _Optional[_Union[SendMessageBatchPayload, _Mapping]] = ..., due_timestamp: _Optional[int] = ...) -> None: ...

class ScheduleTaskResponse(_message.Message):
    __slots__ = ["id", "name", "due_date", "type", "status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    due_date: str
    type: TaskType
    status: TaskStatus
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., due_date: _Optional[str] = ..., type: _Optional[_Union[TaskType, str]] = ..., status: _Optional[_Union[TaskStatus, str]] = ...) -> None: ...
