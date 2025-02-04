from email.policy import default
from pathlib import Path
import shapely
import json
import logging
import os
import sys
from typing import Optional
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from asf_snow.utils import utils
# Add main repo to path if you haven't added with conda-develop
# import sys
# sys.path.append('path/to/the/spicy-snow/')

# from spicy_snow.retrieval import retrieve_snow_depth
from asf_snow.retrieval_sentinel1_snow import retrieve_snow_depth
from spicy_snow.IO.user_dates import get_input_dates

from asf_snow.utils.analyze_sentinel1_snow import *


def sentinel1_snow(area: list, dates: list, flightdir: str='both', workdir=None, jobname=None,
                   existjobname=None, outnc=None, method: str='standard',
                   parameterabc=[2.5, 0.2, 0.55, 0.0, 1.0], wet_snow_thresh:float=-3.0, debug=False):
    """ Calculate the snow depths with sentinel-1 c-band data vv,vh,and incidental angle.
    :param area: list [minlon,minlat,maxlon,maxlat]
    :param date: list [yyyy-mm-dd, yyyy-mm-dd]
    :param workdir: path
    :param jobname: job name
    :param existjobname: existing job name
    :param outnc: path of output nc file
    :param method: standard or vvonly, for test purpose, default is standard, which combines CR and VV
    :param debug: if run the program in debug.
    :param: parameterabc: [A,B,C, ll, ul], default [2.5, 0.2, 0.55, 0.0, 1.0]
    :return:
    """
    '''
    environment_jsonfile = f'{workdir}/tmp/environment.json'
    log = logging.getLogger(__name__)
    if Path(environment_jsonfile).is_file():
        # compare function arguments with the context in the environment.json
        environment = utils.read_environment(environment_jsonfile)
        if not (environment['area'] == area and environment['daterange'] == dates and environment['workdir'] == workdir):
            log.info(f'{workdir} is not empty, you need use other work directory')
            sys.exit(1)
    '''
    log = logging.getLogger(__name__)

    environment = json.loads(os.environ['ENVIRONMENT'])

    if not (environment['area'] == area and environment['daterange'] == dates):
        log.info(f'{workdir} is not empty, you need use other work directory')
        sys.exit(1)

    # change to your minimum longitude, min lat, max long, max lat
    area1 = shapely.geometry.box(area[0], area[1], area[2], area[3])

    Path(workdir).mkdir(parents=True, exist_ok=True)

    # this will be where your results are saved
    out_nc = Path(outnc).expanduser()

    # this will generate a tuple of dates from the previous August 1st to this date
    # dates = get_input_dates(dates)  # run on all s1 images from (2020-08-01, 2021-04-01) in this example
    dates = tuple(dates)
    spicy_ds = retrieve_snow_depth(area=area1, dates=dates, flightdir=flightdir, work_dir=Path(workdir).expanduser(),
                                   job_name=jobname,
                                   existing_job_name=existjobname,
                                   outfp=out_nc,
                                   method=method,
                                   params=parameterabc,
                                   wet_snow_thresh=wet_snow_thresh,
                                    debug=False,
                                   )


    return spicy_ds


def check_earthdata_credentials(username, password):
    if username is None:
        username = os.getenv('EARTHDATA_USERNAME')
        if username is None:
            raise ValueError(
                'Please provide Earthdata username via the --username option '
                'or the EARTHDATA_USERNAME environment variable.'
            )

    if password is None:
        password = os.getenv('EARTHDATA_PASSWORD')
        if password is None:
            raise ValueError(
                'Please provide Earthdata password via the --password option '
                'or the EARTHDATA_PASSWORD environment variable.'
            )

    return username, password


def main():
    log = logging.getLogger(__name__)

    parser = ArgumentParser()
    parser.add_argument('--username', type=str, default=None)
    parser.add_argument('--password', type=str, default=None)
    parser.add_argument('--area', nargs="*", type=float, help='minlon minlat maxlon maxlat of the AOI')
    parser.add_argument('--lon', type=float, help='longitude of the center of the AOI')
    parser.add_argument('--lat', type=float, help='latitude of the center of the AOI')
    parser.add_argument('--res', type=float, help='length in meter of the AOI')
    parser.add_argument('--daterange', nargs="*", type=str, help='yyyy-mm-dd yyyy-mm-dd', default=['2008-08-01', '2021-04-01'])
    parser.add_argument('--flightdir', type=str, choices =['ascending', 'descending', 'both'], default='both')
    parser.add_argument('--workdir', type=str, default='.')
    parser.add_argument('--jobname', type=str, default='testing_job')
    parser.add_argument('--existjobname', type=str, default='testing_job')
    parser.add_argument('--outnc', default='test.nc', help='file name of the output nc file')

    parser.add_argument('--method', type=str, choices=['standard','vvonly'], default='vvonly')
    parser.add_argument('--parameterabc', nargs="*", type=float, default=[2.5, 0.2, 0.55, 0.0, 1.0], help='A B C ll ul')
    parser.add_argument('--wet_snow_thresh', type=float, default=-3.0)

    parser.add_argument('--debug', type=bool, default=False)

    args = parser.parse_args()

    if args.area:
        bbox = args.area
    elif args.lon and args.lat and args.res:
        # lot,lat to bbox
        bbox = bbox_via_point(args.lon, args.lat, args.res)
        args.area = bbox
    else:
        log.info(f'Need to set either area or lon, lat, and res')
        sys.exit(1)

    # write args if args.workdir not exist

    environment_jsonfile = f'{args.workdir}/tmp/environment.json'

    if not Path(environment_jsonfile).is_file():
        environment = vars(args)
        environment['step'] = 'begin'
        os.environ['ENVIRONMENT'] = json.dumps(environment)

    else:
        environment = utils.read_environment(environment_jsonfile)
        os.environ['ENVIRONMENT'] = json.dumps(environment)

       # set environment for share
    username, password = check_earthdata_credentials(args.username, args.password)
    os.environ['EARTHDATA_USERNAME'] = username
    os.environ['EARTHDATA_PASSWORD'] = password



    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    # write_credentials_to_netrc_file(username, password)

    spicy_ds = sentinel1_snow(area=bbox, dates=args.daterange, flightdir=args.flightdir, workdir=args.workdir,
                              jobname=args.jobname, existjobname=args.existjobname, outnc=args.outnc,
                              method=args.method, parameterabc=args.parameterabc,
                              wet_snow_thresh=args.wet_snow_thresh)


if __name__ == '__main__':
    main()


