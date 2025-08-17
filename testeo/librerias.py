from typing import Optional, Annotated

import numpy

nparr = numpy.array([67,89,45,23,56,78,90,12,34,56,78,90,12,34,56,78,90])

print(numpy.__version__)
print(nparr*2)

def say(sms: str | None = None) -> str:
    """
    Function to return a string.
    :param sms: Optional string parameter.
    :return: The input string or a default message.
    """
    if sms is None:
        return 'No hay mensaje'
    return sms

print(say("Hola amigos"))

def say_hi(sms: Annotated[Optional[str], 'Mensaje a imprimir']) -> str:
    """
    Function to return a string with a greeting.
    :param sms: String parameter to greet.
    :return: A greeting message.
    """
    return f'Hola {sms}'

print(say_hi('Pythonistas'))