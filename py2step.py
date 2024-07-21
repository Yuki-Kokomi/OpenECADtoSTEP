import os
import glob
import json
import numpy as np
from OCC.Core.BRepCheck import BRepCheck_Analyzer
from OCC.Extend.DataExchange import read_step_file, write_step_file
import argparse
import sys
sys.path.append(".")
from lib.visualize import vec2CADsolid, create_CAD

from lib.curves import Line, Arc, Circle
# Curves
def add_line(start, end):
    start = np.array(start)
    end = np.array(end)
    return Line(start, end)



def find_circle_center_and_radius(start_point, end_point, mid_point):
    # Convert points to numpy arrays
    start_point = np.array(start_point)
    end_point = np.array(end_point)
    mid_point = np.array(mid_point)
    
    # Calculate midpoints of the chords
    mid_point_start_end = (start_point + end_point) / 2
    mid_point_start_mid = (start_point + mid_point) / 2
    
    # Calculate direction vectors of the chords
    direction_start_end = end_point - start_point
    direction_start_mid = mid_point - start_point
    
    # Calculate perpendicular direction vectors
    perp_start_end = np.array([-direction_start_end[1], direction_start_end[0]])
    perp_start_mid = np.array([-direction_start_mid[1], direction_start_mid[0]])
    
    # Solve for the intersection of the perpendicular bisectors
    A = np.array([perp_start_end, -perp_start_mid]).T
    b = mid_point_start_mid - mid_point_start_end
    
    # Solve the linear system
    t, s = np.linalg.solve(A, b)
    
    # Calculate the center
    center = mid_point_start_end + t * perp_start_end
    
    # Calculate the radius
    radius = np.linalg.norm(center - start_point)
    
    return center, radius
from lib.math_utils import angle_from_vector_to_x
def add_arc(start, end, mid):
    # get radius and center point
    center, radius = find_circle_center_and_radius(start, end, mid)
    start = np.array(start)
    end = np.array(end)
    mid = np.array(mid)
    def get_angles_counterclockwise(eps=1e-8):
        c2s_vec = (start - center) / (np.linalg.norm(start - center) + eps)
        c2m_vec = (mid - center) / (np.linalg.norm(mid - center) + eps)
        c2e_vec = (end - center) / (np.linalg.norm(end - center) + eps)
        angle_s, angle_m, angle_e = angle_from_vector_to_x(c2s_vec), angle_from_vector_to_x(c2m_vec), \
                                    angle_from_vector_to_x(c2e_vec)
        angle_s, angle_e = min(angle_s, angle_e), max(angle_s, angle_e)
        if not angle_s < angle_m < angle_e:
            angle_s, angle_e = angle_e - np.pi * 2, angle_s
        return angle_s, angle_e
    angle_s, angle_e = get_angles_counterclockwise()
    return Arc(start, end, center, radius, start_angle=angle_s, end_angle=angle_e, mid_point=mid)

def add_circle(center, radius):
    center = np.array(center)
    return Circle(center, radius)

from lib.sketch import Loop, Profile
# Loops
def add_loop(curves):
    res =  Loop(curves)
    res.reorder()
    def autofix(loop):
        if len(loop.children) <= 1:
            return
        if isinstance(loop.children[0], Circle):
            return
        for i in range(0, len(loop.children) - 1):
            if not np.allclose(loop.children[i].end_point, loop.children[i+1].start_point):
                loop.children[i+1].start_point = loop.children[i].end_point
                print("warning: fixing loop")
        if not np.allclose(loop.children[len(loop.children) - 1].end_point, loop.children[0].start_point):
            loop.children[len(loop.children) - 1].start_point = loop.children[0].end_point
            print("warning: fixing loop")
            
    autofix(res)
    return res

# Sketch-Profile
def add_profile(loops):
    return Profile(loops)

from lib.extrude import CoordSystem, Extrude, CADSequence
from lib.math_utils import polar_parameterization
def find_n_from_x_and_y(x, y):
    """
    Given vectors x and y, find a vector n such that y = n × x.
    Assumes that n is orthogonal to x.
    
    Parameters:
    x (numpy array): The vector x.
    y (numpy array): The vector y.
    
    Returns:
    numpy array: The vector n.
    """
    # Step 1: Compute the cross product of x and y to get n'
    n_prime = np.cross(x, y)
    
    # Step 2: Normalize n' to get the unit vector
    n_prime_unit = n_prime / np.linalg.norm(n_prime)
    
    # Step 3: Determine the correct sign of n_prime_unit
    # To ensure y = n × x, we should check if the direction is correct
    if np.allclose(np.cross(n_prime_unit, x), y):
        n = n_prime_unit
    else:
        n = -n_prime_unit
    
    return n

def add_sketchplane(origin, normal, x_axis, y_axis):
    origin = np.array(origin)
    normal = np.array(normal)
    x_axis = np.array(x_axis)
    y_axis = np.array(y_axis)
    #print(y_axis)
    normal_axis = find_n_from_x_and_y(x_axis, y_axis)
    # get theta and phi
    theta, phi, gamma = polar_parameterization(normal_axis, x_axis)
    #print(normal_axis, x_axis)
    #print(theta, phi, gamma)
    return CoordSystem(origin, theta, phi, gamma)

class Sketch(object):
    def __init__(self, sketch_plane, profile, sketch_position, sketch_size):
        self.sketch_plane = sketch_plane
        self.profile = profile
        self.sketch_position = sketch_position
        self.sketch_size = sketch_size

def add_sketch(sketch_plane, profile, sketch_position=[0.0,0.0,0.0], sketch_size=0):
    return Sketch(sketch_plane, profile, np.array(sketch_position), sketch_size)

cad_seq = []
def add_extrude(sketch: Sketch, operation, type, extent_one, extent_two):
    res = Extrude(
        sketch.profile, 
        sketch.sketch_plane,
        np.intc(operation), np.intc(type), np.double(extent_one), np.double(extent_two),
        np.double(sketch.sketch_position),
        np.double(sketch.sketch_size)
    )
    cad_seq.append(res)
    return res

def _process(path, path_o):
    global cad_seq
    cad_seq.clear()
    with open(path, 'r') as file:
        code = file.read()
    # 执行读取到的代码
    exec(code)
    cad = CADSequence(cad_seq)
    #print(cad)
    out_shape = create_CAD(cad)
        
    write_step_file(out_shape, path_o)

error_list = []

from lib.file_utils import ensure_dir

parser = argparse.ArgumentParser()
parser.add_argument('--src', type=str, required=True, help="source folder")
parser.add_argument('-o', '--outputs', type=str, default=None, help="save folder")
args = parser.parse_args()

src_dir = args.src
print(src_dir)
out_paths = sorted(glob.glob(os.path.join(src_dir, "*.{}".format("py"))))
save_dir = args.src + "_step" if args.outputs is None else args.outputs
ensure_dir(save_dir)

import traceback

for path in out_paths:
    name = path.split("/")[-1].split(".")[0]
    try:
        save_path = os.path.join(save_dir, name + ".step")
        _process(path, save_path)
        
    except Exception as e:
        print("load and create failed.")
        traceback.print_exc()
        print(name)
        error_list.append(name)

for error in error_list:
    print(error)