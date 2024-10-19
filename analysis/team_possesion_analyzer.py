import numpy as np
import matplotlib.pyplot as plt
import os

class TeamPossessionAnalyzer:
    def __init__(self, frame_rate):
        self.team_possession_frames = []  # To store the team possession at each frame
        self.frame_rate = frame_rate

    def add_possession(self, team_id):
        """Add the team possession for the current frame."""
        self.team_possession_frames.append(team_id)

    def plot_possession_over_time(self):
    # Convert frame numbers to time in seconds
        time_in_seconds = np.arange(0, len(self.team_possession_frames)) / self.frame_rate

    # Convert possession list to numpy array
        possession_array = np.array(self.team_possession_frames)

    # Calculate cumulative possession for Team 1
        cumulative_team_1 = np.cumsum(possession_array == 1)
        cumulative_team_2 = np.cumsum(possession_array == 2)

    # Calculate cumulative possession percentage for Team 1 over time
        total_frames = len(possession_array)
        cumulative_percentage_team_1 = (cumulative_team_1 / np.arange(1, total_frames + 1)) * 100
        cumulative_percentage_team_2 = 100 - cumulative_percentage_team_1  # Since possession percentages sum to 100%

    # Plot the cumulative possession line
        plt.figure(figsize=(10, 6))

    # Fill the area above the line (Team 1 with color #1b2487) and below the line (Team 2 with color #9faeea)
        plt.fill_between(time_in_seconds, 0, cumulative_percentage_team_1, facecolor='#6684a5', alpha=0.6, label='Team 1')
        plt.fill_between(time_in_seconds, cumulative_percentage_team_1, 100, facecolor='#d5f0f5', alpha=0.6, label='Team 2')

    # Plot the line for cumulative possession percentage
        plt.plot(time_in_seconds, cumulative_percentage_team_1, color='black', linewidth=1)

    # Customize chart
        plt.title('Cumulative Team Possession Over Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Cumulative Possession (%)')
        plt.ylim(0, 100)  # Y-axis is percentage from 0% to 100%
        plt.grid(True)
        plt.legend(loc='upper right')

    # Create the assets folder if it doesn't exist
        assets_folder = os.path.join(os.getcwd(), "assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)

    # Save the figure as a PNG in the assets folder
        output_path = os.path.join(assets_folder, "team_possession_percentage_chart.png")
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Cumulative possession percentage chart saved to {output_path}")

    # Close the plot to free memory
        plt.close()

