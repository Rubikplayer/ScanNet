# extrace rgbd streams
# tianye li

import os
from os.path import join, basename, exists
import numpy as np
from glob import glob
from time import time
from utils import list_dirs, safe_mkdir

# -----------------------------------------------------------------------------

def extract_one_folder( data_dir, verbose=False ):

    # parse
    sens_paths = sorted( glob( join( data_dir, '*.sens' ) ) )
    if sens_paths is None or len(sens_paths) != 1:
        raise RuntimeError( 'unexpected number for semantic label files' )
    sens_path = sens_paths[0]

    # extract
    script_path = '../SensReader/python/reader.py'
    output_path = join( data_dir, 'rgbd' )
    safe_mkdir( output_path )
    cmd = "python %s --filename %s --output_path %s" % ( script_path, sens_path, output_path )
    print( "\nrunning: %s" % ( cmd ) )
    # os.system( cmd )
    print( "done: %s" % ( output_path ) )

# -----------------------------------------------------------------------------

def run_extract_all( data_root ):

    # hardcode scene range:
    # scene_list = list_dirs( data_root ) # parse all
    scene_list = [ 'scene%04d_00' % (idx) for idx in range(0,20) ] # parse 0-19, enforce scan 00

    for sid, this_scene in enumerate( scene_list ):
        print( "\nprocessing %d of %d: %s" % ( sid, len(scene_list), this_scene ) )
        this_data_dir = join( data_root, this_scene )

        timer_start = time()
        extract_one_folder( this_data_dir, verbose=True )
        print( "using %f sec" % ( time() - timer_start ) )

# -----------------------------------------------------------------------------

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', required=True, help='root dir to store scannet dataset')
    opt = parser.parse_args()
    print(opt)

    run_extract_all( opt.data_root )