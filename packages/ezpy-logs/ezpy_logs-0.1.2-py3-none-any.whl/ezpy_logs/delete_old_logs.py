# -*- coding: utf-8 -*-

import logging
import os
import shutil
import time

def delete_old_logs(root_dir: str, n_days: int = 30):
    logger1 = logging.getLogger(__name__)
    logger1.debug(f"Deleting files older than {n_days} in {root_dir}")
    n_days_ago = time.time() - int(n_days * 86400)
    for root_path, _, files in os.walk(root_dir):
        for file_ in files:
            path = os.path.join(root_path, file_)
            try:
                if os.stat(path).st_mtime <= n_days_ago:
                    if os.path.isfile(path):
                        try:
                            os.remove(path)
                            logger1.debug(f"Removed file {file_}")
                        except Exception:
                            logger1.exception(f"Could not remove file: {file_}")
                    else:
                        try:
                            shutil.rmtree(path, ignore_errors=True)
                            logger1.debug(f"Removed directory {file_}")
                        except Exception:
                            logger1.exception(f"Could not remove directory: {file_}")
            except FileNotFoundError:
            # Because of a race condition with a concurrent cron job using logger.
                logger1.debug(f"File no longer exists: {path}")
            except Exception as e:
                logger1.exception(f"Error processing {path}: {str(e)}")
