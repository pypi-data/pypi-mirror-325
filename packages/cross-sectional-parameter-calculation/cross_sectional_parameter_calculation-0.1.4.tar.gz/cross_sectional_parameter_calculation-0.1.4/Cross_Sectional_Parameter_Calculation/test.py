import pytest
from core import (
    pi,
    annular_area_mm2,
    annular_area_cm2,
    annular_area_m2,
    annular_moment_of_inertia_mm4,
    annular_moment_of_inertia_cm4,
    annular_moment_of_inertia_m4,
    annular_radius_of_gyration_mm,
    annular_radius_of_gyration_cm,
    annular_radius_of_gyration_m,
)

# 测试 pi 函数
def test_pi():
    assert pi() == 3.141592653589793

# 测试环形面积函数
def test_annular_area_mm2():
    assert annular_area_mm2(400, 8) == pytest.approx(pi() * ((200**2) - (192**2)), rel=1e-6)

def test_annular_area_cm2():
    assert annular_area_cm2(40, 0.8) == annular_area_mm2(400, 8) / 100

def test_annular_area_m2():
    assert annular_area_m2(0.4, 0.008) == annular_area_mm2(400, 8) / 1e6

# 测试环形惯性矩函数
def test_annular_moment_of_inertia_mm4():
    assert annular_moment_of_inertia_mm4(400, 8) == pytest.approx(pi() * ((200**4) - (192**4)) / 64, rel=1e-6)

def test_annular_moment_of_inertia_cm4():
    assert annular_moment_of_inertia_cm4(40, 0.8) == annular_moment_of_inertia_mm4(400, 8) / 10000

def test_annular_moment_of_inertia_m4():
    assert annular_moment_of_inertia_m4(0.4, 0.008) == annular_moment_of_inertia_mm4(400, 8) / 1e12

# 测试环形回转半径函数
def test_annular_radius_of_gyration_mm():
    area = annular_area_mm2(400, 8)
    moment = annular_moment_of_inertia_mm4(400, 8)
    expected_radius = (moment / area) ** 0.5
    assert annular_radius_of_gyration_mm(400, 8) == pytest.approx(expected_radius, rel=1e-6)

def test_annular_radius_of_gyration_cm():
    area = annular_area_cm2(40, 0.8)
    moment = annular_moment_of_inertia_cm4(40, 0.8)
    expected_radius = (moment / area) ** 0.5
    assert annular_radius_of_gyration_cm(40, 0.8) == pytest.approx(expected_radius, rel=1e-6)

def test_annular_radius_of_gyration_m():
    area = annular_area_m2(0.4, 0.008)
    moment = annular_moment_of_inertia_m4(0.4, 0.008)
    expected_radius = (moment / area) ** 0.5
    assert annular_radius_of_gyration_m(0.4, 0.008) == pytest.approx(expected_radius, rel=1e-6)

# 测试负值输入
def test_negative_inputs():
    with pytest.raises(ValueError):
        annular_area_mm2(-400, 8)
    with pytest.raises(ValueError):
        annular_moment_of_inertia_mm4(-400, 8)
    with pytest.raises(ValueError):
        annular_radius_of_gyration_mm(-400, 8)

# 测试零值输入
def test_zero_inputs():
    with pytest.raises(ValueError):
        annular_area_mm2(0, 8)
    with pytest.raises(ValueError):
        annular_moment_of_inertia_mm4(400, 0)
    with pytest.raises(ValueError):
        annular_radius_of_gyration_mm(0, 8)