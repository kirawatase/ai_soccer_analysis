import matplotlib.pyplot as plt
import os
import numpy as np

class PlayerTotalDistanceAnalyzer:
    def __init__(self, tracks, team_assigner):
        self.tracks = tracks
        self.team_assigner = team_assigner
        self.total_distances_team_1 = {}
        self.total_distances_team_2 = {}

    def calculate_total_distance_per_player(self):
        """Calculate the total distance for each player and separate by teams."""
        for frame_num, player_track in enumerate(self.tracks['players']):
            for player_id, track in player_track.items():
                player_id = int(player_id)  # Ensure player ID is an integer
                distance = track.get('distance', 0)  # Get the distance of the player in the current frame
                
                # Determine the player's team
                team = self.team_assigner.get_player_team(None, track['bbox'], player_id)

                # Accumulate total distance for each player on the correct team
                if team == 1:  # Team 1
                    if player_id not in self.total_distances_team_1:
                        self.total_distances_team_1[player_id] = distance
                    else:
                        self.total_distances_team_1[player_id] += distance
                elif team == 2:  # Team 2
                    if player_id not in self.total_distances_team_2:
                        self.total_distances_team_2[player_id] = distance
                    else:
                        self.total_distances_team_2[player_id] += distance


    def plot_total_distances(self):
        """Generate individual horizontal bar charts for the total distances covered by players on Team 1 and Team 2."""
        # Create the assets folder if it doesn't exist
        assets_folder = os.path.join(os.getcwd(), "assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)

        # Filter out players with 0.0 meters
        self.total_distances_team_1 = {player: dist for player, dist in self.total_distances_team_1.items() if dist > 0}
        self.total_distances_team_2 = {player: dist for player, dist in self.total_distances_team_2.items() if dist > 0}

        # Plot horizontal bar chart for Team 1 (individual output)
        if self.total_distances_team_1:
            players_team_1 = list(self.total_distances_team_1.keys())
            distances_team_1 = list(self.total_distances_team_1.values())
            
            plt.figure(figsize=(12, 8))  # Increase the figure size for readability

            # Set the height of the bars (thicker bars)
            bar_height = 0.8  # Make the bars thicker
            
            # Plot horizontal bars with the correct Team 1 color (#6684a5)
            bars = plt.barh(np.arange(len(players_team_1)), distances_team_1, height=bar_height, color='#6684a5')

            # Set the y-axis to show only the player IDs, evenly distributed
            plt.gca().set_yticks(np.arange(len(players_team_1)))  # Set y-ticks evenly spaced for each player
            plt.gca().set_yticklabels(players_team_1, fontsize=10)  # Display player IDs as labels
            
            # Customize the chart
            plt.title('Total Distance of Players on Team 1', fontsize=14, pad=15)
            plt.xlabel('Total Distance (meters)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')

            # Add value labels on the bars
            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height()/2, '{:.2f} m'.format(width),
                         ha='left', va='center', fontsize=10, fontweight='bold')

            # Save the figure for Team 1
            output_path_team_1 = os.path.join(assets_folder, "team_1_total_distance_chart.png")
            plt.savefig(output_path_team_1, dpi=300, bbox_inches='tight')
            print(f"Total distance chart for Team 1 saved to {output_path_team_1}")
            plt.close()

        # Plot horizontal bar chart for Team 2 (individual output)
        if self.total_distances_team_2:
            players_team_2 = list(self.total_distances_team_2.keys())
            distances_team_2 = list(self.total_distances_team_2.values())
            
            plt.figure(figsize=(12, 8))  # Increase the figure size for readability

            # Set the height of the bars (thicker bars)
            bar_height = 0.8  # Make the bars thicker
            
            # Plot horizontal bars with the correct Team 2 color (#d5f0f5)
            bars = plt.barh(np.arange(len(players_team_2)), distances_team_2, height=bar_height, color='#d5f0f5')

            # Set the y-axis to show only the player IDs, evenly distributed
            plt.gca().set_yticks(np.arange(len(players_team_2)))  # Set y-ticks evenly spaced for each player
            plt.gca().set_yticklabels(players_team_2, fontsize=10)  # Display player IDs as labels
            
            # Customize the chart
            plt.title('Total Distance of Players on Team 2', fontsize=14, pad=15)
            plt.xlabel('Total Distance (meters)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')

            # Add value labels on the bars
            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height()/2, '{:.2f} m'.format(width),
                         ha='left', va='center', fontsize=10, fontweight='bold')

            # Save the figure for Team 2
            output_path_team_2 = os.path.join(assets_folder, "team_2_total_distance_chart.png")
            plt.savefig(output_path_team_2, dpi=300, bbox_inches='tight')
            print(f"Total distance chart for Team 2 saved to {output_path_team_2}")
            plt.close()
