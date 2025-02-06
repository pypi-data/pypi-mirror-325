'''
utilities to queue function calls. 

This is helpful when there are functions we need to be run in sequence even when 
the callers are from different threads eg in a web server.

An example is if we want to process one payment at a go regardless of how many 
concurrent threads try to do so at once

usage: decorate your functiona/callable with the `queueCalls` decorator
'''
from threading import Thread, Lock
from functools import wraps
from queue import Queue
from typing import Callable
import sys

from kisa_utils.response import Response, Ok, Error
from kisa_utils.codes import new as newCode

__MAIN_LOCK = Lock()
__WORKER_LOCKS_AND_QUEUES = {}

def __x____createWorker(func:Callable) -> Response:
    lock:Lock = __WORKER_LOCKS_AND_QUEUES[func]['lock']
    queue:Queue = __WORKER_LOCKS_AND_QUEUES[func]['queue']
    resultsDict:dict = __WORKER_LOCKS_AND_QUEUES[func]['resultsDict']

    def worker():
        while 1:
            # wait until tasks are available...
            taskId, args, kwargs = queue.get()

            try:
                resp = func(*args, **kwargs)
                if not isinstance(resp, Response):
                    resp = Error(f'{func.__name__} returned {type(resp)} instead of {Response}')
            except Exception as e:
                resp = Error(f'{func.__name__}: {e}')
            
            with lock:
                resultsDict[taskId] = resp

    thrd = Thread(target=worker, daemon=True)
    thrd.start()

    return Ok()

def __createWorker(group:str) -> Response:
    lock:Lock = __WORKER_LOCKS_AND_QUEUES[group]['lock']
    queue:Queue = __WORKER_LOCKS_AND_QUEUES[group]['queue']
    resultsDict:dict = __WORKER_LOCKS_AND_QUEUES[group]['resultsDict']

    def worker():
        while 1:
            # wait until tasks are available...
            taskId, func, args, kwargs = queue.get()

            try:
                resp = func(*args, **kwargs)
                if not isinstance(resp, Response):
                    resp = Error(f'{func.__name__} returned {type(resp)} instead of {Response}')
            except Exception as e:
                resp = Error(f'{func.__name__}: {e}')
            
            with lock:
                resultsDict[taskId] = resp

    thrd = Thread(target=worker, daemon=True)
    thrd.start()

    return Ok()


def __x__queueCalls(func:Callable):
    '''
    decorator to queue function calls
    '''
    if func in __WORKER_LOCKS_AND_QUEUES:
        sys.exit(f'a worker already exists for the function `{func}`')
    
    if func.__annotations__.get('return') != Response:
        sys.exit(f'{func.__name__} must have {Response} as its return type hint')

    with __MAIN_LOCK:
        __WORKER_LOCKS_AND_QUEUES[func] = {
            'lock':Lock(), # to serialize the function call results 
            'queue': Queue(), # to hold function call data
            'resultsDict': {}, # function call results
        }

        resp = __createWorker(func)
        if not resp:
            sys.exit(resp.log)

    lock:Lock = __WORKER_LOCKS_AND_QUEUES[func]['lock']
    queue:Queue = __WORKER_LOCKS_AND_QUEUES[func]['queue']
    resultsDict:dict = __WORKER_LOCKS_AND_QUEUES[func]['resultsDict']

    @wraps(func)
    def wrapper(*args:tuple, **kwargs:dict) -> Response:
        taskId = newCode()

        queue.put((taskId, args, kwargs))

        while taskId not in resultsDict: pass

        resp = resultsDict[taskId]

        with lock:
            del resultsDict[taskId]

        return resp

    return wrapper

def __queueCallsDecorator(func: Callable, group: str):
    """ Actual decorator logic. """
    if func.__annotations__.get('return') != Response:
        sys.exit(f'{func.__name__} must have {Response} as its return type hint')

    if group not in __WORKER_LOCKS_AND_QUEUES:
        with __MAIN_LOCK:
            __WORKER_LOCKS_AND_QUEUES[group] = {
                'lock': Lock(),
                'queue': Queue(),
                'resultsDict': {},
            }

            resp = __createWorker(group)
            if not resp:
                sys.exit(resp.log)

    lock = __WORKER_LOCKS_AND_QUEUES[group]['lock']
    queue = __WORKER_LOCKS_AND_QUEUES[group]['queue']
    resultsDict = __WORKER_LOCKS_AND_QUEUES[group]['resultsDict']

    @wraps(func)
    def decorated(*args, **kwargs) -> Response:
        taskId = newCode()
        queue.put((taskId, func, args, kwargs))

        while taskId not in resultsDict:
            pass

        resp = resultsDict[taskId]

        with lock:
            del resultsDict[taskId]

        return resp

    return decorated

def queueCalls(func: Callable = None, *, group: str| None = None):
    '''
    Decorator to queue function calls as a group.
    Can be used with or without parentheses.

    Example:

    @queueCalls # decorator not called with parentheses
    def myFunc(): pass

    or

    @queueCalls() # decorator called with empty parentheses, same as first one
    def myFunc(): pass

    or

    @queueCalls(group="my_group") # decorator called with parentheses, specify ONLY the `group` 
    def myFunc(): pass
    '''
    # If the decorator is used without parentheses, the function is passed as the first argument
    if func:
        if callable(func):
            return __queueCallsDecorator(func, newCode())  # Assign default group if no group is provided
        else:
            sys.exit(f'`queueCalls` must be run in one of the following flavours; `@queueCalls`, `@queueCalls()`,`@queueCalls(group=STRING)`')

    if isinstance(group, str):
        group = group.strip()
        if not group:
            sys.exit('empty group given. use `None` if you don’t want to specify the group')
    elif group is not None:
        sys.exit('unexpected type for `group`. Expected `str | None`')

    # If used with parentheses, return the actual decorator
    def wrapper(f: Callable):
        return __queueCallsDecorator(f, group if group else newCode())

    return wrapper
