from enum import Enum
from collections import namedtuple

class ObsCat(Enum):
    DESCRIPTIVE_STATISTICS = "DESCRIPTIVE-STATISTICS"
    OUTLIERS = "OUTLIERS"
    RAW_PLOTS = "RAW-PLOTS"
    SMOOTHED_PLOTS = "SMOOTHED-PLOTS"
    CHANGE_POINTS = "CHANGE-POINTS"
    COMPONENT_CORRELATIONS = "COMPONENT-CORRELATIONS"
    GROUPING = "GROUPING"
    EXPLAINED_VARIANCE = "EXPLAINED-VARIANCE"
    ESTIMATED_NOISE = "ESTIMATED-NOISE"
    SPECIFIC_COMMENTS = "SPECIFIC-COMMENTS"

class ObservationTemplates:
    DESCRIPTIVE_STATISTICS = """Descriptive Statistics: There were {{num_samples}} samples, taken at a frequency of {{sampling_rate}}. The mean was {{ "%0.2f" | format(mean)}} and the standard deviation was {{ "%0.2f" | format(std)}}. Evaluation of the histogram and kernel density plots reveals a {{modality}} distribution."""
    OUTLIERS = """Outliers: Using the interquartile range (IQR) metric, the proportion of outliers was found to be {{ "%0.2f" | format(outlier_proportion)}}."""
    RAW_PLOTS = "Raw Plots: {{remarks}}"
    SMOOTHED_PLOTS = "Smoothed Plots: Visually, the Singular Spectrum Analysis (SSA) appears to achieve {{reconstruction_quality}} reconstruction. {{notes_for_cycles_trends_seasonality}}"
    CHANGE_POINTS = """Change Points: The chosen approach for capturing change points involves working with the smoothed version of the signal rather than the noisy, raw signal. While the drawback of this method is that it may require additional steps to detect change points within the noise component, smoothing allows us to use elementary calculus to identify shifts in the signal's derivative.
Peak-finding algorithms of varying sophistication can be applied for this purpose. Here, SciPy's find_peaks function is used to locate local maxima and minima in the smoothed signal. The code below demarcates these points, representing segments that may hold specific significance within the application's domain—a factor best interpreted by a domain expert.
Recall that the smoothed signal accounts for most of the variation in the observed signal. But what about the residuals? Since they often account for only a small portion of the variation, you might not be concerned with them. However, if you are interested in the nature of the residuals—for instance, if you plan to use the signal in a predictive model and need to confirm that the residuals are independent random variables—you can use the Durbin-Watson test. A test statistic in the range of 1.5 to 2.5 suggests the residuals are likely white noise.
If you need to verify if the noise is homogeneous (a crucial step if downstream predictive modeling is your goal), you can apply the PELT algorithm. Run this algorithm using a recommended penalty, as you likely do not know the exact number of change points in the random component. If the algorithm detects change points, it indicates that the noise level in the observations changes over time. If no change points are reported, then the noise is considered homogeneous.."""
    COMPONENT_CORRELATIONS = "Component Correlations: The following signal components appear to be correlated: {{ comma_sep_components }}."
    GROUPING = "Grouping: Based on the correlation plot, the following components can be grouped together: {{ comma_sep_components }}."
    EXPLAINED_VARIANCE = """Explained Variance: The smoothed signal explains {{ "%0.2f" | format(explained_variance)}}% of the variance."""
    ESTIMATED_NOISE = """Estimated Noise: The unexplained variance (noise) is estimated to be {{ "%0.2f" | format(noise_estimate)}}%."""
    SPECIFIC_COMMENTS = "Specific Comments: The noise appears to be {{correlated}}. {{additional_comments}}"

Observation = namedtuple("Observation", ["category", "observation"])


class ObservationLog:
    def __init__(self):
        self.observations = []

    def add_observation(self, category: ObsCat, observation: str):
        self.observations.append(
            Observation(category=category.value, observation=observation)
        )

    def get_observations(self):
        return self.observations
