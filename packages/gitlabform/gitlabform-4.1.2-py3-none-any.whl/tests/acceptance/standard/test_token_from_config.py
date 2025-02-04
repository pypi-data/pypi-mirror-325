import os

from tests.acceptance import (
    run_gitlabform,
)


class TestTokenFromConfig:
    def test__token_no_quotes(self, project, token_from_env_var):
        config = f"""
        gitlab:
          token: {token_from_env_var}
          
        projects_and_groups:
          placeholder:
        """

        run_gitlabform(config, project)

    def test__token_single_quotes(self, project, token_from_env_var):
        config = f"""
        gitlab:
          token: '{token_from_env_var}'
          
        projects_and_groups:
          placeholder:
        """

        run_gitlabform(config, project)

    def test__token_double_quotes(self, project, token_from_env_var):
        config = f"""
        gitlab:
          token: "{token_from_env_var}"

        projects_and_groups:
          placeholder:
        """

        run_gitlabform(config, project)
