'''
util
tianye li
'''
import numpy as np
import sys
import os
from os.path import exists, join

# -----------------------------------------------------------------------------

def load_binary_pickle( filepath ):
    if sys.version_info[0] < 3:
        import cPickle as pickle
    else:
        import pickle

    with open( filepath, 'rb' ) as f:
        data = pickle.load( f )
    return data

# -----------------------------------------------------------------------------

def save_binary_pickle( data, filepath ):
    if sys.version_info[0] < 3:
        import cPickle as pickle
    else:
        import pickle
    with open( filepath, 'wb' ) as f:
        pickle.dump( data, f )

# -----------------------------------------------------------------------------

def save_npy( data, filepath ):
    with open( filepath, 'wb' ) as fp:
        np.save( fp, data )

# -----------------------------------------------------------------------------

def load_npy( filepath ):
    data = None
    with open( filepath, 'rb' ) as fp:
        data = np.load( fp )
    return data

# -----------------------------------------------------------------------------

def get_extension( file_path ):
    import os.path
    return os.path.splitext( file_path )[1]

# -----------------------------------------------------------------------------

def safe_mkdir( file_dir, enable_777=False ):
    if not os.path.exists( file_dir ):
        os.mkdir( file_dir )
        if enable_777:
            chmod_777( file_dir )

# -----------------------------------------------------------------------------

def safe_mkdirs( paths, enable_777=False ):
    if isinstance( paths, list ) and not isinstance( paths, str ):
        for path in paths:
            safe_mkdir( path, enable_777 )
    else:
        safe_mkdir( paths, enable_777 )

# -----------------------------------------------------------------------------

def list_dirs( file_dir ):
    dirs = os.listdir( file_dir )
    remove_idx = -1
    for did, this_dir in enumerate( dirs ):
        if this_dir == '.DS_Store':
            remove_idx = did
            break
    if remove_idx >= 0:
        dirs.pop( remove_idx )
    return dirs

# -----------------------------------------------------------------------------

def chmod_777( file_dir ):
    cmd = 'chmod -R 777 %s' % ( file_dir )
    os.system( cmd )