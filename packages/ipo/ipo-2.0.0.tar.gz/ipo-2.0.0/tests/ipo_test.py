#!/usr/bin/env python3

import pytest
from functools import partial as p
from io import StringIO
import ipo
from ipo import opi, p


def test_ipo():
	three = ipo.ipo(3)
	assert isinstance(three, ipo.ipo)
	assert three.data == 3
	assert repr(three) == "ipo(3)"

	still_three = three | (lambda x: x)
	assert isinstance(still_three, ipo.ipo)
	assert still_three.data == 3
	assert repr(still_three) == "ipo(3)"

	assert three == ipo.ipo(3)
	assert three == still_three

	assert (ipo.ipo([2, 1, 3]) | sorted | list).data == [1, 2, 3]


def test_opi():
	three = ipo.ipo(3)
	assert three | opi == 3

	# It should be the correct precedence: (three | opi) == 3.
	# The alternative three | (opi == 3), would be an error.
	assert (three | opi) == 3
	with pytest.raises(TypeError, match="'bool' object is not callable") as e:
		three | (opi == 3)

	still_three = three | (lambda x: x)
	assert still_three | opi == 3

	assert ipo.ipo([2, 1, 3]) | sorted | list | opi == [1, 2, 3]


def test_ipo_source():
	five_ipo_source = ipo.ipo_source(lambda: 5)

	ipo_five = five_ipo_source()
	assert isinstance(ipo_five, ipo.ipo)
	assert ipo_five.data == 5


def test_p():
	sort_r = p(sorted)(reverse=True)
	assert sort_r([1, 3, 2]) == [3, 2, 1]


def test_read():
	assert (ipo.read(["Line 1\n", "Line 2\n", "Line 3"]) | list).data == \
		["Line 1", "Line 2", "Line 3"]

	mock_file = StringIO("Line 1\nLine 2\nLine 3")
	assert (ipo.read(mock_file) | list).data == \
		["Line 1", "Line 2", "Line 3"]


def test_write():
	mock_file = StringIO()
	ipo.ipo([1, 2, 3]) | p(ipo.write)(file=mock_file)
	assert mock_file.getvalue() == "1\n2\n3\n"

	mock_file = StringIO()
	ipo.ipo("abc") | p(ipo.write)(file=mock_file)
	assert mock_file.getvalue() == "a\nb\nc\n"


def test_from_csv():
	assert (ipo.ipo(["a,b,c", "d,e,f"]) | ipo.from_csv | list).data == \
		[["a", "b", "c"], ["d", "e", "f"]]


def test_to_csv():
	assert (ipo.ipo([("a", '"b', "c"), ("d", "e,", "f")]) | ipo.to_csv | list).data == \
		['a,"""b",c', 'd,"e,",f']

	assert (ipo.ipo([("a", '"b', "c"), ("d", "e,", "f")]) | p(ipo.to_csv)(escapechar="\\") | list).data == \
		['a,"\\"b",c', 'd,"e,",f']


def test_to_csv_bytes():
	assert (ipo.ipo([(b"1", b'"2', b"3"), (b"4", b"5,", b"6")]) | ipo.to_csv_bytes | list).data == \
		[b'1,"""2",3', b'4,"5,",6']

	assert (ipo.ipo([(b"1", b'"2', b"3"), (b"4", b"5,", b"6")]) | p(ipo.to_csv_bytes)(escapechar=b"\\") | list).data == \
		[b'1,"\\"2",3', b'4,"5,",6']


def test_imputate():
	assert (ipo.ipo(["a", None, "c", "d", "e,", "f", None, "g", None, None]) | p(ipo.imputate)("Z") | list).data == \
		["a", "Z", "c", "d", "e,", "f", "Z", "g", "Z", "Z"]


def test_imputate_2d():
	assert (ipo.ipo([("a", None, "c"), ("d", "e,", "f"), (None, "g", None, None)]) | p(ipo.imputate_2d)(("1", "2", "3")) | list).data == \
		[("a", "2", "c"), ("d", "e,", "f"), ("1", "g", "3", None)]


def test_recompose():
	assert (ipo.ipo(["a", "b", "c"]) | p(ipo.recompose)([2, 0, 1]) | list).data == \
		["c", "a", "b"]

	assert (ipo.ipo(["a", "b", "c"]) | p(ipo.recompose)([2, lambda x: x[0] + x[1]]) | list).data == \
		["c", "ab"]


def test_starstarmap():
	f = lambda x, y: x + y
	assert (
		ipo.ipo([{"x": 1, "y": 2}, {"y": "b", "x": "a"}]) |
		p(ipo.starstarmap)(f) |
		list
	).data == [3, "ab"]


def test_flatten():
	assert (ipo.ipo([[1, 2], [3]]) | ipo.flatten | list).data == [1, 2, 3]


def test_head():
	assert (ipo.ipo([1, 2, 3]) | p(ipo.head)(2) | list).data == [1, 2]
	assert (ipo.ipo([1, 2, 3]) | p(ipo.head)(0) | list).data == []
	assert (ipo.ipo([]) | p(ipo.head)(1) | list).data == []


def test_skip():
	assert (ipo.ipo([1, 2, 3]) | p(ipo.skip)(2) | list).data == [3]
	assert (ipo.ipo([1, 2, 3]) | p(ipo.skip)(0) | list).data == [1, 2, 3]
	assert (ipo.ipo([1, 2, 3]) | p(ipo.skip)(3) | list).data == []
	assert (ipo.ipo([1, 2, 3]) | p(ipo.skip)(4) | list).data == []
	assert (ipo.ipo([]) | p(ipo.skip)(1) | list).data == []


def test_prepended():
	assert (ipo.ipo([2, 3]) | p(ipo.prepended)([1]) | list).data == [1, 2, 3]


def test_appended():
	assert (ipo.ipo([1, 2]) | p(ipo.appended)([3]) | list).data == [1, 2, 3]


def test_parted():
	l = [1, 2, 3, 4]
	assert (ipo.ipo(l) | p(ipo.parted)(1) | p(map)(list) | tuple).data == (l[0:1], l[1:])
	assert (ipo.ipo(l) | p(ipo.parted)(lambda x, _: x > 2) | p(map)(list) | tuple).data == (l[0:2], l[2:])


def test_all_before():
	l = [1, 2, 3, 4]
	assert (ipo.ipo(l) | p(ipo.all_before)(lambda x: x > 2) | list).data == l[0:2]


def test_all_before_incl():
	l = [1, 2, 3, 4]
	assert (ipo.ipo(l) | p(ipo.all_before_incl)(lambda x: x > 2) | list).data == l[0:3]


def test_all_after():
	l = [1, 2, 3, 4]
	assert (ipo.ipo(l) | p(ipo.all_after)(lambda x: x > 2) | list).data == l[3:]


def test_all_after_incl():
	l = [1, 2, 3, 4]
	assert (ipo.ipo(l) | p(ipo.all_after_incl)(lambda x: x > 2) | list).data == l[2:]


def test_flat_enum():
	assert (ipo.ipo([("a", "b"), ("c", "d")]) | ipo.flat_enum | list).data == \
		[(0, "a", "b"), (1, "c", "d")]


def test_intersperse():
	assert (ipo.ipo([]) | p(ipo.intersperse)(0) | list).data == \
		[]
	assert (ipo.ipo([1]) | p(ipo.intersperse)(0) | list).data == \
		[1]
	assert (ipo.ipo([1, 2]) | p(ipo.intersperse)(0) | list).data == \
		[1, 0, 2]
	assert (ipo.ipo([1, 2, 3]) | p(ipo.intersperse)(0) | list).data == \
		[1, 0, 2, 0, 3]


def test_grep():
	assert (
		ipo.ipo(["this is", "ipo", "testing the", "grep function"]) |
		p(ipo.grep)(r"o") | list
	).data == ["ipo", "grep function"]


def test_grepo():
	assert (
		ipo.ipo(["this is", "ipo", "!", "testing the", "grepo function"]) |
		p(ipo.grepo)(r"[aeiou]") | list
	).data == ["i", "i", "i", "o", "e", "i", "e", "e", "o", "u", "i", "o"]
