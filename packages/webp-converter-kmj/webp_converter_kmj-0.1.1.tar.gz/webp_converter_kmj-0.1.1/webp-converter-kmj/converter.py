import os
from pathlib import Path
from PIL import Image

def convert_to_webp(input_dir, output_dir=None, quality=100):
    """
    디렉토리의 모든 하위 폴더를 재귀적으로 탐색하여 이미지를 WebP로 변환합니다.
    """
    input_path = Path(input_dir)
    
    if output_dir is None:
        output_dir = input_dir
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    supported_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'}
    
    converted_count = 0
    error_count = 0
    
    for current_file in input_path.rglob('*'):
        if current_file.is_file() and current_file.suffix.lower() in supported_extensions:
            try:
                relative_path = current_file.relative_to(input_path)
                output_file = output_path / relative_path.with_suffix('.webp')
                
                output_file.parent.mkdir(parents=True, exist_ok=True)
                
                with Image.open(current_file) as img:
                    img.save(output_file, 'WEBP', quality=quality)
                    converted_count += 1
            
            except Exception as e:
                error_count += 1
    
    return converted_count, error_count