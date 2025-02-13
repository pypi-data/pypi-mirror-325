"""Metrics for the FSA collector."""

from loguru import logger as log
from prometheus_client import Gauge

from .collector import FSACollector


class FileSizeAgeMetrics:
    """Product metrics class."""

    def __init__(self, config):
        """FileSizeAgeMetrics constructor.

        Parameters
        ----------
        config : box.Box
            The config as returned by `fsa_metrics.config.load_config_file`.
        """
        log.trace(f"Instantiating {self.__class__}...")
        self._config = config
        self.collectors = {}
        """A dict of `fsa_metrics.collector.FSACollector` for metrics collection."""
        for metrics in config.fsa_metrics:
            ref = f"{metrics.scan_dir}://:{metrics.pattern}"
            self.collectors[ref] = FSACollector(
                metrics.scan_dir, metrics.pattern, config.show_dirs
            )

        self.detail_gauges = {
            "size": Gauge(
                name="fsa_size_bytes",
                documentation="size of the file in bytes",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "age": Gauge(
                name="fsa_age_seconds",
                documentation="age of the file in seconds",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
        }
        """A dict of gauges for the individual files metrics."""

        self.summary_gauges = {
            "oldest_age": Gauge(
                name="fsa_oldest_age_seconds",
                documentation="age of the OLDEST file in the tree in seconds",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "oldest_size": Gauge(
                name="fsa_oldest_size_bytes",
                documentation="size of the OLDEST file in the tree in bytes",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "newest_age": Gauge(
                name="fsa_newest_age_seconds",
                documentation="age of the NEWEST file in the tree in seconds",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "newest_size": Gauge(
                name="fsa_newest_size_bytes",
                documentation="size of the NEWEST file in the tree in bytes",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "biggest_age": Gauge(
                name="fsa_biggest_age_seconds",
                documentation="age of the BIGGEST file in the tree in seconds",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "biggest_size": Gauge(
                name="fsa_biggest_size_bytes",
                documentation="size of the BIGGEST file in the tree in bytes",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "smallest_age": Gauge(
                name="fsa_smallest_age_seconds",
                documentation="age of the SMALLEST file in the tree in seconds",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
            "smallest_size": Gauge(
                name="fsa_smallest_size_bytes",
                documentation="size of the SMALLEST file in the tree in bytes",
                labelnames=["type", "pattern", "path", "name", "parent"],
            ),
        }
        """Summary gauges for oldest / newest / smallest / biggest details."""

        log.trace(f"Finished instantiating {self.__class__}.")

    def clear_all_gauges(self):
        """Clear all registered gauges to prepare them for the next round.

        This is required as otherwise values from previous iterations (that do
        not exist in the current run any) more would still be around with their
        old value.
        """
        for name, gauge in self.detail_gauges.items():
            log.trace(f"Clearing labelsets for details gauge {name}...")
            gauge.clear()

        for name, gauge in self.summary_gauges.items():
            log.trace(f"Clearing labelsets for summary gauge {name}...")
            gauge.clear()

    def update_all_metrics(self):
        """Clear all gauges, collect metrics and set new gauge values."""
        self.clear_all_gauges()

        log.debug("Updating all metrics...")

        for ref, collector in self.collectors.items():
            try:
                pattern = ref.split("://:")[1]
                files_details = collector.collect()
                self.set_values(files_details, pattern)
            except Exception as err:  # pylint: disable-msg=broad-except
                log.exception(f"Update on [{ref}] failed: {err}")

    def set_values(self, details, pattern):
        """Feed the gauges with current metric values.

        Parameters
        ----------
        details : list
            The list of file details as collected by `FSACollector.collect()`.
        pattern: str
            The scan pattern that was used to produce the metrics.
        """
        if not details:
            return

        g_size = self.detail_gauges["size"]
        g_age = self.detail_gauges["age"]

        newest = oldest = biggest = smallest = None

        for cur_detail in details:
            dirname, basename, ftype, size, age, parent = cur_detail
            if not self._config.show_dirs and ftype == "dir":
                continue

            g_size.labels(ftype, pattern, dirname, basename, parent).set(size)
            g_age.labels(ftype, pattern, dirname, basename, parent).set(age)

            # set current item if no extrema values have been recorded before
            # (all items have been of type "dir" and "show_dirs" is `False`)
            if newest is None:
                newest = oldest = biggest = smallest = cur_detail

            if cur_detail[4] < newest[4]:
                newest = cur_detail
            if cur_detail[4] > oldest[4]:
                oldest = cur_detail
            if cur_detail[3] > biggest[3]:
                biggest = cur_detail
            if cur_detail[3] < smallest[3]:
                smallest = cur_detail

        if newest is None:
            log.warning(
                f"No extrema could be found in {len(details)} records. "
                "The tree contains only directories or is completely empty."
            )
            return

        extrema = {
            "newest": newest,
            "oldest": oldest,
            "biggest": biggest,
            "smallest": smallest,
        }

        self.update_summary_metric(extrema, pattern)

    def update_summary_metric(self, extrema, pattern):
        """Helper method to update the various summary metrics gauges.

        Parameters
        ----------
        extrema : dict
            The dict with extrema values of the current scan configuration
            (described by the path and pattern), containing the details for the
            smallest, biggest, oldest and newest items.
        pattern: str
            The scan pattern that was used to produce the metrics.
        """
        for name, details in extrema.items():

            # log.trace(f"Updating '{name}' summary gauge: {details}")
            dirname, basename, ftype, size, age, parent = details

            gauge_size = self.summary_gauges[f"{name}_size"]
            gauge_size.labels(ftype, pattern, dirname, basename, parent).set(size)

            gauge_age = self.summary_gauges[f"{name}_age"]
            gauge_age.labels(ftype, pattern, dirname, basename, parent).set(age)
