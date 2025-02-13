"""Module for serializable objects in the system."""

import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, TypeVar

import cloudpickle
import msgpack

from flock.core.logging import flock_logger, performance_handler

T = TypeVar("T", bound="Serializable")


class Serializable(ABC):
    """Base class for all serializable objects in the system.

    Provides methods for serializing/deserializing objects to various formats
    with comprehensive logging and performance tracking.
    """

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """Convert instance to dictionary representation."""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls: type[T], data: dict[str, Any]) -> T:
        """Create instance from dictionary representation."""
        pass

    def to_json(self) -> str:
        """Serialize to JSON string."""
        try:
            with performance_handler.track_time("json_serialization"):
                flock_logger.debug(
                    "Serializing to JSON",
                    class_name=self.__class__.__name__,
                )
                json_str = json.dumps(self.to_dict())
                flock_logger.debug(
                    "JSON serialization complete",
                    size_bytes=len(json_str),
                )
                return json_str
        except Exception as e:
            flock_logger.error(
                "JSON serialization failed",
                class_name=self.__class__.__name__,
                error=str(e),
            )
            raise

    @classmethod
    def from_json(cls: type[T], json_str: str) -> T:
        """Create instance from JSON string."""
        try:
            with performance_handler.track_time("json_deserialization"):
                flock_logger.debug(
                    "Deserializing from JSON",
                    class_name=cls.__name__,
                    size_bytes=len(json_str),
                )
                instance = cls.from_dict(json.loads(json_str))
                flock_logger.debug("JSON deserialization complete")
                return instance
        except Exception as e:
            flock_logger.error(
                "JSON deserialization failed",
                class_name=cls.__name__,
                error=str(e),
            )
            raise

    def to_msgpack(self, path: Path | None = None) -> bytes:
        """Serialize to msgpack bytes."""
        try:
            with performance_handler.track_time("msgpack_serialization"):
                flock_logger.debug(
                    "Serializing to msgpack",
                    class_name=self.__class__.__name__,
                )
                msgpack_bytes = msgpack.packb(self.to_dict())

                if path:
                    flock_logger.debug(f"Writing msgpack to file: {path}")
                    path.write_bytes(msgpack_bytes)

                flock_logger.debug(
                    "Msgpack serialization complete",
                    size_bytes=len(msgpack_bytes),
                    file_path=str(path) if path else None,
                )
                return msgpack_bytes
        except Exception as e:
            flock_logger.error(
                "Msgpack serialization failed",
                class_name=self.__class__.__name__,
                file_path=str(path) if path else None,
                error=str(e),
            )
            raise

    @classmethod
    def from_msgpack(cls: type[T], msgpack_bytes: bytes) -> T:
        """Create instance from msgpack bytes."""
        try:
            with performance_handler.track_time("msgpack_deserialization"):
                flock_logger.debug(
                    "Deserializing from msgpack",
                    class_name=cls.__name__,
                    size_bytes=len(msgpack_bytes),
                )
                instance = cls.from_dict(msgpack.unpackb(msgpack_bytes))
                flock_logger.debug("Msgpack deserialization complete")
                return instance
        except Exception as e:
            flock_logger.error(
                "Msgpack deserialization failed",
                class_name=cls.__name__,
                error=str(e),
            )
            raise

    @classmethod
    def from_msgpack_file(cls: type[T], path: Path) -> T:
        """Create instance from msgpack file."""
        try:
            with performance_handler.track_time("msgpack_file_read"):
                flock_logger.debug(
                    f"Reading msgpack from file: {path}",
                    class_name=cls.__name__,
                )
                return cls.from_msgpack(path.read_bytes())
        except Exception as e:
            flock_logger.error(
                "Msgpack file read failed",
                class_name=cls.__name__,
                file_path=str(path),
                error=str(e),
            )
            raise

    def to_pickle(self) -> bytes:
        """Serialize to pickle bytes."""
        try:
            with performance_handler.track_time("pickle_serialization"):
                flock_logger.debug(
                    "Serializing to pickle",
                    class_name=self.__class__.__name__,
                )
                pickle_bytes = cloudpickle.dumps(self)
                flock_logger.debug(
                    "Pickle serialization complete",
                    size_bytes=len(pickle_bytes),
                )
                return pickle_bytes
        except Exception as e:
            flock_logger.error(
                "Pickle serialization failed",
                class_name=self.__class__.__name__,
                error=str(e),
            )
            raise

    @classmethod
    def from_pickle(cls, pickle_bytes: bytes) -> T:
        """Create instance from pickle bytes."""
        try:
            with performance_handler.track_time("pickle_deserialization"):
                flock_logger.debug(
                    "Deserializing from pickle",
                    class_name=cls.__name__,
                    size_bytes=len(pickle_bytes),
                )
                instance = cloudpickle.loads(pickle_bytes)
                flock_logger.debug("Pickle deserialization complete")
                return instance
        except Exception as e:
            flock_logger.error(
                "Pickle deserialization failed",
                class_name=cls.__name__,
                error=str(e),
            )
            raise

    @classmethod
    def from_pickle_file(cls: type[T], path: Path) -> T:
        """Create instance from pickle file."""
        try:
            with performance_handler.track_time("pickle_file_read"):
                flock_logger.debug(
                    f"Reading pickle from file: {path}",
                    class_name=cls.__name__,
                )
                return cls.from_pickle(path.read_bytes())
        except Exception as e:
            flock_logger.error(
                "Pickle file read failed",
                class_name=cls.__name__,
                file_path=str(path),
                error=str(e),
            )
            raise
