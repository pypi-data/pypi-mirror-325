#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Generic, Iterable, Iterator, Optional, Sequence, Type, TypeVar, Tuple, Union
from typing import ItemsView, KeysView, ValuesView
from typing import Any, List, Dict, Set
from typing import cast, overload
from ..console.console import Console
from .baseclass import BaseClass


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
ANONYMOUSOBJECT: str = "AnonymousClass"


#--------------------------------------------------------------------------------
#  동적 익명 오브젝트 타입.
# - 타입 클래스 (인스턴스화 될 수 있는 기본 클래스) 중 가장 단순한 형태의 임시 클래스 타입.
# - 이 클래스의 인스턴스는 어트리뷰트 설정 기능만이 존재한다.
# - 실체는 리플렉션과 같은 동적 변수이므로 인텔리센스에서는 해석상 클래스 인정이 되지 않는다. (주의)
# - 다음과 같은 방식으로 사용.
# - temp = AnonymousClass()
# - temp.AAA = 5
#--------------------------------------------------------------------------------
AnonymousObject = type(ANONYMOUSOBJECT, tuple([object]), dict())


#--------------------------------------------------------------------------------
#  정적 무명 클래스 타입.
# - 명시적인 형태로 사용하기 위해 클래스화.
# - 파이썬은 기본적으로 동적 멤버 추가가 가능하므로 인텔리센스 인식을 위해서는
# - 정적으로 해석 가능한 언네임드클래스를 사용하는 것이 좀 더 옳바르다.
# - 다만 동적 익명 오브젝트 타입보다 쓸 때 없는 일반 클래스 관련 기능들이 추가되어있어 약간 더 무겁다.
# - temp = UnnamedClass()
# - temp.AAA = 5
#--------------------------------------------------------------------------------
class UnnamedClass(BaseClass):
	pass