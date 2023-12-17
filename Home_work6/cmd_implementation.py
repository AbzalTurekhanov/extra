import os
from CommandPrompt import CommandPrompt, CommandPromptError

while (command := input(os.getcwd() + '>')) != 'exit':
    command, *args = command.split()
    try:
        eval(f'CommandPrompt.{command}{tuple(args)}')
    except CommandPromptError as e:
        print(e)
    except BaseException as e:
        print('Invalid input. Please enter valid choice.')

print('Exiting Command Prompt. Goodbye!')

