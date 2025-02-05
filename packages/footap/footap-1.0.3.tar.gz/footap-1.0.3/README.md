# FootAP

FootAP (FOOTball Analysis Package) est un package Python pour analyser les touches de balle dans une vidéo de football. Il utilise YOLO pour la détection de balle et MediaPipe pour la détection des pieds.

## Installation

```bash
pip install footap
```

## Utilisation

La fonction `analyze_ball_touch` ne nécessite qu'un seul paramètre obligatoire : le chemin de la vidéo.

### Utilisation minimale (un seul paramètre)
```python
from footap import analyze_ball_touch

# Seul le chemin de la vidéo est obligatoire
analyze_ball_touch("video.mp4")

# ou avec le nom du paramètre
analyze_ball_touch(input_video_path="video.mp4")
```

Cette utilisation simple va :
- Analyser la vidéo en mode silencieux
- Générer un fichier de résultats (video_results.txt)

### Paramètres optionnels disponibles
```python
analyze_ball_touch(
    input_video_path="video.mp4",
    # Tous ces paramètres sont optionnels :
    display_processing=True,    # Pour voir l'analyse en temps réel
    generate_video=True,        # Pour créer une vidéo avec annotations
    video_orientation=90        # Pour pivoter la vidéo si nécessaire
)
```

## Résultats

Le programme génère automatiquement :
1. Un fichier texte contenant :
   - Le nombre de touches pour chaque pied
   - La séquence chronologique des touches

2. Une vidéo annotée (si generate_video=True) montrant :
   - La détection de la balle
   - La détection des pieds
   - Le comptage en temps réel

## Dépendances

- OpenCV (opencv-python, opencv-contrib-python)
- MediaPipe
- NumPy
- Ultralytics (YOLO)
- Pillow

## Licence

Ce projet est sous licence MIT.
