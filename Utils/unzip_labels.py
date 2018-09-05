# unzip label files
# tianye li

import os
from os.path import join, basename, exists
import numpy as np
from glob import glob
from time import time
from utils import list_dirs

# -----------------------------------------------------------------------------

def unzip_one_folder( data_dir, verbose=False ):

    # parse
    semantic_paths = sorted( glob( join( data_dir, '*2d-label-filt.zip' ) ) ) # only filtered folder
    if semantic_paths and len(semantic_paths) != 1:
        raise RuntimeError( 'unexpected number for semantic label files' )
    semantic_zip_path = semantic_paths[0]

    instance_paths = sorted( glob( join( data_dir, '*2d-instance-filt.zip' ) ) ) # only filtered folder
    if instance_paths and len(instance_paths) != 1:
        raise RuntimeError( 'unexpected number for instance instance files' )
    instance_zip_path = instance_paths[0]

    # unzip
    def unzip( file_path, dst_dir ):
        zip_name = basename( file_path )
        folder_name = zip_name[:-4] # hardcode: corresponds to .zip
        target_dir = join( dst_dir, folder_name )

        if not exists( target_dir ):
            os.system( "unzip -qq -o %s -d %s" % ( file_path, dst_dir ) )
            if verbose:
                print( '\nunzipped %s' % ( file_path ) )
                print( '      to %s' % ( dst_dir ) )
        else:
            if verbose:
                print( '\nskipped %s' % ( file_path ) )

    unzip( semantic_zip_path, data_dir )
    unzip( instance_zip_path, data_dir )

# -----------------------------------------------------------------------------

def run_unzip_all( data_root ):

    # hardcode scene range:
    # scene_list = list_dirs( data_root ) # parse all
    scene_list = [ 'scene%04d_00' % (idx) for idx in range(0,20) ] # parse 0-19, enforce scan 00

    for sid, this_scene in enumerate( scene_list ):
        print( "\nprocessing %d of %d: %s" % ( sid, len(scene_list), this_scene ) )
        this_data_dir = join( data_root, this_scene )

        timer_start = time()
        unzip_one_folder( this_data_dir, verbose=True )
        print( "using %f sec" % ( time() - timer_start ) )

# -----------------------------------------------------------------------------

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', required=True, help='root dir to store scannet dataset')
    opt = parser.parse_args()
    print(opt)
    run_unzip_all( opt.data_root )