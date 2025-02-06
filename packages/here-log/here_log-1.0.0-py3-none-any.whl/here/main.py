import traceback
import os


class Here:
    def __str__(self):
        stack = traceback.extract_stack()
        caller_frame = stack[-2]
        filename = os.path.basename(caller_frame.filename)

        if caller_frame.name == '<module>':
            return f"{caller_frame.filename} - {filename} - line {caller_frame.lineno}"
        return f"{caller_frame.filename} - {filename} - line {caller_frame.lineno}"


    def __call__(self, message=None):
        stack = traceback.extract_stack()
        caller_frame = stack[-2]
        filename = os.path.basename(caller_frame.filename)
        if message:
            print(f"{caller_frame.filename} - {filename} - line {caller_frame.lineno}: {message}")
        else:
            print(f"{caller_frame.filename} - {filename} - line {caller_frame.lineno}")


here = Here()
