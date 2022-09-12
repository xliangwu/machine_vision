import paddle
import os

paddle.utils.run_check()

# file name with extension
file_name = os.path.basename('/root/file.ext')

# file name without extension
print(os.path.splitext(file_name)[0])