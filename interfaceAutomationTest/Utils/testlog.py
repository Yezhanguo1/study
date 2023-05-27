import traceback
import util_log
from util_log import Logger

if __name__ == '__main__':
    try:
        util_log.onedome()
    except Exception as e:
        Logger().getlog().error(f"main Expection: {traceback.format_exc()}")