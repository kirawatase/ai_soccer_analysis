import cv2
import numpy as np

class FieldZoneSegmenter:
    def __init__(self):
        # Define the zones of a standard soccer field (in meters)
        self.field_zones = {
            'left_penalty_area': np.array([(0, 13.85), (16.5, 13.85), (16.5, 40.3), (0, 40.3)]),
            'right_penalty_area': np.array([(105, 13.85), (88.5, 13.85), (88.5, 40.3), (105, 40.3)]),
            'center_circle': np.array([(52.5, 34.15), (52.5, 20)]),  # Center and top point of circle
            'left_half': np.array([(0, 0), (52.5, 0), (52.5, 68), (0, 68)]),
            'right_half': np.array([(52.5, 0), (105, 0), (105, 68), (52.5, 68)])
        }
        self.field_dimensions = (105, 68)  # Length and width in meters
        self.homography_matrix = None

    def compute_homography(self, src_points, dst_points):
        self.homography_matrix, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)

    def transform_point(self, point):
        if self.homography_matrix is None:
            raise ValueError("Homography matrix has not been computed yet.")
        transformed_point = cv2.perspectiveTransform(np.array([[point]]), self.homography_matrix)[0][0]
        return tuple(map(int, transformed_point))

    def get_zone(self, point):
        x, y = point
        for zone, coords in self.field_zones.items():
            if zone == 'center_circle':
                center, top = coords
                radius = top[1] - center[1]
                if np.linalg.norm(np.array([x, y]) - center) <= radius:
                    return zone
            elif cv2.pointPolygonTest(coords, (x, y), False) >= 0:
                return zone
        return 'other'

    def draw_zones(self, frame):
        if self.homography_matrix is None:
            raise ValueError("Homography matrix has not been computed yet.")
        
        for zone, coords in self.field_zones.items():
            if zone == 'center_circle':
                center = self.transform_point(coords[0])
                top = self.transform_point(coords[1])
                radius = top[1] - center[1]
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
            else:
                transformed_coords = np.array([self.transform_point(point) for point in coords])
                cv2.polylines(frame, [transformed_coords], True, (0, 255, 0), 2)
        
        return frame