from ..exports import core
from ..intrinsics import _clamp, _decode_utf8, _encode_utf8, _load, _store
from ..types import Err, Ok, Result
import ctypes
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple, Union
import wasmtime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .. import Root

Error = core.Error
TypeId = core.TypeId
FuncParams = core.FuncParams
RuntimeId = core.RuntimeId
MaterializerId = core.MaterializerId
Artifact = core.Artifact
Idempotency = bool
@dataclass
class EffectRead:
    pass

@dataclass
class EffectCreate:
    value: Idempotency

@dataclass
class EffectUpdate:
    value: Idempotency

@dataclass
class EffectDelete:
    value: Idempotency

Effect = Union[EffectRead, EffectCreate, EffectUpdate, EffectDelete]

@dataclass
class BaseMaterializer:
    runtime: RuntimeId
    effect: Effect

@dataclass
class MaterializerDenoFunc:
    code: str
    secrets: List[str]

@dataclass
class MaterializerDenoStatic:
    value: str

@dataclass
class MaterializerDenoPredefined:
    name: str
    param: Optional[str]

@dataclass
class MaterializerDenoImport:
    func_name: str
    module: str
    deps: List[str]
    secrets: List[str]

@dataclass
class GraphqlRuntimeData:
    endpoint: str

@dataclass
class MaterializerGraphqlQuery:
    path: Optional[List[str]]

@dataclass
class HttpRuntimeData:
    endpoint: str
    cert_secret: Optional[str]
    basic_auth_secret: Optional[str]

class HttpMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    PATCH = 3
    DELETE = 4

@dataclass
class MaterializerHttpRequest:
    method: HttpMethod
    path: str
    content_type: Optional[str]
    header_prefix: Optional[str]
    query_fields: Optional[List[str]]
    rename_fields: Optional[List[Tuple[str, str]]]
    body_fields: Optional[List[str]]
    auth_token_field: Optional[str]

@dataclass
class MaterializerPythonDef:
    runtime: RuntimeId
    name: str
    fn: str

@dataclass
class MaterializerPythonLambda:
    runtime: RuntimeId
    fn: str

@dataclass
class MaterializerPythonModule:
    runtime: RuntimeId
    file: str
    deps: List[str]

@dataclass
class MaterializerPythonImport:
    module: int
    func_name: str
    secrets: List[str]

@dataclass
class RandomRuntimeData:
    seed: Optional[int]
    reset: Optional[str]

@dataclass
class MaterializerRandom:
    runtime: RuntimeId

@dataclass
class WasmRuntimeData:
    wasm_artifact: str

@dataclass
class MaterializerWasmReflectedFunc:
    func_name: str

@dataclass
class MaterializerWasmWireHandler:
    func_name: str

@dataclass
class PrismaRuntimeData:
    name: str
    connection_string_secret: str

@dataclass
class PrismaLinkData:
    target_type: TypeId
    relationship_name: Optional[str]
    foreign_key: Optional[bool]
    target_field: Optional[str]
    unique: Optional[bool]

class PrismaMigrationOperation(Enum):
    DIFF = 0
    CREATE = 1
    APPLY = 2
    DEPLOY = 3
    RESET = 4

@dataclass
class TemporalRuntimeData:
    name: str
    host_secret: str
    namespace_secret: Optional[str]

@dataclass
class TemporalOperationTypeStartWorkflow:
    pass

@dataclass
class TemporalOperationTypeSignalWorkflow:
    pass

@dataclass
class TemporalOperationTypeQueryWorkflow:
    pass

@dataclass
class TemporalOperationTypeDescribeWorkflow:
    pass

TemporalOperationType = Union[TemporalOperationTypeStartWorkflow, TemporalOperationTypeSignalWorkflow, TemporalOperationTypeQueryWorkflow, TemporalOperationTypeDescribeWorkflow]

@dataclass
class TemporalOperationData:
    mat_arg: Optional[str]
    func_arg: Optional[TypeId]
    func_out: Optional[TypeId]
    operation: TemporalOperationType

class TypegateOperation(Enum):
    LIST_TYPEGRAPHS = 0
    FIND_TYPEGRAPH = 1
    ADD_TYPEGRAPH = 2
    REMOVE_TYPEGRAPHS = 3
    GET_SERIALIZED_TYPEGRAPH = 4
    GET_ARG_INFO_BY_PATH = 5
    FIND_AVAILABLE_OPERATIONS = 6
    FIND_PRISMA_MODELS = 7
    RAW_PRISMA_READ = 8
    RAW_PRISMA_CREATE = 9
    RAW_PRISMA_UPDATE = 10
    RAW_PRISMA_DELETE = 11
    QUERY_PRISMA_MODEL = 12
    PING = 13

class TypegraphOperation(Enum):
    RESOLVER = 0
    GET_TYPE = 1
    GET_SCHEMA = 2

@dataclass
class RedisBackend:
    connection_string_secret: str

@dataclass
class SubstantialBackendMemory:
    pass

@dataclass
class SubstantialBackendFs:
    pass

@dataclass
class SubstantialBackendRedis:
    value: RedisBackend

SubstantialBackend = Union[SubstantialBackendMemory, SubstantialBackendFs, SubstantialBackendRedis]

class WorkflowKind(Enum):
    PYTHON = 0
    DENO = 1

@dataclass
class WorkflowFileDescription:
    workflows: List[str]
    file: str
    deps: List[str]
    kind: WorkflowKind

@dataclass
class SubstantialRuntimeData:
    backend: SubstantialBackend
    file_descriptions: List[WorkflowFileDescription]

@dataclass
class SubstantialStartData:
    func_arg: Optional[TypeId]
    secrets: List[str]

@dataclass
class SubstantialOperationDataStart:
    value: SubstantialStartData

@dataclass
class SubstantialOperationDataStartRaw:
    value: SubstantialStartData

@dataclass
class SubstantialOperationDataStop:
    pass

@dataclass
class SubstantialOperationDataSend:
    value: TypeId

@dataclass
class SubstantialOperationDataSendRaw:
    pass

@dataclass
class SubstantialOperationDataResources:
    pass

@dataclass
class SubstantialOperationDataResults:
    value: TypeId

@dataclass
class SubstantialOperationDataResultsRaw:
    pass

@dataclass
class SubstantialOperationDataInternalLinkParentChild:
    pass

@dataclass
class SubstantialOperationDataAdvancedFilters:
    pass

SubstantialOperationData = Union[SubstantialOperationDataStart, SubstantialOperationDataStartRaw, SubstantialOperationDataStop, SubstantialOperationDataSend, SubstantialOperationDataSendRaw, SubstantialOperationDataResources, SubstantialOperationDataResults, SubstantialOperationDataResultsRaw, SubstantialOperationDataInternalLinkParentChild, SubstantialOperationDataAdvancedFilters]

@dataclass
class KvRuntimeData:
    url: str

class KvMaterializer(Enum):
    GET = 0
    SET = 1
    DELETE = 2
    KEYS = 3
    VALUES = 4

@dataclass
class GrpcRuntimeData:
    proto_file: str
    endpoint: str

@dataclass
class GrpcData:
    method: str

class Runtimes:
    component: 'Root'
    
    def __init__(self, component: 'Root') -> None:
        self.component = component
    def get_deno_runtime(self, caller: wasmtime.Store) -> RuntimeId:
        ret = self.component.lift_callee28(caller)
        assert(isinstance(ret, int))
        return ret & 0xffffffff
    def register_deno_func(self, caller: wasmtime.Store, data: MaterializerDenoFunc, effect: Effect) -> Result[MaterializerId, Error]:
        record = data
        field = record.code
        field0 = record.secrets
        ptr, len1 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        vec = field0
        len5 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len5 * 8)
        assert(isinstance(result, int))
        for i6 in range(0, len5):
            e = vec[i6]
            base2 = result + i6 * 8
            ptr3, len4 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base2, 4, len4)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base2, 0, ptr3)
        if isinstance(effect, EffectRead):
            variant = 0
            variant10 = 0
        elif isinstance(effect, EffectCreate):
            payload7 = effect.value
            variant = 1
            variant10 = int(payload7)
        elif isinstance(effect, EffectUpdate):
            payload8 = effect.value
            variant = 2
            variant10 = int(payload8)
        elif isinstance(effect, EffectDelete):
            payload9 = effect.value
            variant = 3
            variant10 = int(payload9)
        else:
            raise TypeError("invalid variant specified for Effect")
        ret = self.component.lift_callee29(caller, ptr, len1, result, len5, variant, variant10)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load11 & 0xffffffff)
        elif load == 1:
            load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr19 = load12
            len20 = load13
            result21: List[str] = []
            for i22 in range(0, len20):
                base14 = ptr19 + i22 * 8
                load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, base14, 0)
                load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, base14, 4)
                ptr17 = load15
                len18 = load16
                list = _decode_utf8(self.component._core_memory0, caller, ptr17, len18)
                result21.append(list)
            expected = Err(core.Error(result21))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_deno_static(self, caller: wasmtime.Store, data: MaterializerDenoStatic, type_id: TypeId) -> Result[MaterializerId, Error]:
        record = data
        field = record.value
        ptr, len0 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee30(caller, ptr, len0, _clamp(type_id, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def get_predefined_deno_func(self, caller: wasmtime.Store, data: MaterializerDenoPredefined) -> Result[MaterializerId, Error]:
        record = data
        field = record.name
        field0 = record.param
        ptr, len1 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        if field0 is None:
            variant = 0
            variant5 = 0
            variant6 = 0
        else:
            payload2 = field0
            ptr3, len4 = _encode_utf8(payload2, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant5 = ptr3
            variant6 = len4
        ret = self.component.lift_callee31(caller, ptr, len1, variant, variant5, variant6)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load7 & 0xffffffff)
        elif load == 1:
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr15 = load8
            len16 = load9
            result: List[str] = []
            for i17 in range(0, len16):
                base10 = ptr15 + i17 * 8
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 0)
                load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 4)
                ptr13 = load11
                len14 = load12
                list = _decode_utf8(self.component._core_memory0, caller, ptr13, len14)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def import_deno_function(self, caller: wasmtime.Store, data: MaterializerDenoImport, effect: Effect) -> Result[MaterializerId, Error]:
        record = data
        field = record.func_name
        field0 = record.module
        field1 = record.deps
        field2 = record.secrets
        ptr, len3 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ptr4, len5 = _encode_utf8(field0, self.component._realloc0, self.component._core_memory0, caller)
        vec = field1
        len9 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len9 * 8)
        assert(isinstance(result, int))
        for i10 in range(0, len9):
            e = vec[i10]
            base6 = result + i10 * 8
            ptr7, len8 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base6, 4, len8)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base6, 0, ptr7)
        vec15 = field2
        len17 = len(vec15)
        result16 = self.component._realloc0(caller, 0, 0, 4, len17 * 8)
        assert(isinstance(result16, int))
        for i18 in range(0, len17):
            e11 = vec15[i18]
            base12 = result16 + i18 * 8
            ptr13, len14 = _encode_utf8(e11, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base12, 4, len14)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base12, 0, ptr13)
        if isinstance(effect, EffectRead):
            variant = 0
            variant22 = 0
        elif isinstance(effect, EffectCreate):
            payload19 = effect.value
            variant = 1
            variant22 = int(payload19)
        elif isinstance(effect, EffectUpdate):
            payload20 = effect.value
            variant = 2
            variant22 = int(payload20)
        elif isinstance(effect, EffectDelete):
            payload21 = effect.value
            variant = 3
            variant22 = int(payload21)
        else:
            raise TypeError("invalid variant specified for Effect")
        ret = self.component.lift_callee32(caller, ptr, len3, ptr4, len5, result, len9, result16, len17, variant, variant22)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load23 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load23 & 0xffffffff)
        elif load == 1:
            load24 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load25 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr31 = load24
            len32 = load25
            result33: List[str] = []
            for i34 in range(0, len32):
                base26 = ptr31 + i34 * 8
                load27 = _load(ctypes.c_int32, self.component._core_memory0, caller, base26, 0)
                load28 = _load(ctypes.c_int32, self.component._core_memory0, caller, base26, 4)
                ptr29 = load27
                len30 = load28
                list = _decode_utf8(self.component._core_memory0, caller, ptr29, len30)
                result33.append(list)
            expected = Err(core.Error(result33))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_graphql_runtime(self, caller: wasmtime.Store, data: GraphqlRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.endpoint
        ptr, len0 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee33(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def graphql_query(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerGraphqlQuery) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.path
        if field6 is None:
            variant13 = 0
            variant14 = 0
            variant15 = 0
        else:
            payload8 = field6
            vec = payload8
            len11 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len11 * 8)
            assert(isinstance(result, int))
            for i12 in range(0, len11):
                e = vec[i12]
                base9 = result + i12 * 8
                ptr, len10 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base9, 4, len10)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base9, 0, ptr)
            variant13 = 1
            variant14 = result
            variant15 = len11
        ret = self.component.lift_callee34(caller, _clamp(field, 0, 4294967295), variant, variant4, variant13, variant14, variant15)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load16 & 0xffffffff)
        elif load == 1:
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr24 = load17
            len25 = load18
            result26: List[str] = []
            for i27 in range(0, len25):
                base19 = ptr24 + i27 * 8
                load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, base19, 0)
                load21 = _load(ctypes.c_int32, self.component._core_memory0, caller, base19, 4)
                ptr22 = load20
                len23 = load21
                list = _decode_utf8(self.component._core_memory0, caller, ptr22, len23)
                result26.append(list)
            expected = Err(core.Error(result26))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def graphql_mutation(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerGraphqlQuery) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.path
        if field6 is None:
            variant13 = 0
            variant14 = 0
            variant15 = 0
        else:
            payload8 = field6
            vec = payload8
            len11 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len11 * 8)
            assert(isinstance(result, int))
            for i12 in range(0, len11):
                e = vec[i12]
                base9 = result + i12 * 8
                ptr, len10 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base9, 4, len10)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base9, 0, ptr)
            variant13 = 1
            variant14 = result
            variant15 = len11
        ret = self.component.lift_callee35(caller, _clamp(field, 0, 4294967295), variant, variant4, variant13, variant14, variant15)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load16 & 0xffffffff)
        elif load == 1:
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr24 = load17
            len25 = load18
            result26: List[str] = []
            for i27 in range(0, len25):
                base19 = ptr24 + i27 * 8
                load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, base19, 0)
                load21 = _load(ctypes.c_int32, self.component._core_memory0, caller, base19, 4)
                ptr22 = load20
                len23 = load21
                list = _decode_utf8(self.component._core_memory0, caller, ptr22, len23)
                result26.append(list)
            expected = Err(core.Error(result26))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_http_runtime(self, caller: wasmtime.Store, data: HttpRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.endpoint
        field0 = record.cert_secret
        field1 = record.basic_auth_secret
        ptr, len2 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        if field0 is None:
            variant = 0
            variant6 = 0
            variant7 = 0
        else:
            payload3 = field0
            ptr4, len5 = _encode_utf8(payload3, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant6 = ptr4
            variant7 = len5
        if field1 is None:
            variant12 = 0
            variant13 = 0
            variant14 = 0
        else:
            payload9 = field1
            ptr10, len11 = _encode_utf8(payload9, self.component._realloc0, self.component._core_memory0, caller)
            variant12 = 1
            variant13 = ptr10
            variant14 = len11
        ret = self.component.lift_callee36(caller, ptr, len2, variant, variant6, variant7, variant12, variant13, variant14)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
        if load == 0:
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load15 & 0xffffffff)
        elif load == 1:
            load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr23 = load16
            len24 = load17
            result: List[str] = []
            for i25 in range(0, len24):
                base18 = ptr23 + i25 * 8
                load19 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 0)
                load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 4)
                ptr21 = load19
                len22 = load20
                list = _decode_utf8(self.component._core_memory0, caller, ptr21, len22)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def http_request(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerHttpRequest) -> Result[MaterializerId, Error]:
        ptr = self.component._realloc0(caller, 0, 0, 4, 92)
        assert(isinstance(ptr, int))
        record = base
        field = record.runtime
        field0 = record.effect
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 0, _clamp(field, 0, 4294967295))
        if isinstance(field0, EffectRead):
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 4, 0)
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 4, 1)
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 5, int(payload1))
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 4, 2)
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 5, int(payload2))
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 4, 3)
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 5, int(payload3))
        else:
            raise TypeError("invalid variant specified for Effect")
        record4 = data
        field5 = record4.method
        field6 = record4.path
        field7 = record4.content_type
        field8 = record4.header_prefix
        field9 = record4.query_fields
        field10 = record4.rename_fields
        field11 = record4.body_fields
        field12 = record4.auth_token_field
        _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 8, (field5).value)
        ptr13, len14 = _encode_utf8(field6, self.component._realloc0, self.component._core_memory0, caller)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 16, len14)
        _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 12, ptr13)
        if field7 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 20, 0)
        else:
            payload16 = field7
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 20, 1)
            ptr17, len18 = _encode_utf8(payload16, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 28, len18)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 24, ptr17)
        if field8 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 32, 0)
        else:
            payload20 = field8
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 32, 1)
            ptr21, len22 = _encode_utf8(payload20, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 40, len22)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 36, ptr21)
        if field9 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 44, 0)
        else:
            payload24 = field9
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 44, 1)
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
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 52, len28)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 48, result)
        if field10 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 56, 0)
        else:
            payload31 = field10
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 56, 1)
            vec39 = payload31
            len41 = len(vec39)
            result40 = self.component._realloc0(caller, 0, 0, 4, len41 * 16)
            assert(isinstance(result40, int))
            for i42 in range(0, len41):
                e32 = vec39[i42]
                base33 = result40 + i42 * 16
                (tuplei,tuplei34,) = e32
                ptr35, len36 = _encode_utf8(tuplei, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base33, 4, len36)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base33, 0, ptr35)
                ptr37, len38 = _encode_utf8(tuplei34, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base33, 12, len38)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base33, 8, ptr37)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 64, len41)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 60, result40)
        if field11 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 68, 0)
        else:
            payload44 = field11
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 68, 1)
            vec49 = payload44
            len51 = len(vec49)
            result50 = self.component._realloc0(caller, 0, 0, 4, len51 * 8)
            assert(isinstance(result50, int))
            for i52 in range(0, len51):
                e45 = vec49[i52]
                base46 = result50 + i52 * 8
                ptr47, len48 = _encode_utf8(e45, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base46, 4, len48)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base46, 0, ptr47)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 76, len51)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 72, result50)
        if field12 is None:
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 80, 0)
        else:
            payload54 = field12
            _store(ctypes.c_uint8, self.component._core_memory0, caller, ptr, 80, 1)
            ptr55, len56 = _encode_utf8(payload54, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 88, len56)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, ptr, 84, ptr55)
        ret = self.component.lift_callee37(caller, ptr)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load57 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load57 & 0xffffffff)
        elif load == 1:
            load58 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load59 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr65 = load58
            len66 = load59
            result67: List[str] = []
            for i68 in range(0, len66):
                base60 = ptr65 + i68 * 8
                load61 = _load(ctypes.c_int32, self.component._core_memory0, caller, base60, 0)
                load62 = _load(ctypes.c_int32, self.component._core_memory0, caller, base60, 4)
                ptr63 = load61
                len64 = load62
                list = _decode_utf8(self.component._core_memory0, caller, ptr63, len64)
                result67.append(list)
            expected = Err(core.Error(result67))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_python_runtime(self, caller: wasmtime.Store) -> Result[RuntimeId, Error]:
        ret = self.component.lift_callee38(caller)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def from_python_lambda(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerPythonLambda) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.runtime
        field7 = record5.fn
        ptr, len8 = _encode_utf8(field7, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee39(caller, _clamp(field, 0, 4294967295), variant, variant4, _clamp(field6, 0, 4294967295), ptr, len8)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load9 & 0xffffffff)
        elif load == 1:
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr17 = load10
            len18 = load11
            result: List[str] = []
            for i19 in range(0, len18):
                base12 = ptr17 + i19 * 8
                load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 0)
                load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 4)
                ptr15 = load13
                len16 = load14
                list = _decode_utf8(self.component._core_memory0, caller, ptr15, len16)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def from_python_def(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerPythonDef) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.runtime
        field7 = record5.name
        field8 = record5.fn
        ptr, len9 = _encode_utf8(field7, self.component._realloc0, self.component._core_memory0, caller)
        ptr10, len11 = _encode_utf8(field8, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee40(caller, _clamp(field, 0, 4294967295), variant, variant4, _clamp(field6, 0, 4294967295), ptr, len9, ptr10, len11)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load12 & 0xffffffff)
        elif load == 1:
            load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr20 = load13
            len21 = load14
            result: List[str] = []
            for i22 in range(0, len21):
                base15 = ptr20 + i22 * 8
                load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, base15, 0)
                load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, base15, 4)
                ptr18 = load16
                len19 = load17
                list = _decode_utf8(self.component._core_memory0, caller, ptr18, len19)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def from_python_module(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerPythonModule) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.runtime
        field7 = record5.file
        field8 = record5.deps
        ptr, len9 = _encode_utf8(field7, self.component._realloc0, self.component._core_memory0, caller)
        vec = field8
        len13 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len13 * 8)
        assert(isinstance(result, int))
        for i14 in range(0, len13):
            e = vec[i14]
            base10 = result + i14 * 8
            ptr11, len12 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base10, 4, len12)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base10, 0, ptr11)
        ret = self.component.lift_callee41(caller, _clamp(field, 0, 4294967295), variant, variant4, _clamp(field6, 0, 4294967295), ptr, len9, result, len13)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load15 & 0xffffffff)
        elif load == 1:
            load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr23 = load16
            len24 = load17
            result25: List[str] = []
            for i26 in range(0, len24):
                base18 = ptr23 + i26 * 8
                load19 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 0)
                load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 4)
                ptr21 = load19
                len22 = load20
                list = _decode_utf8(self.component._core_memory0, caller, ptr21, len22)
                result25.append(list)
            expected = Err(core.Error(result25))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def from_python_import(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerPythonImport) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.module
        field7 = record5.func_name
        field8 = record5.secrets
        ptr, len9 = _encode_utf8(field7, self.component._realloc0, self.component._core_memory0, caller)
        vec = field8
        len13 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len13 * 8)
        assert(isinstance(result, int))
        for i14 in range(0, len13):
            e = vec[i14]
            base10 = result + i14 * 8
            ptr11, len12 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base10, 4, len12)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base10, 0, ptr11)
        ret = self.component.lift_callee42(caller, _clamp(field, 0, 4294967295), variant, variant4, _clamp(field6, 0, 4294967295), ptr, len9, result, len13)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load15 & 0xffffffff)
        elif load == 1:
            load16 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr23 = load16
            len24 = load17
            result25: List[str] = []
            for i26 in range(0, len24):
                base18 = ptr23 + i26 * 8
                load19 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 0)
                load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, base18, 4)
                ptr21 = load19
                len22 = load20
                list = _decode_utf8(self.component._core_memory0, caller, ptr21, len22)
                result25.append(list)
            expected = Err(core.Error(result25))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_random_runtime(self, caller: wasmtime.Store, data: RandomRuntimeData) -> Result[MaterializerId, Error]:
        record = data
        field = record.seed
        field0 = record.reset
        if field is None:
            variant = 0
            variant2 = 0
        else:
            payload1 = field
            variant = 1
            variant2 = _clamp(payload1, 0, 4294967295)
        if field0 is None:
            variant6 = 0
            variant7 = 0
            variant8 = 0
        else:
            payload4 = field0
            ptr, len5 = _encode_utf8(payload4, self.component._realloc0, self.component._core_memory0, caller)
            variant6 = 1
            variant7 = ptr
            variant8 = len5
        ret = self.component.lift_callee43(caller, variant, variant2, variant6, variant7, variant8)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load9 & 0xffffffff)
        elif load == 1:
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr17 = load10
            len18 = load11
            result: List[str] = []
            for i19 in range(0, len18):
                base12 = ptr17 + i19 * 8
                load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 0)
                load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 4)
                ptr15 = load13
                len16 = load14
                list = _decode_utf8(self.component._core_memory0, caller, ptr15, len16)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def create_random_mat(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerRandom) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.runtime
        ret = self.component.lift_callee44(caller, _clamp(field, 0, 4294967295), variant, variant4, _clamp(field6, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load7 & 0xffffffff)
        elif load == 1:
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr14 = load8
            len15 = load9
            result: List[str] = []
            for i16 in range(0, len15):
                base10 = ptr14 + i16 * 8
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 0)
                load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 4)
                ptr = load11
                len13 = load12
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len13)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_wasm_reflected_runtime(self, caller: wasmtime.Store, data: WasmRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.wasm_artifact
        ptr, len0 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee45(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def from_wasm_reflected_func(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerWasmReflectedFunc) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.func_name
        ptr, len7 = _encode_utf8(field6, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee46(caller, _clamp(field, 0, 4294967295), variant, variant4, ptr, len7)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load8 & 0xffffffff)
        elif load == 1:
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr16 = load9
            len17 = load10
            result: List[str] = []
            for i18 in range(0, len17):
                base11 = ptr16 + i18 * 8
                load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, base11, 0)
                load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, base11, 4)
                ptr14 = load12
                len15 = load13
                list = _decode_utf8(self.component._core_memory0, caller, ptr14, len15)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_wasm_wire_runtime(self, caller: wasmtime.Store, data: WasmRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.wasm_artifact
        ptr, len0 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee47(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def from_wasm_wire_handler(self, caller: wasmtime.Store, base: BaseMaterializer, data: MaterializerWasmWireHandler) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        record5 = data
        field6 = record5.func_name
        ptr, len7 = _encode_utf8(field6, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee48(caller, _clamp(field, 0, 4294967295), variant, variant4, ptr, len7)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load8 & 0xffffffff)
        elif load == 1:
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr16 = load9
            len17 = load10
            result: List[str] = []
            for i18 in range(0, len17):
                base11 = ptr16 + i18 * 8
                load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, base11, 0)
                load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, base11, 4)
                ptr14 = load12
                len15 = load13
                list = _decode_utf8(self.component._core_memory0, caller, ptr14, len15)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_prisma_runtime(self, caller: wasmtime.Store, data: PrismaRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.name
        field0 = record.connection_string_secret
        ptr, len1 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ptr2, len3 = _encode_utf8(field0, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee49(caller, ptr, len1, ptr2, len3)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
        if load == 0:
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load4 & 0xffffffff)
        elif load == 1:
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr12 = load5
            len13 = load6
            result: List[str] = []
            for i14 in range(0, len13):
                base7 = ptr12 + i14 * 8
                load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, base7, 0)
                load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, base7, 4)
                ptr10 = load8
                len11 = load9
                list = _decode_utf8(self.component._core_memory0, caller, ptr10, len11)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_find_unique(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee50(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_find_many(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee51(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_find_first(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee52(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_aggregate(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee53(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_group_by(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee54(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_create_one(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee55(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_create_many(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee56(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_update_one(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee57(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_update_many(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee58(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_upsert_one(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee59(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_delete_one(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee60(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_delete_many(self, caller: wasmtime.Store, runtime: RuntimeId, model: TypeId) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee61(caller, _clamp(runtime, 0, 4294967295), _clamp(model, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_execute(self, caller: wasmtime.Store, runtime: RuntimeId, query: str, param: TypeId, effect: Effect) -> Result[FuncParams, Error]:
        ptr, len0 = _encode_utf8(query, self.component._realloc0, self.component._core_memory0, caller)
        if isinstance(effect, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(effect, EffectCreate):
            payload1 = effect.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(effect, EffectUpdate):
            payload2 = effect.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(effect, EffectDelete):
            payload3 = effect.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        ret = self.component.lift_callee62(caller, _clamp(runtime, 0, 4294967295), ptr, len0, _clamp(param, 0, 4294967295), variant, variant4)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load5 & 0xffffffff, load6 & 0xffffffff, load7 & 0xffffffff))
        elif load == 1:
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr15 = load8
            len16 = load9
            result: List[str] = []
            for i17 in range(0, len16):
                base10 = ptr15 + i17 * 8
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 0)
                load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 4)
                ptr13 = load11
                len14 = load12
                list = _decode_utf8(self.component._core_memory0, caller, ptr13, len14)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_query_raw(self, caller: wasmtime.Store, runtime: RuntimeId, query: str, param: Optional[TypeId], out: TypeId) -> Result[FuncParams, Error]:
        ptr, len0 = _encode_utf8(query, self.component._realloc0, self.component._core_memory0, caller)
        if param is None:
            variant = 0
            variant2 = 0
        else:
            payload1 = param
            variant = 1
            variant2 = _clamp(payload1, 0, 4294967295)
        ret = self.component.lift_callee63(caller, _clamp(runtime, 0, 4294967295), ptr, len0, variant, variant2, _clamp(out, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load3 & 0xffffffff, load4 & 0xffffffff, load5 & 0xffffffff))
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_link(self, caller: wasmtime.Store, data: PrismaLinkData) -> Result[TypeId, Error]:
        record = data
        field = record.target_type
        field0 = record.relationship_name
        field1 = record.foreign_key
        field2 = record.target_field
        field3 = record.unique
        if field0 is None:
            variant = 0
            variant6 = 0
            variant7 = 0
        else:
            payload4 = field0
            ptr, len5 = _encode_utf8(payload4, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant6 = ptr
            variant7 = len5
        if field1 is None:
            variant10 = 0
            variant11 = 0
        else:
            payload9 = field1
            variant10 = 1
            variant11 = int(payload9)
        if field2 is None:
            variant16 = 0
            variant17 = 0
            variant18 = 0
        else:
            payload13 = field2
            ptr14, len15 = _encode_utf8(payload13, self.component._realloc0, self.component._core_memory0, caller)
            variant16 = 1
            variant17 = ptr14
            variant18 = len15
        if field3 is None:
            variant21 = 0
            variant22 = 0
        else:
            payload20 = field3
            variant21 = 1
            variant22 = int(payload20)
        ret = self.component.lift_callee64(caller, _clamp(field, 0, 4294967295), variant, variant6, variant7, variant10, variant11, variant16, variant17, variant18, variant21, variant22)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load23 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load23 & 0xffffffff)
        elif load == 1:
            load24 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load25 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr31 = load24
            len32 = load25
            result: List[str] = []
            for i33 in range(0, len32):
                base26 = ptr31 + i33 * 8
                load27 = _load(ctypes.c_int32, self.component._core_memory0, caller, base26, 0)
                load28 = _load(ctypes.c_int32, self.component._core_memory0, caller, base26, 4)
                ptr29 = load27
                len30 = load28
                list = _decode_utf8(self.component._core_memory0, caller, ptr29, len30)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def prisma_migration(self, caller: wasmtime.Store, operation: PrismaMigrationOperation) -> Result[FuncParams, Error]:
        ret = self.component.lift_callee65(caller, (operation).value)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load0 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load0 & 0xffffffff, load1 & 0xffffffff, load2 & 0xffffffff))
        elif load == 1:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load3
            len10 = load4
            result: List[str] = []
            for i11 in range(0, len10):
                base5 = ptr9 + i11 * 8
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base5, 4)
                ptr = load6
                len8 = load7
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_temporal_runtime(self, caller: wasmtime.Store, data: TemporalRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.name
        field0 = record.host_secret
        field1 = record.namespace_secret
        ptr, len2 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ptr3, len4 = _encode_utf8(field0, self.component._realloc0, self.component._core_memory0, caller)
        if field1 is None:
            variant = 0
            variant8 = 0
            variant9 = 0
        else:
            payload5 = field1
            ptr6, len7 = _encode_utf8(payload5, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant8 = ptr6
            variant9 = len7
        ret = self.component.lift_callee66(caller, ptr, len2, ptr3, len4, variant, variant8, variant9)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
        if load == 0:
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load10 & 0xffffffff)
        elif load == 1:
            load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr18 = load11
            len19 = load12
            result: List[str] = []
            for i20 in range(0, len19):
                base13 = ptr18 + i20 * 8
                load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, base13, 0)
                load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, base13, 4)
                ptr16 = load14
                len17 = load15
                list = _decode_utf8(self.component._core_memory0, caller, ptr16, len17)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def generate_temporal_operation(self, caller: wasmtime.Store, runtime: RuntimeId, data: TemporalOperationData) -> Result[FuncParams, Error]:
        record = data
        field = record.mat_arg
        field0 = record.func_arg
        field1 = record.func_out
        field2 = record.operation
        if field is None:
            variant = 0
            variant5 = 0
            variant6 = 0
        else:
            payload3 = field
            ptr, len4 = _encode_utf8(payload3, self.component._realloc0, self.component._core_memory0, caller)
            variant = 1
            variant5 = ptr
            variant6 = len4
        if field0 is None:
            variant9 = 0
            variant10 = 0
        else:
            payload8 = field0
            variant9 = 1
            variant10 = _clamp(payload8, 0, 4294967295)
        if field1 is None:
            variant13 = 0
            variant14 = 0
        else:
            payload12 = field1
            variant13 = 1
            variant14 = _clamp(payload12, 0, 4294967295)
        if isinstance(field2, TemporalOperationTypeStartWorkflow):
            variant19 = 0
        elif isinstance(field2, TemporalOperationTypeSignalWorkflow):
            variant19 = 1
        elif isinstance(field2, TemporalOperationTypeQueryWorkflow):
            variant19 = 2
        elif isinstance(field2, TemporalOperationTypeDescribeWorkflow):
            variant19 = 3
        else:
            raise TypeError("invalid variant specified for TemporalOperationType")
        ret = self.component.lift_callee67(caller, _clamp(runtime, 0, 4294967295), variant, variant5, variant6, variant9, variant10, variant13, variant14, variant19)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load21 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load22 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load20 & 0xffffffff, load21 & 0xffffffff, load22 & 0xffffffff))
        elif load == 1:
            load23 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load24 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr30 = load23
            len31 = load24
            result: List[str] = []
            for i32 in range(0, len31):
                base25 = ptr30 + i32 * 8
                load26 = _load(ctypes.c_int32, self.component._core_memory0, caller, base25, 0)
                load27 = _load(ctypes.c_int32, self.component._core_memory0, caller, base25, 4)
                ptr28 = load26
                len29 = load27
                list = _decode_utf8(self.component._core_memory0, caller, ptr28, len29)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_typegate_materializer(self, caller: wasmtime.Store, operation: TypegateOperation) -> Result[MaterializerId, Error]:
        ret = self.component.lift_callee68(caller, (operation).value)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_typegraph_materializer(self, caller: wasmtime.Store, operation: TypegraphOperation) -> Result[MaterializerId, Error]:
        ret = self.component.lift_callee69(caller, (operation).value)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_substantial_runtime(self, caller: wasmtime.Store, data: SubstantialRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.backend
        field0 = record.file_descriptions
        if isinstance(field, SubstantialBackendMemory):
            variant = 0
            variant6 = 0
            variant7 = 0
        elif isinstance(field, SubstantialBackendFs):
            variant = 1
            variant6 = 0
            variant7 = 0
        elif isinstance(field, SubstantialBackendRedis):
            payload2 = field.value
            record3 = payload2
            field4 = record3.connection_string_secret
            ptr, len5 = _encode_utf8(field4, self.component._realloc0, self.component._core_memory0, caller)
            variant = 2
            variant6 = ptr
            variant7 = len5
        else:
            raise TypeError("invalid variant specified for SubstantialBackend")
        vec30 = field0
        len32 = len(vec30)
        result31 = self.component._realloc0(caller, 0, 0, 4, len32 * 28)
        assert(isinstance(result31, int))
        for i33 in range(0, len32):
            e = vec30[i33]
            base8 = result31 + i33 * 28
            record9 = e
            field10 = record9.workflows
            field11 = record9.file
            field12 = record9.deps
            field13 = record9.kind
            vec = field10
            len18 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len18 * 8)
            assert(isinstance(result, int))
            for i19 in range(0, len18):
                e14 = vec[i19]
                base15 = result + i19 * 8
                ptr16, len17 = _encode_utf8(e14, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base15, 4, len17)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base15, 0, ptr16)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base8, 4, len18)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base8, 0, result)
            ptr20, len21 = _encode_utf8(field11, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base8, 12, len21)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base8, 8, ptr20)
            vec26 = field12
            len28 = len(vec26)
            result27 = self.component._realloc0(caller, 0, 0, 4, len28 * 8)
            assert(isinstance(result27, int))
            for i29 in range(0, len28):
                e22 = vec26[i29]
                base23 = result27 + i29 * 8
                ptr24, len25 = _encode_utf8(e22, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base23, 4, len25)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base23, 0, ptr24)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base8, 20, len28)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base8, 16, result27)
            _store(ctypes.c_uint8, self.component._core_memory0, caller, base8, 24, (field13).value)
        ret = self.component.lift_callee70(caller, variant, variant6, variant7, result31, len32)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
        if load == 0:
            load34 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load34 & 0xffffffff)
        elif load == 1:
            load35 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load36 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr42 = load35
            len43 = load36
            result44: List[str] = []
            for i45 in range(0, len43):
                base37 = ptr42 + i45 * 8
                load38 = _load(ctypes.c_int32, self.component._core_memory0, caller, base37, 0)
                load39 = _load(ctypes.c_int32, self.component._core_memory0, caller, base37, 4)
                ptr40 = load38
                len41 = load39
                list = _decode_utf8(self.component._core_memory0, caller, ptr40, len41)
                result44.append(list)
            expected = Err(core.Error(result44))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def generate_substantial_operation(self, caller: wasmtime.Store, runtime: RuntimeId, data: SubstantialOperationData) -> Result[FuncParams, Error]:
        if isinstance(data, SubstantialOperationDataStart):
            payload = data.value
            record = payload
            field = record.func_arg
            field0 = record.secrets
            if field is None:
                variant = 0
                variant3 = 0
            else:
                payload2 = field
                variant = 1
                variant3 = _clamp(payload2, 0, 4294967295)
            vec = field0
            len6 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len6 * 8)
            assert(isinstance(result, int))
            for i7 in range(0, len6):
                e = vec[i7]
                base4 = result + i7 * 8
                ptr, len5 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base4, 4, len5)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base4, 0, ptr)
            variant32 = 0
            variant33 = variant
            variant34 = variant3
            variant35 = result
            variant36 = len6
        elif isinstance(data, SubstantialOperationDataStartRaw):
            payload8 = data.value
            record9 = payload8
            field10 = record9.func_arg
            field11 = record9.secrets
            if field10 is None:
                variant14 = 0
                variant15 = 0
            else:
                payload13 = field10
                variant14 = 1
                variant15 = _clamp(payload13, 0, 4294967295)
            vec20 = field11
            len22 = len(vec20)
            result21 = self.component._realloc0(caller, 0, 0, 4, len22 * 8)
            assert(isinstance(result21, int))
            for i23 in range(0, len22):
                e16 = vec20[i23]
                base17 = result21 + i23 * 8
                ptr18, len19 = _encode_utf8(e16, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base17, 4, len19)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base17, 0, ptr18)
            variant32 = 1
            variant33 = variant14
            variant34 = variant15
            variant35 = result21
            variant36 = len22
        elif isinstance(data, SubstantialOperationDataStop):
            variant32 = 2
            variant33 = 0
            variant34 = 0
            variant35 = 0
            variant36 = 0
        elif isinstance(data, SubstantialOperationDataSend):
            payload25 = data.value
            variant32 = 3
            variant33 = _clamp(payload25, 0, 4294967295)
            variant34 = 0
            variant35 = 0
            variant36 = 0
        elif isinstance(data, SubstantialOperationDataSendRaw):
            variant32 = 4
            variant33 = 0
            variant34 = 0
            variant35 = 0
            variant36 = 0
        elif isinstance(data, SubstantialOperationDataResources):
            variant32 = 5
            variant33 = 0
            variant34 = 0
            variant35 = 0
            variant36 = 0
        elif isinstance(data, SubstantialOperationDataResults):
            payload28 = data.value
            variant32 = 6
            variant33 = _clamp(payload28, 0, 4294967295)
            variant34 = 0
            variant35 = 0
            variant36 = 0
        elif isinstance(data, SubstantialOperationDataResultsRaw):
            variant32 = 7
            variant33 = 0
            variant34 = 0
            variant35 = 0
            variant36 = 0
        elif isinstance(data, SubstantialOperationDataInternalLinkParentChild):
            variant32 = 8
            variant33 = 0
            variant34 = 0
            variant35 = 0
            variant36 = 0
        elif isinstance(data, SubstantialOperationDataAdvancedFilters):
            variant32 = 9
            variant33 = 0
            variant34 = 0
            variant35 = 0
            variant36 = 0
        else:
            raise TypeError("invalid variant specified for SubstantialOperationData")
        ret = self.component.lift_callee71(caller, _clamp(runtime, 0, 4294967295), variant32, variant33, variant34, variant35, variant36)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load37 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load38 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load39 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load37 & 0xffffffff, load38 & 0xffffffff, load39 & 0xffffffff))
        elif load == 1:
            load40 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load41 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr47 = load40
            len48 = load41
            result49: List[str] = []
            for i50 in range(0, len48):
                base42 = ptr47 + i50 * 8
                load43 = _load(ctypes.c_int32, self.component._core_memory0, caller, base42, 0)
                load44 = _load(ctypes.c_int32, self.component._core_memory0, caller, base42, 4)
                ptr45 = load43
                len46 = load44
                list = _decode_utf8(self.component._core_memory0, caller, ptr45, len46)
                result49.append(list)
            expected = Err(core.Error(result49))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_kv_runtime(self, caller: wasmtime.Store, data: KvRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.url
        ptr, len0 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee72(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
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
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def kv_operation(self, caller: wasmtime.Store, base: BaseMaterializer, data: KvMaterializer) -> Result[MaterializerId, Error]:
        record = base
        field = record.runtime
        field0 = record.effect
        if isinstance(field0, EffectRead):
            variant = 0
            variant4 = 0
        elif isinstance(field0, EffectCreate):
            payload1 = field0.value
            variant = 1
            variant4 = int(payload1)
        elif isinstance(field0, EffectUpdate):
            payload2 = field0.value
            variant = 2
            variant4 = int(payload2)
        elif isinstance(field0, EffectDelete):
            payload3 = field0.value
            variant = 3
            variant4 = int(payload3)
        else:
            raise TypeError("invalid variant specified for Effect")
        ret = self.component.lift_callee73(caller, _clamp(field, 0, 4294967295), variant, variant4, (data).value)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[MaterializerId, Error]
        if load == 0:
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load5 & 0xffffffff)
        elif load == 1:
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr12 = load6
            len13 = load7
            result: List[str] = []
            for i14 in range(0, len13):
                base8 = ptr12 + i14 * 8
                load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, base8, 0)
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base8, 4)
                ptr = load9
                len11 = load10
                list = _decode_utf8(self.component._core_memory0, caller, ptr, len11)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def register_grpc_runtime(self, caller: wasmtime.Store, data: GrpcRuntimeData) -> Result[RuntimeId, Error]:
        record = data
        field = record.proto_file
        field0 = record.endpoint
        ptr, len1 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ptr2, len3 = _encode_utf8(field0, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee74(caller, ptr, len1, ptr2, len3)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[RuntimeId, Error]
        if load == 0:
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load4 & 0xffffffff)
        elif load == 1:
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr12 = load5
            len13 = load6
            result: List[str] = []
            for i14 in range(0, len13):
                base7 = ptr12 + i14 * 8
                load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, base7, 0)
                load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, base7, 4)
                ptr10 = load8
                len11 = load9
                list = _decode_utf8(self.component._core_memory0, caller, ptr10, len11)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def call_grpc_method(self, caller: wasmtime.Store, runtime: RuntimeId, data: GrpcData) -> Result[FuncParams, Error]:
        record = data
        field = record.method
        ptr, len0 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee75(caller, _clamp(runtime, 0, 4294967295), ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[FuncParams, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 12)
            expected = Ok(core.FuncParams(load1 & 0xffffffff, load2 & 0xffffffff, load3 & 0xffffffff))
        elif load == 1:
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr11 = load4
            len12 = load5
            result: List[str] = []
            for i13 in range(0, len12):
                base6 = ptr11 + i13 * 8
                load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, base6, 0)
                load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, base6, 4)
                ptr9 = load7
                len10 = load8
                list = _decode_utf8(self.component._core_memory0, caller, ptr9, len10)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    