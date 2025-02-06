# WebP 이미지 변환기

## 설치 방법

```bash
pip install webp-converter-kmj
```

## 사용 방법

### GUI 실행

```bash
webp-converter-kmj-gui
```

### Python 스크립트에서 사용

```python
from webp_converter import convert_to_webp

# 폴더 내 이미지를 WebP로 변환
convert_to_webp('/input/path', '/output/path', quality=100)
```
