"""
footap - Package d'analyse des touches de balle au football
"""

from .video_processing import track_ball_and_feet
from .main import analyze_ball_touch, main

__version__ = "1.0"
__author__ = "Dims"

# Exposer les fonctions principales
__all__ = ['analyze_ball_touch', 'track_ball_and_feet', 'main']
