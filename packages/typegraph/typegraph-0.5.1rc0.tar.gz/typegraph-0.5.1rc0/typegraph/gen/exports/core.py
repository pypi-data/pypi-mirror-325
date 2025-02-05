from ..intrinsics import _clamp, _decode_utf8, _encode_utf8, _list_canon_lower, _load, _store
from ..types import Err, Ok, Result
import ctypes
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union
import wasmtime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .. import Root

@dataclass
class Error:
    stack: List[str]

@dataclass
class Cors:
    allow_origin: List[str]
    allow_headers: List[str]
    expose_headers: List[str]
    allow_methods: List[str]
    allow_credentials: bool
    max_age_sec: Optional[int]

@dataclass
class Rate:
    window_limit: int
    window_sec: int
    query_limit: int
    context_identifier: Optional[str]
    local_excess: int

@dataclass
class TypegraphInitParams:
    name: str
    dynamic: Optional[bool]
    path: str
    prefix: Optional[str]
    cors: Cors
    rate: Optional[Rate]

@dataclass
class Artifact:
    path: str
    hash: str
    size: int

@dataclass
class MigrationAction:
    apply: bool
    create: bool
    reset: bool

@dataclass
class PrismaMigrationConfig:
    migrations_dir: str
    migration_actions: List[Tuple[str, MigrationAction]]
    default_migration_action: MigrationAction

@dataclass
class SerializeParams:
    typegraph_path: str
    prefix: Optional[str]
    artifact_resolution: bool
    codegen: bool
    prisma_migration: PrismaMigrationConfig
    pretty: bool

TypeId = int
@dataclass
class TypeProxy:
    name: str
    extras: List[Tuple[str, str]]

@dataclass
class TypeInteger:
    min: Optional[int]
    max: Optional[int]
    exclusive_minimum: Optional[int]
    exclusive_maximum: Optional[int]
    multiple_of: Optional[int]
    enumeration: Optional[List[int]]

@dataclass
class TypeFloat:
    min: Optional[float]
    max: Optional[float]
    exclusive_minimum: Optional[float]
    exclusive_maximum: Optional[float]
    multiple_of: Optional[float]
    enumeration: Optional[List[float]]

@dataclass
class TypeString:
    min: Optional[int]
    max: Optional[int]
    format: Optional[str]
    pattern: Optional[str]
    enumeration: Optional[List[str]]

@dataclass
class TypeFile:
    min: Optional[int]
    max: Optional[int]
    allow: Optional[List[str]]

@dataclass
class TypeList:
    of: TypeId
    min: Optional[int]
    max: Optional[int]
    unique_items: Optional[bool]

@dataclass
class TypeOptional:
    of: TypeId
    default_item: Optional[str]

@dataclass
class TypeUnion:
    variants: List[TypeId]

@dataclass
class TypeEither:
    variants: List[TypeId]

@dataclass
class TypeStruct:
    props: List[Tuple[str, TypeId]]
    additional_props: bool
    min: Optional[int]
    max: Optional[int]
    enumeration: Optional[List[str]]

@dataclass
class ValueSourceRaw:
    value: str

@dataclass
class ValueSourceContext:
    value: str

@dataclass
class ValueSourceSecret:
    value: str

@dataclass
class ValueSourceParent:
    value: str

@dataclass
class ValueSourceParam:
    value: str

ValueSource = Union[ValueSourceRaw, ValueSourceContext, ValueSourceSecret, ValueSourceParent, ValueSourceParam]

@dataclass
class ParameterTransform:
    resolver_input: TypeId
    transform_tree: str

@dataclass
class TransformData:
    query_input: TypeId
    parameter_transform: ParameterTransform

PolicyId = int
@dataclass
class PolicyPerEffect:
    read: Optional[PolicyId]
    create: Optional[PolicyId]
    update: Optional[PolicyId]
    delete: Optional[PolicyId]

@dataclass
class PolicySpecSimple:
    value: PolicyId

@dataclass
class PolicySpecPerEffect:
    value: PolicyPerEffect

PolicySpec = Union[PolicySpecSimple, PolicySpecPerEffect]

@dataclass
class ContextCheckNotNull:
    pass

@dataclass
class ContextCheckValue:
    value: str

@dataclass
class ContextCheckPattern:
    value: str

ContextCheck = Union[ContextCheckNotNull, ContextCheckValue, ContextCheckPattern]

RuntimeId = int
MaterializerId = int
@dataclass
class TypeFunc:
    inp: TypeId
    parameter_transform: Optional[ParameterTransform]
    out: TypeId
    mat: MaterializerId
    rate_calls: bool
    rate_weight: Optional[int]

@dataclass
class Policy:
    name: str
    materializer: MaterializerId

@dataclass
class FuncParams:
    inp: TypeId
    out: TypeId
    mat: MaterializerId

class Core:
    component: 'Root'
    
    def __init__(self, component: 'Root') -> None:
        self.component = component
    def init_typegraph(self, caller: wasmtime.Store, params: TypegraphInitParams) -> Result[None, Error]:
        ptr = self.component._realloc0(caller, 0, 0, 4, 108)
        assert(isinstance(ptr, int))
        record = params
        field = record.name
        field0 = record.dynamic
        field1 = record.path
        field2 = record.prefix
        field3 = record.cors
        field4 = record.rate
        ptr5, len6 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 4, len6)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 0, ptr5)
        if field0 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 8, 0)
        else:
            payload7 = field0
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 8, 1)
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 9, int(payload7))
        ptr8, len9 = _encode_utf8(field1, self.component._realloc0, self.component._core_memory0, caller)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 16, len9)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 12, ptr8)
        if field2 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 20, 0)
        else:
            payload11 = field2
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 20, 1)
            ptr12, len13 = _encode_utf8(payload11, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 28, len13)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 24, ptr12)
        record14 = field3
        field15 = record14.allow_origin
        field16 = record14.allow_headers
        field17 = record14.expose_headers
        field18 = record14.allow_methods
        field19 = record14.allow_credentials
        field20 = record14.max_age_sec
        vec = field15
        len24 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len24 * 8)
        assert(isinstance(result, int))
        for i25 in range(0, len24):
            e = vec[i25]
            base21 = result + i25 * 8
            ptr22, len23 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base21, 4, len23)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base21, 0, ptr22)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 36, len24)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 32, result)
        vec30 = field16
        len32 = len(vec30)
        result31 = self.component._realloc0(caller, 0, 0, 4, len32 * 8)
        assert(isinstance(result31, int))
        for i33 in range(0, len32):
            e26 = vec30[i33]
            base27 = result31 + i33 * 8
            ptr28, len29 = _encode_utf8(e26, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base27, 4, len29)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base27, 0, ptr28)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 44, len32)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 40, result31)
        vec38 = field17
        len40 = len(vec38)
        result39 = self.component._realloc0(caller, 0, 0, 4, len40 * 8)
        assert(isinstance(result39, int))
        for i41 in range(0, len40):
            e34 = vec38[i41]
            base35 = result39 + i41 * 8
            ptr36, len37 = _encode_utf8(e34, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base35, 4, len37)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base35, 0, ptr36)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 52, len40)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 48, result39)
        vec46 = field18
        len48 = len(vec46)
        result47 = self.component._realloc0(caller, 0, 0, 4, len48 * 8)
        assert(isinstance(result47, int))
        for i49 in range(0, len48):
            e42 = vec46[i49]
            base43 = result47 + i49 * 8
            ptr44, len45 = _encode_utf8(e42, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base43, 4, len45)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base43, 0, ptr44)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 60, len48)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 56, result47)
        _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 64, int(field19))
        if field20 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 68, 0)
        else:
            payload51 = field20
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 68, 1)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 72, _clamp(payload51, 0, 4294967295))
        if field4 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 76, 0)
        else:
            payload53 = field4
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 76, 1)
            record54 = payload53
            field55 = record54.window_limit
            field56 = record54.window_sec
            field57 = record54.query_limit
            field58 = record54.context_identifier
            field59 = record54.local_excess
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 80, _clamp(field55, 0, 4294967295))
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 84, _clamp(field56, 0, 4294967295))
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 88, _clamp(field57, 0, 4294967295))
            if field58 is None:
                _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 92, 0)
            else:
                payload61 = field58
                _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 92, 1)
                ptr62, len63 = _encode_utf8(payload61, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 100, len63)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 96, ptr62)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 104, _clamp(field59, 0, 4294967295))
        ret = self.component.lift_callee0(caller, ptr)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[None, Error]
        if load == 0:
            expected = Ok(None)
        elif load == 1:
            load64 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load65 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr71 = load64
            len72 = load65
            result73: List[str] = []
            for i74 in range(0, len72):
                base66 = ptr71 + i74 * 8
                load67 = _load(ctypes.c_int32, self.component._core_memory0, caller, base66, 0)
                load68 = _load(ctypes.c_int32, self.component._core_memory0, caller, base66, 4)
                ptr69 = load67
                len70 = load68
                list = _decode_utf8(self.component._core_memory0, caller, ptr69, len70)
                result73.append(list)
            expected = Err(Error(result73))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def serialize_typegraph(self, caller: wasmtime.Store, params: SerializeParams) -> Result[Tuple[str, List[Artifact]], Error]:
        record = params
        field = record.typegraph_path
        field0 = record.prefix
        field1 = record.artifact_resolution
        field2 = record.codegen
        field3 = record.prisma_migration
        field4 = record.pretty
        ptr, len5 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        if field0 is None:
            variant = 0
            variant9 = 0
            variant10 = 0
        else:
            payload6 = field0
            ptr7, len8 = _encode_utf8(payload6, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant9 = ptr7
            variant10 = len8
        record11 = field3
        field12 = record11.migrations_dir
        field13 = record11.migration_actions
        field14 = record11.default_migration_action
        ptr15, len16 = _encode_utf8(field12, self.component._realloc0, self.component._core_memory0, caller)
        vec = field13
        len25 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len25 * 12)
        assert(isinstance(result, int))
        for i26 in range(0, len25):
            e = vec[i26]
            base17 = result + i26 * 12
            (tuplei,tuplei18,) = e
            ptr19, len20 = _encode_utf8(tuplei, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base17, 4, len20)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base17, 0, ptr19)
            record21 = tuplei18
            field22 = record21.apply
            field23 = record21.create
            field24 = record21.reset
            _store(ctypes.c_uint8, self.component._core_memory0, caller, base17, 8, int(field22))
            _store(ctypes.c_uint8, self.component._core_memory0, caller, base17, 9, int(field23))
            _store(ctypes.c_uint8, self.component._core_memory0, caller, base17, 10, int(field24))
        record27 = field14
        field28 = record27.apply
        field29 = record27.create
        field30 = record27.reset
        ret = self.component.lift_callee1(caller, ptr, len5, variant, variant9, variant10, int(field1), int(field2), ptr15, len16, result, len25, int(field28), int(field29), int(field30), int(field4))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[Tuple[str, List[Artifact]], Error]
        if load == 0:
            load31 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load32 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr33 = load31
            len34 = load32
            list = _decode_utf8(self.component._core_memory0, caller, ptr33, len34)
            load35 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            load36 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 16)
            ptr49 = load35
            len50 = load36
            result51: List[Artifact] = []
            for i52 in range(0, len50):
                base37 = ptr49 + i52 * 20
                load38 = _load(ctypes.c_int32, self.component._core_memory0, caller, base37, 0)
                load39 = _load(ctypes.c_int32, self.component._core_memory0, caller, base37, 4)
                ptr40 = load38
                len41 = load39
                list42 = _decode_utf8(self.component._core_memory0, caller, ptr40, len41)
                load43 = _load(ctypes.c_int32, self.component._core_memory0, caller, base37, 8)
                load44 = _load(ctypes.c_int32, self.component._core_memory0, caller, base37, 12)
                ptr45 = load43
                len46 = load44
                list47 = _decode_utf8(self.component._core_memory0, caller, ptr45, len46)
                load48 = _load(ctypes.c_int32, self.component._core_memory0, caller, base37, 16)
                result51.append(Artifact(list42, list47, load48 & 0xffffffff))
            expected = Ok((list, result51,))
        elif load == 1:
            load53 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load54 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr61 = load53
            len62 = load54
            result63: List[str] = []
            for i64 in range(0, len62):
                base55 = ptr61 + i64 * 8
                load56 = _load(ctypes.c_int32, self.component._core_memory0, caller, base55, 0)
                load57 = _load(ctypes.c_int32, self.component._core_memory0, caller, base55, 4)
                ptr58 = load56
                len59 = load57
                list60 = _decode_utf8(self.component._core_memory0, caller, ptr58, len59)
                result63.append(list60)
            expected = Err(Error(result63))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return1(caller, ret)
        return expected
    def with_injection(self, caller: wasmtime.Store, type_id: TypeId, injection: str) -> Result[TypeId, Error]:
        ptr, len0 = _encode_utf8(injection, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee2(caller, _clamp(type_id, 0, 4294967295), ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load1 & 0xffffffff)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load2
            len10 = load3
            result: List[str] = []
            for i11 in range(0, len10):
                base4 = ptr9 + i11 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr7 = load5
                len8 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def with_config(self, caller: wasmtime.Store, type_id: TypeId, config: str) -> Result[TypeId, Error]:
        ptr, len0 = _encode_utf8(config, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee3(caller, _clamp(type_id, 0, 4294967295), ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load1 & 0xffffffff)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load2
            len10 = load3
            result: List[str] = []
            for i11 in range(0, len10):
                base4 = ptr9 + i11 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr7 = load5
                len8 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def refb(self, caller: wasmtime.Store, name: str, attributes: Optional[str]) -> Result[TypeId, Error]:
        ptr, len0 = _encode_utf8(name, self.component._realloc0, self.component._core_memory0, caller)
        if attributes is None:
            variant = 0
            variant4 = 0
            variant5 = 0
        else:
            payload1 = attributes
            ptr2, len3 = _encode_utf8(payload1, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant4 = ptr2
            variant5 = len3
        ret = self.component.lift_callee4(caller, ptr, len0, variant, variant4, variant5)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load6 & 0xffffffff)
        elif load == 1:
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr14 = load7
            len15 = load8
            result: List[str] = []
            for i16 in range(0, len15):
                base9 = ptr14 + i16 * 8
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 0)
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 4)
                ptr12 = load10
                len13 = load11
                list = _decode_utf8(self.component._core_memory0, caller, ptr12, len13)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def integerb(self, caller: wasmtime.Store, data: TypeInteger) -> Result[TypeId, Error]:
        record = data
        field = record.min
        field0 = record.max
        field1 = record.exclusive_minimum
        field2 = record.exclusive_maximum
        field3 = record.multiple_of
        field4 = record.enumeration
        if field is None:
            variant = 0
            variant6 = 0
        else:
            payload5 = field
            variant = 1
            variant6 = _clamp(payload5, -2147483648, 2147483647)
        if field0 is None:
            variant9 = 0
            variant10 = 0
        else:
            payload8 = field0
            variant9 = 1
            variant10 = _clamp(payload8, -2147483648, 2147483647)
        if field1 is None:
            variant13 = 0
            variant14 = 0
        else:
            payload12 = field1
            variant13 = 1
            variant14 = _clamp(payload12, -2147483648, 2147483647)
        if field2 is None:
            variant17 = 0
            variant18 = 0
        else:
            payload16 = field2
            variant17 = 1
            variant18 = _clamp(payload16, -2147483648, 2147483647)
        if field3 is None:
            variant21 = 0
            variant22 = 0
        else:
            payload20 = field3
            variant21 = 1
            variant22 = _clamp(payload20, -2147483648, 2147483647)
        if field4 is None:
            variant26 = 0
            variant27 = 0
            variant28 = 0
        else:
            payload24 = field4
            ptr, len25 = _list_canon_lower(payload24, ctypes.c_int32, 4, 4, self.component._realloc0, self.component._core_memory0, caller)
            variant26 = 1
            variant27 = ptr
            variant28 = len25
        ret = self.component.lift_callee5(caller, variant, variant6, variant9, variant10, variant13, variant14, variant17, variant18, variant21, variant22, variant26, variant27, variant28)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load29 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load29 & 0xffffffff)
        elif load == 1:
            load30 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load31 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr37 = load30
            len38 = load31
            result: List[str] = []
            for i39 in range(0, len38):
                base32 = ptr37 + i39 * 8
                load33 = _load(ctypes.c_int32, self.component._core_memory0, caller, base32, 0)
                load34 = _load(ctypes.c_int32, self.component._core_memory0, caller, base32, 4)
                ptr35 = load33
                len36 = load34
                list = _decode_utf8(self.component._core_memory0, caller, ptr35, len36)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def floatb(self, caller: wasmtime.Store, data: TypeFloat) -> Result[TypeId, Error]:
        record = data
        field = record.min
        field0 = record.max
        field1 = record.exclusive_minimum
        field2 = record.exclusive_maximum
        field3 = record.multiple_of
        field4 = record.enumeration
        if field is None:
            variant = 0
            variant6 = 0.0
        else:
            payload5 = field
            variant = 1
            variant6 = payload5
        if field0 is None:
            variant9 = 0
            variant10 = 0.0
        else:
            payload8 = field0
            variant9 = 1
            variant10 = payload8
        if field1 is None:
            variant13 = 0
            variant14 = 0.0
        else:
            payload12 = field1
            variant13 = 1
            variant14 = payload12
        if field2 is None:
            variant17 = 0
            variant18 = 0.0
        else:
            payload16 = field2
            variant17 = 1
            variant18 = payload16
        if field3 is None:
            variant21 = 0
            variant22 = 0.0
        else:
            payload20 = field3
            variant21 = 1
            variant22 = payload20
        if field4 is None:
            variant26 = 0
            variant27 = 0
            variant28 = 0
        else:
            payload24 = field4
            ptr, len25 = _list_canon_lower(payload24, ctypes.c_double, 8, 8, self.component._realloc0, self.component._core_memory0, caller)
            variant26 = 1
            variant27 = ptr
            variant28 = len25
        ret = self.component.lift_callee6(caller, variant, variant6, variant9, variant10, variant13, variant14, variant17, variant18, variant21, variant22, variant26, variant27, variant28)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load29 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load29 & 0xffffffff)
        elif load == 1:
            load30 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load31 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr37 = load30
            len38 = load31
            result: List[str] = []
            for i39 in range(0, len38):
                base32 = ptr37 + i39 * 8
                load33 = _load(ctypes.c_int32, self.component._core_memory0, caller, base32, 0)
                load34 = _load(ctypes.c_int32, self.component._core_memory0, caller, base32, 4)
                ptr35 = load33
                len36 = load34
                list = _decode_utf8(self.component._core_memory0, caller, ptr35, len36)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def booleanb(self, caller: wasmtime.Store) -> Result[TypeId, Error]:
        ret = self.component.lift_callee7(caller)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load0 & 0xffffffff)
        elif load == 1:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr7 = load1
            len8 = load2
            result: List[str] = []
            for i9 in range(0, len8):
                base3 = ptr7 + i9 * 8
                load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, base3, 0)
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base3, 4)
                ptr = load4
                len6 = load5
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len6)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def stringb(self, caller: wasmtime.Store, data: TypeString) -> Result[TypeId, Error]:
        record = data
        field = record.min
        field0 = record.max
        field1 = record.format
        field2 = record.pattern
        field3 = record.enumeration
        if field is None:
            variant = 0
            variant5 = 0
        else:
            payload4 = field
            variant = 1
            variant5 = _clamp(payload4, 0, 4294967295)
        if field0 is None:
            variant8 = 0
            variant9 = 0
        else:
            payload7 = field0
            variant8 = 1
            variant9 = _clamp(payload7, 0, 4294967295)
        if field1 is None:
            variant13 = 0
            variant14 = 0
            variant15 = 0
        else:
            payload11 = field1
            ptr, len12 = _encode_utf8(payload11, self.component._realloc0, self.component._core_memory0, caller)
            variant13 = 1
            variant14 = ptr
            variant15 = len12
        if field2 is None:
            variant20 = 0
            variant21 = 0
            variant22 = 0
        else:
            payload17 = field2
            ptr18, len19 = _encode_utf8(payload17, self.component._realloc0, self.component._core_memory0, caller)
            variant20 = 1
            variant21 = ptr18
            variant22 = len19
        if field3 is None:
            variant30 = 0
            variant31 = 0
            variant32 = 0
        else:
            payload24 = field3
            vec = payload24
            len28 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len28 * 8)
            assert(isinstance(result, int))
            for i29 in range(0, len28):
                e = vec[i29]
                base25 = result + i29 * 8
                ptr26, len27 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base25, 4, len27)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base25, 0, ptr26)
            variant30 = 1
            variant31 = result
            variant32 = len28
        ret = self.component.lift_callee8(caller, variant, variant5, variant8, variant9, variant13, variant14, variant15, variant20, variant21, variant22, variant30, variant31, variant32)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load33 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load33 & 0xffffffff)
        elif load == 1:
            load34 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load35 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr41 = load34
            len42 = load35
            result43: List[str] = []
            for i44 in range(0, len42):
                base36 = ptr41 + i44 * 8
                load37 = _load(ctypes.c_int32, self.component._core_memory0, caller, base36, 0)
                load38 = _load(ctypes.c_int32, self.component._core_memory0, caller, base36, 4)
                ptr39 = load37
                len40 = load38
                list = _decode_utf8(self.component._core_memory0, caller, ptr39, len40)
                result43.append(list)
            expected = Err(Error(result43))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def as_id(self, caller: wasmtime.Store, id: TypeId, composite: bool) -> Result[TypeId, Error]:
        ret = self.component.lift_callee9(caller, _clamp(id, 0, 4294967295), int(composite))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load0 & 0xffffffff)
        elif load == 1:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr7 = load1
            len8 = load2
            result: List[str] = []
            for i9 in range(0, len8):
                base3 = ptr7 + i9 * 8
                load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, base3, 0)
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base3, 4)
                ptr = load4
                len6 = load5
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len6)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def fileb(self, caller: wasmtime.Store, data: TypeFile) -> Result[TypeId, Error]:
        record = data
        field = record.min
        field0 = record.max
        field1 = record.allow
        if field is None:
            variant = 0
            variant3 = 0
        else:
            payload2 = field
            variant = 1
            variant3 = _clamp(payload2, 0, 4294967295)
        if field0 is None:
            variant6 = 0
            variant7 = 0
        else:
            payload5 = field0
            variant6 = 1
            variant7 = _clamp(payload5, 0, 4294967295)
        if field1 is None:
            variant14 = 0
            variant15 = 0
            variant16 = 0
        else:
            payload9 = field1
            vec = payload9
            len12 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len12 * 8)
            assert(isinstance(result, int))
            for i13 in range(0, len12):
                e = vec[i13]
                base10 = result + i13 * 8
                ptr, len11 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base10, 4, len11)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base10, 0, ptr)
            variant14 = 1
            variant15 = result
            variant16 = len12
        ret = self.component.lift_callee10(caller, variant, variant3, variant6, variant7, variant14, variant15, variant16)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load17 & 0xffffffff)
        elif load == 1:
            load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load19 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr25 = load18
            len26 = load19
            result27: List[str] = []
            for i28 in range(0, len26):
                base20 = ptr25 + i28 * 8
                load21 = _load(ctypes.c_int32, self.component._core_memory0, caller, base20, 0)
                load22 = _load(ctypes.c_int32, self.component._core_memory0, caller, base20, 4)
                ptr23 = load21
                len24 = load22
                list = _decode_utf8(self.component._core_memory0, caller, ptr23, len24)
                result27.append(list)
            expected = Err(Error(result27))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def listb(self, caller: wasmtime.Store, data: TypeList) -> Result[TypeId, Error]:
        record = data
        field = record.of
        field0 = record.min
        field1 = record.max
        field2 = record.unique_items
        if field0 is None:
            variant = 0
            variant4 = 0
        else:
            payload3 = field0
            variant = 1
            variant4 = _clamp(payload3, 0, 4294967295)
        if field1 is None:
            variant7 = 0
            variant8 = 0
        else:
            payload6 = field1
            variant7 = 1
            variant8 = _clamp(payload6, 0, 4294967295)
        if field2 is None:
            variant11 = 0
            variant12 = 0
        else:
            payload10 = field2
            variant11 = 1
            variant12 = int(payload10)
        ret = self.component.lift_callee11(caller, _clamp(field, 0, 4294967295), variant, variant4, variant7, variant8, variant11, variant12)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load13 & 0xffffffff)
        elif load == 1:
            load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr20 = load14
            len21 = load15
            result: List[str] = []
            for i22 in range(0, len21):
                base16 = ptr20 + i22 * 8
                load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 0)
                load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 4)
                ptr = load17
                len19 = load18
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len19)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def optionalb(self, caller: wasmtime.Store, data: TypeOptional) -> Result[TypeId, Error]:
        record = data
        field = record.of
        field0 = record.default_item
        if field0 is None:
            variant = 0
            variant3 = 0
            variant4 = 0
        else:
            payload1 = field0
            ptr, len2 = _encode_utf8(payload1, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant3 = ptr
            variant4 = len2
        ret = self.component.lift_callee12(caller, _clamp(field, 0, 4294967295), variant, variant3, variant4)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load5 & 0xffffffff)
        elif load == 1:
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr13 = load6
            len14 = load7
            result: List[str] = []
            for i15 in range(0, len14):
                base8 = ptr13 + i15 * 8
                load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, base8, 0)
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base8, 4)
                ptr11 = load9
                len12 = load10
                list = _decode_utf8(self.component._core_memory0, caller, ptr11, len12)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def unionb(self, caller: wasmtime.Store, data: TypeUnion) -> Result[TypeId, Error]:
        record = data
        field = record.variants
        ptr, len0 = _list_canon_lower(field, ctypes.c_uint32, 4, 4, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee13(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load1 & 0xffffffff)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load2
            len10 = load3
            result: List[str] = []
            for i11 in range(0, len10):
                base4 = ptr9 + i11 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr7 = load5
                len8 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def eitherb(self, caller: wasmtime.Store, data: TypeEither) -> Result[TypeId, Error]:
        record = data
        field = record.variants
        ptr, len0 = _list_canon_lower(field, ctypes.c_uint32, 4, 4, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee14(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load1 & 0xffffffff)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load2
            len10 = load3
            result: List[str] = []
            for i11 in range(0, len10):
                base4 = ptr9 + i11 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr7 = load5
                len8 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def structb(self, caller: wasmtime.Store, data: TypeStruct) -> Result[TypeId, Error]:
        record = data
        field = record.props
        field0 = record.additional_props
        field1 = record.min
        field2 = record.max
        field3 = record.enumeration
        vec = field
        len7 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len7 * 12)
        assert(isinstance(result, int))
        for i8 in range(0, len7):
            e = vec[i8]
            base4 = result + i8 * 12
            (tuplei,tuplei5,) = e
            ptr, len6 = _encode_utf8(tuplei, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base4, 4, len6)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base4, 0, ptr)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base4, 8, _clamp(tuplei5, 0, 4294967295))
        if field1 is None:
            variant = 0
            variant10 = 0
        else:
            payload9 = field1
            variant = 1
            variant10 = _clamp(payload9, 0, 4294967295)
        if field2 is None:
            variant13 = 0
            variant14 = 0
        else:
            payload12 = field2
            variant13 = 1
            variant14 = _clamp(payload12, 0, 4294967295)
        if field3 is None:
            variant25 = 0
            variant26 = 0
            variant27 = 0
        else:
            payload16 = field3
            vec21 = payload16
            len23 = len(vec21)
            result22 = self.component._realloc0(caller, 0, 0, 4, len23 * 8)
            assert(isinstance(result22, int))
            for i24 in range(0, len23):
                e17 = vec21[i24]
                base18 = result22 + i24 * 8
                ptr19, len20 = _encode_utf8(e17, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base18, 4, len20)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base18, 0, ptr19)
            variant25 = 1
            variant26 = result22
            variant27 = len23
        ret = self.component.lift_callee15(caller, result, len7, int(field0), variant, variant10, variant13, variant14, variant25, variant26, variant27)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load28 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load28 & 0xffffffff)
        elif load == 1:
            load29 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load30 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr36 = load29
            len37 = load30
            result38: List[str] = []
            for i39 in range(0, len37):
                base31 = ptr36 + i39 * 8
                load32 = _load(ctypes.c_int32, self.component._core_memory0, caller, base31, 0)
                load33 = _load(ctypes.c_int32, self.component._core_memory0, caller, base31, 4)
                ptr34 = load32
                len35 = load33
                list = _decode_utf8(self.component._core_memory0, caller, ptr34, len35)
                result38.append(list)
            expected = Err(Error(result38))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def extend_struct(self, caller: wasmtime.Store, tpe: TypeId, props: List[Tuple[str, TypeId]]) -> Result[TypeId, Error]:
        vec = props
        len3 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len3 * 12)
        assert(isinstance(result, int))
        for i4 in range(0, len3):
            e = vec[i4]
            base0 = result + i4 * 12
            (tuplei,tuplei1,) = e
            ptr, len2 = _encode_utf8(tuplei, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 4, len2)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 0, ptr)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 8, _clamp(tuplei1, 0, 4294967295))
        ret = self.component.lift_callee16(caller, _clamp(tpe, 0, 4294967295), result, len3)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load5 & 0xffffffff)
        elif load == 1:
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr13 = load6
            len14 = load7
            result15: List[str] = []
            for i16 in range(0, len14):
                base8 = ptr13 + i16 * 8
                load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, base8, 0)
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base8, 4)
                ptr11 = load9
                len12 = load10
                list = _decode_utf8(self.component._core_memory0, caller, ptr11, len12)
                result15.append(list)
            expected = Err(Error(result15))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def get_type_repr(self, caller: wasmtime.Store, id: TypeId) -> Result[str, Error]:
        ret = self.component.lift_callee17(caller, _clamp(id, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[str, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr = load0
            len2 = load1
            list = _decode_utf8(self.component._core_memory0, caller, ptr, len2)
            expected = Ok(list)
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr11 = load3
            len12 = load4
            result: List[str] = []
            for i13 in range(0, len12):
                base5 = ptr11 + i13 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr8 = load6
                len9 = load7
                list10 = _decode_utf8(self.component._core_memory0, caller, ptr8, len9)
                result.append(list10)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return2(caller, ret)
        return expected
    def funcb(self, caller: wasmtime.Store, data: TypeFunc) -> Result[TypeId, Error]:
        record = data
        field = record.inp
        field0 = record.parameter_transform
        field1 = record.out
        field2 = record.mat
        field3 = record.rate_calls
        field4 = record.rate_weight
        if field0 is None:
            variant = 0
            variant10 = 0
            variant11 = 0
            variant12 = 0
        else:
            payload5 = field0
            record6 = payload5
            field7 = record6.resolver_input
            field8 = record6.transform_tree
            ptr, len9 = _encode_utf8(field8, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant10 = _clamp(field7, 0, 4294967295)
            variant11 = ptr
            variant12 = len9
        if field4 is None:
            variant15 = 0
            variant16 = 0
        else:
            payload14 = field4
            variant15 = 1
            variant16 = _clamp(payload14, 0, 4294967295)
        ret = self.component.lift_callee18(caller, _clamp(field, 0, 4294967295), variant, variant10, variant11, variant12, _clamp(field1, 0, 4294967295), _clamp(field2, 0, 4294967295), int(field3), variant15, variant16)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load17 & 0xffffffff)
        elif load == 1:
            load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load19 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr25 = load18
            len26 = load19
            result: List[str] = []
            for i27 in range(0, len26):
                base20 = ptr25 + i27 * 8
                load21 = _load(ctypes.c_int32, self.component._core_memory0, caller, base20, 0)
                load22 = _load(ctypes.c_int32, self.component._core_memory0, caller, base20, 4)
                ptr23 = load21
                len24 = load22
                list = _decode_utf8(self.component._core_memory0, caller, ptr23, len24)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def get_transform_data(self, caller: wasmtime.Store, resolver_input: TypeId, transform_tree: str) -> Result[TransformData, Error]:
        ptr, len0 = _encode_utf8(transform_tree, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee19(caller, _clamp(resolver_input, 0, 4294967295), ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TransformData, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 16)
            ptr5 = load3
            len6 = load4
            list = _decode_utf8(self.component._core_memory0, caller, ptr5, len6)
            expected = Ok(TransformData(load1 & 0xffffffff, ParameterTransform(load2 & 0xffffffff, list)))
        elif load == 1:
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr15 = load7
            len16 = load8
            result: List[str] = []
            for i17 in range(0, len16):
                base9 = ptr15 + i17 * 8
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 0)
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 4)
                ptr12 = load10
                len13 = load11
                list14 = _decode_utf8(self.component._core_memory0, caller, ptr12, len13)
                result.append(list14)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return3(caller, ret)
        return expected
    def register_policy(self, caller: wasmtime.Store, pol: Policy) -> Result[PolicyId, Error]:
        record = pol
        field = record.name
        field0 = record.materializer
        ptr, len1 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee20(caller, ptr, len1, _clamp(field0, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[PolicyId, Error]
        if load == 0:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load2 & 0xffffffff)
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr10 = load3
            len11 = load4
            result: List[str] = []
            for i12 in range(0, len11):
                base5 = ptr10 + i12 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr8 = load6
                len9 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr8, len9)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def with_policy(self, caller: wasmtime.Store, type_id: TypeId, policy_chain: List[PolicySpec]) -> Result[TypeId, Error]:
        vec = policy_chain
        len13 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len13 * 36)
        assert(isinstance(result, int))
        for i14 in range(0, len13):
            e = vec[i14]
            base0 = result + i14 * 36
            if isinstance(e, PolicySpecSimple):
                payload = e.value
                _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 0, 0)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 4, _clamp(payload, 0, 4294967295))
            elif isinstance(e, PolicySpecPerEffect):
                payload1 = e.value
                _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 0, 1)
                record = payload1
                field = record.read
                field2 = record.create
                field3 = record.update
                field4 = record.delete
                if field is None:
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 4, 0)
                else:
                    payload6 = field
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 4, 1)
                    _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 8, _clamp(payload6, 0, 4294967295))
                if field2 is None:
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 12, 0)
                else:
                    payload8 = field2
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 12, 1)
                    _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 16, _clamp(payload8, 0, 4294967295))
                if field3 is None:
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 20, 0)
                else:
                    payload10 = field3
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 20, 1)
                    _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 24, _clamp(payload10, 0, 4294967295))
                if field4 is None:
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 28, 0)
                else:
                    payload12 = field4
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 28, 1)
                    _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 32, _clamp(payload12, 0, 4294967295))
            else:
                raise TypeError("invalid variant specified for PolicySpec")
        ret = self.component.lift_callee21(caller, _clamp(type_id, 0, 4294967295), result, len13)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load15 & 0xffffffff)
        elif load == 1:
            load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr22 = load16
            len23 = load17
            result24: List[str] = []
            for i25 in range(0, len23):
                base18 = ptr22 + i25 * 8
                load19 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 0)
                load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 4)
                ptr = load19
                len21 = load20
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len21)
                result24.append(list)
            expected = Err(Error(result24))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def get_public_policy(self, caller: wasmtime.Store) -> Result[Tuple[PolicyId, str], Error]:
        ret = self.component.lift_callee22(caller)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[Tuple[PolicyId, str], Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            ptr = load1
            len3 = load2
            list = _decode_utf8(self.component._core_memory0, caller, ptr, len3)
            expected = Ok((load0 & 0xffffffff, list,))
        elif load == 1:
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr12 = load4
            len13 = load5
            result: List[str] = []
            for i14 in range(0, len13):
                base6 = ptr12 + i14 * 8
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base6, 0)
                load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, base6, 4)
                ptr9 = load7
                len10 = load8
                list11 = _decode_utf8(self.component._core_memory0, caller, ptr9, len10)
                result.append(list11)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return4(caller, ret)
        return expected
    def get_internal_policy(self, caller: wasmtime.Store) -> Result[Tuple[PolicyId, str], Error]:
        ret = self.component.lift_callee23(caller)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[Tuple[PolicyId, str], Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            ptr = load1
            len3 = load2
            list = _decode_utf8(self.component._core_memory0, caller, ptr, len3)
            expected = Ok((load0 & 0xffffffff, list,))
        elif load == 1:
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr12 = load4
            len13 = load5
            result: List[str] = []
            for i14 in range(0, len13):
                base6 = ptr12 + i14 * 8
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base6, 0)
                load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, base6, 4)
                ptr9 = load7
                len10 = load8
                list11 = _decode_utf8(self.component._core_memory0, caller, ptr9, len10)
                result.append(list11)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return4(caller, ret)
        return expected
    def register_context_policy(self, caller: wasmtime.Store, key: str, check: ContextCheck) -> Result[Tuple[PolicyId, str], Error]:
        ptr, len0 = _encode_utf8(key, self.component._realloc0, self.component._core_memory0, caller)
        if isinstance(check, ContextCheckNotNull):
            variant = 0
            variant7 = 0
            variant8 = 0
        elif isinstance(check, ContextCheckValue):
            payload1 = check.value
            ptr2, len3 = _encode_utf8(payload1, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant7 = ptr2
            variant8 = len3
        elif isinstance(check, ContextCheckPattern):
            payload4 = check.value
            ptr5, len6 = _encode_utf8(payload4, self.component._realloc0, self.component._core_memory0, caller)
            variant = 2
            variant7 = ptr5
            variant8 = len6
        else:
            raise TypeError("invalid variant specified for ContextCheck")
        ret = self.component.lift_callee24(caller, ptr, len0, variant, variant7, variant8)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[Tuple[PolicyId, str], Error]
        if load == 0:
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            ptr12 = load10
            len13 = load11
            list = _decode_utf8(self.component._core_memory0, caller, ptr12, len13)
            expected = Ok((load9 & 0xffffffff, list,))
        elif load == 1:
            load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr22 = load14
            len23 = load15
            result: List[str] = []
            for i24 in range(0, len23):
                base16 = ptr22 + i24 * 8
                load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 0)
                load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 4)
                ptr19 = load17
                len20 = load18
                list21 = _decode_utf8(self.component._core_memory0, caller, ptr19, len20)
                result.append(list21)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return4(caller, ret)
        return expected
    def rename_type(self, caller: wasmtime.Store, tpe: TypeId, new_name: str) -> Result[TypeId, Error]:
        ptr, len0 = _encode_utf8(new_name, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee25(caller, _clamp(tpe, 0, 4294967295), ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load1 & 0xffffffff)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load2
            len10 = load3
            result: List[str] = []
            for i11 in range(0, len10):
                base4 = ptr9 + i11 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr7 = load5
                len8 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def expose(self, caller: wasmtime.Store, fns: List[Tuple[str, TypeId]], default_policy: Optional[List[PolicySpec]]) -> Result[None, Error]:
        vec = fns
        len3 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len3 * 12)
        assert(isinstance(result, int))
        for i4 in range(0, len3):
            e = vec[i4]
            base0 = result + i4 * 12
            (tuplei,tuplei1,) = e
            ptr, len2 = _encode_utf8(tuplei, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 4, len2)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 0, ptr)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 8, _clamp(tuplei1, 0, 4294967295))
        if default_policy is None:
            variant = 0
            variant25 = 0
            variant26 = 0
        else:
            payload5 = default_policy
            vec21 = payload5
            len23 = len(vec21)
            result22 = self.component._realloc0(caller, 0, 0, 4, len23 * 36)
            assert(isinstance(result22, int))
            for i24 in range(0, len23):
                e6 = vec21[i24]
                base7 = result22 + i24 * 36
                if isinstance(e6, PolicySpecSimple):
                    payload8 = e6.value
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 0, 0)
                    _store(ctypes.c_uint32, self.component._core_memory0, caller, base7, 4, _clamp(payload8, 0, 4294967295))
                elif isinstance(e6, PolicySpecPerEffect):
                    payload9 = e6.value
                    _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 0, 1)
                    record = payload9
                    field = record.read
                    field10 = record.create
                    field11 = record.update
                    field12 = record.delete
                    if field is None:
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 4, 0)
                    else:
                        payload14 = field
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 4, 1)
                        _store(ctypes.c_uint32, self.component._core_memory0, caller, base7, 8, _clamp(payload14, 0, 4294967295))
                    if field10 is None:
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 12, 0)
                    else:
                        payload16 = field10
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 12, 1)
                        _store(ctypes.c_uint32, self.component._core_memory0, caller, base7, 16, _clamp(payload16, 0, 4294967295))
                    if field11 is None:
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 20, 0)
                    else:
                        payload18 = field11
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 20, 1)
                        _store(ctypes.c_uint32, self.component._core_memory0, caller, base7, 24, _clamp(payload18, 0, 4294967295))
                    if field12 is None:
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 28, 0)
                    else:
                        payload20 = field12
                        _store(ctypes.c_uint8, self.component._core_memory0, caller, base7, 28, 1)
                        _store(ctypes.c_uint32, self.component._core_memory0, caller, base7, 32, _clamp(payload20, 0, 4294967295))
                else:
                    raise TypeError("invalid variant specified for PolicySpec")
            variant = 1
            variant25 = result22
            variant26 = len23
        ret = self.component.lift_callee26(caller, result, len3, variant, variant25, variant26)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[None, Error]
        if load == 0:
            expected = Ok(None)
        elif load == 1:
            load27 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load28 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr34 = load27
            len35 = load28
            result36: List[str] = []
            for i37 in range(0, len35):
                base29 = ptr34 + i37 * 8
                load30 = _load(ctypes.c_int32, self.component._core_memory0, caller, base29, 0)
                load31 = _load(ctypes.c_int32, self.component._core_memory0, caller, base29, 4)
                ptr32 = load30
                len33 = load31
                list = _decode_utf8(self.component._core_memory0, caller, ptr32, len33)
                result36.append(list)
            expected = Err(Error(result36))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def set_seed(self, caller: wasmtime.Store, seed: Optional[int]) -> Result[None, Error]:
        if seed is None:
            variant = 0
            variant1 = 0
        else:
            payload0 = seed
            variant = 1
            variant1 = _clamp(payload0, 0, 4294967295)
        ret = self.component.lift_callee27(caller, variant, variant1)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[None, Error]
        if load == 0:
            expected = Ok(None)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr8 = load2
            len9 = load3
            result: List[str] = []
            for i10 in range(0, len9):
                base4 = ptr8 + i10 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr = load5
                len7 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len7)
                result.append(list)
            expected = Err(Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    