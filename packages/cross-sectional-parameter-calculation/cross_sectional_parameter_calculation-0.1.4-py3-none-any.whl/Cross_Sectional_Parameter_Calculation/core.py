def pi():
    """返回圆周率 π 的值"""
    return 3.141592653589793

# 单位转换函数
def _convert_units(value, from_unit, to_unit):
    """将值从一个单位转换为另一个单位"""
    conversion_factors = {
        ('mm', 'cm'): 0.1,
        ('mm', 'm'): 0.001,
        ('cm', 'mm'): 10.0,
        ('cm', 'm'): 0.01,
        ('m', 'mm'): 1000.0,
        ('m', 'cm'): 100.0,
    }
    return value * conversion_factors[(from_unit, to_unit)]

# 公共计算函数
def _calculate_annular_area(diameter, thickness):
    """计算环形面积"""
    radius_outer = diameter / 2
    radius_inner = (diameter - 2 * thickness) / 2
    return pi() * (radius_outer ** 2 - radius_inner ** 2)

def _calculate_annular_moment_of_inertia(diameter, thickness):
    """计算环形惯性矩"""
    radius_outer = diameter / 2
    radius_inner = (diameter - 2 * thickness) / 2
    return pi() * (radius_outer ** 4 - radius_inner ** 4) / 64

def _calculate_annular_radius_of_gyration(area_moment, area):
    """计算环形回转半径"""
    return (area_moment / area) ** 0.5

# 公共接口函数
def annular_area_mm2(diameter_mm, thickness_mm):
    """计算环形面积（单位：平方毫米，mm²）"""
    #输入合法判断
    if diameter_mm <= 0 or thickness_mm <= 0:
        raise ValueError("直径和厚度不能为负值")

    return _calculate_annular_area(diameter_mm, thickness_mm)

def annular_area_cm2(diameter_cm, thickness_cm):
    """计算环形面积（单位：平方厘米，cm²）"""
    # 输入合法判断
    if diameter_cm <= 0 or thickness_cm <= 0:
        raise ValueError("直径和厚度不能为负值")

    diameter_mm = _convert_units(diameter_cm, 'cm', 'mm')
    thickness_mm = _convert_units(thickness_cm, 'cm', 'mm')
    return annular_area_mm2(diameter_mm, thickness_mm) / 100

def annular_area_m2(diameter_m, thickness_m):
    """计算环形面积（单位：平方米，m²）"""

    # 输入合法判断
    if diameter_m <= 0 or thickness_m <= 0:
        raise ValueError("直径和厚度不能为负值")

    diameter_mm = _convert_units(diameter_m, 'm', 'mm')
    thickness_mm = _convert_units(thickness_m, 'm', 'mm')
    return annular_area_mm2(diameter_mm, thickness_mm) / 1e6

def annular_moment_of_inertia_mm4(diameter_mm, thickness_mm):
    """计算环形惯性矩（单位：立方毫米，mm⁴）"""

    # 输入合法判断
    if diameter_mm <= 0 or thickness_mm <= 0:
        raise ValueError("直径和厚度不能为负值")

    return _calculate_annular_moment_of_inertia(diameter_mm, thickness_mm)

def annular_moment_of_inertia_cm4(diameter_cm, thickness_cm):
    """计算环形惯性矩（单位：立方厘米，cm⁴）"""

    # 输入合法判断
    if diameter_cm <= 0 or thickness_cm <= 0:
        raise ValueError("直径和厚度不能为负值")

    diameter_mm = _convert_units(diameter_cm, 'cm', 'mm')
    thickness_mm = _convert_units(thickness_cm, 'cm', 'mm')
    return annular_moment_of_inertia_mm4(diameter_mm, thickness_mm) / 10000

def annular_moment_of_inertia_m4(diameter_m, thickness_m):
    """计算环形惯性矩（单位：m⁴）"""

    # 输入合法判断
    if diameter_m <= 0 or thickness_m <= 0:
        raise ValueError("直径和厚度不能为负值")

    diameter_mm = _convert_units(diameter_m, 'm', 'mm')
    thickness_mm = _convert_units(thickness_m, 'm', 'mm')
    return annular_moment_of_inertia_mm4(diameter_mm, thickness_mm) / 1e12

def annular_radius_of_gyration_mm(diameter_mm, thickness_mm):
    """计算环形回转半径（单位：毫米，mm）"""

    # 输入合法判断
    if diameter_mm <= 0 or thickness_mm <= 0:
        raise ValueError("直径和厚度不能为负值")

    area = annular_area_mm2(diameter_mm, thickness_mm)
    moment = annular_moment_of_inertia_mm4(diameter_mm, thickness_mm)
    return _calculate_annular_radius_of_gyration(moment, area)

def annular_radius_of_gyration_cm(diameter_cm, thickness_cm):
    """计算环形回转半径（单位：厘米，cm）"""

    # 输入合法判断
    if diameter_cm <= 0 or thickness_cm <= 0:
        raise ValueError("直径和厚度不能为负值")

    diameter_mm = _convert_units(diameter_cm, 'cm', 'mm')
    thickness_mm = _convert_units(thickness_cm, 'cm', 'mm')
    return _convert_units(annular_radius_of_gyration_mm(diameter_mm, thickness_mm), 'mm', 'cm')

def annular_radius_of_gyration_m(diameter_m, thickness_m):
    """计算环形回转半径（单位：米，m）"""

    # 输入合法判断
    if diameter_m <= 0 or thickness_m <= 0:
        raise ValueError("直径和厚度不能为负值")

    diameter_mm = _convert_units(diameter_m, 'm', 'mm')
    thickness_mm = _convert_units(thickness_m, 'm', 'mm')
    return _convert_units(annular_radius_of_gyration_mm(diameter_mm, thickness_mm), 'mm', 'm')