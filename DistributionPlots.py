# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student_exam_scores.csv')
sns.set_style("whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(24, 7))

# Plot 1: Hours Studied
sns.histplot(data=df, x='hours_studied', kde=True, ax=axes[0], color='skyblue', bins=15)
axes[0].axvline(x=6.15, color='red', linestyle='--', linewidth=2.5, label='Threshold (6.15)')
axes[0].set_title('Distribution of Hours Studied', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Hours Studied', fontsize=14)
axes[0].set_ylabel('Count', fontsize=14)
axes[0].legend(fontsize=12)

# Plot 2: Attendance Percent
sns.histplot(data=df, x='attendance_percent', kde=True, ax=axes[1], color='lightgreen', bins=15)
axes[1].axvline(x=75, color='red', linestyle='--', linewidth=2.5, label='Threshold (75%)')
axes[1].set_title('Distribution of Attendance', fontsize=16, fontweight='bold')
axes[1].set_xlabel('Attendance (%)', fontsize=14)
axes[1].set_ylabel('Count', fontsize=14)
axes[1].legend(fontsize=12)

# Plot 3: Sleep Hours
sleep_median = df['sleep_hours'].median()
sns.histplot(data=df, x='sleep_hours', kde=True, ax=axes[2], color='mediumpurple', bins=15)
axes[2].axvline(x=sleep_median, color='red', linestyle='--', linewidth=2.5, label=f'Threshold ({sleep_median})')
axes[2].set_title('Distribution of Sleep Hours', fontsize=16, fontweight='bold')
axes[2].set_xlabel('Sleep Hours', fontsize=14)
axes[2].set_ylabel('Count', fontsize=14)
axes[2].legend(fontsize=12)
plt.tight_layout()
plt.savefig('distribution_plots.png', dpi=300, bbox_inches='tight')

plt.show()

# %%



