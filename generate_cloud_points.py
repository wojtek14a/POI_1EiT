from scipy.stats import norm
from csv import writer


def genrate_points(num=1000, shape="flat_h"):
    if shape == "flat_h":
        dist_x = norm(loc=0, scale=100)
        dist_y = norm(loc=0, scale=150)
        dist_z = norm(loc=0, scale=0)
    elif shape == "flat_v":
        dist_x = norm(loc=500, scale=100)
        dist_y = norm(loc=500, scale=0)
        dist_z = norm(loc=500, scale=150)
    elif shape == "cylindrical":
        dist_x = norm(loc=1000, scale=50)
        dist_y = dist_x
        dist_z = norm(loc=1000, scale=80)

    x = dist_x.rvs(size=num)
    y = dist_y.rvs(size=num)
    z = dist_z.rvs(size=num)

    points = zip(x, y, z)
    return points


if __name__ == "__main__":
    points = []
    for shape in ["flat_h", "flat_v", "cylindrical"]:
        point = genrate_points(shape=shape)
        points.extend(point)

    with open('points.xyz', 'w', newline='\n') as csvfile:
        csvwriter = writer(csvfile)

        for p in points:
            csvwriter.writerow(p)
