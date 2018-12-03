import numpy as np

def geo_data_parse(data):
    ## take the floor of the x and y coordinates. Do not round to nearest integer.
    ## lat_log[0] is latitude; lat_log[1] is logtitude
    # PI_=3.14159
    data=np.array(data)
    deg = data.astype(int)
    min=data-deg

    lat_log=np.pi*(deg+5.0*min/3.0)/180.0

    ## this formula rounds the distance to the nearest integer.
    RRR=6378.388
    N=data.shape[0]
    adj=-1*np.ones((N,N))
    for i in range(N):
        for j in range(N):
            if i ==j:
                adj[i,j]=0
            else:
                if adj[i,j]==-1:
                    q1=np.cos(lat_log[i][1]-lat_log[j][1])
                    q2=np.cos(lat_log[i][0]-lat_log[j][0])
                    q3=np.cos(lat_log[i][0]+lat_log[j][0])
                    adj[i, j] = (RRR * np.arccos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0).astype(int)
                    adj[j, i]=adj[i,j]
    return adj


# elif dtype == "GEO":
# deg = coor.astype(int)
# coors = ((coor - deg) * 5. / 3. + deg) / 180. * np.pi
#
# q21 = np.cos(np.tile(coors, v_num).reshape((-1, 2)) - \
#              np.tile(coors.flatten(), v_num).reshape((-1, 2)))
#
# q1, q2 = q21[:, [1]].flatten(), q21[:, [0]].flatten()
# lat = coors[:, [0]]
#
# q3 = np.cos(np.tile(lat, v_num).flatten() + np.tile(lat.flatten(), v_num).flatten())
# dist = (np.arccos(.5 * ((1 + q1) * q2 - (1 - q1) * q3)) * 6378.388 + 1).reshape((v_num, v_num))
# cost_mat = np.diag([float('inf')] * v_num) + dist.astype(int)
# return cost_mat

