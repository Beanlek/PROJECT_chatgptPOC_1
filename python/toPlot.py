# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

### define dataframe
df = pd.DataFrame({
    'van_id': ['V2XV001', 'V2XV001', 'V2XV001', 'V2XV001', 'V2XV001', 'V2XV001', 'V2XV001'],
    'visit_date': ['1/7/2023', '4/7/2023', '3/7/2023', '4/7/2023', '3/7/2023', '4/7/2023', '1/7/2023'],
    'outlet_id': [21101013, 21110043, 349751, 698148, 594670, 739071, 21108050],
    'lng': [100.71856, 100.74137, 100.72426, 100.73873, 100.74109, 100.74296, 100.71282],
    'lat': [4.85454, 4.84993, 4.84123, 4.85025, 4.8508, 4.85025, 4.85297],
    'check_in_at': ['2023-07-01 12:05:25.000 +0800', '2023-07-04 17:00:57.000 +0800',
                    '2023-07-03 08:48:37.000 +0800', '2023-07-04 16:59:44.000 +0800',
                    '2023-07-03 17:04:18.000 +0800', '2023-07-04 08:51:23.000 +0800',
                    '2023-07-01 11:35:18.000 +0800'],
    'check_out_at': ['2023-07-01 12:06:57.924 +0800', '2023-07-04 17:03:41.550 +0800',
                        '2023-07-03 17:02:43.514 +0800', '2023-07-04 17:03:54.591 +0800',
                        '2023-07-03 17:05:49.854 +0800', '2023-07-04 09:58:31.858 +0800',
                        '2023-07-01 11:35:43.702 +0800'],
    'travelled_time': ['02:34.1', '02:09.6', '07:52.5', '04:04.6', '01:23.9',
                        '06:34.9', '05:16.3']})

### plotting the graph
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.plot(df['lat'], df['lng'], 'bo')
plt.show()