from cmath import cos, pi

import numpy as np


def get_static_map_bounds(lat, lng, zoom, sx, sy):
    # lat, lng - center
    # sx, sy - map size in pixels

    # 256 pixels - initial map size for zoom factor 0
    sz = 256 * 2 ** zoom

    # resolution in degrees per pixel
    res_lat = cos(lat * pi / 180.) * 360. / sz
    res_lng = 360./sz

    d_lat = (res_lat * sy / 2).real
    d_lng = (res_lng * sx / 2).real
    return (lat - d_lat, lng - d_lng), (lat + d_lat, lng + d_lng)


def get_image_changes_per_px(bounds, sx, sy):
    b_left_bottom = bounds[0]
    b_right_top = bounds[1]

    dx = (b_right_top[1] - b_left_bottom[1]) / sx
    dy = (b_right_top[0] - b_left_bottom[0]) / sy
    return dx, dy


def get_image_points_location(bounds, sx, sy, points):
    dx, dy = get_image_changes_per_px(bounds, sx, sy)

    locations = []
    for point in points:
        lat = bounds[0][0] + (dy * (sy - point[1]))
        lng = bounds[0][1] + (dx * point[0])
        locations.append((lat, lng))
    return np.array(locations)


