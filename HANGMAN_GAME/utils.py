import os

def ekranı_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')
def step_0 ():
    ekranı_temizle()
    print(r"""
      ┌───┐
      │   │
          │
          │
          │
          │
    ══════╧══
    """)

def step_1 ():
    ekranı_temizle()
    print(r"""
      ┌───┐
      │   │
      O   │
          │
          │
          │
    ══════╧══
        """)

def step_2 ():
    ekranı_temizle()
    print(r"""
      ┌───┐
      │   │
      O   │
      │   │
          │
          │
    ══════╧══
        """)

def step_3 ():
    ekranı_temizle()
    print(r"""
      ┌───┐
      │   │
      O   │
     /│   │
          │
          │
    ══════╧══
        """)

def step_4 ():
    ekranı_temizle()
    print(r"""
      ┌───┐
      │   │
      O   │
     /│\  │
          │
          │
    ══════╧══
        """)

def step_5 ():
    ekranı_temizle()
    print(r"""
      ┌───┐
      │   │
      O   │
     /│\  │
     /    │
          │
    ══════╧══
        """)

def step_6 ():
    ekranı_temizle()
    print(r"""
      ┌───┐
      │   │
      O   │
     /│\  │
     / \  │
          │
    ══════╧══
        """)