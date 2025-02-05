# FootAP

FootAP (FOOTball Analysis Package) is a Python package for analyzing ball touches in football videos.

## Installation

```bash
pip install footap
```

## Usage

The `analyze_ball_touch` function requires only one mandatory parameter: the video path.

### Minimal Usage (single parameter)
```python
from footap import analyze_ball_touch

# Only the video path is required
analyze_ball_touch("video.mp4")

# or with the parameter name
analyze_ball_touch(input_video_path="video.mp4")
```

This simple usage will:
- Analyze the video in silent mode
- Generate a results file (video_results.txt)

### Available Optional Parameters
```python
analyze_ball_touch(
    input_video_path="video.mp4",
    # All these parameters are optional:
    display_processing=True,    # To see real-time analysis
    generate_video=True,        # To create an annotated video
    video_orientation=90        # To rotate the video if needed
)
```

## Results

The program automatically generates:
1. A text file containing:
   - Number of touches for each foot
   - Chronological sequence of touches

2. An annotated video (if generate_video=True) showing:
   - Ball detection
   - Feet detection
   - Real-time touch counting

## Dependencies

- OpenCV (opencv-python, opencv-contrib-python)
- MediaPipe
- NumPy
- Ultralytics (YOLO)
- Pillow

## License

This project is licensed under the MIT License.
