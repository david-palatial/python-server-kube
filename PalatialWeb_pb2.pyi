from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectInfo(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ImportInfo(_message.Message):
    __slots__ = ["project_id", "download_link", "info"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    download_link: str
    info: ProjectInfo
    def __init__(self, project_id: _Optional[str] = ..., download_link: _Optional[str] = ..., info: _Optional[_Union[ProjectInfo, _Mapping]] = ...) -> None: ...

class NewAccountInfo(_message.Message):
    __slots__ = ["username", "email", "password"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    email: str
    password: str
    def __init__(self, username: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AccountResult(_message.Message):
    __slots__ = ["result"]
    class AccountCreationResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        FAILURE_UNSPECIFIED: _ClassVar[AccountResult.AccountCreationResult]
        SUCCESS: _ClassVar[AccountResult.AccountCreationResult]
        USERNAME_TAKEN: _ClassVar[AccountResult.AccountCreationResult]
    FAILURE_UNSPECIFIED: AccountResult.AccountCreationResult
    SUCCESS: AccountResult.AccountCreationResult
    USERNAME_TAKEN: AccountResult.AccountCreationResult
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: AccountResult.AccountCreationResult
    def __init__(self, result: _Optional[_Union[AccountResult.AccountCreationResult, str]] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["username", "user_id"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    username: str
    user_id: str
    def __init__(self, username: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DashboardProjectsInfo(_message.Message):
    __slots__ = ["projects", "first_time_user"]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIME_USER_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[ProjectInfo]
    first_time_user: bool
    def __init__(self, projects: _Optional[_Iterable[_Union[ProjectInfo, _Mapping]]] = ..., first_time_user: bool = ...) -> None: ...

class PixelStreamingLink(_message.Message):
    __slots__ = ["project_id", "pixelstreaming_link"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PIXELSTREAMING_LINK_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    pixelstreaming_link: str
    def __init__(self, project_id: _Optional[str] = ..., pixelstreaming_link: _Optional[str] = ...) -> None: ...

class DeleteProject(_message.Message):
    __slots__ = ["project_id", "user_info"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    user_info: str
    def __init__(self, project_id: _Optional[str] = ..., user_info: _Optional[str] = ...) -> None: ...

class CommitAction(_message.Message):
    __slots__ = ["project_id", "do_commit"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DO_COMMIT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    do_commit: bool
    def __init__(self, project_id: _Optional[str] = ..., do_commit: bool = ...) -> None: ...

class EditingAction(_message.Message):
    __slots__ = ["project_id", "batch_delete_action", "flip_normal_action", "add_light_action", "batch_light_setting_action", "batch_translate_action", "adjust_context_action", "crop_context_action", "undo_action", "toggle_nanite_action", "set_player_start_action", "add_saved_view_action", "set_saved_view_action", "batch_replace_material_action", "place_context_action"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_DELETE_ACTION_FIELD_NUMBER: _ClassVar[int]
    FLIP_NORMAL_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADD_LIGHT_ACTION_FIELD_NUMBER: _ClassVar[int]
    BATCH_LIGHT_SETTING_ACTION_FIELD_NUMBER: _ClassVar[int]
    BATCH_TRANSLATE_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADJUST_CONTEXT_ACTION_FIELD_NUMBER: _ClassVar[int]
    CROP_CONTEXT_ACTION_FIELD_NUMBER: _ClassVar[int]
    UNDO_ACTION_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_NANITE_ACTION_FIELD_NUMBER: _ClassVar[int]
    SET_PLAYER_START_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADD_SAVED_VIEW_ACTION_FIELD_NUMBER: _ClassVar[int]
    SET_SAVED_VIEW_ACTION_FIELD_NUMBER: _ClassVar[int]
    BATCH_REPLACE_MATERIAL_ACTION_FIELD_NUMBER: _ClassVar[int]
    PLACE_CONTEXT_ACTION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    batch_delete_action: BatchDelete
    flip_normal_action: FlipNormal
    add_light_action: AddLight
    batch_light_setting_action: BatchLightSettings
    batch_translate_action: BatchTranslate
    adjust_context_action: AdjustContext
    crop_context_action: CropContext
    undo_action: Undo
    toggle_nanite_action: ToggleNanite
    set_player_start_action: SetPlayerStart
    add_saved_view_action: AddSavedView
    set_saved_view_action: SetSavedView
    batch_replace_material_action: BatchReplaceMaterial
    place_context_action: PlaceContext
    def __init__(self, project_id: _Optional[str] = ..., batch_delete_action: _Optional[_Union[BatchDelete, _Mapping]] = ..., flip_normal_action: _Optional[_Union[FlipNormal, _Mapping]] = ..., add_light_action: _Optional[_Union[AddLight, _Mapping]] = ..., batch_light_setting_action: _Optional[_Union[BatchLightSettings, _Mapping]] = ..., batch_translate_action: _Optional[_Union[BatchTranslate, _Mapping]] = ..., adjust_context_action: _Optional[_Union[AdjustContext, _Mapping]] = ..., crop_context_action: _Optional[_Union[CropContext, _Mapping]] = ..., undo_action: _Optional[_Union[Undo, _Mapping]] = ..., toggle_nanite_action: _Optional[_Union[ToggleNanite, _Mapping]] = ..., set_player_start_action: _Optional[_Union[SetPlayerStart, _Mapping]] = ..., add_saved_view_action: _Optional[_Union[AddSavedView, _Mapping]] = ..., set_saved_view_action: _Optional[_Union[SetSavedView, _Mapping]] = ..., batch_replace_material_action: _Optional[_Union[BatchReplaceMaterial, _Mapping]] = ..., place_context_action: _Optional[_Union[PlaceContext, _Mapping]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Vector(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class BatchDelete(_message.Message):
    __slots__ = ["delete_action"]
    class Delete(_message.Message):
        __slots__ = ["mesh_id"]
        MESH_ID_FIELD_NUMBER: _ClassVar[int]
        mesh_id: str
        def __init__(self, mesh_id: _Optional[str] = ...) -> None: ...
    DELETE_ACTION_FIELD_NUMBER: _ClassVar[int]
    delete_action: _containers.RepeatedCompositeFieldContainer[BatchDelete.Delete]
    def __init__(self, delete_action: _Optional[_Iterable[_Union[BatchDelete.Delete, _Mapping]]] = ...) -> None: ...

class FlipNormal(_message.Message):
    __slots__ = ["mesh_id"]
    MESH_ID_FIELD_NUMBER: _ClassVar[int]
    mesh_id: str
    def __init__(self, mesh_id: _Optional[str] = ...) -> None: ...

class AddLight(_message.Message):
    __slots__ = ["unique_id", "type", "location"]
    class LightType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        POINT_LIGHT: _ClassVar[AddLight.LightType]
        SPOT_LIGHT: _ClassVar[AddLight.LightType]
        RECT_LIGHT: _ClassVar[AddLight.LightType]
    POINT_LIGHT: AddLight.LightType
    SPOT_LIGHT: AddLight.LightType
    RECT_LIGHT: AddLight.LightType
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    unique_id: str
    type: AddLight.LightType
    location: Location
    def __init__(self, unique_id: _Optional[str] = ..., type: _Optional[_Union[AddLight.LightType, str]] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class BatchLightSettings(_message.Message):
    __slots__ = ["light_setting_action"]
    class LightSettings(_message.Message):
        __slots__ = ["light_id", "enabled", "cast_shadows", "intensity", "attenuation", "source_radius", "soft_source_radius", "source_length", "inner_cone_angle", "outer_cone_angle", "source_width", "source_weight", "barn_door_angle", "barn_door_length", "color_r", "color_g", "color_b"]
        LIGHT_ID_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CAST_SHADOWS_FIELD_NUMBER: _ClassVar[int]
        INTENSITY_FIELD_NUMBER: _ClassVar[int]
        ATTENUATION_FIELD_NUMBER: _ClassVar[int]
        SOURCE_RADIUS_FIELD_NUMBER: _ClassVar[int]
        SOFT_SOURCE_RADIUS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_LENGTH_FIELD_NUMBER: _ClassVar[int]
        INNER_CONE_ANGLE_FIELD_NUMBER: _ClassVar[int]
        OUTER_CONE_ANGLE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_WIDTH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
        BARN_DOOR_ANGLE_FIELD_NUMBER: _ClassVar[int]
        BARN_DOOR_LENGTH_FIELD_NUMBER: _ClassVar[int]
        COLOR_R_FIELD_NUMBER: _ClassVar[int]
        COLOR_G_FIELD_NUMBER: _ClassVar[int]
        COLOR_B_FIELD_NUMBER: _ClassVar[int]
        light_id: str
        enabled: bool
        cast_shadows: bool
        intensity: float
        attenuation: float
        source_radius: float
        soft_source_radius: float
        source_length: float
        inner_cone_angle: float
        outer_cone_angle: float
        source_width: float
        source_weight: float
        barn_door_angle: float
        barn_door_length: float
        color_r: float
        color_g: float
        color_b: float
        def __init__(self, light_id: _Optional[str] = ..., enabled: bool = ..., cast_shadows: bool = ..., intensity: _Optional[float] = ..., attenuation: _Optional[float] = ..., source_radius: _Optional[float] = ..., soft_source_radius: _Optional[float] = ..., source_length: _Optional[float] = ..., inner_cone_angle: _Optional[float] = ..., outer_cone_angle: _Optional[float] = ..., source_width: _Optional[float] = ..., source_weight: _Optional[float] = ..., barn_door_angle: _Optional[float] = ..., barn_door_length: _Optional[float] = ..., color_r: _Optional[float] = ..., color_g: _Optional[float] = ..., color_b: _Optional[float] = ...) -> None: ...
    LIGHT_SETTING_ACTION_FIELD_NUMBER: _ClassVar[int]
    light_setting_action: _containers.RepeatedCompositeFieldContainer[BatchLightSettings.LightSettings]
    def __init__(self, light_setting_action: _Optional[_Iterable[_Union[BatchLightSettings.LightSettings, _Mapping]]] = ...) -> None: ...

class BatchTranslate(_message.Message):
    __slots__ = ["translate"]
    class Translate(_message.Message):
        __slots__ = ["mesh_id", "location"]
        MESH_ID_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        mesh_id: str
        location: Location
        def __init__(self, mesh_id: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...
    TRANSLATE_FIELD_NUMBER: _ClassVar[int]
    translate: _containers.RepeatedCompositeFieldContainer[BatchTranslate.Translate]
    def __init__(self, translate: _Optional[_Iterable[_Union[BatchTranslate.Translate, _Mapping]]] = ...) -> None: ...

class AdjustContext(_message.Message):
    __slots__ = ["lat", "long", "height", "angle"]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    lat: float
    long: float
    height: float
    angle: float
    def __init__(self, lat: _Optional[float] = ..., long: _Optional[float] = ..., height: _Optional[float] = ..., angle: _Optional[float] = ...) -> None: ...

class CropContext(_message.Message):
    __slots__ = ["spline_point"]
    SPLINE_POINT_FIELD_NUMBER: _ClassVar[int]
    spline_point: _containers.RepeatedCompositeFieldContainer[Location]
    def __init__(self, spline_point: _Optional[_Iterable[_Union[Location, _Mapping]]] = ...) -> None: ...

class Undo(_message.Message):
    __slots__ = ["ack"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: bool
    def __init__(self, ack: bool = ...) -> None: ...

class ToggleNanite(_message.Message):
    __slots__ = ["mesh_id", "disabled"]
    MESH_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    mesh_id: str
    disabled: bool
    def __init__(self, mesh_id: _Optional[str] = ..., disabled: bool = ...) -> None: ...

class SetPlayerStart(_message.Message):
    __slots__ = ["camera_id"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    camera_id: str
    def __init__(self, camera_id: _Optional[str] = ...) -> None: ...

class AddSavedView(_message.Message):
    __slots__ = ["unique_id", "name", "location", "rotation_x", "rotation_y", "rotation_z"]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_X_FIELD_NUMBER: _ClassVar[int]
    ROTATION_Y_FIELD_NUMBER: _ClassVar[int]
    ROTATION_Z_FIELD_NUMBER: _ClassVar[int]
    unique_id: str
    name: str
    location: Location
    rotation_x: float
    rotation_y: float
    rotation_z: float
    def __init__(self, unique_id: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., rotation_x: _Optional[float] = ..., rotation_y: _Optional[float] = ..., rotation_z: _Optional[float] = ...) -> None: ...

class SetSavedView(_message.Message):
    __slots__ = ["camera_id", "enabled", "name"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    camera_id: str
    enabled: bool
    name: str
    def __init__(self, camera_id: _Optional[str] = ..., enabled: bool = ..., name: _Optional[str] = ...) -> None: ...

class BatchReplaceMaterial(_message.Message):
    __slots__ = ["old_material_path", "new_material_path", "mesh_ids"]
    OLD_MATERIAL_PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_MATERIAL_PATH_FIELD_NUMBER: _ClassVar[int]
    MESH_IDS_FIELD_NUMBER: _ClassVar[int]
    old_material_path: str
    new_material_path: str
    mesh_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, old_material_path: _Optional[str] = ..., new_material_path: _Optional[str] = ..., mesh_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PlaceContext(_message.Message):
    __slots__ = ["enabled"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class Ack(_message.Message):
    __slots__ = ["ack"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: bool
    def __init__(self, ack: bool = ...) -> None: ...
