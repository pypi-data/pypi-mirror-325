## preload variables to have faster dataframe grouping

NETWORK_WEEKLY_GROUP_COLS = ['plan_id', 'country', 'week']
REGION_WEEKLY_GROUP_COLS = ['plan_id', 'country', 'region', 'week']
STATION_WEEKLY_GROUP_COLS = ['plan_id', 'country', 'region', 'station', 'week'] 

NETWORK_DAILY_GROUP_COLS = ['plan_id', 'country', 'week', 'dow', 'date']
REGION_DAILY_GROUP_COLS = ['plan_id', 'country', 'region', 'week', 'dow', 'date']