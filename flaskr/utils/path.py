import os
import shutil
from flaskr.configs.logger import log_system

# 获取当前代码所在文件所属的文件夹路径
# os.path.dirname(__file__)


class __PathOperate:

    def mkdir(self, dir_path: str, clear=False):
        abspath = os.path.abspath(dir_path)

        if os.path.exists(abspath) and os.path.isdir(abspath):
            if clear:
                self.remove(abspath)
            else:
                return abspath

        if not os.path.exists(abspath):
            try:
                os.makedirs(abspath)
            except Exception as e:
                log_system.warning(f'create directory {abspath} with error {e}')

        return abspath

    def remove(self, path: str):
        abspath = os.path.abspath(path)

        if not os.path.exists(abspath):
            return

        if os.path.isdir(abspath):
            def onerror(func, exc_path, exc_info):
                log_system.warning(f'remove {exc_path} with error {exc_info[1]}')

            shutil.rmtree(path=abspath, ignore_errors=False, onerror=onerror)
        else:
            try:
                os.remove(abspath)
            except Exception as e:
                log_system.warning(f'remove file {abspath} with error {e}')


Path = __PathOperate()
