# -*- coding: utf-8 -*-
import sys

#import serbian_rules

# Define how you want to query route master of your GTFS. This is main entry to program and only one you need to think
# how to define. Based on this, you define all route masters you want to check. There are two options:
# 'agency_name' - take 'agency name from GTFS and find all route masters in world by "gtfs:agency_name" tag
# 'operator' - take operator from ROUTE_MASTER_OPERATOR and query all route masters in world for "operator" tag. If you
# use this approach, make sure to fill ROUTE_MASTER_OPERATOR.
ROUTE_MASTER_QUERY_METHOD = 'network'

# If GTFS contains multiple entries, you will need to define specific ID of agency you want to check. If it is None,
# tool will check if there is only one entry in agency and fail if there is more.
AGENCY_ID = None

# If you use 'operator' for ROUTE_MASTER_QUERY_METHOD, here you can define what operator you want to query
ROUTE_MASTER_NETWORK = 'Burlington Transit'

# lookup OSM master route ref in gtfs name
REF_AS_NAME = True

# Program will (by default) check master route and routes and then stops. If you want to check only routes,
# without checking individual stops, set this to False.
CHECK_STOPS = True

# If names in GTFS and in OSM should not be the same (you need to strip something, to change it a bit...), this is place
# where you can define function that will be applied on all names from GTFS and from OSM.
# It should take one argument of type string and return string. Check Serbian version to see how it can be used.
# Default is to just use GTFS and OSM as-is.
#NORMALIZE_GTFS_NAME = lambda s: serbian_rules.normalize_gtfs_name(s)  # Serbian version
#NORMALIZE_OSM_NAME = lambda s: serbian_rules.normalize_osm_name(s)  # Serbian version
NORMALIZE_GTFS_NAME = lambda s: s
NORMALIZE_OSM_NAME = lambda s: s


# If you also want to check operator tag for some specific value, add it here as string
# For example, in Serbia it is "ГСП Београд", in France it could be "TVO"...
OPERATOR = 'City of Burlington'

# If you also want to check network tag for some specific value, add it here as string
NETWORK = 'Burlington Transit'

# Define what key you want to check for stops.
# It can be either "gtfs_id" or "gtfs:stop_id, as per https://wiki.openstreetmap.org/wiki/Key:gtfs:stop_id
# Stops usually have "ref" also defined, so it makes sense to put your GTFS stop id here too.
GTFS_STOP_KEY = ['ref', 'gtfs_id', 'gtfs_stop_code']

# (Hausdorff) distance (max deviation) between route in OSM and GTFS above which value this tool will report it
DISTANCE_ROUTE_METERS_THRESHOLD = 300

# Distance between stop in OSM and in GTFS (in meters) above which value this tool will report it
DISTANCE_STOPS_METERS_THRESHOLD = 50

# Nearest distance between platform/stop and its route in OSM (in meters) above which value this tool will report it
DISTANCE_STOP_FROM_ROUTE_METERS_THRESHOLD = 50

# Threshold (in percent) by which total distance of route in OSM and GTFS should differ above which this tool will
# report it. If it is 30% and if route in OSM is 1000m, we will report if GTFS route is > 1300m or < 700m.
TOTAL_ROUTE_DISTANCE_PERCENTAGE_THRESHOLD = 30

# Change this if you want to use different Overpass instance. While this app is resilient on Overpass throttling,
# and while it is not using Overpass heavily, you might get better results with different or your own instance.
#OVERPASS_API_SERVER = "http://localhost:12345/api/interpreter"
OVERPASS_API_SERVER = "http://overpass-api.de/api/interpreter"
