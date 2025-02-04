import glob
from PIL import Image

class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320,240)):
        """
        path_in : 변환한 이미지 원본 (Ex : images/*.png)
        path_out : 결과 이미지 경로(Ex : output/filename.gif)
        resize : 리사이징 크기((320,240))
        """
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize
        
    def convert_gif(self):
        """
        GIF 이미지 변환 기능 수행
        """
        print(self.path_in, self.path_out, self.resize)
        img, *images = [Image.open(f).convert('RGB').resize(self.resize, Image.Resampling.LANCZOS) for f in sorted(glob.glob(self.path_in))]
        try:
            img.save(
                fp=self.path_out,
                format='GIF',
                append_images=images,
                save_all=True,
                duration=500,
                loop=0
            )        
        except IOError:
            print('Cannot convert', img)

if __name__ == '__main__':        
    c = GifConverter('./project/images/*.png', './project/image_out/result.gif', (320,240))
    
    c.convert_gif()