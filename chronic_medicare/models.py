from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AnalysisFile(models.Model):
    name = models.CharField(max_length=512)
    csv_file = models.FileField(upload_to='analysis-files/')
    description = models.TextField(max_length=1024, blank=True)

    class Meta:
      verbose_name_plural = "Raw Analysis Files"

    def __str__(self):
        return "{name}: {csv_file}".format(
            name=self.name,
            csv_file=self.csv_file.name.split('/')[-1])


@python_2_unicode_compatible
class ChronicConditionRegression(models.Model):
    source_file = models.ForeignKey(AnalysisFile, related_name="regressions")
    # NOTE: This is a very good case for either a FK, M2M, or ArrayField
    features = models.CharField(max_length=512)
    target = models.CharField(max_length=512)
    # NOTE: specify regression type, such as linear, logistic, etc. -- can this go wrong?
    analysis_type = models.CharField(max_length=512)
    description = models.TextField(max_length=2048, blank=True)
    summary_html = models.CharField(max_length=8192, blank=True)
    plot_html = models.CharField(max_length=8388608, blank=True)
    # Aikake's information criteria
    aic = models.FloatField(max_length=64, null=True, blank=True)
    # Bayes' information criteria
    bic = models.FloatField(max_length=64, null=True, blank=True)
    num_observations = models.IntegerField(null=True, blank=True)
    df_residuals = models.IntegerField(null=True, blank=True)
    r_squared = models.FloatField(max_length=64, null=True, blank=True)
    r_squared_adjusted = models.FloatField(max_length=64, null=True, blank=True)
    f_statistic = models.FloatField(max_length=64, null=True, blank=True)
    jarque_bera = models.FloatField(max_length=64, null=True, blank=True)
    jarque_bera_prob = models.FloatField(max_length=64, null=True, blank=True)
    skew = models.FloatField(max_length=64, null=True, blank=True)
    kurtosis = models.FloatField(max_length=64, null=True, blank=True)

    def __str__(self):
        return "{}: {} Regression from {}".format(
          self.id,
          self.analysis_type,
          self.source_file.name)