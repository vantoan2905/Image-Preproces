


import argparse
import cv2
import numpy as np
import logging
from pathlib import Path
from typing import Optional, Tuple, Union
from datetime import datetime
import sys
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('arpr.log')
    ]
)
logger = logging.getLogger(__name__)

class AspectRatioPreserving:
    
    def __init__(self, img_path: Union[str, Path], new_width: Optional[int] = None, 
                 new_height: Optional[int] = None):
        self.img_path = Path(img_path)
       
        self.img = cv2.imread(str(self.img_path))
        
            
        self.height, self.width = self.img.shape[:2]
        self.aspect_ratio = self.width / self.height
        self.new_width = new_width
        self.new_height = new_height
        
        logger.debug(f"Initialized {img_path}: {self.width}x{self.height}")
    
    def get_dimensions(self) -> Tuple[int, int]:
        if self.new_width and not self.new_height:
            target_width = self.new_width
            target_height = int(target_width / self.aspect_ratio)
        elif self.new_height and not self.new_width:
            target_height = self.new_height
            target_width = int(target_height * self.aspect_ratio)
        else:
            target_width = self.new_width
            target_height = self.new_height
            
        return target_width, target_height
    
    def resize(self, interpolation: int = cv2.INTER_LANCZOS4) -> np.ndarray:
        target_width, target_height = self.get_dimensions()
        return cv2.resize(self.img, (target_width, target_height), 
                         interpolation=interpolation)
    
    def save(self, output_path: Union[str, Path], quality: int = 95) -> None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        img_resized = self.resize()
        
        if output_path.suffix.lower() in ['.jpg', '.jpeg']:
            cv2.imwrite(str(output_path), img_resized, 
                       [cv2.IMWRITE_JPEG_QUALITY, quality])
        elif output_path.suffix.lower() in ['.png']:
            cv2.imwrite(str(output_path), img_resized)
        else:
            raise ValueError(f"Unsupported format: {output_path.suffix}")
            
        logger.info(f"Saved: {output_path}")

def process_single(args: argparse.Namespace) -> None:
    try:
        processor = AspectRatioPreserving(args.input_path, args.width, args.height)
        
        if args.output:
            output_dir = Path(args.output)
            output_path = output_dir / f"resized_{Path(args.input_path).name}"
        else:
            input_path = Path(args.input_path)
            output_path = input_path.parent / f"resized_{input_path.name}"
        
        processor.save(output_path, quality=args.quality)
        logger.info(f"Successfully processed: {args.input_path}")
        
    except Exception as e:
        logger.error(f"Error processing {args.input_path}: {str(e)}")
        sys.exit(1)

def process_batch(args: argparse.Namespace) -> None:
    input_dir = Path(args.input_path)
    output_dir = Path(args.output) if args.output else input_dir / "resized"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    image_files = []
    for ext in ['.jpg', '.jpeg', '.png']:
        image_files.extend(input_dir.glob(f"*{ext}"))

    
    logger.info(f"Found {len(image_files)} images to process")
    
    failed = []
    for img_path in tqdm(image_files, desc="Processing images"):
        try:
            processor = AspectRatioPreserving(img_path, args.width, args.height)
            output_path = output_dir / img_path.name
            processor.save(output_path, quality=args.quality)
        except Exception as e:
            logger.error(f"Error processing {img_path}: {str(e)}")
            failed.append(img_path)
    
    # Report results
    success_count = len(image_files) - len(failed)
    logger.info(f"Processed {success_count}/{len(image_files)} images successfully")
    if failed:
        logger.warning(f"Failed to process {len(failed)} images")
        for path in failed:
            logger.warning(f"Failed: {path}")

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Aspect Ratio Preserving Resize (ARPR) Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument("input_path", help="Input image or directory path")
    parser.add_argument("--width", type=int, help="Target width in pixels")
    parser.add_argument("--height", type=int, help="Target height in pixels")
    parser.add_argument("--quality", type=int, default=95,
                        help="JPEG quality (0-100, default: 95)")
    parser.add_argument("--output", "-o", help="Output directory path")
    parser.add_argument("--batch", "-b", action="store_true",
                        help="Process all images in input directory")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Enable verbose logging")
    
    args = parser.parse_args()
    
    if not args.width and not args.height:
        parser.error("Either --width or --height must be specified")
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if args.batch:
        process_batch(args)
    else:
        process_single(args)

if __name__ == "__main__":
    main()