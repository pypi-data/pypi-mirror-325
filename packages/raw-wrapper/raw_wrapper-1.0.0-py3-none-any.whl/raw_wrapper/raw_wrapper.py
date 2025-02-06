"""RawWrapper class"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, fields
from struct import calcsize, pack, unpack
from typing import Type, TypeVar

from simple_classproperty import ClasspropertyMeta


class RawWrapperMeta(ABCMeta, ClasspropertyMeta):
    """RawWrapper Meta class"""


T = TypeVar('T', bound='RawWrapper')


@dataclass
class RawWrapper(metaclass=RawWrapperMeta):
    """RawWrapper class"""

    @staticmethod
    @abstractmethod
    def get_format() -> str:
        """Returns format"""

    @staticmethod
    @abstractmethod
    def expected_size() -> int:
        """Returns expected size"""

    @classmethod
    def get_size(cls, dynamic=False):
        """Returns size"""
        if dynamic:
            size = len(cls().unwrap())
        else:
            size = calcsize(cls.get_format())
        assert size == cls.expected_size(), \
            "Expected size of {cls.__name__} is {size}" + \
            "(got {cls.expected_size})"
        return size

    @classmethod
    def wrap(cls: Type[T], data) -> T:
        """Wrap raw data to this class"""
        return cls(*unpack(cls.get_format(), data))

    def attrs(self):
        """Return attributes for all fields"""
        return (getattr(self, f.name) for f in fields(self.__class__))

    def unwrap(self) -> bytes:
        """Unwrap this class to raw data"""
        return pack(self.__class__.get_format(), *self.attrs)

    def decode_bytes_fields_to_str(self) -> None:
        """Decode internal str fields"""
        flds = ((f, getattr(self, f.name)) for f in fields(self.__class__))
        for fld in flds:
            if fld[0].type == str and isinstance(fld[0].default, bytes):
                try:
                    val = fld[1].decode().strip()
                except (UnicodeDecodeError, AttributeError):
                    continue
                setattr(self, fld[0].name, val)
