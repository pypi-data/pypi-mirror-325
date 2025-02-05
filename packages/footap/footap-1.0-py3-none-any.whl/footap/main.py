try:
    from .video_processing import track_ball_and_feet
except ImportError:
    from video_processing import track_ball_and_feet
import argparse
import sys
import os

def get_output_names(input_video_path):
    """Génère les noms des fichiers de sortie à partir du nom de la vidéo d'entrée"""
    # Extraire le nom de base sans extension et le chemin
    base_path = os.path.dirname(input_video_path)
    base_name = os.path.splitext(os.path.basename(input_video_path))[0]
    
    # Générer les noms complets
    output_video = os.path.join(base_path, f"{base_name}_output.mp4")
    output_file = os.path.join(base_path, f"{base_name}_results.txt")
    
    return output_video, output_file

def analyze_ball_touch(input_video_path, display_processing=False, generate_video=False, video_orientation=0):
    """
    Analyse une vidéo de jonglage de football et compte les touches de balle pour chaque pied.
    Génère un rapport détaillé avec le nombre de touches et leur séquence chronologique.
    
    Args:
        input_video_path (str): Chemin d'accès à la vidéo d'entrée
        display_processing (bool, optional): Si True, affiche le traitement en temps réel. Par défaut False (mode silencieux)
        generate_video (bool, optional): Si True, génère une vidéo de sortie avec les annotations. Par défaut False
        video_orientation (int, optional): Orientation de la vidéo en degrés (0, 90, 180, 270). Par défaut 0
    """
    output_video, output_file = get_output_names(input_video_path)
    
    track_ball_and_feet(
        video_source=input_video_path,
        output_video=output_video if generate_video else None,
        output_file=output_file,
        save_output_video=generate_video,
        save_output_file=True,
        silent_mode=not display_processing,
        video_orientation=video_orientation
    )

def parse_args(args=None):
    """Parse les arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(description='Analyse de touches de balle au football')
    parser.add_argument('video', help='Chemin vers la vidéo à analyser')
    parser.add_argument('-o', '--output', help='Nom du fichier vidéo de sortie (optionnel)')
    parser.add_argument('-r', '--results', help='Nom du fichier de résultats (optionnel)')
    parser.add_argument('--orientation', type=int, choices=[0, 90, 180, 270], default=0,
                      help='Orientation de la vidéo (0, 90, 180, 270 degrés)')
    parser.add_argument('--display', action='store_true',
                      help='Afficher le traitement en temps réel')
    parser.add_argument('--save-video', action='store_true',
                      help='Générer une vidéo de sortie avec les annotations')
    
    return parser.parse_args(args)

def main(args=None):
    """Point d'entrée principal, fonctionne en mode script ou ligne de commande"""
    # Si aucun argument n'est passé et qu'on exécute le script directement
    if args is None and len(sys.argv) == 1:
        # Mode exécution directe du script
        analyze_ball_touch(
            input_video_path="jongle.mp4",  # Valeur par défaut
            display_processing=True,
            generate_video=False,  # Par défaut, pas de vidéo
            video_orientation=0
        )
    else:
        # Mode ligne de commande
        args = parse_args(args)
        
        # Obtenir les noms de fichiers de sortie
        default_output_video, default_output_file = get_output_names(args.video)
        
        # Utiliser les noms spécifiés ou les noms par défaut
        output_video = args.output if args.output else default_output_video
        output_file = args.results if args.results else default_output_file
        
        track_ball_and_feet(
            video_source=args.video,
            output_video=output_video if args.save_video else None,
            output_file=output_file,
            video_orientation=args.orientation,
            save_output_video=args.save_video,
            save_output_file=True,
            silent_mode=not args.display
        )

if __name__ == "__main__":
    main()