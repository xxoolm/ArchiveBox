# __package__ = 'archivebox.filestore'

# import time
# import os
# from datetime import timedelta
# from typing import ClassVar

# from django.utils import timezone

# from rich import print

# from statemachine import State, StateMachine

# from workers.actor import ActorType

# from .models import File

# class FileMachine(StateMachine, strict_states=True):
#     """
#     State machine for managing File lifecycle.

#     https://github.com/ArchiveBox/ArchiveBox/wiki/ArchiveBox-Architecture-Diagrams
#     """
    
#     model: File
#     MAX_LOCK_TIME: ClassVar[int] = 600
    
#     # States
#     unlocked = State(value=File.StatusChoices.UNLOCKED, initial=True)
#     locked = State(value=File.StatusChoices.LOCKED)
    
#     # Transition Events
#     lock = unlocked.to(locked, cond='can_lock')
#     unlock = locked.to(unlocked)
    
    
#     def __init__(self, file, *args, **kwargs):
#         self.file = file
#         super().__init__(file, *args, **kwargs)
        
#     def __repr__(self) -> str:
#         return f'[grey53]File\\[{self.file.ABID}] 🏃‍♂️ Worker\\[pid={os.getpid()}].tick()[/grey53] [blue]{self.file.status.upper()}[/blue] ⚙️ [grey37]Machine[/grey37]'
    
#     def __str__(self) -> str:
#         return self.__repr__()
    
#     @locked.enter
#     def enter_locked(self):
#         print(f'{self}.on_locked() ↳ file.locked_at = now()')
#         self.file.lock_file(seconds=self.MAX_LOCK_TIME)
        
#     def can_lock(self) -> bool:
#         return self.file.status == File.StatusChoices.UNLOCKED
        

# class FileWorker(ActorType[File]):
#     Model = File
#     StateMachineClass = FileMachine
    
#     ACTIVE_STATE: ClassVar[State] = FileMachine.locked
    
#     MAX_CONCURRENT_ACTORS: ClassVar[int] = 4
#     MAX_TICK_TIME: ClassVar[int] = 600
#     CLAIM_FROM_TOP_N: ClassVar[int] = MAX_CONCURRENT_ACTORS * 10



