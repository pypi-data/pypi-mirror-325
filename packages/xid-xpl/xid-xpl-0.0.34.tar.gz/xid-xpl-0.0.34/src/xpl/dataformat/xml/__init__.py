#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Generic, Iterable, Iterator, Optional, Sequence, Type, TypeVar, Tuple, Union
from typing import ItemsView, KeysView, ValuesView
from typing import IO, TextIO, BinaryIO
from typing import Any, List, Dict, Set
from typing import cast, overload
import builtins


#--------------------------------------------------------------------------------
# 패키지 포함 목록.
#--------------------------------------------------------------------------------
from .document import Document
from .element import Element
from .path import Path


#--------------------------------------------------------------------------------
# 참고 패키지 목록.
#--------------------------------------------------------------------------------
from xml.etree import ElementTree as XML
from xml.etree.ElementTree import ElementTree as XMLDocument # 파이썬 내장 XML 라이브러리의 XML 문서.
from xml.etree.ElementTree import Element as XMLElement # 파이썬 내장 XML 라이브러리의 XML 요소.