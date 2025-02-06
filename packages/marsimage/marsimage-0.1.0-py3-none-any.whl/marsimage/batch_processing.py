"""Batch processing of MarsImages for photogrammetry.

These functions are work in progress and subject to change in a future release!
"""

import concurrent.futures
import logging
import os
from pathlib import Path

from tqdm.auto import tqdm

from marsimage import MarsImage
from marsimage.filename import Filename
from marsimage.imagebase import SUPPORTED_PRODUCT_TYPES

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)


def filter_photogrammetry(img):
    """Determine if an image should be used for photogrammetry based on its metadata.

    Parameters
    ----------
    img : MarsImage
        The image to be filtered.

    See Also
    --------
    filter_ecam_photogrammetry
    filter_mcam_photogrammetry
    filter_mahli_photogrammetry

    Returns
    -------
    bool
        True if the image should be used for photogrammetry, False otherwise.
    """
    return_val = True  # default to keep image
    # terminate if filter conditions are met
    if 'NAV' in img.instrument_id or 'HAZ' in img.instrument_id:
        return_val = filter_ecam_photogrammetry(img)
    elif 'MAST' in img.instrument_id:
        return_val = filter_mcam_photogrammetry(img)
    elif 'MAHLI' in img.instrument_id:
        return_val = filter_mahli_photogrammetry(img)
    return return_val


def filter_ecam_photogrammetry(img):
    """Filter ECAM images that are not suitable for photogrammetry."""
    if (
        img.target not in {'MARS', 'Mars'}  # filter out sky  # noqa: PLR0916
        or 'MXY'
        in img.fname.name  # filter out images which are specifically targeted at instruments
        or img.metafind(
            ('OBSERVATION_REQUEST_PARMS', 'MSL:INSTRUMENT_COORD_FRAME_ID'), fallback='UNSET'
        )
        not in {
            'LL',
            None,
            'RNAV',
            'NONE',
            'UNSET',
        }  # filter images which are specifically targeted at instruments
        or img.metafind(
            ('ROVER_DERIVED_GEOMETRY_PARMS', 'INSTRUMENT_ELEVATION'), fallback='UNSET'
        )['value']
        < -53  # filter images pointing at the rover deck
        or img.metafind('ROVER_MOTION_COUNTER')[3] > 0  # filter images after the arm was deployed
        or img.metafind('FRAME_TYPE')
        == 'MONO'  # filter non-stereo observations which are often Atmospheric ovserverations
    ):
        logger.debug(
            f'Skipping image {img.fname.name} due to filter conditions: target: {img.target}, '
            f'frame_type: {img.metafind("FRAME_TYPE")}, '
            f'Image Target Frame: {img.metafind(("OBSERVATION_REQUEST_PARMS", "MSL:INSTRUMENT_COORD_FRAME_ID"), fallback="UNSET")}, '
            f'Image Elevation: {img.metafind(("ROVER_DERIVED_GEOMETRY_PARMS", "INSTRUMENT_ELEVATION"), fallback="UNSET")["value"]}, '
            f'Rover Motion Counter (ARM): {img.metafind("ROVER_MOTION_COUNTER")[3]}'
        )
        return False
    return True


def filter_mcam_photogrammetry(img):
    """Filter Mastcam images that are not suitable for photogrammetry."""
    if (
        img.target not in {'MARS', 'Mars'}  # filter out sky
        or img.metafind(('INSTRUMENT_STATE_PARMS', 'FILTER_NUMBER'))
        not in ['0', 0]  # filter out non-clear filter images
        or
        # max(img.width, img.height) < 850 or # filter out small images which are likely Calibration or Autofocus or instrument images
        # max(img.width, img.height) in [1600, 1536, 1408, 1344] or # filter out full frame images which are likely of Hardware
        img.subframe_orig[2]
        not in {1328, 1200, 1152, 672}  # filter out images which not in default subframe
        or img.subframe_orig[3]
        not in {1200, 1184, 432, 896}  # filter out images which not in default subframe
    ):
        logger.debug(
            f'Skipping image {img.fname.name} due to filter conditions: target: {img.target}, '
            f'filter_number: {img.metafind(("INSTRUMENT_STATE_PARMS", "FILTER_NUMBER"))}, '
            f'Image Subframe: {img.subframe_orig}'
        )
        return False
    return True


def filter_mahli_photogrammetry(img):
    """Filter MAHLI images that are not suitable for photogrammetry."""
    if (
        img.target not in {'MARS', 'Mars'}  # filter out sky
        or img.metafind(('DERIVED_IMAGE_PARMS', 'MSL:COVER_STATE_FLAG'))
        == 'CLOSED'  # filter images with closed cover
        or img.width < 1500
        or img.height
        < 1100  # filter out small images which are likely Calibration or Autofocus or instrument images
        or 'calibration' in img.rationale
        or 'wheel inspection'
        in img.rationale  # filter out images which are specifically targeted at instruments
        or 'image relative focus stack'
        in img.rationale  # filter out images which are part of a focus stack but not merged
    ):
        logger.debug(
            f'Skipping image {img.fname.name} due to filter conditions: target: {img.target},'
            f'Image Subframe: {img.subframe_orig},'
            f' Rationale: {img.metafind(("OBSERVATION_REQUEST_PARMS", "RATIONALE_DESC"))},'
            f'Cover State: {img.metafind(("DERIVED_IMAGE_PARMS", "MSL:COVER_STATE_FLAG"))}'
        )
        return False
    return True


def process_image(
    image_path,
    output_dir=None,
    uncrop=True,
    image_filter=filter_photogrammetry,
    group='cam_id',
    apply_mask=True,
):
    """Process a single image file.

    Parameters
    ----------
    image_path : Path
        The path to the image file to be processed.
    output_dir : Path, optional
        The directory to save the converted images. If None, the converted images will be saved
        in a subdirectory of the original images.
    image_filter : callable, optional
        A function to filter that returns True if the image should be processed.
        If the image_filter argument is set to None, all images will be processed.
        See filter_photogrammetry for an example.
    group : str, optional
        The method to group the converted images. If 'cam_id', the images will be grouped by camera id.
        If None, the images will not be grouped.
    apply_mask : bool, optional
        If True, apply the mask to the converted images as an alpha channel.
    num_threads : int, optional
        The number of threads to use for parallel processing
    """
    try:
        img = MarsImage(image_path)

        # Skip images that don't meet the photogrammetry filter criteria
        if image_filter and not image_filter(img):
            return

        # The output path for the converted image
        if output_dir is None:
            # Save the converted image in a subdirectory of the original image
            converted_path = image_path.parent / ('converted/' + image_path.stem + '.tif')

        elif group == 'cam_id':
            # Save the converted image in a subdirectory based on the camera id
            converted_path = Path(output_dir) / (
                img.instrument_id + '/' + image_path.stem + '.tif'
            )
        elif group is None:
            converted_path = Path(output_dir) / (image_path.stem + '.tif')
        else:
            raise ValueError(f'Invalid grouping method: {group}')

        # Ensure the directories exist
        converted_path.parent.mkdir(parents=True, exist_ok=True)

        # apply preprocessing steps:
        # uncrop will revert the image to the full sensor size (excluding downsampling)
        # undebayer will revert default debayering and allow better debayering with RawTherapee
        img.process(undebayer=True, uncrop=uncrop)

        # Using an intermediate DNG file and RawTherapee,
        # convert the image to tiff with color calibration, whitebalancing, exposure correction
        # apply the mask to the image as an alpha channel
        img.rawtherapee_convert(converted_path, apply_mask=apply_mask)
    # Catch non keyboard interrupts
    except KeyboardInterrupt:
        raise KeyboardInterrupt('The processing was interrupted by the user.') from None

    except Exception as e:
        logger.error(f'Error processing image {image_path.name}: {e}')


def process_images(
    image_list,
    output_dir=None,
    uncrop=True,
    group='cam_id',
    apply_mask=True,
    image_filter=filter_photogrammetry,
    num_threads=None,
):
    """Process a list of images in parallel.

    Parameters
    ----------
    image_list : list of Path
        A list of paths to the image files to be processed.
    output_dir : Path, optional
        The directory to save the converted images. If None, the converted images will be saved
        in a subdirectory of the original images.
    group : str, optional
        The method to group the converted images. If 'cam_id', the images will be grouped by camera id.
        If None, the images will not be grouped.
    image_filter : callable, optional
        A function to filter that returns True if the image should be processed.
        See filter_photogrammetry for an example.
    apply_mask : bool, optional
        If True, apply the mask to the converted images as an alpha channel.
    num_threads : int, optional
        The number of threads to use for parallel processing.
        By default, the number of threads is set to the number of CPU cores.
    """

    def filter_supported_product_types(image_path):
        return Filename(image_path).prod_code in SUPPORTED_PRODUCT_TYPES

    image_list = [image for image in image_list if filter_supported_product_types(image)]
    image_list.sort()

    i, tot = (1, len(image_list))
    logger.info(f'Starting processing of {tot} images')

    if num_threads is None:
        num_threads = os.cpu_count()

    pbar_images = tqdm(total=tot, desc=f'Processing {tot} images', leave=True, smoothing=0.1)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=num_threads)

    with pbar_images, executor:
        future_to_image = {
            executor.submit(
                process_image, image, output_dir, uncrop, image_filter, group, apply_mask
            ): image
            for image in image_list
        }
        for future in concurrent.futures.as_completed(future_to_image):
            image = future_to_image[future]
            try:
                future.result()  # This will raise an exception if the processing failed
                logger.debug(f'Saved image {i}/{tot} {image.name}')
            except KeyboardInterrupt:
                raise KeyboardInterrupt('The processing was interrupted by the user.') from None

            except Exception as e:
                logger.error(f'Processing failed for image {image}: {e}')
            i += 1
            pbar_images.update(1)
