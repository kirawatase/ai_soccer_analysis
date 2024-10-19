from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_and_distance_estimator import SpeedAndDistance_Estimator
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = ['Arial', 'Tahoma', 'DejaVu Sans']


class TeamPossessionAnalyzer:
    def __init__(self, frame_rate):
        self.team_possession_frames = []  # To store the team possession at each frame
        self.frame_rate = frame_rate

    def add_possession(self, team_id):
        """Add the team possession for the current frame."""
        self.team_possession_frames.append(team_id)

    def plot_possession_over_time(self):
        """Plot and save a cumulative possession percentage line chart over time with custom team colors."""
        time_in_seconds = np.arange(0, len(self.team_possession_frames)) / self.frame_rate
        possession_array = np.array(self.team_possession_frames)

        cumulative_team_1 = np.cumsum(possession_array == 1)
        cumulative_team_2 = np.cumsum(possession_array == 2)

        total_frames = len(possession_array)
        cumulative_percentage_team_1 = (cumulative_team_1 / np.arange(1, total_frames + 1)) * 100
        cumulative_percentage_team_2 = 100 - cumulative_percentage_team_1

        plt.figure(figsize=(10, 6))
        plt.fill_between(time_in_seconds, 0, cumulative_percentage_team_1, facecolor='#6684a5', alpha=0.6, label='Team 1')
        plt.fill_between(time_in_seconds, cumulative_percentage_team_1, 100, facecolor='#d5f0f5', alpha=0.6, label='Team 2')
        plt.plot(time_in_seconds, cumulative_percentage_team_1, color='black', linewidth=1)
        plt.title('Cumulative Team Possession Over Time', fontsize=14)
        plt.xlabel('Time (seconds)', fontsize=12)
        plt.ylabel('Cumulative Possession (%)', fontsize=12)
        plt.ylim(0, 100)
        plt.grid(True)
        plt.legend(loc='upper right')

        assets_folder = os.path.join(os.getcwd(), "assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)
        output_path = os.path.join(assets_folder, "team_possession_percentage_chart.png")
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()


class PlayerMaxSpeedAnalyzer:
    def __init__(self, tracks, team_assigner):
        self.tracks = tracks
        self.team_assigner = team_assigner
        self.max_speeds_team_1 = {}
        self.max_speeds_team_2 = {}

    def calculate_max_speed_per_player(self):
        """Calculate the maximum speed for each player, limited to 11 players per team."""
        for frame_num, player_track in enumerate(self.tracks['players']):
            for player_id, track in player_track.items():
                speed = track.get('speed', 0)  # Get the speed of the player in the current frame

                # Exclude players with 0.0 m/s speeds
                if speed == 0:
                    continue

                # Determine the player's team
                team = self.team_assigner.get_player_team(None, track['bbox'], player_id)

                # Store maximum speed for each player on the correct team, limit to 11 players per team
                if team == 1 and len(self.max_speeds_team_1) < 11:
                    self.max_speeds_team_1[player_id] = max(self.max_speeds_team_1.get(player_id, 0), speed)
                elif team == 2 and len(self.max_speeds_team_2) < 11:
                    self.max_speeds_team_2[player_id] = max(self.max_speeds_team_2.get(player_id, 0), speed)

    def plot_max_speeds(self):
        """Generate individual horizontal bar charts for the maximum speeds of players on Team 1 and Team 2."""
        assets_folder = os.path.join(os.getcwd(), "assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)

        # Plot horizontal bar chart for Team 1
        if self.max_speeds_team_1:
            players_team_1 = list(self.max_speeds_team_1.keys())
            speeds_team_1 = list(self.max_speeds_team_1.values())

            plt.figure(figsize=(12, 8))
            bar_height = 0.8
            bars = plt.barh(np.arange(len(players_team_1)), speeds_team_1, height=bar_height, color='#6684a5')
            plt.gca().set_yticks(np.arange(len(players_team_1)))
            plt.gca().set_yticklabels(players_team_1, fontsize=10)
            plt.title('Maximum Speed of Players on Team 1', fontsize=14, pad=15)
            plt.xlabel('Max Speed (m/s)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')
            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height() / 2, '{:.2f} m/s'.format(width), ha='left', va='center', fontsize=10, fontweight='bold')
            output_path_team_1 = os.path.join(assets_folder, "team_1_max_speed_chart.png")
            plt.savefig(output_path_team_1, dpi=300, bbox_inches='tight')
            plt.close()

        # Plot horizontal bar chart for Team 2
        if self.max_speeds_team_2:
            players_team_2 = list(self.max_speeds_team_2.keys())
            speeds_team_2 = list(self.max_speeds_team_2.values())

            plt.figure(figsize=(12, 8))
            bar_height = 0.8
            bars = plt.barh(np.arange(len(players_team_2)), speeds_team_2, height=bar_height, color='#d5f0f5')
            plt.gca().set_yticks(np.arange(len(players_team_2)))
            plt.gca().set_yticklabels(players_team_2, fontsize=10)
            plt.title('Maximum Speed of Players on Team 2', fontsize=14, pad=15)
            plt.xlabel('Max Speed (m/s)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')
            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height() / 2, '{:.2f} m/s'.format(width), ha='left', va='center', fontsize=10, fontweight='bold')
            output_path_team_2 = os.path.join(assets_folder, "team_2_max_speed_chart.png")
            plt.savefig(output_path_team_2, dpi=300, bbox_inches='tight')
            plt.close()


class PlayerTotalDistanceAnalyzer:
    def __init__(self, tracks, team_assigner):
        self.tracks = tracks
        self.team_assigner = team_assigner
        self.total_distances_team_1 = {}
        self.total_distances_team_2 = {}

    def calculate_total_distance_per_player(self):
        """Calculate the total distance for each player, limited to 11 players per team."""
        for frame_num, player_track in enumerate(self.tracks['players']):
            for player_id, track in player_track.items():
                distance = track.get('distance', 0)

                # Exclude players with 0.0 m distance
                if distance == 0:
                    continue

                team = self.team_assigner.get_player_team(None, track['bbox'], player_id)

                # Accumulate total distance for each player, limit to 11 players per team
                if team == 1 and len(self.total_distances_team_1) < 11:
                    self.total_distances_team_1[player_id] = self.total_distances_team_1.get(player_id, 0) + distance
                elif team == 2 and len(self.total_distances_team_2) < 11:
                    self.total_distances_team_2[player_id] = self.total_distances_team_2.get(player_id, 0) + distance

    def plot_total_distances(self):
        """Generate individual horizontal bar charts for the total distances covered by players on Team 1 and Team 2."""
        assets_folder = os.path.join(os.getcwd(), "assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)

        # Plot horizontal bar chart for Team 1
        if self.total_distances_team_1:
            players_team_1 = list(self.total_distances_team_1.keys())
            distances_team_1 = list(self.total_distances_team_1.values())

            plt.figure(figsize=(12, 8))
            bar_height = 0.8
            bars = plt.barh(np.arange(len(players_team_1)), distances_team_1, height=bar_height, color='#6684a5')
            plt.gca().set_yticks(np.arange(len(players_team_1)))
            plt.gca().set_yticklabels(players_team_1, fontsize=10)
            plt.title('Total Distance of Players on Team 1', fontsize=14, pad=15)
            plt.xlabel('Total Distance (meters)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')
            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height() / 2, '{:.2f} m'.format(width), ha='left', va='center', fontsize=10, fontweight='bold')
            output_path_team_1 = os.path.join(assets_folder, "team_1_total_distance_chart.png")
            plt.savefig(output_path_team_1, dpi=300, bbox_inches='tight')
            plt.close()

        # Plot horizontal bar chart for Team 2
        if self.total_distances_team_2:
            players_team_2 = list(self.total_distances_team_2.keys())
            distances_team_2 = list(self.total_distances_team_2.values())

            plt.figure(figsize=(12, 8))
            bar_height = 0.8
            bars = plt.barh(np.arange(len(players_team_2)), distances_team_2, height=bar_height, color='#d5f0f5')
            plt.gca().set_yticks(np.arange(len(players_team_2)))
            plt.gca().set_yticklabels(players_team_2, fontsize=10)
            plt.title('Total Distance of Players on Team 2', fontsize=14, pad=15)
            plt.xlabel('Total Distance (meters)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')
            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height() / 2, '{:.2f} m'.format(width), ha='left', va='center', fontsize=10, fontweight='bold')
            output_path_team_2 = os.path.join(assets_folder, "team_2_total_distance_chart.png")
            plt.savefig(output_path_team_2, dpi=300, bbox_inches='tight')
            plt.close()


def main():
    video_frames = read_video('input_videos/08fd33_4.mp4')
    tracker = Tracker('models/best.pt')

    # Get object tracks
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')

    tracker.add_position_to_tracks(tracks)

    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames, read_from_stub=True, stub_path='stubs/camera_movement_stub.pkl')
    camera_movement_estimator.add_adjust_positions_to_tracks(tracks, camera_movement_per_frame)

    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)

    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    speed_and_distance_estimator = SpeedAndDistance_Estimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

    frame_rate = 24
    possession_analyzer = TeamPossessionAnalyzer(frame_rate)

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    player_assigner = PlayerBallAssigner()
    team_ball_control = []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])

        possession_analyzer.add_possession(team_ball_control[-1])

    possession_analyzer.plot_possession_over_time()

    player_max_speed_analyzer = PlayerMaxSpeedAnalyzer(tracks, team_assigner)
    player_max_speed_analyzer.calculate_max_speed_per_player()
    player_max_speed_analyzer.plot_max_speeds()

    player_total_distance_analyzer = PlayerTotalDistanceAnalyzer(tracks, team_assigner)
    player_total_distance_analyzer.calculate_total_distance_per_player()
    player_total_distance_analyzer.plot_total_distances()

    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)
    speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)

    save_video(output_video_frames, 'output_videos/output_video.mp4')


if __name__ == '__main__':
    main()
