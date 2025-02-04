#!/bin/bash

years=("2021-2022" "2022-2023" "2023-2024")

for i in ${years[*]}
do
	y1=$(echo $i | cut -f1 -d-)
	y2=$(echo $i | cut -f2 -d-)
	echo $y1 $y2

	echo "python -m pdb investigate_s1_snotel.py --s1file /media/jiangzhu/Elements/crrel/SNOTEL/creamers/${y1}0801_${y2}0731/sentinel1_creamers_${y1}0801_${y2}0731.nc --snotelfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/${y1}0801_${y2}0731/creamers_${y1}0801_${y2}0731_sd_precip_temp_ratio.txt --lon -147.74532 --lat 64.86575  --aoigeojsonfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/creamers.geojson --stdate ${y1}-11-15 --eddate ${y2}-03-15 --outfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/${y1}0801_${y2}0731/sentinel1_creamers_${y1}0801_${y2}0731_aoi_snow.png"

	
	python investigate_s1_snotel.py --s1file /media/jiangzhu/Elements/crrel/SNOTEL/creamers/${y1}0801_${y2}0731/sentinel1_creamers_${y1}0801_${y2}0731.nc --snotelfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/${y1}0801_${y2}0731/creamers_${y1}0801_${y2}0731_sd_precip_temp_ratio.txt --lon -147.74532 --lat 64.86575  --aoigeojsonfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/creamers.geojson --stdate ${y1}-11-15 --eddate ${y2}-03-15 --outfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/${y1}0801_${y2}0731/sentinel1_creamers_${y1}0801_${y2}0731_aoi_snow.png

done


#python -m pdb investigate_s1_snotel.py --s1file /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20210801_20220731/sentinel1_creamers_20210801_20220731.nc --snotelfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20210801_20220731/creamers_20210801_20220731_sd_precip_temp_ratio.txt --lon -147.74532 --lat 64.86575  --aoigeojsonfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/creamers.geojson --stdate 2021-11-15 --eddate 2022-03-15 --outfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20210801_20220731/sentinel1_creamers_20210801_20220731_aoi_snow.png

#python -m pdb investigate_s1_snotel.py --s1file /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20220801_20230731/sentinel1_creamers_20220801_20230731.nc --snotelfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20220801_20230731/creamers_20220801_20230731_sd_precip_temp_ratio.txt --lon -147.74532 --lat 64.86575  --aoigeojsonfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/creamers.geojson --stdate 2022-11-15 --eddate 2023-03-15 --outfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20220801_20230731/sentinel1_creamers_20220801_20230731_aoi_snow.png

#python -m pdb investigate_s1_snotel.py --s1file /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20230801_20240731/sentinel1_creamers_20230801_20240731.nc --snotelfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20230801_20240731/creamers_20230801_20240731_sd_precip_temp_ratio.txt --lon -147.74532 --lat 64.86575  --aoigeojsonfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/creamers.geojson --stdate 2023-11-15 --eddate 2024-03-15 --outfile /media/jiangzhu/Elements/crrel/SNOTEL/creamers/20230801_20240731/sentinel1_creamers_20230801_20240731_aoi_snow.png
