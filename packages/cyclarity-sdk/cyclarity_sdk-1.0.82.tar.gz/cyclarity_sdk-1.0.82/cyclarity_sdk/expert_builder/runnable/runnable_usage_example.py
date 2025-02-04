""" Usage example """

from typing import Optional
from cyclarity_sdk.expert_builder import Runnable, BaseResultsModel
from cyclarity_sdk.sdk_models.findings import PTFinding, FindingType, TestResult
from cyclarity_sdk.sdk_models.findings.types import FindingStatus, TestBasicResultType
import time


class CanTestResult(BaseResultsModel):
    res_str: str


class canRunnableInstance(Runnable[CanTestResult]):
    desc: str
    cli_args: str
    _num: Optional[int] = 1  # not appear in the model_json_schema

    def setup(self):
        self.logger.info("setup")

    def run(self) -> CanTestResult:

        # example usage for send_test_description API function
        self.platform_api.send_test_report_description(
            "This is dummy description for test"
        )

        # example usage for reporting test progress
        for percentage in range(101):
            self.platform_api.report_test_progress(percentage=percentage)
            time.sleep(0.01)

        # example usage for sending test findings
        pt_finding = {"topic": "test",
                      "type": FindingType.FINDING,
                      "purpose": "test",
                      "description": "dummy PT finding for test purposes",
                      "status": FindingStatus.FINISHED,
                      "extra_field": "testing extra field which are not part of the model"}

        generic_test_result = {"topic": "test",
                               "type": TestBasicResultType.PASSED,
                               "purpose": "test",
                               "description": "dummy generic test result for test purposes",
                               "request": "extra_field_request",
                               "response": "extra_field_response"}

        pt_finding = PTFinding(**pt_finding)
        generic_test_result = TestResult(**generic_test_result)
        self.platform_api.send_finding(pt_finding)
        self.platform_api.send_finding(generic_test_result)

        return CanTestResult(res_str="success!")

    def teardown(self, exception_type, exception_value, traceback):
        self.logger.info("teardown")


# --- senity checks for runnable usage ---
# generates params schema from the runnable class attributes
print("\nParams schema - private members not included")
print(canRunnableInstance.model_json_schema())


# generate result schema
print("\nResult json schema:")
print(canRunnableInstance.generate_results_schema())

# Initiate runnable - option 1

# with canRunnableInstance(
#     desc="test", cli_args="-as -fsd -dsd"
# ) as runnable_instance:  # noqa
#     result: CanTestResult = runnable_instance()

#     # generates result json object
#     print("\nDirect running results: ")
#     print(result.model_dump_json())


# Initiate runnable - option 2
input = {
    "desc": "test",
    "cli_args": "-as -fsd -dsd",
}

with canRunnableInstance(**input) as runnable_instance:  # noqa
    result: CanTestResult = runnable_instance()

    # generates result json object
    print("\ndictionary running results: ")
    print(result.model_dump_json())
