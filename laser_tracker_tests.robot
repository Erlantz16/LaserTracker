*** Settings ***
Library           LaserLibrary.py

*** Test Cases ***
Controlar Laser Tracker
    Conectar Laser Tracker
    # Mover Laser Tracker 10 20 30
    # Desconectar Laser Tracker

Mover Laser Tracker
    [Arguments] ${x} ${y} ${z}
    MoverLaserTracker ${x} ${y} ${z}

Desconectar Laser Tracker
    DesconectarLaserTracker