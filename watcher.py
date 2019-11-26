import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification
import argparse
import git
from git import Repo
import os
import threading
from multiprocessing.dummy import Process
from watchdog.events import PatternMatchingEventHandler

repo_path = ""
branch = ""
old_commit_summary = None
count = 0
commitData = ""
                                     

def get_commits():
    global commitData
    COMMITS_TO_PRINT = 1
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits(branch))[:COMMITS_TO_PRINT]
    for commit in commits:
        name = commit.author.name
        summary = commit.summary
        c_time = commit.authored_datetime
    return summary, name, c_time


def notify():
    notification.notify(
        title='Commit Changes',
        message="{} changes since last commit of \n\"{}\" at {} by {}".format(
            int(count), commitData[0], commitData[2], commitData[1]),
        app_name='Forgit2Commit',
        app_icon=os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'icon.ico')
    )
     
  
def sendToNotify():
    global old_commit_summary
    global count
    global commitData
    commitData = get_commits()
                        
    if old_commit_summary != commitData[0] and old_commit_summary != None:
            count = 0
            old_commit_summary = commitData[0]
    if count % 5 == 0 and count != 0:
            get_commits()
            notify()
            old_commit_summary = commitData[0]
    count += 1
                     
                  
class Watchdog(PatternMatchingEventHandler, Observer):           
    global repo_path 
    paused = False 
                               
                                        
    def __init__(self, path=repo_path, patterns='*', ignore_patterns=["*git*"], logfunc=print):#
        PatternMatchingEventHandler.__init__(self, patterns, ignore_patterns)
        Observer.__init__(self)
        self.schedule(self, path=path, recursive=True)     
        self.log = logfunc
    def set_false(self):
        Watchdog.paused = False
         
    def on_modified(self, event):
        
        timer = threading.Timer(1.0, lambda: Watchdog().set_false())
        if Watchdog.paused is True:
            return
        Watchdog.paused = True    
        if os.path.abspath(repo_path) not in os.path.abspath(event.src_path):
            Watchdog.stop(self)
         
        if not event.is_directory:
            sendToNotify()
        
        timer.start()
        
    def on_created(self, event):
        
        timer = threading.Timer(1.0, lambda: Watchdog().set_false())
        if Watchdog.paused is True:
            return
        Watchdog.paused = True    
        if os.path.abspath(repo_path) not in os.path.abspath(event.src_path):
            Watchdog.stop(self)

        if not event.is_directory:
            sendToNotify()
        
        timer.start()
        
    
class strt():
    watchdog = None
    def set_repo_path(self):
        global count
        global repo_path
        
        global commitData
        try:
            self.watchdog.stop()
        except:
            pass
        self.watchdog = None
        count = 0
        self.watchdog = Watchdog(path=repo_path)
        self.watchdog.start()
        commitData = get_commits()
        
