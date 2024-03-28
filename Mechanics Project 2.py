import math

def tensile_resistance(area_list: list) -> list:
    """
    Return a factored tensile strength based on the area provided.

    1 Pa = 1 N/M^2
    """
    PHI = 0.9
    STRENGTH = 370
    tensile_list = []
    for area in area_list:
        tension = (PHI * STRENGTH * area)/1000
        tensile_list.append(tension)
        tension = 0
    return tensile_list

def compressive_resistance_vertical(radius_list: list, area_list: list) -> list:
    VERTICAL_MEMBER = 3180 # 3.18m to 3180mm
    ELASTICITY = 20000
    sigma_y = 370
    N = 1.34
    PHI = 0.9
    compressive_list_vert = []
    i = 0
    for radius in radius_list:
        sigma_e = math.pow(math.pi, 2) * ELASTICITY / math.pow(VERTICAL_MEMBER / radius, 2)
        lamb = math.sqrt(sigma_y / sigma_e)
        slender_factor = 1 / math.pow((1 + math.pow(lamb, (2*N))), (1/N))
        compression = (PHI * slender_factor * sigma_y * area[i])/1000
        compressive_list_vert.append(compression)
        i += 1

    return compressive_list_vert
    
def compressive_resistance_horizontal(radius_list: list, area_list: list) -> list:
    HORIZONTAL_MEMBER = 2500 # 2.5m 2500 mm
    ELASTICITY = 20000
    sigma_y = 370
    N = 1.34
    PHI = 0.9
    compressive_list_horz = []
    i = 0
    for radius in radius_list:
        sigma_e = math.pow(math.pi, 2) * ELASTICITY / math.pow(HORIZONTAL_MEMBER / radius, 2)
        lamb = math.sqrt(sigma_y / sigma_e)
        slender_factor = 1 / math.pow((1 + math.pow(lamb, (2*N))), (1/N))
        compression = (PHI * slender_factor * sigma_y * area[i])/1000
        compressive_list_horz.append(compression)
        i += 1
    
    return compressive_list_horz

def compressive_resistance_diagonal(radius_list: list, area_list: list) -> list:
    DIAGONAL_MEMBER = 4050 # 4.05m 4050 mm
    ELASTICITY = 20000
    sigma_y = 370
    N = 1.34
    PHI = 0.9
    compressive_list_diag = []
    i = 0
    for radius in radius_list:
        sigma_e = math.pow(math.pi, 2) * ELASTICITY / math.pow(DIAGONAL_MEMBER / radius, 2)
        lamb = math.sqrt(sigma_y / sigma_e)
        slender_factor = 1 / math.pow((1 + math.pow(lamb, (2*N))), (1/N))
        compression = (PHI * slender_factor * sigma_y * area[i])/1000
        compressive_list_diag.append(compression)
        i += 1

    return compressive_list_diag

area = [1030, 1350, 1600, 2010, 2320, 2410, 2790, 3030, 3280, 3620, 4240, 4840, 5210, 5870, 6680, 6180, 7100, 7660, 9090, 11800, 7970, 8230, 9260, 9280, 9090, 10500, 11800, 12800, 14400]
radius = [17.6, 26.1, 25.1, 30.5, 38.4, 35.8, 35.0, 41.7, 43.2, 54.8, 54.0, 53.1, 70.3, 69.3, 68.4, 75.1, 74.2, 99.9, 99.1, 97.6, 73.4, 91.0, 90.1, 121, 113, 112, 111, 119, 118]

tensile = tensile_resistance(area)
print(tensile)
compressive_vert = compressive_resistance_vertical(radius, area)
print(compressive_vert)
compressive_horz = compressive_resistance_horizontal(radius, area)
print(compressive_horz)
compressive_diag = compressive_resistance_diagonal(radius, area)
print(compressive_diag)
