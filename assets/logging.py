from assets.config import conf
from interactions import User
from time import time

def file_log(text: str):
    if not conf.get("enable_logging"): return
    logfile = conf.get("log_file")
    
    
    open(logfile, 'a').write(
                f"[{time()}]: {text}\n"
            )

def log(user: User,
        res : bool,):
    if not conf.get("enable_logging"): return
    
    if res is True:
        if conf.get("success-log_to_console"): 
            print(f"User ID: {str(user.id)} ({user.display_name}) has SUCCESSFULLY authenticated.")
        
        if conf.get("success-log_to_file"):
            file_log(f"User ID: {str(user.id)} ({user.display_name}) has SUCCESSFULLY authenticated.")
    elif res is False:
        if conf.get("failure-log_to_console"): print(f"User ID: {str(user.id)} ({user.display_name}) has FAILED to authenticate.")
        
        if conf.get("failure-log_to_file"):
            file_log(f"User ID: {str(user.id)} ({user.display_name}) has FAILED to authenticate.")