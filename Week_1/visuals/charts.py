import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


SIGNAL_META = [
    ("stress_index",     "Stress Index",     "crimson",    "High = stressed / nervous"),
    ("confidence_score", "Confidence Score", "steelblue",  "High = composed / authoritative"),
    ("vocal_stability",  "Vocal Stability",  "seagreen",   "High = consistent, steady voice"),
    ("engagement_level", "Engagement Level", "darkorange", "High = active, energetic"),
]

EMOTION_COLORS = {
    "angry":   "crimson",
    "happy":   "steelblue",
    "neutral": "seagreen",
    "sad":     "darkorange",
}


def plot_signal_timeline(df: pd.DataFrame) -> plt.Figure:
    """
    4-panel signal timeline chart.
    One panel per interview signal with peak stress annotated.
    """
    fig, axes = plt.subplots(4, 1, figsize=(13, 11), sharex=True)
    fig.suptitle(
        "Interview Emotional Intelligence — Signal Timeline",
        fontsize=14, fontweight="bold", y=1.01
    )

    segments = df["segment"]

    for ax, (col, label, color, desc) in zip(axes, SIGNAL_META):
        ax.plot(segments, df[col], color=color, linewidth=2.3,
                marker="o", markersize=4, zorder=3)
        ax.fill_between(segments, df[col], alpha=0.12, color=color)
        ax.set_ylabel(label, fontsize=10)
        ax.set_ylim(0, 10)
        ax.axhline(y=5, color="gray", linestyle="--", linewidth=0.7, alpha=0.4)
        ax.set_title(desc, fontsize=8, color="gray", loc="right", pad=2)
        ax.grid(True, alpha=0.22)

        if col == "stress_index":
            peak_idx  = df[col].idxmax()
            peak_val  = df.loc[peak_idx, col]
            peak_seg  = df.loc[peak_idx, "segment"]
            peak_time = df.loc[peak_idx, "timestamp"]
            ax.annotate(
                f"Peak @ {peak_time}",
                xy=(peak_seg, peak_val),
                xytext=(peak_seg + 0.3, min(peak_val + 0.9, 9.5)),
                arrowprops=dict(arrowstyle="->", color="crimson", lw=1.2),
                fontsize=8, color="crimson",
            )

    if len(df) <= 35:
        axes[-1].set_xticks(segments)
        axes[-1].set_xticklabels(df["timestamp"], rotation=30, fontsize=7)

    axes[-1].set_xlabel("Segment (Timestamp)", fontsize=10)
    plt.tight_layout()
    return fig


def plot_acoustic_timeline(df: pd.DataFrame) -> plt.Figure:
    """
    2-panel chart showing raw acoustic signals (pitch + jitter).
    Shown separately so users can see the underlying measurements.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 6), sharex=True)
    fig.suptitle("Raw Acoustic Features", fontsize=13, fontweight="bold")

    segments = df["segment"]

    ax1.plot(segments, df["pitch_mean_hz"], color="purple",
             linewidth=2, marker="s", markersize=3)
    ax1.fill_between(segments, df["pitch_mean_hz"], alpha=0.10, color="purple")
    ax1.set_ylabel("Pitch Mean (Hz)", fontsize=10)
    ax1.set_title(
        "Fundamental Frequency — stress raises pitch involuntarily",
        fontsize=8, color="gray", loc="right"
    )
    ax1.grid(True, alpha=0.22)

    ax2.bar(segments, df["jitter"], color="slategray", alpha=0.75)
    ax2.set_ylabel("Jitter", fontsize=10)
    ax2.set_xlabel("Segment", fontsize=10)
    ax2.set_title(
        "Jitter — cycle-to-cycle pitch variation, impossible to control under stress",
        fontsize=8, color="gray", loc="right"
    )
    ax2.grid(True, alpha=0.22, axis="y")

    if len(df) <= 35:
        ax2.set_xticks(segments)
        ax2.set_xticklabels(df["timestamp"], rotation=30, fontsize=7)

    plt.tight_layout()
    return fig


def plot_emotion_distribution(df: pd.DataFrame) -> plt.Figure:
    """Bar chart of how many segments each emotion was detected."""
    counts = df["detected_emotion"].value_counts()
    colors = [EMOTION_COLORS.get(e, "gray") for e in counts.index]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(counts.index, counts.values, color=colors, edgecolor="white", linewidth=0.8)
    ax.set_title("Emotion Distribution Across Interview", fontsize=12)
    ax.set_xlabel("Detected Emotion")
    ax.set_ylabel("Segments")
    ax.grid(True, alpha=0.2, axis="y")
    plt.tight_layout()
    return fig