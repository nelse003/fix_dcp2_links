import os
# Check whether symbolic link fails
def symlink_fail(path):
    if not os.path.exists(os.readlink(path)):
        print('path %s is a broken symlink' % path)
    return os.path.exists(os.readlink(path))

# Loop over all DCP2 symbolic links

ini_model_path = "/dls/labxchem/data/2016/lb13385-64/processing/analysis/initial_model"

for folder in os.listdir(ini_model_path):

    aimless_log_symlink_path = os.path.join(ini_model_path,
                                            folder,
                                            "{}.log".format(folder))
    symlink_fail(aimless_log_symlink_path)

# Write link to Database