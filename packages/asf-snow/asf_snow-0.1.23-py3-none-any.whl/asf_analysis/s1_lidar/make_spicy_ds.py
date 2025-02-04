import shapely
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
import rioxarray as rxa
from rasterio.enums import Resampling

from datetime import datetime

# from asf_snow.spicy_snow.retrieval import retrieve_snow_depth
from asf_snow.retrieval_sentinel1_snow import retrieve_snow_depth

from spicy_snow.download.snowex_lidar import download_dem, download_snow_depth,\
      download_veg_height

from asf_snow.spicy_snow.IO.user_dates import get_input_dates


lidar_dir = Path('/home/jiangzhu/data/crrel/lidar_via_zach')

sites = {'USCOCP': 'Cameron', 'USCOFR': 'Frasier', 'USIDBS': 'Banner', 
         'USIDDC': 'Dry_Creek', 'USIDMC': 'Mores', 'USUTLC': 'Little_Cottonwood'}

sites = {'USIDBS': 'Banner'}

filename_filter = '*20200218_20200219*'

def make_site_ds(site: str, lidar_dir: Path, filename_filter='*') -> xr.Dataset:
    """
    Makes a dataset of snow depth, veg height, and DEM for a specific site abbreviation
    in the lidar directory. Returns it reprojected to EPSG4326.

    Args:
    site: Site abbreviation to search for
    lidar_dir: Direction of lidar tiffs

    Returns:
    dataset: xarray dataset of dem, sd, vh for site
    """

    dataset = xr.Dataset()

    for img_type in ['SD', 'VH', 'DEM']:
        # files = glob(join(lidar_dir, f'*_{img_type}_*_{site}_*.tif'))
        if img_type == 'DEM':
            files = lidar_dir.glob(f'*_{img_type}_*_{site}_*.tif')
        else:
            files = lidar_dir.glob(f'*_{img_type}_*_{site}_{filename_filter}.tif')

        assert files, f"No files found for {img_type} at {site}"
        
        imgs = []
        for f in files:
            print(f)

            if img_type != 'DEM':
                date = pd.to_datetime(f.stem.split('_')[-2])
                sd_date = date
            else:
                date = sd_date

            img = rxa.open_rasterio(f)

            img = img.squeeze(dim = 'band')
            
            if img_type != 'DEM':
                img = img.expand_dims(time = [date])

            imgs.append(img)
        
        if img_type != 'DEM':
            dataset['lidar-' + img_type.lower()] = xr.concat(imgs, dim = 'time')
        else:
            dataset['lidar-' + img_type.lower()] = imgs[0]

    dataset = dataset.rio.reproject('EPSG:4326')
    
    return dataset


# param_set = Path('/bsuhome/zacharykeskinen/spicy-analysis/results/params/stat_res_0.5tree.csv')
# param_df = pd.DataFrame()
# if param_set.exists():
#     param_df = pd.read_csv(param_set, index_col = 0)

def main():

    for site, site_name in sites.items():
        print(''.center(40, '-'))
        print(f'Starting {site_name}')
        if Path(f'{lidar_dir}/lidar_ds_site_validdata.nc').is_file():
            lidar_ds_site = xr.open_dataset(f'{lidar_dir}/lidar_ds_site_validdata.nc')
        else:
            if Path(f'{lidar_dir}/lidar_ds_site.nc').is_file():
                lidar_ds_site = xr.open_dataset(f'{lidar_dir}/lidar_ds_site.nc')
            else:
                lidar_ds_site = make_site_ds(site, lidar_dir = lidar_dir, filename_filter=filename_filter)
            # lidar_ds_site = lidar_ds_site.where(lidar_ds_site < 1e9).where(lidar_ds_site >= 0)
            ch = np.logical_and(lidar_ds_site < 1e9, lidar_ds_site >= 0)
            lidar_ds_site['lidar-sd'] = lidar_ds_site['lidar-sd'].where(ch['lidar-sd'])
            lidar_ds_site['lidar-vh'] = lidar_ds_site['lidar-vh'].where(ch['lidar-vh'])
            lidar_ds_site['lidar-dem'] = lidar_ds_site['lidar-dem'].where(ch['lidar-dem'])
            lidar_ds_site.to_netcdf(f'{lidar_dir}/lidar_ds_site_validdata.nc')

        area = shapely.geometry.box(*lidar_ds_site.rio.bounds())

        for date in lidar_ds_site.time:

            # if param_df.size > 0:
            #     out_dir = Path('/bsuhome/zacharykeskinen/scratch/spicy/SnowEx-Data-params/')
            # else:
            out_dir = Path(f'{lidar_dir}/scratch/spicy/SnowEx-Data-lave/')
            out_dir.mkdir(parents=True, exist_ok = True)

            out_nc = out_dir.joinpath(f'{site_name}_{(date).dt.strftime("%Y-%m-%d").values}.nc')

            if out_nc.exists():
                print(f'Outfile {out_nc} exists already.')
                continue

            print(f'Starting {site_name} snow depth @ {date.values}')

            if date.dt.month > 4:
                continue

            lidar_ds = lidar_ds_site.sel(time = date)

            dates = get_input_dates(date.data + pd.Timedelta('14 day'))

            if Path(f'{lidar_dir}/spicy_ds.nc').is_file():
                spicy_ds = xr.open_dataset(f'{lidar_dir}/spicy_ds.nc')
            # if param_df.size > 0:
            else:
                spicy_ds = retrieve_snow_depth(area = area, dates = dates, work_dir = '/home/jiangzhu/data/crrel/lidar_via_zach/scratch/spicy/', \
                                            job_name = f'spicy_{site}_{dates[1]}', existing_job_name = f'spicy_{site}_{dates[1]}', \
                                            params = [1.5, 0.1, 0.59])
                spicy_ds.to_netcdf(f'{lidar_dir}/spicy_ds.nc')

            # else:
                # spicy_ds = retrieve_snow_depth(area = area, dates = dates, work_dir = '/bsuhome/zacharykeskinen/scratch/spicy/', job_name = f'spicy_{site}_{dates[1]}', existing_job_name = f'spicy_{site}_{dates[1]}')

            for var in lidar_ds:
                lidar_ds[var] = lidar_ds[var].rio.write_nodata(np.nan)

            lidar_ds = lidar_ds.rio.reproject_match(spicy_ds, resampling = Resampling.average, nodata=np.nan)

            ds = xr.merge([spicy_ds, lidar_ds], combine_attrs = 'drop_conflicts')

            # ds = ds[['lidar-sd', 'lidar-vh', 'lidar-dem', 'snow_depth', 's1', 'wet_snow']]

            ds.attrs['site'] = site_name
            ds.attrs['site_abbrev'] = site
            ds.attrs['lidar-flight-time'] = str((date[0]).dt.strftime("%Y-%m-%d").values)
            ds.attrs['processing-date'] = f'{datetime.now()}'

            try:
                ds.to_netcdf(out_nc)
            except:
                print('Unable to create netcdf4 for {site_name}')


if __name__ == '__main__':

    main()