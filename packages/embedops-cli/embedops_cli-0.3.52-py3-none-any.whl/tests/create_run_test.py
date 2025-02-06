"""
`create_run_test.py`
=======================================================================
Unit tests for code to create CI run records based on CI environment variables
* Author(s): Bryan Siepert
"""
from uuid import uuid1
import pytest
from unittest.mock import MagicMixin, MagicMock, call, ANY as mock_ANY
from embedops_cli.eotools.ci_run import CIRun, create_entry, CiConfigs

from embedops_cli.api.models import CIRun as APICIRun
from embedops_cli.api import rest

"""
- Given an
    - analysis type
    - commit sha
    - branch name
    - embedops api key
    - embedops host
- Then
    - The commit sha, branch name, and analysis type should be set as parameters to the CI run creation API call
    - An API Call should be made to the CI run creation endpoint on the given host
- Given
    - An API response with a 2xx return code
- Then
    - The included record id should be printed to stdout
    - The return code should be 0
"""


class TestEntrypoint:
    @pytest.fixture(autouse=True)
    def configure_env(self, monkeypatch, mocker):
        monkeypatch.setenv("CI", "true")
        monkeypatch.setenv("EMBEDOPS_API_REPO_KEY", "special_pwefix")
        monkeypatch.setenv("EMBEDOPS_ANALYSIS_TYPE", "memusage")
        monkeypatch.setenv("BITBUCKET_BRANCH", "main")
        monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "10")
        monkeypatch.setenv("BITBUCKET_COMMIT", "abcd1234")
        monkeypatch.setenv(
            "BITBUCKET_GIT_HTTP_ORIGIN", "http://bitbucket.org/dojofive/embedops-tools"
        )
        monkeypatch.setenv("BITBUCKET_STEP_UUID", "yoo-yoo-eye-dee")
        self.ci_run_caller = mocker.patch(
            "embedops_cli.eotools.create_run.CIRun.create"
        )
        self.logger_mock = mocker.patch("embedops_cli.eotools.ci_run._logger")
        self.ci_run = CIRun()
        yield
        del self.ci_run

    def test_ci_envvar_not_set_is_local(self, monkeypatch):
        """If we're not in CI we shant create a CI run, return zero, and output "LOCAL" for the id"""

        monkeypatch.delenv("CI")

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0

        self.logger_mock.info.assert_called_with("LOCAL")
        self.ci_run_caller.assert_not_called()

    def test_no_commit_id(self, monkeypatch):
        if getenv("BITBUCKET_COMMIT"):
            monkeypatch.delenv("BITBUCKET_COMMIT")
        if getenv("GITHUB_SHA"):
            monkeypatch.delenv("GITHUB_SHA")
        if getenv("CI_COMMIT_SHA"):
            monkeypatch.delenv("CI_COMMIT_SHA")
        ci_run = CIRun()
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ci_run.create_main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

        self.logger_mock.error.has_calls(call("ERROR: No commit id envvar found"))
        self.ci_run_caller.assert_not_called()

    def test_no_branch_name_or_tag(self, monkeypatch):
        monkeypatch.delenv("BITBUCKET_BRANCH")
        ci_run = CIRun()
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ci_run.create_main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

        self.logger_mock.error.assert_has_calls(
            [call("ERROR: No branch or tag name envvar found")]
        )
        self.ci_run_caller.assert_not_called()

    def test_no_analysis_type(self, monkeypatch):
        monkeypatch.delenv("EMBEDOPS_ANALYSIS_TYPE")
        ci_run = CIRun()
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ci_run.create_main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

        self.logger_mock.error.assert_has_calls(
            [call("ERROR: No analysis type envvar found")]
        )
        self.ci_run_caller.assert_not_called()

    def test_multiple_errors_shown(self, monkeypatch):
        monkeypatch.delenv("EMBEDOPS_ANALYSIS_TYPE", "memusage")
        # remove commit envvars
        if getenv("BITBUCKET_COMMIT"):
            monkeypatch.delenv("BITBUCKET_COMMIT")
        if getenv("GITHUB_SHA"):
            monkeypatch.delenv("GITHUB_SHA")
        if getenv("CI_COMMIT_SHA"):
            monkeypatch.delenv("CI_COMMIT_SHA")

        # remove branch envvars
        if getenv("BITBUCKET_BRANCH"):
            monkeypatch.delenv("BITBUCKET_BRANCH")
        if getenv("GITHUB_REF_NAME"):
            monkeypatch.delenv("GITHUB_REF_NAME")
        if getenv("CI_COMMIT_REF_NAME"):
            monkeypatch.delenv("CI_COMMIT_REF_NAME")

        ci_run = CIRun()
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ci_run.create_main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

        expected_calls = [
            call("ERROR: No analysis type envvar found"),
            call("ERROR: No branch or tag name envvar found"),
            call("ERROR: No commit id envvar found"),
        ]

        self.logger_mock.error.assert_has_calls(expected_calls, any_order=True)
        self.ci_run_caller.assert_not_called()

    def test_missing_api_key(self, monkeypatch):
        monkeypatch.delenv("EMBEDOPS_API_REPO_KEY")
        ci_run = CIRun()
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ci_run.create_main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

        self.logger_mock.error.assert_called_with(
            "ERROR: No EMBEDOPS_API_REPO_KEY envvar found"
        )

    def test_successful_call(self):
        expected_id = "yabbazabba"
        new_ci_run = MagicMock()
        new_ci_run.id = expected_id
        self.ci_run_caller.return_value = new_ci_run
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0

        ci_configs = self.ci_run_caller.call_args[0][1]
        assert isinstance(ci_configs, CiConfigs)
        assert ci_configs.commit_id == "abcd1234"
        assert ci_configs.branch_name == "main"
        assert ci_configs.pipeline_id == None
        assert ci_configs.commit_message == None
        assert (
            ci_configs.pipeline_url
            == "http://bitbucket.org/dojofive/embedops-tools/addon/pipelines/home#!/results/10/steps/yoo-yoo-eye-dee"
        )

        self.ci_run_caller.assert_called_with(
            "memusage",
            mock_ANY,
            60,  # default timeout
            5,  # default max_retries
            None,
        )
        self.logger_mock.info.assert_called_with(expected_id)

    def test_successful_call_with_tag(self, monkeypatch):
        monkeypatch.delenv("BITBUCKET_BRANCH")
        monkeypatch.setenv("BITBUCKET_TAG", "production-0.0.1")
        expected_id = "yabbazabba"
        new_ci_run = MagicMock()
        new_ci_run.id = expected_id
        self.ci_run_caller.return_value = new_ci_run
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0

        ci_configs = self.ci_run_caller.call_args[0][1]
        assert isinstance(ci_configs, CiConfigs)
        assert ci_configs.commit_id == "abcd1234"
        assert ci_configs.branch_name == "production-0.0.1"
        assert ci_configs.pipeline_id == None
        assert ci_configs.commit_message == None
        assert (
            ci_configs.pipeline_url
            == "http://bitbucket.org/dojofive/embedops-tools/addon/pipelines/home#!/results/10/steps/yoo-yoo-eye-dee"
        )

        self.ci_run_caller.assert_called_with(
            "memusage",
            mock_ANY,
            60,  # default timeout
            5,  # default max_retries
            None,
        )
        self.logger_mock.info.assert_called_with(expected_id)

    def test_successful_call_with_job_name_and_pipeline_id(self, monkeypatch):
        monkeypatch.setenv("EMBEDOPS_JOB_NAME", "build_job")
        monkeypatch.setenv("BITBUCKET_PIPELINE_UUID", "pipe-1234")
        expected_id = "yabbazabba"
        new_ci_run = MagicMock()
        new_ci_run.id = expected_id
        self.ci_run_caller.return_value = new_ci_run
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0

        ci_configs = self.ci_run_caller.call_args[0][1]
        assert isinstance(ci_configs, CiConfigs)
        assert ci_configs.commit_id == "abcd1234"
        assert ci_configs.branch_name == "main"
        assert ci_configs.pipeline_id == "pipe-1234"
        assert ci_configs.commit_message == None
        assert (
            ci_configs.pipeline_url
            == "http://bitbucket.org/dojofive/embedops-tools/addon/pipelines/home#!/results/10/steps/yoo-yoo-eye-dee"
        )

        self.ci_run_caller.assert_called_with(
            "memusage",
            mock_ANY,
            60,  # default timeout
            5,  # default max_retries
            "build_job",
        )
        self.logger_mock.info.assert_called_with(expected_id)


class TestSourceType:
    @pytest.fixture(autouse=True)
    def configure_env(self, monkeypatch, mocker):
        monkeypatch.setenv("CI", "true")
        monkeypatch.setenv("EMBEDOPS_API_REPO_KEY", "special_pwefix")
        monkeypatch.setenv("EMBEDOPS_ANALYSIS_TYPE", "memusage")
        self.ci_run_caller = mocker.patch(
            "embedops_cli.eotools.create_run.CIRun.create"
        )
        self.logger_mock = mocker.patch("embedops_cli.eotools.ci_run._logger")
        self.ci_run = CIRun()
        yield
        del self.ci_run

    def run_create_entry_and_check_ref(self, source_type, name):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0

        ci_configs = self.ci_run_caller.call_args[0][1]
        assert isinstance(ci_configs, CiConfigs)
        assert ci_configs.source_type == source_type
        assert ci_configs.branch_name == name

    def test_bb_branch_source_type(self, monkeypatch):
        monkeypatch.setenv("BITBUCKET_BRANCH", "main")
        monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "10")
        monkeypatch.setenv("BITBUCKET_COMMIT", "abcd1234")
        monkeypatch.setenv(
            "BITBUCKET_GIT_HTTP_ORIGIN", "http://bitbucket.org/dojofive/embedops-tools"
        )
        monkeypatch.setenv("BITBUCKET_STEP_UUID", "yoo-yoo-eye-dee")
        self.run_create_entry_and_check_ref("branch", "main")

    def test_bb_tag_source_type(self, monkeypatch):
        monkeypatch.setenv("BITBUCKET_TAG", "tag-0.0.1")
        monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "10")
        monkeypatch.setenv("BITBUCKET_COMMIT", "abcd1234")
        monkeypatch.setenv(
            "BITBUCKET_GIT_HTTP_ORIGIN", "http://bitbucket.org/dojofive/embedops-tools"
        )
        monkeypatch.setenv("BITBUCKET_STEP_UUID", "yoo-yoo-eye-dee")
        self.run_create_entry_and_check_ref("tag", "tag-0.0.1")

    def test_gh_branch_source_type(self, monkeypatch):
        monkeypatch.setenv("GITHUB_SHA", "fdsa94")
        monkeypatch.setenv("GITHUB_REF_NAME", "main")
        monkeypatch.setenv("GITHUB_REF_TYPE", "branch")
        monkeypatch.setenv("GITHUB_SERVER_URL", "example.com")
        monkeypatch.setenv("GITHUB_REPOSITORY", "rep")
        monkeypatch.setenv("GITHUB_RUN_ID", "1")
        self.run_create_entry_and_check_ref("branch", "main")

    def test_gh_tag_source_type(self, monkeypatch):
        monkeypatch.setenv("GITHUB_SHA", "fdsa94")
        monkeypatch.setenv("GITHUB_REF_NAME", "tag-0.0.1")
        monkeypatch.setenv("GITHUB_REF_TYPE", "tag")
        monkeypatch.setenv("GITHUB_SERVER_URL", "example.com")
        monkeypatch.setenv("GITHUB_REPOSITORY", "rep")
        monkeypatch.setenv("GITHUB_RUN_ID", "1")
        self.run_create_entry_and_check_ref("tag", "tag-0.0.1")

    def test_gl_branch_source_type(self, monkeypatch):
        monkeypatch.setenv("CI_COMMIT_SHA", "fdsa94")
        monkeypatch.setenv("CI_COMMIT_BRANCH", "main")
        monkeypatch.setenv("CI_COMMIT_REF_NAME", "main")
        monkeypatch.setenv("CI_PIPELINE_ID", "5")
        monkeypatch.setenv("CI_JOB_URL", "example.com")
        # remove CI_COMMIT_TAG since possibly present in Gitlab CI/CD
        monkeypatch.delenv("CI_COMMIT_TAG", False)
        self.run_create_entry_and_check_ref("branch", "main")

    def test_gl_tag_source_type(self, monkeypatch):
        monkeypatch.setenv("CI_COMMIT_SHA", "fdsa94")
        monkeypatch.setenv("CI_COMMIT_REF_NAME", "tag-0.0.1")
        monkeypatch.setenv("CI_COMMIT_TAG", "tag-0.0.1")
        monkeypatch.setenv("CI_PIPELINE_ID", "5")
        monkeypatch.setenv("CI_JOB_URL", "example.com")
        # remove CI_COMMIT_BRANCH since possibly present in Gitlab CI/CD
        monkeypatch.delenv("CI_COMMIT_BRANCH", False)
        self.run_create_entry_and_check_ref("tag", "tag-0.0.1")

    def test_gl_mr_source_type(self, monkeypatch):
        monkeypatch.setenv("CI_COMMIT_SHA", "fdsa94")
        monkeypatch.setenv("CI_MERGE_REQUEST_TARGET_BRANCH_NAME", "main")
        monkeypatch.setenv("CI_COMMIT_REF_NAME", "main")
        monkeypatch.setenv("CI_PIPELINE_ID", "5")
        monkeypatch.setenv("CI_JOB_URL", "example.com")
        # remove CI_COMMIT_BRANCH and CI_COMMIT_TAG since possibly present in Gitlab CI/CD
        monkeypatch.delenv("CI_COMMIT_BRANCH", False)
        monkeypatch.delenv("CI_COMMIT_TAG", False)
        self.run_create_entry_and_check_ref("branch", "main")


from os import getenv
import importlib


class TestSwaggerCall:
    @pytest.fixture(autouse=True)
    def configure_env(self, monkeypatch, mocker):
        self.expected_host = "https://dev-01.embedops.io"
        self.expected_type = "memusage"
        self.expected_commit_id = "deadb00f"
        self.expected_branch = "main"
        monkeypatch.setenv("CI", "true")
        monkeypatch.setenv("EMBEDOPS_HOST", self.expected_host)
        monkeypatch.setenv("EMBEDOPS_API_REPO_KEY", "special_pwefix")
        monkeypatch.setenv("EMBEDOPS_ANALYSIS_TYPE", self.expected_type)
        monkeypatch.setenv("BITBUCKET_COMMIT", self.expected_commit_id)
        monkeypatch.setenv("BITBUCKET_BRANCH", self.expected_branch)
        monkeypatch.setenv(
            "BITBUCKET_GIT_HTTP_ORIGIN", "http://bitbucket.org/dojofive/embedops-tools"
        )
        monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "10")
        monkeypatch.setenv("BITBUCKET_STEP_UUID", "yoo-yoo-eye-de")
        self.logger_mock = mocker.patch("embedops_cli.eotools.ci_run._logger")

        self.ci_run = CIRun()
        yield
        del self.ci_run

    def test_successful_create_response(self, mocker):
        mocked_id = "123123"
        ci_run = MagicMock()
        ci_run.id = mocked_id

        get_client = mocker.patch("embedops_cli.eotools.ci_run.get_client")

        get_client().create_ci_run_from_ci.return_value = ci_run
        response = self.ci_run.create(
            "memusage",
            CiConfigs("deadb00f", "main", "branch", None),
            60,  # default timeout
            5,  # default max_retries
        )
        assert response.id == mocked_id

    def test_create_response_has_source_type_branch(self, mocker):
        ci_run = MagicMock()

        get_client = mocker.patch("embedops_cli.eotools.ci_run.get_client")

        get_client().create_ci_run_from_ci.return_value = ci_run
        ci_run = mocker.patch("embedops_cli.eotools.create_run.CIRun.create")
        _ = self.ci_run.create(
            "memusage",
            CiConfigs("deadb00f", "main", "branch", None),
            60,  # default timeout
            5,  # default max_retries
        )

        ci_configs = ci_run.call_args[0][1]
        assert isinstance(ci_configs, CiConfigs)
        assert ci_configs.source_type == "branch"

    def test_create_response_has_source_type_tag(self, mocker):
        ci_run = MagicMock()

        get_client = mocker.patch("embedops_cli.eotools.ci_run.get_client")

        get_client().create_ci_run_from_ci.return_value = ci_run
        ci_run = mocker.patch("embedops_cli.eotools.create_run.CIRun.create")
        _ = self.ci_run.create(
            "memusage",
            CiConfigs("deadb00f", "main", "tag", None),
            60,  # default timeout
            5,  # default max_retries
        )

        ci_configs = ci_run.call_args[0][1]
        assert isinstance(ci_configs, CiConfigs)
        assert ci_configs.source_type == "tag"

    def test_failed_create_response(self, mocker):
        get_client = mocker.patch("embedops_cli.eotools.ci_run.get_client")

        get_client().create_ci_run_from_ci.side_effect = ValueError("garbage!")
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        self.logger_mock.error.assert_called_with("garbage!")

        get_client().create_ci_run_from_ci.side_effect = TypeError("trash!")
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        self.logger_mock.error.assert_called_with("trash!")

        get_client().create_ci_run_from_ci.side_effect = rest.ApiException("refuse!")
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry()
        self.logger_mock.error.assert_called_with("refuse!")

        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1
