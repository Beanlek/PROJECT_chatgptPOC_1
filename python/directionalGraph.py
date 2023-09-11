import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data from your CSV with timestamps
van_data = [
    # van_id  ,visit_date, outlet_id, lng,lat, created_at
    # ("V2XV001", "1/7/2023", 376882, 100.7183, 4.85454, "2023-07-01 10:36:24.865 +0800"),
    # ("V2XV001", "1/7/2023", 815056, 100.73165, 4.85208, "2023-07-01 10:39:18.468 +0800"),
    # ("V2XV001", "1/7/2023", 21108180, 100.72157, 4.85204, "2023-07-01 10:46:37.656 +0800"),
    # ("V2XV001", "1/7/2023", 21108181, 100.7216, 4.85192, "2023-07-01 10:50:35.525 +0800"),
    # ("V2XV001", "1/7/2023", 816261, 100.72155, 4.85158, "2023-07-01 10:56:02.518 +0800"),
    # ("V2XV001", "1/7/2023", 245941, 100.72076, 4.85139, "2023-07-01 10:59:17.304 +0800"),
    # ("V2XV001", "1/7/2023", 722409, 100.72067, 4.85199, "2023-07-01 11:08:48.511 +0800"),
    # ("V2XV001", "1/7/2023", 774608, 100.71812, 4.85412, "2023-07-01 11:20:45.935 +0800"),
    # ("V2XV001", "1/7/2023", 669662, 100.71192, 4.8528, "2023-07-01 11:31:05.755 +0800"),
    # ("V2XV001", "1/7/2023", 21108046, 100.71208, 4.85317, "2023-07-01 11:32:00.687 +0800"),
    # ("V2XV001", "1/7/2023", 21108044, 100.71202, 4.85324, "2023-07-01 11:32:48.878 +0800"),
    # ("V2XV001", "1/7/2023", 21108042, 100.71285, 4.85304, "2023-07-01 11:33:30.480 +0800"),
    # ("V2XV001", "1/7/2023", 21108049, 100.71275, 4.85286, "2023-07-01 11:34:34.805 +0800"),
    # ("V2XV001", "1/7/2023", 21108050, 100.71282, 4.85297, "2023-07-01 11:35:18.643 +0800"),
    # ("V2XV001", "1/7/2023", 21108122, 100.71109, 4.84972, "2023-07-01 11:41:00.422 +0800"),
    # ("V2XV001", "1/7/2023", 21101013, 100.71856, 4.85454, "2023-07-01 12:05:25.460 +0800"),
    # ("V2XV001", "1/7/2023", 829233, 100.71258, 4.85244, "2023-07-01 12:09:32.579 +0800"),

    # ("V2XV001", "3/7/2023", 245941, 100.72076, 4.85139, "2023-07-03 08:37:49.346 +0800"),
    # ("V2XV001", "3/7/2023", 21102148, 100.73984, 4.85131, "2023-07-03 08:54:51.500 +0800"),
    # ("V2XV001", "3/7/2023", 21102148, 100.73984, 4.85131, "2023-07-03 08:54:51.500 +0800"),
    # ("V2XV001", "3/7/2023", 345483, 100.73911, 4.84866, "2023-07-03 09:00:02.350 +0800"),
    # ("V2XV001", "3/7/2023", 21101018, 100.72374, 4.84139, "2023-07-03 10:50:12.411 +0800"),
    # ("V2XV001", "3/7/2023", 21101019, 100.72368, 4.84134, "2023-07-03 10:50:30.631 +0800"),
    # ("V2XV001", "3/7/2023", 21101018, 100.72374, 4.84139, "2023-07-03 10:50:34.340 +0800"),
    # ("V2XV001", "3/7/2023", 21101019, 100.72368, 4.84134, "2023-07-03 10:50:36.744 +0800"),
    # ("V2XV001", "3/7/2023", 21101015, 100.72451, 4.84125, "2023-07-03 17:02:54.529 +0800"),
    # ("V2XV001", "3/7/2023", 289735, 100.73946, 4.85197, "2023-07-03 17:03:03.241 +0800"),
    # ("V2XV001", "3/7/2023", 21111107, 100.73861, 4.85177, "2023-07-03 17:03:10.287 +0800"),
    # ("V2XV001", "3/7/2023", 21111129, 100.73819, 4.85103, "2023-07-03 17:03:17.717 +0800"),
    # ("V2XV001", "3/7/2023", 769008, 100.73881, 4.85342, "2023-07-03 17:03:24.185 +0800"),
    # ("V2XV001", "3/7/2023", 21110009, 100.73837, 4.85243, "2023-07-03 17:03:30.617 +0800"),
    # ("V2XV001", "3/7/2023", 21111062, 100.74029, 4.85203, "2023-07-03 17:03:37.313 +0800"),
    # ("V2XV001", "3/7/2023", 21110018, 100.74142, 4.85272, "2023-07-03 17:03:43.749 +0800"),
    # ("V2XV001", "3/7/2023", 21110020, 100.7423, 4.85274, "2023-07-03 17:03:50.824 +0800"),
    # ("V2XV001", "3/7/2023", 21110068, 100.74261, 4.85206, "2023-07-03 17:03:57.771 +0800"),
    # ("V2XV001", "3/7/2023", 21110071, 100.74174, 4.8508, "2023-07-03 17:04:04.356 +0800"),
    # ("V2XV001", "3/7/2023", 21110104, 100.74049, 4.85103, "2023-07-03 17:04:11.216 +0800"),
    # ("V2XV001", "3/7/2023", 594670, 100.74109, 4.8508, "2023-07-03 17:04:18.846 +0800"),
    # ("V2XV001", "3/7/2023", 21111039, 100.74028, 4.849441, "2023-07-03 17:04:26.159 +0800"),
    # ("V2XV001", "3/7/2023", 21111038, 100.74001, 4.84942, "2023-07-03 17:04:33.921 +0800"),
    # ("V2XV001", "3/7/2023", 21111026, 100.74033, 4.85022, "2023-07-03 17:04:57.947 +0800"),
    # ("V2XV001", "3/7/2023", 21111004, 100.74031, 4.85011, "2023-07-03 17:05:06.149 +0800"),
    # ("V2XV001", "3/7/2023", 21111006, 100.74037, 4.84978, "2023-07-03 17:05:13.939 +0800"),
    # ("V2XV001", "3/7/2023", 21111011, 100.74037, 4.84978, "2023-07-03 17:05:27.707 +0800"),
    # ("V2XV001", "3/7/2023", 21111105, 100.74039, 4.85014, "2023-07-03 17:05:40.385 +0800"),
    # ("V2XV001", "3/7/2023", 21111020, 100.7403, 4.84996, "2023-07-03 17:05:47.897 +0800"),
    # ("V2XV001", "3/7/2023", 21111026, 100.74033, 4.85022, "2023-07-03 17:06:24.796 +0800"),

    # ("V2XV001", "4/7/2023", 21110138, 100.74382, 4.84922, "2023-07-04 08:50:53.745 +0800"),
    # ("V2XV001", "4/7/2023", 739071, 100.74296, 4.85025, "2023-07-04 08:51:24.014 +0800"),
    # ("V2XV001", "4/7/2023", 732868, 100.74288, 4.85389, "2023-07-04 08:51:58.055 +0800"),
    # ("V2XV001", "4/7/2023", 698148, 100.73873, 4.85025, "2023-07-04 16:59:44.001 +0800"),
    # ("V2XV001", "4/7/2023", 21110088, 100.74023, 4.84738, "2023-07-04 16:59:50.129 +0800"),
    # ("V2XV001", "4/7/2023", 463231, 100.74028, 4.84741, "2023-07-04 16:59:56.104 +0800"),
    # ("V2XV001", "4/7/2023", 21110121, 100.74265, 4.84836, "2023-07-04 17:00:02.139 +0800"),
    # ("V2XV001", "4/7/2023", 21110051, 100.74262, 4.84864, "2023-07-04 17:00:09.565 +0800"),
    # ("V2XV001", "4/7/2023", 670483, 100.74362, 4.84816, "2023-07-04 17:00:16.045 +0800"),
    # ("V2XV001", "4/7/2023", 21103151, 100.74331, 4.84936, "2023-07-04 17:00:22.495 +0800"),
    # ("V2XV001", "4/7/2023", 21110081, 100.74389, 4.85034, "2023-07-04 17:00:29.946 +0800"),
    # ("V2XV001", "4/7/2023", 21110058, 100.74401, 4.84987, "2023-07-04 17:00:36.842 +0800"),
    # ("V2XV001", "4/7/2023", 21110057, 100.7439, 4.85032, "2023-07-04 17:00:43.245 +0800"),
    # ("V2XV001", "4/7/2023", 360882, 100.74391, 4.85021, "2023-07-04 17:00:50.113 +0800"),
    # ("V2XV001", "4/7/2023", 21110043, 100.74137, 4.84993, "2023-07-04 17:00:57.075 +0800"),
    # ("V2XV001", "4/7/2023", 807887, 100.74339, 4.85184, "2023-07-04 17:01:32.505 +0800"),
    # ("V2XV001", "4/7/2023", 21114067, 100.74648, 4.86096, "2023-07-04 17:01:39.733 +0800"),
    # ("V2XV001", "4/7/2023", 21114047, 100.74231, 4.85398, "2023-07-04 17:01:46.431 +0800"),
    # ("V2XV001", "4/7/2023", 21101168, 100.74315, 4.85332, "2023-07-04 17:01:53.286 +0800"),
    # ("V2XV001", "4/7/2023", 21110083, 100.74274, 4.84725, "2023-07-04 17:02:07.761 +0800"),
    # ("V2XV001", "4/7/2023", 21110086, 100.74041, 4.84678, "2023-07-04 17:02:16.170 +0800"),
    # ("V2XV001", "4/7/2023", 821249, 100.74383, 4.85258, "2023-07-04 17:02:49.130 +0800"),
    # ("V2XV001", "4/7/2023", 834699, 100.743484, 4.84965, "2023-07-04 17:02:57.465 +0800"),
    # ("V2XV001", "4/7/2023", 21101100, 100.7477, 4.84457, "2023-07-04 17:03:09.483 +0800"),
    # ("V2XV001", "4/7/2023", 21114108, 100.74403, 4.84909, "2023-07-04 17:03:24.740 +0800"),
    # ("V2XV001", "4/7/2023", 21101069, 100.75128, 4.84286, "2023-07-04 17:03:31.883 +0800"),

    # ("V2XV001", "5/7/2023", 21108053, 100.71276, 4.84637, "2023-07-05 17:55:03.041 +0800"),
    # ("V2XV001", "5/7/2023", 803336, 100.72451, 4.83978, "2023-07-05 17:54:50.830 +0800"),
    # ("V2XV001", "5/7/2023", 21108161, 100.71788, 4.85121, "2023-07-05 17:54:36.501 +0800"),
    # ("V2XV001", "5/7/2023", 829233, 100.71258, 4.85244, "2023-07-05 17:54:07.282 +0800"),
    # ("V2XV001", "5/7/2023", 21108050, 100.71282, 4.85297, "2023-07-05 17:53:55.450 +0800"),
    # ("V2XV001", "5/7/2023", 21108049, 100.71275, 4.85286, "2023-07-05 17:53:32.659 +0800"),
    # ("V2XV001", "5/7/2023", 21108042, 100.71285, 4.85304, "2023-07-05 17:53:25.088 +0800"),
    # ("V2XV001", "5/7/2023", 21108098, 100.718, 4.85297, "2023-07-05 17:53:15.771 +0800"),
    # ("V2XV001", "5/7/2023", 21108100, 100.71861, 4.85256, "2023-07-05 17:53:08.048 +0800"),
    # ("V2XV001", "5/7/2023", 21108065, 100.71983, 4.85242, "2023-07-05 17:53:01.037 +0800"),
    # ("V2XV001", "5/7/2023", 664662, 100.7218, 4.85359, "2023-07-05 17:52:53.814 +0800"),
    # ("V2XV001", "5/7/2023", 405711, 100.71879, 4.8545, "2023-07-05 17:52:33.062 +0800"),
    # ("V2XV001", "5/7/2023", 21108112, 100.71854, 4.85456, "2023-07-05 17:51:43.823 +0800"),
    # ("V2XV001", "5/7/2023", 824778, 100.71876, 4.85498, "2023-07-05 17:51:20.949 +0800"),
    # ("V2XV001", "5/7/2023", 714188, 100.71837, 4.85509, "2023-07-05 17:51:01.572 +0800"),
    # ("V2XV001", "5/7/2023", 21108172, 100.71809, 4.85499, "2023-07-05 17:50:53.033 +0800"),
    # ("V2XV001", "5/7/2023", 347900, 100.71755, 4.85515, "2023-07-05 17:50:28.100 +0800"),
    # ("V2XV001", "5/7/2023", 21108057, 100.71721, 4.8555, "2023-07-05 17:50:21.551 +0800"),
    # ("V2XV001", "5/7/2023", 21108064, 100.71419, 4.8557, "2023-07-05 17:50:08.556 +0800"),
    # ("V2XV001", "5/7/2023", 816260, 100.71403, 4.85572, "2023-07-05 17:50:02.454 +0800"),
    # ("V2XV001", "5/7/2023", 669662, 100.71192, 4.8528, "2023-07-05 17:49:51.347 +0800"),
    # ("V2XV001", "5/7/2023", 531551, 100.71154, 4.85354, "2023-07-05 17:49:44.194 +0800"),
    # ("V2XV001", "5/7/2023", 21108068, 100.71233, 4.85652, "2023-07-05 17:49:24.926 +0800"),
    # ("V2XV001", "5/7/2023", 21108067, 100.70857, 4.85206, "2023-07-05 17:49:05.662 +0800"),
    # ("V2XV001", "5/7/2023", 21108046, 100.71208, 4.85317, "2023-07-05 17:48:57.843 +0800"),
    # ("V2XV001", "5/7/2023", 817414, 100.70764, 4.86383, "2023-07-05 17:47:47.236 +0800"),
    # ("V2XV001", "5/7/2023", 21108044, 100.71202, 4.85324, "2023-07-05 17:46:47.145 +0800"),
    # ("V2XV001", "5/7/2023", 320382, 100.71811, 4.85464, "2023-07-05 17:46:35.481 +0800"),
    # ("V2XV001", "5/7/2023", 376882, 100.7183, 4.85454, "2023-07-05 17:46:28.625 +0800"),
    # ("V2XV001", "5/7/2023", 21108137, 100.72245, 4.85477, "2023-07-05 17:46:22.439 +0800"),
    # ("V2XV001", "5/7/2023", 21108097, 100.73132, 4.85491, "2023-07-05 17:46:16.641 +0800"),
    # ("V2XV001", "5/7/2023", 803395, 100.73204, 4.85567, "2023-07-05 17:46:10.967 +0800"),
    # ("V2XV001", "5/7/2023", 807293, 100.73257, 4.85248, "2023-07-05 17:46:05.229 +0800"),
    # ("V2XV001", "5/7/2023", 815056, 100.73165, 4.85208, "2023-07-05 17:45:59.534 +0800"),
    # ("V2XV001", "5/7/2023", 621840, 100.71861, 4.84789, "2023-07-05 08:38:16.058 +0800"),

    ("V2XV001", "6/7/2023", 21101015, 100.72451, 4.84125, "2023-07-06 17:00:28.715 +0800"),
    ("V2XV001", "6/7/2023", 597428, 100.71922, 4.84213, "2023-07-06 17:00:40.972 +0800"),
    ("V2XV001", "6/7/2023", 590172, 100.71938, 4.84207, "2023-07-06 17:01:11.773 +0800"),
    ("V2XV001", "6/7/2023", 718010, 100.71928, 4.84672, "2023-07-06 17:01:23.677 +0800"),
    ("V2XV001", "6/7/2023", 21101022, 100.72116, 4.84435, "2023-07-06 17:01:36.127 +0800"),
    ("V2XV001", "6/7/2023", 735768, 100.72073, 4.84504, "2023-07-06 17:01:53.357 +0800"),
    ("V2XV001", "6/7/2023", 21110043, 100.74137, 4.84993, "2023-07-06 17:02:00.710 +0800"),
    ("V2XV001", "6/7/2023", 21101158, 100.72135, 4.844, "2023-07-06 17:02:06.608 +0800"),
    ("V2XV001", "6/7/2023", 21110044, 100.74142, 4.84997, "2023-07-06 17:02:12.805 +0800"),
    ("V2XV001", "6/7/2023", 21111069, 100.73702, 4.84882, "2023-07-06 17:02:18.922 +0800"),
    ("V2XV001", "6/7/2023", 21110018, 100.74142, 4.85272, "2023-07-06 17:02:35.290 +0800"),
    ("V2XV001", "6/7/2023", 21110101, 100.74245, 4.85105, "2023-07-06 17:02:41.721 +0800"),
    ("V2XV001", "6/7/2023", 21111038, 100.74001, 4.84942, "2023-07-06 17:02:48.245 +0800"),
    ("V2XV001", "6/7/2023", 21111039, 100.74028, 4.849441, "2023-07-06 17:02:58.232 +0800"),
    ("V2XV001", "6/7/2023", 21111006, 100.74037, 4.84978, "2023-07-06 17:03:05.057 +0800"),
    ("V2XV001", "6/7/2023", 21110070, 100.74177, 4.85097, "2023-07-06 17:03:12.384 +0800"),
    ("V2XV001", "6/7/2023", 21111004, 100.74031, 4.85011, "2023-07-06 17:03:20.888 +0800"),
    ("V2XV001", "6/7/2023", 21111011, 100.74037, 4.84978, "2023-07-06 17:03:29.371 +0800"),
    ("V2XV001", "6/7/2023", 21111026, 100.74033, 4.85022, "2023-07-06 17:03:37.050 +0800"),
    ("V2XV001", "6/7/2023", 21111020, 100.7403, 4.84996, "2023-07-06 17:03:45.289 +0800"),
    ("V2XV001", "6/7/2023", 21111105, 100.74039, 4.85014, "2023-07-06 17:03:52.711 +0800"),
    ("V2XV001", "6/7/2023", 21114052, 100.74605, 4.857, "2023-07-06 17:04:00.433 +0800"),
    ("V2XV001", "6/7/2023", 698148, 100.73873, 4.85025, "2023-07-06 17:04:10.680 +0800"),
]

# Sort van_data based on timestamps
van_data.sort(key=lambda x: x[5])

# Extract coordinates and outlet_ids for plotting
lng_values = [data[3] for data in van_data]
lat_values = [data[4] for data in van_data]
outlet_ids = [data[2] for data in van_data]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(lat_values, lng_values, c='blue', marker='o', label=van_data[0][0])

# # Draw arrows between consecutive points
# for i in range(len(lat_values) - 1):
#     dx = lat_values[i + 1] - lat_values[i]
#     dy = lng_values[i + 1] - lng_values[i]
#     arrow = patches.Arrow(lat_values[i], lng_values[i], dx, dy, width=0.0005, color='blue')
#     plt.gca().add_patch(arrow)

# Draw directional paths between consecutive points
for i in range(len(lat_values) - 1):
    plt.plot([lat_values[i], lat_values[i+1]], [lng_values[i], lng_values[i+1]], c='gray')

# Annotate points with outlet_id labels
for i, (lat, lng, outlet_id) in enumerate(zip(lat_values, lng_values, outlet_ids)):
    plt.annotate(f'Outlet: {outlet_id}', (lat, lng), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title(f'Van Movement for V2XV001 on {van_data[0][1]}')
plt.legend()
plt.grid(True)
# plt.xlim(min(lat_values) - 0.01, max(lat_values) + 0.01)  # Adjust the x-axis range
# plt.ylim(min(lng_values) - 0.01, max(lng_values) + 0.01)  # Adjust the y-axis range
plt.show()
