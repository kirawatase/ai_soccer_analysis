import matplotlib.pyplot as plt
import os
import numpy as np

class PlayerMaxAccelerationAnalyzer:
    def __init__(self, tracks, team_assigner):
        self.tracks = tracks
        self.team_assigner = team_assigner
        self.max_accelerations_team_1 = {}
        self.max_accelerations_team_2 = {}

    def calculate_max_acceleration_per_player(self):
        """Calculate the maximum acceleration for each player, limited to 11 players per team."""
        for frame_num, player_track in enumerate(self.tracks['players']):
            for player_id, track in player_track.items():
                acceleration = track.get('acceleration', 0)  # Get the acceleration of the player in the current frame

                # Exclude players with 0.0 m/s² acceleration
                if acceleration == 0:
                    continue

                # Determine the player's team
                team = self.team_assigner.get_player_team(None, track['bbox'], player_id)

                # Store maximum acceleration for each player on the correct team, limit to 11 players per team
                if team == 1 and len(self.max_accelerations_team_1) < 11:
                    self.max_accelerations_team_1[player_id] = max(self.max_accelerations_team_1.get(player_id, 0), acceleration)
                elif team == 2 and len(self.max_accelerations_team_2) < 11:
                    self.max_accelerations_team_2[player_id] = max(self.max_accelerations_team_2.get(player_id, 0), acceleration)

    def plot_max_accelerations(self):
        """Generate individual horizontal bar charts for the maximum accelerations of players on Team 1 and Team 2."""
        assets_folder = os.path.join(os.getcwd(), "assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)

        # Plot horizontal bar chart for Team 1 (individual output)
        if self.max_accelerations_team_1:
            players_team_1 = list(self.max_accelerations_team_1.keys())
            accelerations_team_1 = list(self.max_accelerations_team_1.values())

            plt.figure(figsize=(12, 8))
            bar_height = 0.8
            bars = plt.barh(np.arange(len(players_team_1)), accelerations_team_1, height=bar_height, color='#6684a5')
            plt.gca().set_yticks(np.arange(len(players_team_1)))
            plt.gca().set_yticklabels(players_team_1, fontsize=10)
            plt.title('Maximum Acceleration of Players on Team 1', fontsize=14, pad=15)
            plt.xlabel('Max Acceleration (m/s²)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')

            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height() / 2, '{:.2f} m/s²'.format(width), ha='left', va='center', fontsize=10, fontweight='bold')

            output_path_team_1 = os.path.join(assets_folder, "team_1_max_acceleration_chart.png")
            plt.savefig(output_path_team_1, dpi=300, bbox_inches='tight')
            plt.close()

        # Plot horizontal bar chart for Team 2 (individual output)
        if self.max_accelerations_team_2:
            players_team_2 = list(self.max_accelerations_team_2.keys())
            accelerations_team_2 = list(self.max_accelerations_team_2.values())

            plt.figure(figsize=(12, 8))
            bar_height = 0.8
            bars = plt.barh(np.arange(len(players_team_2)), accelerations_team_2, height=bar_height, color='#d5f0f5')
            plt.gca().set_yticks(np.arange(len(players_team_2)))
            plt.gca().set_yticklabels(players_team_2, fontsize=10)
            plt.title('Maximum Acceleration of Players on Team 2', fontsize=14, pad=15)
            plt.xlabel('Max Acceleration (m/s²)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')

            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height() / 2, '{:.2f} m/s²'.format(width), ha='left', va='center', fontsize=10, fontweight='bold')

            output_path_team_2 = os.path.join(assets_folder, "team_2_max_acceleration_chart.png")
            plt.savefig(output_path_team_2, dpi=300, bbox_inches='tight')
            plt.close()
