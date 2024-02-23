#!/bin/bash

which scrapy
if [[ ! $? = 0 ]]; then
	echo "Install scrapy. Here is the link: https://docs.scrapy.org/en/latest/intro/install.html#installing-scrapy"
	exit 1
fi

declare -A urls=(
# Mobile
	[smartphones]="https://www.samsung.com/sec/smartphones/all-smartphones/"
	[tablets]="https://www.samsung.com/sec/tablets/all-tablets/"
	[galaxy_books]="https://www.samsung.com/sec/galaxybook/all-galaxybook/"
	[watches]="https://www.samsung.com/sec/watches/all-watches/"
	[buds]="https://www.samsung.com/sec/buds/all-buds/"
	[mobile_accessories]="https://www.samsung.com/sec/mobile-accessories/all-mobile-accessories/"
# TV & Audio
	[tvs]="https://www.samsung.com/sec/tvs/all-tvs/"
	[lifestyle_tvs]="https://www.samsung.com/sec/lifestyletv/all-lifestyletv/"
	[samsung_audios]="https://www.samsung.com/sec/samsung-audio/all-samsung-audio/"
	[harman_lifestyle_audios]="https://www.samsung.com/sec/harman-life-style-audio/all-harman-life-style-audio/"
	[tv_accessories]="https://www.samsung.com/sec/tv-accessories/all-tv-accessories/"
# Kitchen appliances
	[refrigerators]="https://www.samsung.com/sec/refrigerators/all-refrigerators/"
	[kimchi_refrigerators]="https://www.samsung.com/sec/kimchi-refrigerators/all-kimchi-refrigerators/"
	[dishwashers]="https://www.samsung.com/sec/dishwashers/all-dishwashers/"
	[water_purifiers]="https://www.samsung.com/sec/water-purifier/all-water-purifier/"
	[electric_ranges]="https://www.samsung.com/sec/electric-range/all-electric-range/"
	[cooking_appliances]="https://www.samsung.com/sec/cooking-appliances/all-cooking-appliances/"
	[microwave_ovens]="https://www.samsung.com/sec/micro-wave-ovens/all-micro-wave-ovens/"
	[hoods]="https://www.samsung.com/sec/hood/all-hood/"
	[kitchen_small_appliances]="https://www.samsung.com/sec/kitchen-small-appliance/all-kitchen-small-appliance/"
	[kitchen_accessories]="https://www.samsung.com/sec/kitchen-accessories/all-kitchen-accessories/"
# Living appliances
	[washing_machines]="https://www.samsung.com/sec/washing-machines/all-washing-machines/"
	[dryers]="https://www.samsung.com/sec/dryers/all-dryers/"
	[airdressers]="https://www.samsung.com/sec/airdresser/all-airdresser/"
	[shoedressers]="https://www.samsung.com/sec/shoedresser/all-shoedresser/"
	[air_conditioners]="https://www.samsung.com/sec/air-conditioners/all-air-conditioners/"
	[system_air_conditioners]="https://www.samsung.com/sec/system-air-conditioners/all-system-air-conditioners/"
	[air_cleaners]="https://www.samsung.com/sec/air-cleaner/all-air-cleaner/"
	[vacuum_cleaners]="https://www.samsung.com/sec/air-cleaner/all-air-cleaner/"
	[small_appliances]="https://www.samsung.com/sec/small-appliances/all-small-appliances/"
	[living_accessories]="https://www.samsung.com/sec/living-accessories/all-living-accessories/"
# PC & Peripherals
	[desktops]="https://www.samsung.com/sec/desktop/all-desktop/"
	[pc_accessories]="https://www.samsung.com/sec/pc-accessories/all-pc-accessories/"
	[monitors]="https://www.samsung.com/sec/monitors/all-monitors/"
	[memory_storages]="https://www.samsung.com/sec/memory-storage/all-memory-storage/"
	[printers]="https://www.samsung.com/sec/memory-storage/all-memory-storage/"
	[printer_supplies]="https://www.samsung.com/sec/printer-supplies/all-printer-supplies/"
# Smart Things
	[smartthings_accessories]="https://www.samsung.com/sec/smartthings-accessories/all-smartthings-accessories/"
)

for category in ${!urls[@]};
do
	scrapy genspider $category ${urls[$category]}
done
