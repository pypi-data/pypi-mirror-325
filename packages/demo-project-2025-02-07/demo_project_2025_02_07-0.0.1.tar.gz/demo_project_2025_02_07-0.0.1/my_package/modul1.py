# modul1.py
#import modul2
try:
    from . import modul2
except ImportError:
    import modul2

def funktion1():
    print("Grüße aus Modul 1!")
