import base64

from sapiopylib.rest.DataRecordManagerService import DataRecordManager
from sapiopylib.rest.ELNService import ElnManager
from sapiopylib.rest.User import SapioUser
from sapiopylib.rest.pojo.DataRecord import DataRecord
from sapiopylib.rest.pojo.chartdata.DashboardDefinition import GaugeChartDefinition
from sapiopylib.rest.pojo.chartdata.DashboardEnums import ChartGroupingType, ChartOperationType, ChartType
from sapiopylib.rest.pojo.chartdata.DashboardSeries import GaugeChartSeries
from sapiopylib.rest.pojo.eln.ElnExperiment import ElnExperiment
from sapiopylib.rest.pojo.eln.ExperimentEntry import ExperimentEntry
from sapiopylib.rest.pojo.eln.ExperimentEntryCriteria import ElnEntryCriteria, ElnFormEntryUpdateCriteria
from sapiopylib.rest.pojo.eln.SapioELNEnums import ElnEntryType, ElnBaseDataType
from sapiopylib.rest.pojo.eln.eln_headings import ElnExperimentTabAddCriteria, ElnExperimentTab
from sapiopylib.rest.pojo.eln.field_set import ElnFieldSetInfo
from sapiopylib.rest.utils.ProtocolUtils import ELNStepFactory
from sapiopylib.rest.utils.Protocols import ElnEntryStep, ElnExperimentProtocol

from sapiopycommons.general.exceptions import SapioException


# FR-47422: Create utility methods to assist the tool of tools.
def create_tot_headers(url: str, username: str, password: str, experiment_id: int, tab_prefix: str) \
        -> tuple[str, dict[str, str]]:
    """
    Create the headers to be passed to a tool of tools endpoint.

    :param url: The webservice URL of the system to make the changes in.
    :param username: The username of the user making the changes.
    :param password: The password of the user making the changes.
    :param experiment_id: The ID of the experiment to make the changes in.
    :param tab_prefix: The prefix to use for the tab name that will be created by the tool.
    :return: The encoded credentials and the headers to be passed to the endpoint.
    """
    # Combine the credentials into the format "username:password"
    credentials: str = f"{username}:{password}"
    # Encode the credentials to bytes, then encode them using base64,
    # and finally convert the result back into a string.
    encoded_credentials: str = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    headers: dict[str, str] = {
        "SAPIO_APP_API_KEY": f"Basic {encoded_credentials}",
        "SAPIO_APP_API_URL": url,
        "EXPERIMENT_ID": str(experiment_id),
        "TAB_PREFIX": tab_prefix
    }
    return encoded_credentials, headers


def create_user_from_tot_headers(headers: dict[str, str]) -> SapioUser:
    """
    Create a SapioUser object from the headers passed to a tool of tools endpoint.

    :param headers: The headers that were passed to the endpoint.
    :return: A SapioUser object created from the headers that can be used to communicate with the Sapio server.
    """
    credentials = base64.b64decode(headers["SAPIO_APP_API_KEY"].removeprefix("Basic ")).decode("utf-8").split(":", 1)
    return SapioUser(headers["SAPIO_APP_API_URL"], username=credentials[0], password=credentials[1])


class ToolOfToolsHelper:
    """
    A class with helper methods utilized by the Tool of Tools for the creation and updating of experiment tabs that
    track a tool's progress and results.
    """
    # Contextual info.
    user: SapioUser
    tab_prefix: str
    exp_id: int
    _protocol: ElnExperimentProtocol

    # Tool info.
    name: str
    description: str
    results_data_type: str | None

    # Managers.
    eln_man: ElnManager
    dr_man: DataRecordManager

    # Stuff created by this helper.
    _initialized: bool
    """Whether a tab for this tool has been initialized."""
    tab: ElnExperimentTab
    """The tab that contains the tool's entries."""
    description_entry: ElnEntryStep
    """The text entry that displays the description of the tool."""
    progress_entry: ElnEntryStep
    """A hidden entry for tracking the progress of the tool."""
    progress_record: DataRecord
    """The record that stores the progress of the tool."""
    progress_gauge_entry: ElnEntryStep
    """A chart entry that displays the progress of the tool using the hidden progress entry."""
    results_entry: ElnEntryStep | None
    """An entry for displaying the results of the tool. If None, the tool does not produce result records."""

    def __init__(self, headers: dict[str, str], name: str, description: str, results_data_type: str | None = None):
        """
        :param headers: The headers that were passed to the endpoint.
        :param name: The name of the tool.
        :param description: A description of the tool.
        :param results_data_type: The data type name for the results of the tool. If None, the tool does not produce
            result records.
        """
        self.user = create_user_from_tot_headers(headers)
        self.exp_id = int(headers["EXPERIMENT_ID"])
        self.tab_prefix = headers["TAB_PREFIX"]
        # The experiment name and record ID aren't necessary to know.
        self._protocol = ElnExperimentProtocol(ElnExperiment(self.exp_id, "", 0), self.user)

        self.name = name
        self.description = description
        self.results_data_type = results_data_type

        self.eln_man = ElnManager(self.user)
        self.dr_man = DataRecordManager(self.user)

        self._initialized = False

    def initialize_tab(self) -> ElnExperimentTab:
        if self._initialized:
            return self.tab
        self._initialized = True

        # Create the tab for the tool progress and results.
        # The entry IDs list can't be empty, so we need to create a dummy entry just to get the tab created.
        tab_crit = ElnExperimentTabAddCriteria(f"{self.tab_prefix} {self.name}", [])
        tab: ElnExperimentTab = self.eln_man.add_tab_for_experiment(self.exp_id, tab_crit)
        self.tab = tab

        # Create a hidden entry for tracking the progress of the tool.
        field_sets: list[ElnFieldSetInfo] = self.eln_man.get_field_set_info_list()
        progress_field_set: list[ElnFieldSetInfo] = [x for x in field_sets if
                                                     x.field_set_name == "Tool of Tools Progress"]
        if not progress_field_set:
            raise SapioException("Unable to locate the field set for the Tool of Tools progress.")
        progress_entry_crit = ElnEntryCriteria(ElnEntryType.Form, f"ELaiN: {self.name} Progress",
                                               ElnBaseDataType.EXPERIMENT_DETAIL.data_type_name, 1,
                                               notebook_experiment_tab_id=tab.tab_id,
                                               enb_field_set_id=progress_field_set[0].field_set_id)
        progress_entry = ElnEntryStep(self._protocol,
                                      self.eln_man.add_experiment_entry(self.exp_id, progress_entry_crit))
        self.progress_entry = progress_entry
        self.progress_record = progress_entry.get_records()[0]

        # Hide the progress entry.
        update_crit = ElnFormEntryUpdateCriteria()
        update_crit.is_hidden = True
        self.eln_man.update_experiment_entry(self.exp_id, progress_entry.get_id(), update_crit)

        # Create a gauge entry to display the progress.
        gauge_entry: ElnEntryStep = self._create_gauge_chart(self._protocol, progress_entry,
                                                             f"{self.name} Progress", "Progress")
        self.progress_gauge_entry = gauge_entry

        # Create the text entry that displays the description of the tool.
        text_entry: ElnEntryStep = ELNStepFactory.create_text_entry(self._protocol, self.description)
        self.description_entry = text_entry

        # Create a results entry if this tool produces result records.
        if self.results_data_type:
            results_entry = ELNStepFactory.create_table_step(self._protocol, f"{self.name} Results", self.results_data_type)
            self.results_entry = results_entry
        else:
            self.results_entry = None

        return tab

    def update_progress(self, progress: float, status_msg: str | None = None) -> None:
        """
        Updates the progress of the tool.

        :param progress: A value between 0 and 100 representing the progress of the tool.
        :param status_msg: A status message to display to the user alongside the progress gauge.
        """
        if not self._initialized:
            raise SapioException("The tab for this tool has not been initialized.")
        self.progress_record.set_field_value("Progress", progress)
        self.progress_record.set_field_value("StatusMsg", status_msg)
        self.dr_man.commit_data_records([self.progress_record])

    def add_attachment_entry(self, file_name: str, file_data: str | bytes, entry_name: str,
                             tab: ElnExperimentTab | None = None) -> ExperimentEntry:
        """
        Add a new attachment entry to the experiment with the provided attachment data.

        :param file_name: The name of the attachment.
        :param file_data: The data of the attachment. This can be a string or bytes.
        :param entry_name: Name of the attachment entry to create in the experiment.
        :param tab: The tab where the attachment will be added. If not provided, the tab initialized by this helper
            will be used.
        :return: The created entry object.
        """
        # Check if the tab has been initialized or a tab has been provided.
        if not self._initialized and tab is None:
            raise SapioException("The tab for this tool has not been initialized. Either initialize a tab for this "
                                 "tool or provide the tab to this function to add the attachment entry to.")
        tab_id: int = self.tab.tab_id if tab is None else tab.tab_id

        # Encode the file contents in base64.
        if isinstance(file_data, str):
            file_data: bytes = file_data.encode("utf-8")
        base64_encoded: str = base64.b64encode(file_data).decode("utf-8")

        # Crete an attachment entry with the provided data.
        attachment_entry = self.eln_man.add_experiment_entry(
            self.exp_id,
            ElnEntryCriteria(ElnEntryType.Attachment, entry_name, "Attachment", order=2,
                             notebook_experiment_tab_id=tab_id, attachment_file_name=file_name,
                             attachment_data_base64=base64_encoded)
        )

        # Return the entry object for further use.
        return attachment_entry

    def add_attachment_entry_from_file_system(self, file_path: str, entry_name: str,
                                              tab: ElnExperimentTab | None = None) -> ExperimentEntry:
        """
        Add a new attachment entry to the experiment with the provided file path to a file in the file system.

        :param file_path: The path to a file in the system to attach to the experiment.
        :param entry_name: Name of the attachment entry to create in the experiment.
        :param tab: The tab where the attachment will be added. If not provided, the tab initialized by this helper
            will be used.
        :return: The created entry object.
        """
        # Check if the tab has been initialized or a tab has been provided.
        # This is redundant with the same check in the add_attachment_entry function, but it's duplicated here as to
        # not read the provided file and then find out we can't do anything with it anyway.
        if not self._initialized and tab is None:
            raise SapioException("The tab for this tool has not been initialized. Either initialize a tab for this "
                                 "tool or provide the tab to this function to add the attachment entry to.")

        with open(file_path, 'rb') as f:
            file_contents: bytes = f.read()
            return self.add_attachment_entry(file_path, file_contents, entry_name, tab)

    # TODO: Remove this once pylib has a gauge chart function in ElnStepFactory.
    @staticmethod
    def _create_gauge_chart(protocol: ElnExperimentProtocol, data_source_step: ElnEntryStep, step_name: str,
                            field_name: str, group_by_field_name: str = "DataRecordName") -> ElnEntryStep:
        """
        Create a gauge chart step in the experiment protocol.
        """
        if not data_source_step.get_data_type_names():
            raise ValueError("The data source step did not declare a data type name.")
        data_type_name: str = data_source_step.get_data_type_names()[0]
        series = GaugeChartSeries(data_type_name, field_name)
        series.operation_type = ChartOperationType.VALUE
        chart = _FixedGaugeChartDefinition()
        chart.minimum_value = 0.
        chart.maximum_value = 100.
        chart.series_list = [series]
        chart.grouping_type = ChartGroupingType.GROUP_BY_FIELD
        chart.grouping_type_data_type_name = data_type_name
        chart.grouping_type_data_field_name = group_by_field_name
        dashboard, step = ELNStepFactory._create_dashboard_step_from_chart(chart, data_source_step, protocol, step_name)
        protocol.invalidate()
        return step


# TODO: This is only here because the get_chart_type function in pylib is wrong. Remove this once pylib is fixed.
class _FixedGaugeChartDefinition(GaugeChartDefinition):
    def get_chart_type(self) -> ChartType:
        return ChartType.GAUGE_CHART
