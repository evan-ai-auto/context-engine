"""Frozen string enums for the Project Context domain model."""

from enum import Enum


class ModuleType(str, Enum):
    APPLICATION = "application"
    LIBRARY = "library"
    SERVICE = "service"
    TOOL = "tool"
    UNKNOWN = "unknown"


class DependencyScope(str, Enum):
    COMPILE = "compile"
    RUNTIME = "runtime"
    TEST = "test"
    DEVELOPMENT = "development"
    OPTIONAL = "optional"
    UNKNOWN = "unknown"


class EvidenceType(str, Enum):
    BUILD_FILE = "build_file"
    LOCK_FILE = "lock_file"
    MANIFEST = "manifest"
    SOURCE = "source"
    CONFIG = "config"
    OTHER = "other"


class AnalysisStatus(str, Enum):
    PENDING = "pending"
    PARTIAL = "partial"
    COMPLETED = "completed"
    FAILED = "failed"
